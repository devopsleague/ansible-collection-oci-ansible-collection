# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_config_utils,
    oci_wait_utils,
)
from ansible.module_utils._text import to_bytes
import os

try:
    from oci.exceptions import ServiceError, MaximumWaitTimeExceeded
    from oci.util import to_dict
    from oci.object_storage.models import PutObjectLifecyclePolicyDetails
    from oci.object_storage import (
        ObjectStorageClient,
        UploadManager,
        MultipartObjectAssembler,
    )
    from oci.object_storage.models import ObjectSummary
    from oci.object_storage.transfer.internal.multipart_object_assembler import (
        READ_BUFFER_SIZE,
    )

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class BucketHelperCustom:
    """
    Customize the generated BucketHelperGen.
    """

    VALID_FIELDS_FOR_GET = ["approximateSize", "approximateCount", "autoTiering"]

    def get_resource(self, *args, **kwargs):
        return oci_common_utils.call_with_backoff(
            self.client.get_bucket,
            namespace_name=self.module.params.get("namespace_name"),
            bucket_name=self.module.params.get("name"),
            fields=self.VALID_FIELDS_FOR_GET,
        )

    def delete_resource(self):
        """
        Ensure bucket is deleted by deleting all objects in it,
        before call to delete bucket.
        """

        if self.module.params.get("force"):
            BucketsHelper.delete_all_entities(
                self,
                self.module.params.get("namespace_name"),
                self.module.params.get("name"),
            )

        return super(BucketHelperCustom, self).delete_resource()


class BucketFactsHelperCustom:
    VALID_FIELDS_FOR_GET = ["approximateSize", "approximateCount", "autoTiering"]
    VALID_FIELDS_FOR_LIST = ["tags"]

    def get_resource(self, *args, **kwargs):
        fields = self.module.params.get("fields") or []
        get_fields = [field for field in self.VALID_FIELDS_FOR_GET if field in fields]
        if get_fields:
            self.module.params["fields"] = get_fields
        return super(BucketFactsHelperCustom, self).get_resource(*args, **kwargs)

    def list_resources(self, *args, **kwargs):
        fields = self.module.params.get("fields") or []
        get_fields = [field for field in self.VALID_FIELDS_FOR_GET if field in fields]
        list_fields = [field for field in self.VALID_FIELDS_FOR_LIST if field in fields]
        if not fields or not get_fields:
            return super(BucketFactsHelperCustom, self).list_resources(*args, **kwargs)
        # there are some fields requested which are available only in the get call
        self.module.params["fields"] = list_fields
        return [
            self.client.get_bucket(
                namespace_name=self.module.params["namespace_name"],
                bucket_name=bucket.name,
                fields=get_fields,
            ).data
            for bucket in super(BucketFactsHelperCustom, self).list_resources(
                *args, **kwargs
            )
        ]


class BucketsHelper:
    """
    Helper class with api's common to different Buckets modules.
    """

    @staticmethod
    def delete_all_entities(resource_helper, namespace_name, bucket_name):
        """
        Deletes all entities within a bucket.
        These include objects, preauthenticated requests,
        replication policies, retention rules and lifecycle policies.

        @param resource_helper: ResourceHelper object for the ansible module.
        @param namespace_name:  str, bucket namespace
        @param bucket_name:     str, bucket name
        """

        # Delete object retention rules upfront.
        BucketsHelper.delete_all_retention_rules(
            resource_helper, namespace_name, bucket_name
        )

        list_fns = [
            resource_helper.client.list_objects,
            resource_helper.client.list_preauthenticated_requests,
            resource_helper.client.list_replication_policies,
        ]

        list_entities_kwargs = [
            {
                "entity_list_fn": list_fn,
                "namespace_name": namespace_name,
                "bucket_name": bucket_name,
            }
            for list_fn in list_fns
        ]

        # list all entities i.e. objects, preauthentication
        # requests and replication policies
        with oci_common_utils.threaded_worker_pool(4) as pool:
            (list_summary, preauthenticated_requests, replication_policies,) = pool.map(
                BucketsHelper.list_entities, list_entities_kwargs
            )

        entity_kwargs = []
        entity_kwargs += [
            {
                "call_fn_kwargs": {
                    "namespace_name": namespace_name,
                    "bucket_name": bucket_name,
                    "object_name": object.name,
                },
                "call_fn": resource_helper.client.delete_object,
                "resource_helper": resource_helper,
            }
            for object in list_summary.objects
        ]

        entity_kwargs += [
            {
                "call_fn_kwargs": {
                    "namespace_name": namespace_name,
                    "bucket_name": bucket_name,
                    "par_id": par.id,
                },
                "call_fn": resource_helper.client.delete_preauthenticated_request,
                "resource_helper": resource_helper,
            }
            for par in preauthenticated_requests
        ]

        entity_kwargs += [
            {
                "call_fn_kwargs": {
                    "namespace_name": namespace_name,
                    "bucket_name": bucket_name,
                    "replication_id": replication_policy.id,
                },
                "call_fn": resource_helper.client.delete_replication_policy,
                "resource_helper": resource_helper,
            }
            for replication_policy in replication_policies
        ]

        entity_kwargs.append(
            {
                "call_fn_kwargs": {
                    "namespace_name": namespace_name,
                    "bucket_name": bucket_name,
                },
                "call_fn": resource_helper.client.delete_object_lifecycle_policy,
                "resource_helper": resource_helper,
            }
        )

        if entity_kwargs:
            # delete all entities
            with oci_common_utils.threaded_worker_pool(
                min(50, len(entity_kwargs))
            ) as pool:
                pool.map(BucketsHelper.delete_entity, entity_kwargs)

    @staticmethod
    def list_entities(kwargs):
        return oci_common_utils.list_all_resources(
            kwargs.get("entity_list_fn"),
            namespace_name=kwargs.get("namespace_name"),
            bucket_name=kwargs.get("bucket_name"),
        )

    @staticmethod
    def delete_all_retention_rules(resource_helper, namespace_name, bucket_name):
        """
        Fetches and deletes all retention rules in the bucket, if any.

        @param resource_helper: ResourceHelper object for the ansible module.
        @param namespace_name:  str, bucket namespace
        @param bucket_name:     str, bucket name
        """

        retention_rules = oci_common_utils.list_all_resources(
            resource_helper.client.list_retention_rules,
            namespace_name=namespace_name,
            bucket_name=bucket_name,
        )
        if retention_rules:
            delete_kwargs = [
                {
                    "call_fn_kwargs": {
                        "namespace_name": namespace_name,
                        "bucket_name": bucket_name,
                        "retention_rule_id": retention_rule.id,
                    },
                    "call_fn": resource_helper.client.delete_retention_rule,
                    "resource_helper": resource_helper,
                }
                for retention_rule in retention_rules
            ]

            # delete all objects
            with oci_common_utils.threaded_worker_pool(
                min(50, len(delete_kwargs))
            ) as pool:
                pool.map(BucketsHelper.delete_entity, delete_kwargs)

    @staticmethod
    def delete_entity(delete_kwargs):
        """
        Deletes an entity in the object storage bucket.
        """
        return oci_wait_utils.call_and_wait(
            call_fn=delete_kwargs.get("call_fn"),
            call_fn_args=(),
            call_fn_kwargs=delete_kwargs.get("call_fn_kwargs"),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=delete_kwargs.get("resource_helper").get_waiter_client(),
            resource_helper=delete_kwargs.get("resource_helper"),
            wait_for_states=oci_common_utils.DELETE_OPERATION_KEY,
        )


class BucketActionsHelperCustom:
    def is_action_necessary(self, action, resource):
        if action == "make_bucket_writable":
            if resource.is_read_only:
                return True
            return False
        return super(BucketActionsHelperCustom, self).is_action_necessary(
            action, resource
        )


def get_object_summary_response_fields_to_retrieve():
    return [
        oci_common_utils.camelize(field)
        for field in list(ObjectSummary().attribute_map)
    ]


def get_object(client, namespace_name, bucket_name, object_name):
    obj = None
    fields_to_retrieve = ",".join(get_object_summary_response_fields_to_retrieve())
    for o in oci_common_utils.list_all_resources(
        client.list_objects,
        namespace_name=namespace_name,
        bucket_name=bucket_name,
        prefix=object_name,
        fields=fields_to_retrieve,
    ).objects:
        if o.name == object_name:
            obj = o

    head_object_response_headers = to_dict(
        oci_common_utils.call_with_backoff(
            client.head_object,
            namespace_name=namespace_name,
            bucket_name=bucket_name,
            object_name=object_name,
        ).headers
    )
    setattr(obj, "headers", head_object_response_headers)
    # also add attr to the swagger_types so that it is returned when converted to dict using to_dict
    if hasattr(obj, "swagger_types"):
        obj.swagger_types["headers"] = "dict(str, str)"
    return obj


class ObjectFactsHelperCustom:
    def get(self):
        obj = get_object(
            self.client,
            self.module.params.get("namespace_name"),
            self.module.params.get("bucket_name"),
            self.module.params.get("object_name"),
        )
        if not obj:
            self.module.fail_json(
                msg="Could not find the object {0} in bucket {1}".format(
                    self.module.params.get("object_name"),
                    self.module.params.get("bucket_name"),
                )
            )
        return to_dict(obj)

    def list(self, *args, **kwargs):
        list_objects = super(ObjectFactsHelperCustom, self).list(*args, **kwargs)
        objects = list_objects.get("objects") or []
        return objects


class ObjectHelperCustom:
    def is_update(self):
        if not self.module.params.get("state") == "present":
            return False
        return True

    def get_resource(self, *args, **kwargs):
        obj = get_object(
            self.client,
            self.module.params.get("namespace_name"),
            self.module.params.get("bucket_name"),
            self.module.params.get("object_name"),
        )
        if not obj:
            oci_common_utils.raise_does_not_exist_service_error()

        head_response = oci_common_utils.call_with_backoff(
            self.client.head_object,
            namespace_name=self.module.params.get("namespace_name"),
            bucket_name=self.module.params.get("bucket_name"),
            object_name=self.module.params.get("object_name"),
        )
        return oci_common_utils.get_default_response_from_resource(
            obj, headers=head_response.headers
        )

    def list_resources(self, *args, **kwargs):
        list_objects = super(ObjectHelperCustom, self).list_resources(*args, **kwargs)
        return list_objects.objects

    def download_object(self, dest, force):

        dest = os.path.expanduser(dest)
        try:
            get_response = self.get_resource()
        except ServiceError as ex:
            self.module.fail_json(msg=ex.message)

        if force is True or not os.path.isfile(to_bytes(dest)):

            try:
                download_response = oci_common_utils.call_with_backoff(
                    self.client.get_object,
                    namespace_name=self.module.params.get("namespace_name"),
                    bucket_name=self.module.params.get("bucket_name"),
                    object_name=self.module.params.get("object_name"),
                )
            except ServiceError as ex:
                self.module.fail_json(msg=ex.message)

            # create dest file if it does not exist
            try:
                with open(dest, "a"):
                    pass
            except IOError as ioex:
                self.module.fail_json(
                    msg="Error opening/creating the dest file: {0}".format(str(ioex))
                )

            # Check if file exists with the same checksum. Get md5 hexdigest of the file content, convert it to
            # binary and then get base-64 encoded MD5 hash.
            dest_md5 = MultipartObjectAssembler.calculate_md5(dest, 0, READ_BUFFER_SIZE)
            if os.path.isfile(to_bytes(dest)) and (
                dest_md5 == download_response.headers.get("Content-MD5", None)
                or dest_md5 == download_response.headers.get("opc-multipart-md5", None)
            ):
                return self.prepare_result(
                    changed=False,
                    resource_type=self.get_response_field_name(),
                    resource=to_dict(get_response.data),
                )
            else:
                # Read 1MB at a time
                chunk_size = 1024 * 1024
                with open(to_bytes(dest), "wb") as dest_file:
                    for chunk in download_response.data.raw.stream(
                        chunk_size, decode_content=False
                    ):
                        dest_file.write(chunk)
                return self.prepare_result(
                    changed=True,
                    resource_type=self.get_response_field_name(),
                    resource=to_dict(get_response.data),
                )
        else:
            return self.prepare_result(
                changed=False,
                resource_type=self.get_response_field_name(),
                resource=to_dict(get_response.data),
                msg="Destination %s already exists. Use force option to overwrite."
                % dest,
            )

    def upload_object(self, src, force):
        src = os.path.expanduser(src)
        if not os.path.isfile(to_bytes(src)):
            self.module.fail_json(msg="The source path %s must be a file." % src)

        if not os.access(to_bytes(src), os.R_OK):
            self.module.fail_json(
                msg="Failed to access %s. Make sure the file exists and that you have "
                "read access." % src
            )

        object_exists = False
        try:
            response = self.get_resource()
            object_exists = True
        except ServiceError as ex:
            if ex.status != 404:
                self.module.fail_json(msg=ex.message)

        if object_exists and force is False:
            return self.prepare_result(
                changed=False,
                resource_type=self.get_response_field_name(),
                resource=to_dict(response.data),
                msg="Object %s already present in bucket. Use force option to overwrite."
                % self.module.params.get("object_name"),
            )

        src_md5 = MultipartObjectAssembler.calculate_md5(src, 0, READ_BUFFER_SIZE)
        if object_exists and (
            src_md5 == response.headers.get("Content-MD5", None)
            or src_md5 == response.headers.get("opc-multipart-md5", None)
        ):
            return self.prepare_result(
                changed=False,
                resource_type=self.get_response_field_name(),
                resource=to_dict(response.data),
            )

        try:
            # sdk complains if the value is None
            self.module.params["opc_meta"] = (
                self.module.params.get("opc_meta") or dict()
            )
            upload_manager = UploadManager(self.client,)
            oci_common_utils.call_with_backoff(
                upload_manager.upload_file,
                namespace_name=self.module.params.get("namespace_name"),
                bucket_name=self.module.params.get("bucket_name"),
                object_name=self.module.params.get("object_name"),
                content_encoding=self.module.params.get("content_encoding"),
                content_language=self.module.params.get("content_language"),
                content_length=self.module.params.get("content_length"),
                content_md5=self.module.params.get("content_md5"),
                content_type=self.module.params.get("content_type"),
                content_disposition=self.module.params.get("content_disposition"),
                cache_control=self.module.params.get("cache_control"),
                opc_sse_customer_algorithm=self.module.params.get(
                    "opc_sse_customer_algorithm"
                ),
                opc_sse_customer_key=self.module.params.get("opc_sse_customer_key"),
                opc_sse_customer_key_sha256=self.module.params.get(
                    "opc_sse_customer_key_sha256"
                ),
                opc_meta=self.module.params.get("opc_meta"),
                file_path=src,
            )

            uploaded_object_response = self.get_resource()
            return self.prepare_result(
                changed=True,
                resource_type=self.get_response_field_name(),
                resource=to_dict(uploaded_object_response.data),
            )

        except ServiceError as ex:
            self.module.fail_json(msg=ex.message)

    def update(self, *args, **kwargs):

        dest = self.module.params.get("dest")
        src = self.module.params.get("src")
        force = self.module.params.get("force")
        if dest is not None:
            return self.download_object(dest, force)
        elif src is not None:
            return self.upload_object(src, force)

    def get_object_version(self):
        for object_version in oci_common_utils.list_all_resources(
            self.client.list_object_versions,
            namespace_name=self.module.params.get("namespace_name"),
            bucket_name=self.module.params.get("bucket_name"),
            prefix=self.module.params.get("object_name"),
        ):
            if object_version.name == self.module.params.get(
                "object_name"
            ) and object_version.version_id == self.module.params.get("version_id"):
                return object_version
        return None

    def delete(self, *args, **kwargs):
        if not self.module.params.get("version_id"):
            return super(ObjectHelperCustom, self).delete(*args, **kwargs)
        object_version = self.get_object_version()
        if not object_version:
            return self.prepare_result(
                changed=True,
                resource_type=self.get_response_field_name(),
                resource=dict(),
            )
        if self.check_mode:
            return self.prepare_result(
                changed=True,
                resource_type=self.get_response_field_name(),
                resource=to_dict(object_version),
            )
        try:
            self.delete_resource()
        except MaximumWaitTimeExceeded as mwtex:
            self.module.fail_json(msg=str(mwtex))
        except ServiceError as se:
            if se.status == 404:
                return self.prepare_result(
                    changed=True,
                    resource_type=self.get_response_field_name(),
                    resource=to_dict(object_version),
                )
            self.module.fail_json(
                msg="Deleting resource failed with exception: {0}".format(se.message)
            )
        else:
            return self.prepare_result(
                changed=True,
                resource_type=self.get_response_field_name(),
                resource=to_dict(object_version),
            )


class ObjectActionsHelperCustom:

    COPY_ACTION = "copy"
    RENAME_ACTION = "rename"
    RESTORE_ACTION = "restore"
    REENCRYPT_ACTION = "reencrypt"
    UPDATE_OBJECT_STORAGE_TIER_ACTION = "update_object_storage_tier"

    def perform_copy(self):
        obj = get_object(
            self.client,
            self.module.params.get("namespace_name"),
            self.module.params.get("bucket_name"),
            self.module.params.get("source_object_name"),
        )
        if not obj:
            self.module.fail_json(
                msg="Could not find the object {0} in bucket {1}".format(
                    self.module.params.get("source_object_name"),
                    self.module.params.get("bucket_name"),
                )
            )
        is_action_necessary = self.is_action_necessary(self.COPY_ACTION, obj)
        if not is_action_necessary:
            return self.prepare_result(
                changed=False,
                resource_type=self.get_response_field_name(self.COPY_ACTION),
                resource=to_dict(obj),
            )
        if self.check_mode:
            return self.prepare_result(
                changed=True,
                resource_type=self.get_response_field_name(self.COPY_ACTION),
                resource=to_dict(obj),
            )
        try:
            self.copy()
        except MaximumWaitTimeExceeded as mwtex:
            self.module.fail_json(msg=str(mwtex))
        except ServiceError as se:
            self.module.fail_json(
                msg="Performing action failed with exception: {0}".format(se.message)
            )
        else:
            destination_region_client = oci_config_utils.create_service_client(
                self.module,
                ObjectStorageClient,
                dict(
                    oci_config_utils.get_oci_config(self.module),
                    region=self.module.params.get("destination_region"),
                ),
            )
            copied_obj = get_object(
                destination_region_client,
                self.module.params.get("destination_namespace"),
                self.module.params.get("destination_bucket"),
                self.module.params.get("destination_object_name"),
            )
            if not copied_obj:
                self.module.fail_json(
                    msg="Could not find the copied object {0} in bucket {1} and namespace {2}".format(
                        self.module.params.get("destination_object_name"),
                        self.module.params.get("destination_bucket"),
                        self.module.params.get("destination_namespace"),
                    )
                )
            return self.prepare_result(
                changed=True,
                resource_type=self.get_response_field_name(self.COPY_ACTION),
                resource=to_dict(copied_obj),
            )

    def perform_rename(self):
        obj = get_object(
            self.client,
            self.module.params.get("namespace_name"),
            self.module.params.get("bucket_name"),
            self.module.params.get("source_name"),
        )
        if not obj:
            self.module.fail_json(
                msg="Could not find the object {0} in bucket {1}".format(
                    self.module.params.get("source_name"),
                    self.module.params.get("bucket_name"),
                )
            )
        is_action_necessary = self.is_action_necessary(self.RENAME_ACTION, obj)
        if not is_action_necessary:
            return self.prepare_result(
                changed=False,
                resource_type=self.get_response_field_name(self.RENAME_ACTION),
                resource=to_dict(obj),
            )
        if self.check_mode:
            return self.prepare_result(
                changed=True,
                resource_type=self.get_response_field_name(self.RENAME_ACTION),
                resource=to_dict(obj),
            )
        try:
            self.rename()
        except MaximumWaitTimeExceeded as mwtex:
            self.module.fail_json(msg=str(mwtex))
        except ServiceError as se:
            self.module.fail_json(
                msg="Performing action failed with exception: {0}".format(se.message)
            )
        else:
            renamed_obj = get_object(
                self.client,
                self.module.params.get("namespace_name"),
                self.module.params.get("bucket_name"),
                self.module.params.get("new_name"),
            )
            if not renamed_obj:
                self.module.fail_json(
                    msg="Could not find the renamed object {0} in bucket {1} and namespace {2}".format(
                        self.module.params.get("new_name"),
                        self.module.params.get("bucket_name"),
                        self.module.params.get("namespace_name"),
                    )
                )
            return self.prepare_result(
                changed=True,
                resource_type=self.get_response_field_name(self.RENAME_ACTION),
                resource=to_dict(renamed_obj),
            )

    def perform_restore(self):
        obj = get_object(
            self.client,
            self.module.params.get("namespace_name"),
            self.module.params.get("bucket_name"),
            self.module.params.get("object_name"),
        )
        if not obj:
            self.module.fail_json(
                msg="Could not find the object {0} in bucket {1}".format(
                    self.module.params.get("object_name"),
                    self.module.params.get("bucket_name"),
                )
            )
        is_action_necessary = self.is_action_necessary(self.RESTORE_ACTION, obj)
        if not is_action_necessary:
            return self.prepare_result(
                changed=False,
                resource_type=self.get_response_field_name(self.RESTORE_ACTION),
                resource=to_dict(obj),
            )
        if self.check_mode:
            return self.prepare_result(
                changed=True,
                resource_type=self.get_response_field_name(self.RESTORE_ACTION),
                resource=to_dict(obj),
            )
        try:
            self.restore()
        except MaximumWaitTimeExceeded as mwtex:
            self.module.fail_json(msg=str(mwtex))
        except ServiceError as se:
            self.module.fail_json(
                msg="Performing action failed with exception: {0}".format(se.message)
            )
        else:
            restored_obj = get_object(
                self.client,
                self.module.params.get("namespace_name"),
                self.module.params.get("bucket_name"),
                self.module.params.get("object_name"),
            )
            if not restored_obj:
                self.module.fail_json(
                    msg="Could not find the restored object {0} in bucket {1} and namespace {2}".format(
                        self.module.params.get("object_name"),
                        self.module.params.get("bucket_name"),
                        self.module.params.get("namespace_name"),
                    )
                )
            return self.prepare_result(
                changed=True,
                resource_type=self.get_response_field_name(self.RESTORE_ACTION),
                resource=to_dict(restored_obj),
            )

    def perform_reencrypt(self):
        obj = get_object(
            self.client,
            self.module.params.get("namespace_name"),
            self.module.params.get("bucket_name"),
            self.module.params.get("object_name"),
        )
        if not obj:
            self.module.fail_json(
                msg="Could not find the object {0} in bucket {1}".format(
                    self.module.params.get("object_name"),
                    self.module.params.get("bucket_name"),
                )
            )
        is_action_necessary = self.is_action_necessary(self.REENCRYPT_ACTION, obj)
        if not is_action_necessary:
            return self.prepare_result(
                changed=False,
                resource_type=self.get_response_field_name(self.REENCRYPT_ACTION),
                resource=to_dict(obj),
            )
        if self.check_mode:
            return self.prepare_result(
                changed=True,
                resource_type=self.get_response_field_name(self.REENCRYPT_ACTION),
                resource=to_dict(obj),
            )
        try:
            self.reencrypt()
        except MaximumWaitTimeExceeded as mwtex:
            self.module.fail_json(msg=str(mwtex))
        except ServiceError as se:
            self.module.fail_json(
                msg="Performing action failed with exception: {0}".format(se.message)
            )
        else:
            reencrypted_obj = get_object(
                self.client,
                self.module.params.get("namespace_name"),
                self.module.params.get("bucket_name"),
                self.module.params.get("object_name"),
            )
            if not reencrypted_obj:
                self.module.fail_json(
                    msg="Could not find the reencrypted object {0} in bucket {1} and namespace {2}".format(
                        self.module.params.get("object_name"),
                        self.module.params.get("bucket_name"),
                        self.module.params.get("namespace_name"),
                    )
                )
            return self.prepare_result(
                changed=True,
                resource_type=self.get_response_field_name(self.REENCRYPT_ACTION),
                resource=to_dict(reencrypted_obj),
            )

    def perform_update_object_storage_tier(self):
        obj = get_object(
            self.client,
            self.module.params.get("namespace_name"),
            self.module.params.get("bucket_name"),
            self.module.params.get("object_name"),
        )
        if not obj:
            self.module.fail_json(
                msg="Could not find the object {0} in bucket {1}".format(
                    self.module.params.get("object_name"),
                    self.module.params.get("bucket_name"),
                )
            )
        is_action_necessary = self.is_action_necessary(
            self.UPDATE_OBJECT_STORAGE_TIER_ACTION, obj
        )
        if not is_action_necessary:
            return self.prepare_result(
                changed=False,
                resource_type=self.get_response_field_name(
                    self.UPDATE_OBJECT_STORAGE_TIER_ACTION
                ),
                resource=to_dict(obj),
            )
        if self.check_mode:
            return self.prepare_result(
                changed=True,
                resource_type=self.get_response_field_name(
                    self.UPDATE_OBJECT_STORAGE_TIER_ACTION
                ),
                resource=to_dict(obj),
            )
        try:
            self.update_object_storage_tier()
        except MaximumWaitTimeExceeded as mwtex:
            self.module.fail_json(msg=str(mwtex))
        except ServiceError as se:
            self.module.fail_json(
                msg="Performing action failed with exception: {0}".format(se.message)
            )
        else:
            updated_object_storage_tier_obj = get_object(
                self.client,
                self.module.params.get("namespace_name"),
                self.module.params.get("bucket_name"),
                self.module.params.get("object_name"),
            )
            if not updated_object_storage_tier_obj:
                self.module.fail_json(
                    msg="Could not find the updated object {0} in bucket {1} and namespace {2}".format(
                        self.module.params.get("object_name"),
                        self.module.params.get("bucket_name"),
                        self.module.params.get("namespace_name"),
                    )
                )
            return self.prepare_result(
                changed=True,
                resource_type=self.get_response_field_name(
                    self.UPDATE_OBJECT_STORAGE_TIER_ACTION
                ),
                resource=to_dict(updated_object_storage_tier_obj),
            )

    def is_action_necessary(self, action, resource=None):
        if action == "update_object_storage_tier":
            if resource.storage_tier == self.module.params.get("storage_tier"):
                return False
            return True
        return True

    def perform_action(self, action):
        action_fn = self.get_action_fn(action)
        if not action_fn:
            self.module.fail_json(msg="{0} not supported by the module.".format(action))
        perform_action_fn = getattr(
            self,
            "perform_{0}".format(action),
            lambda: super(ObjectActionsHelperCustom, self).perform_action(action),
        )
        return perform_action_fn()


class ObjectLifecyclePolicyHelperCustom:
    # - Most modules use the *_id input parameter to determine if the operation
    #   is an update instead of a create, but in this case we don't need that
    #   because the ObjectLifecyclePolicy is identified uniquely by the namespace_name
    #   and bucket_name. Thus, a CREATE and UPDATE attempt look identical in a user playbook
    # - ObjectLifecyclePolicy only supports PUT and not POST so PutObjectLifecyclePolicy
    #   gets classified as an UPDATE operation on the resource and thus none of the normal
    #   create related operations are generated, thus we define them below

    # methods necessary for CREATE
    def list_resources(self):
        # ObjectLifecyclePolicy is defined per Bucket so listing is just returning
        # the single policy if it is defined and otherwise an empty list
        try:
            return [self.get_resource().data]
        except ServiceError as e:
            if e.status != 404:
                raise e

        return []

    def get_create_model_class(self):
        return PutObjectLifecyclePolicyDetails

    def create_resource(self):
        return self.update_resource()

    # override UPDATE to use CREATE underneath because there may be no existing
    # resource to fetch which is fine for CREATE but causes UPDATE to fail
    def update(self):
        return self.create()


class PreauthenticatedRequestHelperCustom:
    # Creating a preauthenticated request returns access_uri only at the time of creation and is not available
    # in get calls. So the idempotent create runs would not return access_uri which might cause the workflow to brealk
    # if it depends on the access_uri. So making create call not idempotent so that any one creating a preauthenticated
    # request would get all the information needed to use it.
    def get_matching_resource(self):
        return None

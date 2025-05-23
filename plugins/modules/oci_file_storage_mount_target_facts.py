#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.
# GENERATED FILE - DO NOT EDIT - MANUAL CHANGES WILL BE OVERWRITTEN


from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_file_storage_mount_target_facts
short_description: Fetches details about one or multiple MountTarget resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple MountTarget resources in Oracle Cloud Infrastructure
    - Lists the mount target resources in the specified compartment.
    - If I(mount_target_id) is specified, the details of a single MountTarget will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    mount_target_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the mount target.
            - Required to get a specific mount_target.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required to list multiple mount_targets.
        type: str
    availability_domain:
        description:
            - The name of the availability domain.
            - "Example: `Uocm:PHX-AD-1`"
            - Required to list multiple mount_targets.
        type: str
    display_name:
        description:
            - A user-friendly name. It does not have to be unique, and it is changeable.
            - "Example: `My resource`"
        type: str
        aliases: ["name"]
    export_set_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the export set.
        type: str
    lifecycle_state:
        description:
            - Filter results by the specified lifecycle state. Must be a valid
              state for the resource type.
        type: str
        choices:
            - "CREATING"
            - "ACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    sort_by:
        description:
            - The field to sort by. You can choose either value, but not both.
              By default, when you sort by time created, results are shown
              in descending order. When you sort by display name, results are
              shown in ascending order.
        type: str
        choices:
            - "TIMECREATED"
            - "DISPLAYNAME"
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc', where 'asc' is
              ascending and 'desc' is descending. The default order is 'desc'
              except for numeric values.
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific mount_target
  oci_file_storage_mount_target_facts:
    # required
    mount_target_id: "ocid1.mounttarget.oc1..xxxxxxEXAMPLExxxxxx"

- name: List mount_targets
  oci_file_storage_mount_target_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    availability_domain: Uocm:PHX-AD-1

    # optional
    display_name: display_name_example
    export_set_id: "ocid1.exportset.oc1..xxxxxxEXAMPLExxxxxx"
    lifecycle_state: CREATING
    sort_by: TIMECREATED
    sort_order: ASC

"""

RETURN = """
mount_targets:
    description:
        - List of MountTarget resources
    returned: on success
    type: complex
    contains:
        lifecycle_details:
            description:
                - Additional information about the current 'lifecycleState'.
                - Returned for get operation
            returned: on success
            type: str
            sample: lifecycle_details_example
        idmap_type:
            description:
                - The method used to map a Unix UID to secondary groups. If NONE, the mount target will not use the Unix UID for ID mapping.
                - Returned for get operation
            returned: on success
            type: str
            sample: LDAP
        ldap_idmap:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                schema_type:
                    description:
                        - Schema type of the LDAP account.
                    returned: on success
                    type: str
                    sample: RFC2307
                cache_refresh_interval_seconds:
                    description:
                        - The amount of time that the mount target should allow an entry to persist in its cache before attempting to refresh the entry.
                    returned: on success
                    type: int
                    sample: 56
                cache_lifetime_seconds:
                    description:
                        - The maximum amount of time the mount target is allowed to use a cached entry.
                    returned: on success
                    type: int
                    sample: 56
                negative_cache_lifetime_seconds:
                    description:
                        - The amount of time that a mount target will maintain information that a user is not found in the ID mapping configuration.
                    returned: on success
                    type: int
                    sample: 56
                user_search_base:
                    description:
                        - All LDAP searches are recursive starting at this user.
                        - "Example: `CN=User,DC=domain,DC=com`"
                    returned: on success
                    type: str
                    sample: user_search_base_example
                group_search_base:
                    description:
                        - All LDAP searches are recursive starting at this group.
                        - "Example: `CN=Group,DC=domain,DC=com`"
                    returned: on success
                    type: str
                    sample: group_search_base_example
                outbound_connector1_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the first connector to use to communicate with
                          the LDAP server.
                    returned: on success
                    type: str
                    sample: "ocid1.outboundconnector1.oc1..xxxxxxEXAMPLExxxxxx"
                outbound_connector2_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the second connector to use to communicate with
                          the LDAP server.
                    returned: on success
                    type: str
                    sample: "ocid1.outboundconnector2.oc1..xxxxxxEXAMPLExxxxxx"
        kerberos:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                kerberos_realm:
                    description:
                        - The Kerberos realm that the mount target will join.
                    returned: on success
                    type: str
                    sample: kerberos_realm_example
                key_tab_secret_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the keytab secret in the Vault.
                    returned: on success
                    type: str
                    sample: "ocid1.keytabsecret.oc1..xxxxxxEXAMPLExxxxxx"
                current_key_tab_secret_version:
                    description:
                        - Version of the keytab secret in the Vault to use.
                    returned: on success
                    type: int
                    sample: 56
                backup_key_tab_secret_version:
                    description:
                        - Version of the keytab secert in the Vault to use as a backup.
                    returned: on success
                    type: int
                    sample: 56
                is_kerberos_enabled:
                    description:
                        - Specifies whether to enable or disable Kerberos.
                    returned: on success
                    type: bool
                    sample: true
        availability_domain:
            description:
                - The availability domain the mount target is in. May be unset
                  as a blank or NULL value.
                - "Example: `Uocm:PHX-AD-1`"
            returned: on success
            type: str
            sample: Uocm:PHX-AD-1
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment that contains the mount target.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly name. It does not have to be unique, and it is changeable.
                  Avoid entering confidential information.
                - "Example: `My mount target`"
            returned: on success
            type: str
            sample: display_name_example
        export_set_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the associated export set. Controls what file
                  systems will be exported through Network File System (NFS) protocol on this
                  mount target.
            returned: on success
            type: str
            sample: "ocid1.exportset.oc1..xxxxxxEXAMPLExxxxxx"
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the mount target.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current state of the mount target.
            returned: on success
            type: str
            sample: CREATING
        private_ip_ids:
            description:
                - The OCIDs of the private IP addresses associated with this mount target.
            returned: on success
            type: list
            sample: []
        subnet_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the subnet the mount target is in.
            returned: on success
            type: str
            sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
        nsg_ids:
            description:
                - A list of Network Security Group L(OCIDs,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) associated with this mount
                  target.
                  A maximum of 5 is allowed.
                  Setting this to an empty array after the list is created removes the mount target from all NSGs.
                  For more information about NSGs, see L(Security Rules,https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm).
            returned: on success
            type: list
            sample: []
        time_created:
            description:
                - The date and time the mount target was created, expressed
                  in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) timestamp format.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        freeform_tags:
            description:
                - "Free-form tags for this resource. Each tag is a simple key-value pair
                   with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: [{
        "lifecycle_details": "lifecycle_details_example",
        "idmap_type": "LDAP",
        "ldap_idmap": {
            "schema_type": "RFC2307",
            "cache_refresh_interval_seconds": 56,
            "cache_lifetime_seconds": 56,
            "negative_cache_lifetime_seconds": 56,
            "user_search_base": "user_search_base_example",
            "group_search_base": "group_search_base_example",
            "outbound_connector1_id": "ocid1.outboundconnector1.oc1..xxxxxxEXAMPLExxxxxx",
            "outbound_connector2_id": "ocid1.outboundconnector2.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "kerberos": {
            "kerberos_realm": "kerberos_realm_example",
            "key_tab_secret_id": "ocid1.keytabsecret.oc1..xxxxxxEXAMPLExxxxxx",
            "current_key_tab_secret_version": 56,
            "backup_key_tab_secret_version": 56,
            "is_kerberos_enabled": true
        },
        "availability_domain": "Uocm:PHX-AD-1",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "export_set_id": "ocid1.exportset.oc1..xxxxxxEXAMPLExxxxxx",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "CREATING",
        "private_ip_ids": [],
        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
        "nsg_ids": [],
        "time_created": "2013-10-20T19:20:30+01:00",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.file_storage import FileStorageClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MountTargetFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "mount_target_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
            "availability_domain",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_mount_target,
            mount_target_id=self.module.params.get("mount_target_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
            "export_set_id",
            "lifecycle_state",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_mount_targets,
            compartment_id=self.module.params.get("compartment_id"),
            availability_domain=self.module.params.get("availability_domain"),
            **optional_kwargs
        )


MountTargetFactsHelperCustom = get_custom_class("MountTargetFactsHelperCustom")


class ResourceFactsHelper(MountTargetFactsHelperCustom, MountTargetFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            mount_target_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            availability_domain=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            export_set_id=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"],
            ),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="mount_target",
        service_client_class=FileStorageClient,
        namespace="file_storage",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(mount_targets=result)


if __name__ == "__main__":
    main()

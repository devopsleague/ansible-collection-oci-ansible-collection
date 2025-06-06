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
module: oci_compute_instance_console_connection
short_description: Manage an InstanceConsoleConnection resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an InstanceConsoleConnection resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new console connection to the specified instance.
      After the console connection has been created and is available,
      you connect to the console using SSH.
    - For more information about instance console connections, see L(Troubleshooting Instances Using Instance Console
      Connections,https://docs.cloud.oracle.com/iaas/Content/Compute/References/serialconsole.htm).
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    instance_id:
        description:
            - The OCID of the instance to create the console connection to.
            - Required for create using I(state=present).
        type: str
    public_key:
        description:
            - The SSH public key used to authenticate the console connection.
            - Required for create using I(state=present).
        type: str
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a
              namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no
              predefined name, type, or namespace. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    instance_console_connection_id:
        description:
            - The OCID of the instance console connection.
            - Required for update using I(state=present).
            - Required for delete using I(state=absent).
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required for create using I(state=present).
        type: str
    state:
        description:
            - The state of the InstanceConsoleConnection.
            - Use I(state=present) to create or update an InstanceConsoleConnection.
            - Use I(state=absent) to delete an InstanceConsoleConnection.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create instance_console_connection
  oci_compute_instance_console_connection:
    # required
    instance_id: "ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx"
    public_key: "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAz..."

    # optional
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    freeform_tags: {'Department': 'Finance'}

- name: Update instance_console_connection
  oci_compute_instance_console_connection:
    # required
    instance_console_connection_id: "ocid1.instanceconsoleconnection.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    freeform_tags: {'Department': 'Finance'}

- name: Delete instance_console_connection
  oci_compute_instance_console_connection:
    # required
    instance_console_connection_id: "ocid1.instanceconsoleconnection.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
instance_console_connection:
    description:
        - Details of the InstanceConsoleConnection resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The OCID of the compartment to contain the console connection.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        connection_string:
            description:
                - The SSH connection string for the console connection.
            returned: on success
            type: str
            sample: connection_string_example
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a
                  namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        fingerprint:
            description:
                - The SSH public key's fingerprint for client authentication to the console connection.
            returned: on success
            type: str
            sample: fingerprint_example
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        id:
            description:
                - The OCID of the console connection.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        instance_id:
            description:
                - The OCID of the instance the console connection connects to.
            returned: on success
            type: str
            sample: "ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current state of the console connection.
            returned: on success
            type: str
            sample: ACTIVE
        service_host_key_fingerprint:
            description:
                - The SSH public key's fingerprint for the console connection service host.
            returned: on success
            type: str
            sample: service_host_key_fingerprint_example
        vnc_connection_string:
            description:
                - The SSH connection string for the SSH tunnel used to
                  connect to the console connection over VNC.
            returned: on success
            type: str
            sample: vnc_connection_string_example
    sample: {
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "connection_string": "connection_string_example",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "fingerprint": "fingerprint_example",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "instance_id": "ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "ACTIVE",
        "service_host_key_fingerprint": "service_host_key_fingerprint_example",
        "vnc_connection_string": "vnc_connection_string_example"
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.core import ComputeClient
    from oci.core.models import CreateInstanceConsoleConnectionDetails
    from oci.core.models import UpdateInstanceConsoleConnectionDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class InstanceConsoleConnectionHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(
            InstanceConsoleConnectionHelperGen, self
        ).get_possible_entity_types() + [
            "instanceconsoleconnection",
            "instanceconsoleconnections",
            "coreinstanceconsoleconnection",
            "coreinstanceconsoleconnections",
            "instanceconsoleconnectionresource",
            "instanceconsoleconnectionsresource",
            "core",
        ]

    def get_module_resource_id_param(self):
        return "instance_console_connection_id"

    def get_module_resource_id(self):
        return self.module.params.get("instance_console_connection_id")

    def get_get_fn(self):
        return self.client.get_instance_console_connection

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_instance_console_connection,
            instance_console_connection_id=self.module.params.get(
                "instance_console_connection_id"
            ),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["instance_id"]

        return dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                self._use_name_as_identifier()
                or (
                    not self.module.params.get("key_by")
                    or param in self.module.params.get("key_by")
                )
            )
        )

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_instance_console_connections, **kwargs
        )

    def get_create_model_class(self):
        return CreateInstanceConsoleConnectionDetails

    def get_exclude_attributes(self):
        return ["public_key"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_instance_console_connection,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_instance_console_connection_details=create_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateInstanceConsoleConnectionDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_instance_console_connection,
            call_fn_args=(),
            call_fn_kwargs=dict(
                instance_console_connection_id=self.module.params.get(
                    "instance_console_connection_id"
                ),
                update_instance_console_connection_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_instance_console_connection,
            call_fn_args=(),
            call_fn_kwargs=dict(
                instance_console_connection_id=self.module.params.get(
                    "instance_console_connection_id"
                ),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


InstanceConsoleConnectionHelperCustom = get_custom_class(
    "InstanceConsoleConnectionHelperCustom"
)


class ResourceHelper(
    InstanceConsoleConnectionHelperCustom, InstanceConsoleConnectionHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            instance_id=dict(type="str"),
            public_key=dict(type="str"),
            defined_tags=dict(type="dict"),
            freeform_tags=dict(type="dict"),
            instance_console_connection_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="instance_console_connection",
        service_client_class=ComputeClient,
        namespace="core",
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()

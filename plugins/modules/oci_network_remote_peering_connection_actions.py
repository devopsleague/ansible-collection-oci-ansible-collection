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
module: oci_network_remote_peering_connection_actions
short_description: Perform actions on a RemotePeeringConnection resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a RemotePeeringConnection resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a remote peering connection (RPC) into a different compartment within the same tenancy. For information
      about moving resources between compartments, see
      L(Moving Resources to a Different Compartment,https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).
    - "For I(action=connect), connects this RPC to another one in a different region.
      This operation must be called by the VCN administrator who is designated as
      the *requestor* in the peering relationship. The *acceptor* must implement
      an Identity and Access Management (IAM) policy that gives the requestor permission
      to connect to RPCs in the acceptor's compartment. Without that permission, this
      operation will fail. For more information, see
      L(VCN Peering,https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/VCNpeering.htm)."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to move the
              remote peering connection to.
            - Required for I(action=change_compartment).
        type: str
    remote_peering_connection_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the remote peering connection (RPC).
        type: str
        aliases: ["id"]
        required: true
    peer_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the RPC you want to peer with.
            - Required for I(action=connect).
        type: str
    peer_region_name:
        description:
            - The name of the region that contains the RPC you want to peer with.
            - "Example: `us-ashburn-1`"
            - Required for I(action=connect).
        type: str
    action:
        description:
            - The action to perform on the RemotePeeringConnection.
        type: str
        required: true
        choices:
            - "change_compartment"
            - "connect"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on remote_peering_connection
  oci_network_remote_peering_connection_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    remote_peering_connection_id: "ocid1.remotepeeringconnection.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

- name: Perform action connect on remote_peering_connection
  oci_network_remote_peering_connection_actions:
    # required
    remote_peering_connection_id: "ocid1.remotepeeringconnection.oc1..xxxxxxEXAMPLExxxxxx"
    peer_id: "ocid1.peer.oc1..xxxxxxEXAMPLExxxxxx"
    peer_region_name: us-phoenix-1
    action: connect

"""

RETURN = """
remote_peering_connection:
    description:
        - Details of the RemotePeeringConnection resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment that contains the RPC.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a
                  namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        drg_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the DRG that this RPC belongs to.
            returned: on success
            type: str
            sample: "ocid1.drg.oc1..xxxxxxEXAMPLExxxxxx"
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
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the RPC.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        is_cross_tenancy_peering:
            description:
                - Whether the VCN at the other end of the peering is in a different tenancy.
                - "Example: `false`"
            returned: on success
            type: bool
            sample: true
        lifecycle_state:
            description:
                - The RPC's current lifecycle state.
            returned: on success
            type: str
            sample: AVAILABLE
        peer_id:
            description:
                - If this RPC is peered, this value is the L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the other RPC.
            returned: on success
            type: str
            sample: "ocid1.peer.oc1..xxxxxxEXAMPLExxxxxx"
        peer_region_name:
            description:
                - If this RPC is peered, this value is the region that contains the other RPC.
                - "Example: `us-ashburn-1`"
            returned: on success
            type: str
            sample: us-phoenix-1
        peer_tenancy_id:
            description:
                - If this RPC is peered, this value is the L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the other
                  RPC's tenancy.
            returned: on success
            type: str
            sample: "ocid1.peertenancy.oc1..xxxxxxEXAMPLExxxxxx"
        peering_status:
            description:
                - Whether the RPC is peered with another RPC. `NEW` means the RPC has not yet been
                  peered. `PENDING` means the peering is being established. `REVOKED` means the
                  RPC at the other end of the peering has been deleted.
            returned: on success
            type: str
            sample: INVALID
        time_created:
            description:
                - The date and time the RPC was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: {
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "drg_id": "ocid1.drg.oc1..xxxxxxEXAMPLExxxxxx",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "is_cross_tenancy_peering": true,
        "lifecycle_state": "AVAILABLE",
        "peer_id": "ocid1.peer.oc1..xxxxxxEXAMPLExxxxxx",
        "peer_region_name": "us-phoenix-1",
        "peer_tenancy_id": "ocid1.peertenancy.oc1..xxxxxxEXAMPLExxxxxx",
        "peering_status": "INVALID",
        "time_created": "2013-10-20T19:20:30+01:00"
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.core import VirtualNetworkClient
    from oci.core.models import ChangeRemotePeeringConnectionCompartmentDetails
    from oci.core.models import ConnectRemotePeeringConnectionsDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class RemotePeeringConnectionActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
        connect
    """

    @staticmethod
    def get_module_resource_id_param():
        return "remote_peering_connection_id"

    def get_module_resource_id(self):
        return self.module.params.get("remote_peering_connection_id")

    def get_get_fn(self):
        return self.client.get_remote_peering_connection

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_remote_peering_connection,
            remote_peering_connection_id=self.module.params.get(
                "remote_peering_connection_id"
            ),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeRemotePeeringConnectionCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_remote_peering_connection_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                remote_peering_connection_id=self.module.params.get(
                    "remote_peering_connection_id"
                ),
                change_remote_peering_connection_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )

    def connect(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ConnectRemotePeeringConnectionsDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.connect_remote_peering_connections,
            call_fn_args=(),
            call_fn_kwargs=dict(
                remote_peering_connection_id=self.module.params.get(
                    "remote_peering_connection_id"
                ),
                connect_remote_peering_connections_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )


RemotePeeringConnectionActionsHelperCustom = get_custom_class(
    "RemotePeeringConnectionActionsHelperCustom"
)


class ResourceHelper(
    RemotePeeringConnectionActionsHelperCustom, RemotePeeringConnectionActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            remote_peering_connection_id=dict(
                aliases=["id"], type="str", required=True
            ),
            peer_id=dict(type="str"),
            peer_region_name=dict(type="str"),
            action=dict(
                type="str", required=True, choices=["change_compartment", "connect"]
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="remote_peering_connection",
        service_client_class=VirtualNetworkClient,
        namespace="core",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()

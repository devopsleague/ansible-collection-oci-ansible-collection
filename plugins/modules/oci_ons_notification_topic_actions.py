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
module: oci_ons_notification_topic_actions
short_description: Perform actions on a NotificationTopic resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a NotificationTopic resource in Oracle Cloud Infrastructure
    - "For I(action=change_compartment), moves a topic into a different compartment within the same tenancy. For information about moving resources
      between compartments, see
      L(Moving Resources to a Different Compartment,https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).
      Transactions Per Minute (TPM) per-tenancy limit for this operation: 60."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    topic_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the topic to move.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to move the specified topic
              or subscription to.
        type: str
        required: true
    action:
        description:
            - The action to perform on the NotificationTopic.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on notification_topic
  oci_ons_notification_topic_actions:
    # required
    topic_id: "ocid1.topic.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
notification_topic:
    description:
        - Details of the NotificationTopic resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        name:
            description:
                - The name of the topic.
            returned: on success
            type: str
            sample: name_example
        topic_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the topic.
            returned: on success
            type: str
            sample: "ocid1.topic.oc1..xxxxxxEXAMPLExxxxxx"
        short_topic_id:
            description:
                - A unique short topic Id. This is used only for SMS subscriptions.
            returned: on success
            type: str
            sample: "ocid1.shorttopic.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment for the topic.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The lifecycle state of the topic.
            returned: on success
            type: str
            sample: ACTIVE
        description:
            description:
                - The description of the topic.
            returned: on success
            type: str
            sample: description_example
        time_created:
            description:
                - The time the topic was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        etag:
            description:
                - For optimistic concurrency control. See `if-match`.
            returned: on success
            type: str
            sample: etag_example
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see
                  L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        api_endpoint:
            description:
                - The endpoint for managing subscriptions or publishing messages to the topic.
            returned: on success
            type: str
            sample: api_endpoint_example
    sample: {
        "name": "name_example",
        "topic_id": "ocid1.topic.oc1..xxxxxxEXAMPLExxxxxx",
        "short_topic_id": "ocid1.shorttopic.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "ACTIVE",
        "description": "description_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "etag": "etag_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "api_endpoint": "api_endpoint_example"
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
    from oci.ons import NotificationControlPlaneClient
    from oci.ons.models import ChangeCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class NotificationTopicActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "topic_id"

    def get_module_resource_id(self):
        return self.module.params.get("topic_id")

    def get_get_fn(self):
        return self.client.get_topic

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_topic, topic_id=self.module.params.get("topic_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_topic_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                topic_id=self.module.params.get("topic_id"),
                change_topic_compartment_details=action_details,
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


NotificationTopicActionsHelperCustom = get_custom_class(
    "NotificationTopicActionsHelperCustom"
)


class ResourceHelper(
    NotificationTopicActionsHelperCustom, NotificationTopicActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            topic_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="notification_topic",
        service_client_class=NotificationControlPlaneClient,
        namespace="ons",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()

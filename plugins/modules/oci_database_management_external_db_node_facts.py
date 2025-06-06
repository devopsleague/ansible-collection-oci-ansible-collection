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
module: oci_database_management_external_db_node_facts
short_description: Fetches details about one or multiple ExternalDbNode resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ExternalDbNode resources in Oracle Cloud Infrastructure
    - Lists the external DB nodes in the specified external DB system.
    - If I(external_db_node_id) is specified, the details of a single ExternalDbNode will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    external_db_node_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external database node.
            - Required to get a specific external_db_node.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
        type: str
    external_db_system_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external DB system.
        type: str
    display_name:
        description:
            - A filter to only return the resources that match the entire display name.
        type: str
        aliases: ["name"]
    sort_by:
        description:
            - The field to sort information by. Only one sortOrder can be used. The default sort order
              for `TIMECREATED` is descending and the default sort order for `DISPLAYNAME` is ascending.
              The `DISPLAYNAME` sort order is case-sensitive.
        type: str
        choices:
            - "TIMECREATED"
            - "DISPLAYNAME"
    sort_order:
        description:
            - The option to sort information in ascending ('ASC') or descending ('DESC') order. Ascending order is the default order.
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific external_db_node
  oci_database_management_external_db_node_facts:
    # required
    external_db_node_id: "ocid1.externaldbnode.oc1..xxxxxxEXAMPLExxxxxx"

- name: List external_db_nodes
  oci_database_management_external_db_node_facts:

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    external_db_system_id: "ocid1.externaldbsystem.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    sort_by: TIMECREATED
    sort_order: ASC

"""

RETURN = """
external_db_nodes:
    description:
        - List of ExternalDbNode resources
    returned: on success
    type: complex
    contains:
        cpu_core_count:
            description:
                - The number of CPU cores available on the DB node.
                - Returned for get operation
            returned: on success
            type: float
            sample: 3.4
        memory_size_in_gbs:
            description:
                - The total memory in gigabytes (GB) on the DB node.
                - Returned for get operation
            returned: on success
            type: float
            sample: 3.4
        additional_details:
            description:
                - "The additional details of the external DB node defined in `{\\"key\\": \\"value\\"}` format.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
                - Returned for get operation
            returned: on success
            type: dict
            sample: {}
        domain_name:
            description:
                - Name of the domain.
                - Returned for get operation
            returned: on success
            type: str
            sample: domain_name_example
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external DB node.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The user-friendly name for the external DB node. The name does not have to be unique.
            returned: on success
            type: str
            sample: display_name_example
        component_name:
            description:
                - The name of the external DB node.
            returned: on success
            type: str
            sample: component_name_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        external_db_system_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external DB system that the DB node is a part of.
            returned: on success
            type: str
            sample: "ocid1.externaldbsystem.oc1..xxxxxxEXAMPLExxxxxx"
        external_connector_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external connector.
            returned: on success
            type: str
            sample: "ocid1.externalconnector.oc1..xxxxxxEXAMPLExxxxxx"
        host_name:
            description:
                - The host name for the DB node.
            returned: on success
            type: str
            sample: host_name_example
        lifecycle_state:
            description:
                - The current lifecycle state of the external DB node.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - Additional information about the current lifecycle state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        time_created:
            description:
                - The date and time the external DB node was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time the external DB node was last updated.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: [{
        "cpu_core_count": 3.4,
        "memory_size_in_gbs": 3.4,
        "additional_details": {},
        "domain_name": "domain_name_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "component_name": "component_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "external_db_system_id": "ocid1.externaldbsystem.oc1..xxxxxxEXAMPLExxxxxx",
        "external_connector_id": "ocid1.externalconnector.oc1..xxxxxxEXAMPLExxxxxx",
        "host_name": "host_name_example",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.database_management import DbManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ExternalDbNodeFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "external_db_node_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_external_db_node,
            external_db_node_id=self.module.params.get("external_db_node_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "external_db_system_id",
            "display_name",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_external_db_nodes, **optional_kwargs
        )


ExternalDbNodeFactsHelperCustom = get_custom_class("ExternalDbNodeFactsHelperCustom")


class ResourceFactsHelper(
    ExternalDbNodeFactsHelperCustom, ExternalDbNodeFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            external_db_node_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            external_db_system_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="external_db_node",
        service_client_class=DbManagementClient,
        namespace="database_management",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(external_db_nodes=result)


if __name__ == "__main__":
    main()

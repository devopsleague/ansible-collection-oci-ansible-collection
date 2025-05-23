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
module: oci_data_catalog_type_facts
short_description: Fetches details about one or multiple Type resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Type resources in Oracle Cloud Infrastructure
    - Returns a list of all types within a data catalog.
    - If I(type_key) is specified, the details of a single Type will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    type_key:
        description:
            - Unique type key.
            - Required to get a specific type.
        type: str
    catalog_id:
        description:
            - Unique catalog identifier.
        type: str
        required: true
    name:
        description:
            - Immutable resource name.
        type: str
    lifecycle_state:
        description:
            - A filter to return only resources that match the specified lifecycle state. The value is case insensitive.
        type: str
        choices:
            - "CREATING"
            - "ACTIVE"
            - "INACTIVE"
            - "UPDATING"
            - "DELETING"
            - "DELETED"
            - "FAILED"
            - "MOVING"
    is_internal:
        description:
            - Indicates whether the type is internal, making it unavailable for use by metadata elements.
        type: str
    is_tag:
        description:
            - Indicates whether the type can be used for tagging metadata elements.
        type: str
    is_approved:
        description:
            - Indicates whether the type is approved for use as a classifying object.
        type: str
    external_type_name:
        description:
            - Data type as defined in an external system.
        type: str
    type_category:
        description:
            - Indicates the category of this type . For example, data assets or connections.
        type: str
    fields:
        description:
            - Specifies the fields to return in a type response.
        type: list
        elements: str
        choices:
            - "key"
            - "description"
            - "name"
            - "catalogId"
            - "properties"
            - "isInternal"
            - "isTag"
            - "isApproved"
            - "typeCategory"
            - "externalTypeName"
            - "lifecycleState"
            - "uri"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is
              ascending. If no value is specified TIMECREATED is default.
        type: str
        choices:
            - "TIMECREATED"
            - "DISPLAYNAME"
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific type
  oci_data_catalog_type_facts:
    # required
    type_key: type_key_example
    catalog_id: "ocid1.catalog.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    fields: [ "key" ]

- name: List types
  oci_data_catalog_type_facts:
    # required
    catalog_id: "ocid1.catalog.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    name: name_example
    lifecycle_state: CREATING
    is_internal: is_internal_example
    is_tag: is_tag_example
    is_approved: is_approved_example
    external_type_name: external_type_name_example
    type_category: type_category_example
    fields: [ "key" ]
    sort_by: TIMECREATED
    sort_order: ASC

"""

RETURN = """
types:
    description:
        - List of Type resources
    returned: on success
    type: complex
    contains:
        properties:
            description:
                - |
                  "A map of arrays which defines the type specific properties, both required and optional. The map keys are
                  category names and the values are arrays contiaing all property details. Every property is contained inside
                  of a category. Most types have required properties within the \\"default\\" category.
                  Example:
                  `{
                     \\"properties\\": {
                       \\"default\\": {
                         \\"attributes:\\": [
                           {
                             \\"name\\": \\"host\\",
                             \\"type\\": \\"string\\",
                             \\"isRequired\\": true,
                             \\"isUpdatable\\": false
                           },
                           ...
                         ]
                       }
                     }
                   }`"
                - Returned for get operation
            returned: on success
            type: dict
            sample: {}
        is_internal:
            description:
                - Indicates whether the type is internal, making it unavailable for use by metadata elements.
                - Returned for get operation
            returned: on success
            type: bool
            sample: true
        is_tag:
            description:
                - Indicates whether the type can be used for tagging metadata elements.
                - Returned for get operation
            returned: on success
            type: bool
            sample: true
        is_approved:
            description:
                - Indicates whether the type is approved for use as a classifying object.
                - Returned for get operation
            returned: on success
            type: bool
            sample: true
        external_type_name:
            description:
                - Mapping type equivalence in the external system.
                - Returned for get operation
            returned: on success
            type: str
            sample: external_type_name_example
        custom_properties:
            description:
                - Custom properties associated with this Type.
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                key:
                    description:
                        - Unique custom property key that is immutable.
                    returned: on success
                    type: str
                    sample: key_example
                display_name:
                    description:
                        - Display name of the custom property
                    returned: on success
                    type: str
                    sample: display_name_example
                description:
                    description:
                        - Description of the custom property
                    returned: on success
                    type: str
                    sample: description_example
                data_type:
                    description:
                        - Data type of the custom property
                    returned: on success
                    type: str
                    sample: TEXT
                namespace_name:
                    description:
                        - Namespace name of the custom property
                    returned: on success
                    type: str
                    sample: namespace_name_example
                is_sortable:
                    description:
                        - If this field allows to sort from UI
                    returned: on success
                    type: bool
                    sample: true
                is_filterable:
                    description:
                        - If this field allows to filter or create facets from UI
                    returned: on success
                    type: bool
                    sample: true
                is_multi_valued:
                    description:
                        - If this field allows multiple values to be set
                    returned: on success
                    type: bool
                    sample: true
                is_hidden:
                    description:
                        - If this field is a hidden field
                    returned: on success
                    type: bool
                    sample: true
                is_editable:
                    description:
                        - If this field is a editable field
                    returned: on success
                    type: bool
                    sample: true
                is_shown_in_list:
                    description:
                        - If this field is displayed in a list view of applicable objects.
                    returned: on success
                    type: bool
                    sample: true
                is_service_defined:
                    description:
                        - If this field is defined by service or by a user
                    returned: on success
                    type: bool
                    sample: true
                is_hidden_in_search:
                    description:
                        - If this field is allowed to pop in search results
                    returned: on success
                    type: bool
                    sample: true
                time_created:
                    description:
                        - "The date and time the custom property was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                          Example: `2019-03-25T21:10:29.600Z`"
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                lifecycle_state:
                    description:
                        - The current state of the custom property.
                    returned: on success
                    type: str
                    sample: CREATING
                usage_count:
                    description:
                        - Total number of first class objects using this custom property
                    returned: on success
                    type: int
                    sample: 56
                scope:
                    description:
                        - Type or scope of the custom property belongs to. This will be an array of type id it will be belongs to
                    returned: on success
                    type: complex
                    contains:
                        type_id:
                            description:
                                - Unique type key identifier
                            returned: on success
                            type: str
                            sample: "ocid1.type.oc1..xxxxxxEXAMPLExxxxxx"
                        type_name:
                            description:
                                - Name of the type associated with
                            returned: on success
                            type: str
                            sample: type_name_example
                        count:
                            description:
                                - Number of objects associated with this type
                            returned: on success
                            type: int
                            sample: 56
                        is_event_enabled:
                            description:
                                - If an OCI Event will be emitted when the custom property is modified.
                            returned: on success
                            type: bool
                            sample: true
                allowed_values:
                    description:
                        - Allowed values for the custom property if any
                    returned: on success
                    type: list
                    sample: []
                time_updated:
                    description:
                        - The last time that any change was made to the custom property. An L(RFC3339,https://tools.ietf.org/html/rfc3339) formatted datetime
                          string.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                created_by_id:
                    description:
                        - OCID of the user who created the custom property.
                    returned: on success
                    type: str
                    sample: "ocid1.createdby.oc1..xxxxxxEXAMPLExxxxxx"
                updated_by_id:
                    description:
                        - OCID of the user who last modified the custom property.
                    returned: on success
                    type: str
                    sample: "ocid1.updatedby.oc1..xxxxxxEXAMPLExxxxxx"
                is_event_enabled:
                    description:
                        - If an OCI Event will be emitted when the custom property is modified.
                    returned: on success
                    type: bool
                    sample: true
                events:
                    description:
                        - Event configuration for this custom property, against the desired subset of object types to which the property applies.
                    returned: on success
                    type: complex
                    contains:
                        type_id:
                            description:
                                - Unique type key identifier.
                            returned: on success
                            type: str
                            sample: "ocid1.type.oc1..xxxxxxEXAMPLExxxxxx"
                        type_name:
                            description:
                                - Name of the type.
                            returned: on success
                            type: str
                            sample: type_name_example
                        property_id:
                            description:
                                - Unique property key identifier.
                            returned: on success
                            type: str
                            sample: "ocid1.property.oc1..xxxxxxEXAMPLExxxxxx"
                        property_name:
                            description:
                                - Name of the property.
                            returned: on success
                            type: str
                            sample: property_name_example
                        event_config_status:
                            description:
                                - Status of the configuration.
                            returned: on success
                            type: str
                            sample: ENABLED
                        time_created:
                            description:
                                - "The date and time the event was configured, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                                  Example: `2019-03-25T21:10:29.600Z`"
                            returned: on success
                            type: str
                            sample: "2013-10-20T19:20:30+01:00"
                        time_updated:
                            description:
                                - The last time that any change was made to the configuration. An L(RFC3339,https://tools.ietf.org/html/rfc3339) formatted
                                  datetime string.
                            returned: on success
                            type: str
                            sample: "2013-10-20T19:20:30+01:00"
                        created_by_id:
                            description:
                                - OCID of the user who created the configuration.
                            returned: on success
                            type: str
                            sample: "ocid1.createdby.oc1..xxxxxxEXAMPLExxxxxx"
                        updated_by_id:
                            description:
                                - OCID of the user who last modified the configuration.
                            returned: on success
                            type: str
                            sample: "ocid1.updatedby.oc1..xxxxxxEXAMPLExxxxxx"
        key:
            description:
                - Unique type key that is immutable.
            returned: on success
            type: str
            sample: key_example
        name:
            description:
                - The immutable name of the type.
            returned: on success
            type: str
            sample: name_example
        description:
            description:
                - Detailed description of the type.
            returned: on success
            type: str
            sample: description_example
        catalog_id:
            description:
                - The data catalog's OCID.
            returned: on success
            type: str
            sample: "ocid1.catalog.oc1..xxxxxxEXAMPLExxxxxx"
        type_category:
            description:
                - Indicates the category this type belongs to. For instance, data assets, connections.
            returned: on success
            type: str
            sample: type_category_example
        uri:
            description:
                - URI to the type instance in the API.
            returned: on success
            type: str
            sample: uri_example
        lifecycle_state:
            description:
                - The current state of the type.
            returned: on success
            type: str
            sample: CREATING
        parent_type_key:
            description:
                - Unique key of the parent type.
            returned: on success
            type: str
            sample: parent_type_key_example
        parent_type_name:
            description:
                - Name of the parent type.
            returned: on success
            type: str
            sample: parent_type_name_example
    sample: [{
        "properties": {},
        "is_internal": true,
        "is_tag": true,
        "is_approved": true,
        "external_type_name": "external_type_name_example",
        "custom_properties": [{
            "key": "key_example",
            "display_name": "display_name_example",
            "description": "description_example",
            "data_type": "TEXT",
            "namespace_name": "namespace_name_example",
            "is_sortable": true,
            "is_filterable": true,
            "is_multi_valued": true,
            "is_hidden": true,
            "is_editable": true,
            "is_shown_in_list": true,
            "is_service_defined": true,
            "is_hidden_in_search": true,
            "time_created": "2013-10-20T19:20:30+01:00",
            "lifecycle_state": "CREATING",
            "usage_count": 56,
            "scope": [{
                "type_id": "ocid1.type.oc1..xxxxxxEXAMPLExxxxxx",
                "type_name": "type_name_example",
                "count": 56,
                "is_event_enabled": true
            }],
            "allowed_values": [],
            "time_updated": "2013-10-20T19:20:30+01:00",
            "created_by_id": "ocid1.createdby.oc1..xxxxxxEXAMPLExxxxxx",
            "updated_by_id": "ocid1.updatedby.oc1..xxxxxxEXAMPLExxxxxx",
            "is_event_enabled": true,
            "events": [{
                "type_id": "ocid1.type.oc1..xxxxxxEXAMPLExxxxxx",
                "type_name": "type_name_example",
                "property_id": "ocid1.property.oc1..xxxxxxEXAMPLExxxxxx",
                "property_name": "property_name_example",
                "event_config_status": "ENABLED",
                "time_created": "2013-10-20T19:20:30+01:00",
                "time_updated": "2013-10-20T19:20:30+01:00",
                "created_by_id": "ocid1.createdby.oc1..xxxxxxEXAMPLExxxxxx",
                "updated_by_id": "ocid1.updatedby.oc1..xxxxxxEXAMPLExxxxxx"
            }]
        }],
        "key": "key_example",
        "name": "name_example",
        "description": "description_example",
        "catalog_id": "ocid1.catalog.oc1..xxxxxxEXAMPLExxxxxx",
        "type_category": "type_category_example",
        "uri": "uri_example",
        "lifecycle_state": "CREATING",
        "parent_type_key": "parent_type_key_example",
        "parent_type_name": "parent_type_name_example"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.data_catalog import DataCatalogClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataCatalogTypeFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "catalog_id",
            "type_key",
        ]

    def get_required_params_for_list(self):
        return [
            "catalog_id",
        ]

    def get_resource(self):
        optional_get_method_params = [
            "fields",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_type,
            catalog_id=self.module.params.get("catalog_id"),
            type_key=self.module.params.get("type_key"),
            **optional_kwargs
        )

    def list_resources(self):
        optional_list_method_params = [
            "name",
            "lifecycle_state",
            "is_internal",
            "is_tag",
            "is_approved",
            "external_type_name",
            "type_category",
            "fields",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_types,
            catalog_id=self.module.params.get("catalog_id"),
            **optional_kwargs
        )


DataCatalogTypeFactsHelperCustom = get_custom_class("DataCatalogTypeFactsHelperCustom")


class ResourceFactsHelper(
    DataCatalogTypeFactsHelperCustom, DataCatalogTypeFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            type_key=dict(type="str", no_log=True),
            catalog_id=dict(type="str", required=True),
            name=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "ACTIVE",
                    "INACTIVE",
                    "UPDATING",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                    "MOVING",
                ],
            ),
            is_internal=dict(type="str"),
            is_tag=dict(type="str"),
            is_approved=dict(type="str"),
            external_type_name=dict(type="str"),
            type_category=dict(type="str"),
            fields=dict(
                type="list",
                elements="str",
                choices=[
                    "key",
                    "description",
                    "name",
                    "catalogId",
                    "properties",
                    "isInternal",
                    "isTag",
                    "isApproved",
                    "typeCategory",
                    "externalTypeName",
                    "lifecycleState",
                    "uri",
                ],
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
        resource_type="type",
        service_client_class=DataCatalogClient,
        namespace="data_catalog",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(types=result)


if __name__ == "__main__":
    main()

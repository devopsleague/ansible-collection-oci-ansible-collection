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
module: oci_network_vcn
short_description: Manage a Vcn resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Vcn resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new virtual cloud network (VCN). For more information, see
      L(VCNs and Subnets,https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingVCNs.htm).
    - "For the VCN, you specify a list of one or more IPv4 CIDR blocks that meet the following criteria:"
    - "- The CIDR blocks must be valid.
      - They must not overlap with each other or with the on-premises network CIDR block.
      - The number of CIDR blocks does not exceed the limit of CIDR blocks allowed per VCN."
    - "For a CIDR block, Oracle recommends that you use one of the private IP address ranges specified in L(RFC 1918,https://tools.ietf.org/html/rfc1918)
      (10.0.0.0/8, 172.16/12, and 192.168/16). Example:
      172.16.0.0/16. The CIDR blocks can range from /16 to /30."
    - For the purposes of access control, you must provide the L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the
      compartment where you want the VCN to
      reside. Consult an Oracle Cloud Infrastructure administrator in your organization if you're not sure which
      compartment to use. Notice that the VCN doesn't have to be in the same compartment as the subnets or other
      Networking Service components. For more information about compartments and access control, see
      L(Overview of the IAM Service,https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/overview.htm). For information about OCIDs, see
      L(Resource Identifiers,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
    - "You may optionally specify a *display name* for the VCN, otherwise a default is provided. It does not have to
      be unique, and you can change it. Avoid entering confidential information."
    - You can also add a DNS label for the VCN, which is required if you want the instances to use the
      Interent and VCN Resolver option for DNS in the VCN. For more information, see
      L(DNS in Your Virtual Cloud Network,https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/dns.htm).
    - The VCN automatically comes with a default route table, default security list, and default set of DHCP options.
      The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) for each is returned in the response. You can't delete these
      default objects, but you can change their
      contents (that is, change the route rules, security list rules, and so on).
    - The VCN and subnets you create are not accessible until you attach an internet gateway or set up a Site-to-Site VPN
      or FastConnect. For more information, see
      L(Overview of the Networking Service,https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/overview.htm).
    - "This resource has the following action operations in the M(oracle.oci.oci_network_vcn_actions) module: add_ipv6_vcn_cidr, add_vcn_cidr,
      change_compartment, modify_vcn_cidr, remove_ipv6_vcn_cidr, remove_vcn_cidr."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    cidr_block:
        description:
            - "**Deprecated.** Do *not* set this value. Use `cidrBlocks` instead.
              Example: `10.0.0.0/16`"
        type: str
    cidr_blocks:
        description:
            - "The list of one or more IPv4 CIDR blocks for the VCN that meet the following criteria:
              - The CIDR blocks must be valid.
              - They must not overlap with each other or with the on-premises network CIDR block.
              - The number of CIDR blocks must not exceed the limit of CIDR blocks allowed per VCN."
            - "**Important:** Do *not* specify a value for `cidrBlock`. Use this parameter instead."
        type: list
        elements: str
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to contain the VCN.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    ipv6_private_cidr_blocks:
        description:
            - "The list of one or more ULA or Private IPv6 prefixes for the VCN that meets the following criteria:
              - The CIDR blocks must be valid.
              - Multiple CIDR blocks must not overlap each other or the on-premises network prefix.
              - The number of CIDR blocks must not exceed the limit of IPv6 prefixes allowed to a VCN."
            - "**Important:** Do *not* specify a value for `ipv6CidrBlock`. Use this parameter instead."
        type: list
        elements: str
    is_oracle_gua_allocation_enabled:
        description:
            - Specifies whether to skip Oracle allocated IPv6 GUA. By default, Oracle will allocate one GUA of /56
              size for an IPv6 enabled VCN.
        type: bool
    byoipv6_cidr_details:
        description:
            - The list of BYOIPv6 OCIDs and BYOIPv6 prefixes required to create a VCN that uses BYOIPv6 address ranges.
        type: list
        elements: dict
        suboptions:
            byoipv6_range_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the `ByoipRange` resource to which the CIDR
                      block belongs.
                type: str
                required: true
            ipv6_cidr_block:
                description:
                    - "An IPv6 prefix required to create a VCN with a BYOIP prefix. It could be the whole prefix identified in `byoipv6RangeId`, or a subrange.
                      Example: `2001:0db8:0123::/48`"
                type: str
                required: true
    dns_label:
        description:
            - A DNS label for the VCN, used in conjunction with the VNIC's hostname and
              subnet's DNS label to form a fully qualified domain name (FQDN) for each VNIC
              within this subnet (for example, `bminstance1.subnet123.vcn1.oraclevcn.com`).
              Not required to be unique, but it's a best practice to set unique DNS labels
              for VCNs in your tenancy. Must be an alphanumeric string that begins with a letter.
              The value cannot be changed.
            - You must set this value if you want instances to be able to use hostnames to
              resolve other instances in the VCN. Otherwise the Internet and VCN Resolver
              will not work.
            - For more information, see
              L(DNS in Your Virtual Cloud Network,https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/dns.htm).
            - "Example: `vcn1`"
        type: str
    is_ipv6_enabled:
        description:
            - Whether IPv6 is enabled for the VCN. Default is `false`.
              If enabled, Oracle will assign the VCN a IPv6 /56 CIDR block.
              You may skip having Oracle allocate the VCN a IPv6 /56 CIDR block by setting isOracleGuaAllocationEnabled to `false`.
              For important details about IPv6 addressing in a VCN, see L(IPv6 Addresses,https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/ipv6.htm).
            - "Example: `true`"
        type: bool
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a
              namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    display_name:
        description:
            - A user-friendly name. Does not have to be unique, and it's changeable.
              Avoid entering confidential information.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no
              predefined name, type, or namespace. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    vcn_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VCN.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the Vcn.
            - Use I(state=present) to create or update a Vcn.
            - Use I(state=absent) to delete a Vcn.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create vcn
  oci_network_vcn:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    cidr_block: cidr_block_example
    cidr_blocks: [ "cidr_blocks_example" ]
    ipv6_private_cidr_blocks: [ "ipv6_private_cidr_blocks_example" ]
    is_oracle_gua_allocation_enabled: true
    byoipv6_cidr_details:
    - # required
      byoipv6_range_id: "ocid1.byoipv6range.oc1..xxxxxxEXAMPLExxxxxx"
      ipv6_cidr_block: ipv6_cidr_block_example
    dns_label: dns_label_example
    is_ipv6_enabled: true
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}

- name: Update vcn
  oci_network_vcn:
    # required
    vcn_id: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}

- name: Update vcn using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_network_vcn:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    freeform_tags: {'Department': 'Finance'}

- name: Delete vcn
  oci_network_vcn:
    # required
    vcn_id: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete vcn using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_network_vcn:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
vcn:
    description:
        - Details of the Vcn resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        byoipv6_cidr_blocks:
            description:
                - The list of BYOIPv6 prefixes required to create a VCN that uses BYOIPv6 ranges.
            returned: on success
            type: list
            sample: []
        ipv6_private_cidr_blocks:
            description:
                - For an IPv6-enabled VCN, this is the list of Private IPv6 prefixes for the VCN's IP address space.
            returned: on success
            type: list
            sample: []
        cidr_block:
            description:
                - Deprecated. The first CIDR IP address from cidrBlocks.
                - "Example: `172.16.0.0/16`"
            returned: on success
            type: str
            sample: cidr_block_example
        cidr_blocks:
            description:
                - The list of IPv4 CIDR blocks the VCN will use.
            returned: on success
            type: list
            sample: []
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the VCN.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        default_dhcp_options_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) for the VCN's default set of DHCP options.
            returned: on success
            type: str
            sample: "ocid1.defaultdhcpoptions.oc1..xxxxxxEXAMPLExxxxxx"
        default_route_table_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) for the VCN's default route table.
            returned: on success
            type: str
            sample: "ocid1.defaultroutetable.oc1..xxxxxxEXAMPLExxxxxx"
        default_security_list_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) for the VCN's default security list.
            returned: on success
            type: str
            sample: "ocid1.defaultsecuritylist.oc1..xxxxxxEXAMPLExxxxxx"
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
        dns_label:
            description:
                - A DNS label for the VCN, used in conjunction with the VNIC's hostname and
                  subnet's DNS label to form a fully qualified domain name (FQDN) for each VNIC
                  within this subnet (for example, `bminstance1.subnet123.vcn1.oraclevcn.com`).
                  Must be an alphanumeric string that begins with a letter.
                  The value cannot be changed.
                - The absence of this parameter means the Internet and VCN Resolver will
                  not work for this VCN.
                - For more information, see
                  L(DNS in Your Virtual Cloud Network,https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/dns.htm).
                - "Example: `vcn1`"
            returned: on success
            type: str
            sample: dns_label_example
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
                - The VCN's Oracle ID (L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm)).
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        ipv6_cidr_blocks:
            description:
                - For an IPv6-enabled VCN, this is the list of IPv6 prefixes for the VCN's IP address space.
                  The prefixes are provided by Oracle and the sizes are always /56.
            returned: on success
            type: list
            sample: []
        lifecycle_state:
            description:
                - The VCN's current state.
            returned: on success
            type: str
            sample: PROVISIONING
        time_created:
            description:
                - The date and time the VCN was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        vcn_domain_name:
            description:
                - The VCN's domain name, which consists of the VCN's DNS label, and the
                  `oraclevcn.com` domain.
                - For more information, see
                  L(DNS in Your Virtual Cloud Network,https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/dns.htm).
                - "Example: `vcn1.oraclevcn.com`"
            returned: on success
            type: str
            sample: vcn_domain_name_example
    sample: {
        "byoipv6_cidr_blocks": [],
        "ipv6_private_cidr_blocks": [],
        "cidr_block": "cidr_block_example",
        "cidr_blocks": [],
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "default_dhcp_options_id": "ocid1.defaultdhcpoptions.oc1..xxxxxxEXAMPLExxxxxx",
        "default_route_table_id": "ocid1.defaultroutetable.oc1..xxxxxxEXAMPLExxxxxx",
        "default_security_list_id": "ocid1.defaultsecuritylist.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "dns_label": "dns_label_example",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "ipv6_cidr_blocks": [],
        "lifecycle_state": "PROVISIONING",
        "time_created": "2013-10-20T19:20:30+01:00",
        "vcn_domain_name": "vcn_domain_name_example"
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
    from oci.core import VirtualNetworkClient
    from oci.core.models import CreateVcnDetails
    from oci.core.models import UpdateVcnDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class VcnHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(VcnHelperGen, self).get_possible_entity_types() + [
            "vcn",
            "vcns",
            "corevcn",
            "corevcns",
            "vcnresource",
            "vcnsresource",
            "core",
        ]

    def get_module_resource_id_param(self):
        return "vcn_id"

    def get_module_resource_id(self):
        return self.module.params.get("vcn_id")

    def get_get_fn(self):
        return self.client.get_vcn

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_vcn, vcn_id=self.module.params.get("vcn_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["display_name"]

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
        return oci_common_utils.list_all_resources(self.client.list_vcns, **kwargs)

    def get_create_model_class(self):
        return CreateVcnDetails

    def get_exclude_attributes(self):
        return [
            "byoipv6_cidr_details",
            "is_oracle_gua_allocation_enabled",
            "is_ipv6_enabled",
        ]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_vcn,
            call_fn_args=(),
            call_fn_kwargs=dict(create_vcn_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateVcnDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_vcn,
            call_fn_args=(),
            call_fn_kwargs=dict(
                vcn_id=self.module.params.get("vcn_id"),
                update_vcn_details=update_details,
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
            call_fn=self.client.delete_vcn,
            call_fn_args=(),
            call_fn_kwargs=dict(vcn_id=self.module.params.get("vcn_id"),),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


VcnHelperCustom = get_custom_class("VcnHelperCustom")


class ResourceHelper(VcnHelperCustom, VcnHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            cidr_block=dict(type="str"),
            cidr_blocks=dict(type="list", elements="str"),
            compartment_id=dict(type="str"),
            ipv6_private_cidr_blocks=dict(type="list", elements="str"),
            is_oracle_gua_allocation_enabled=dict(type="bool"),
            byoipv6_cidr_details=dict(
                type="list",
                elements="dict",
                options=dict(
                    byoipv6_range_id=dict(type="str", required=True),
                    ipv6_cidr_block=dict(type="str", required=True),
                ),
            ),
            dns_label=dict(type="str"),
            is_ipv6_enabled=dict(type="bool"),
            defined_tags=dict(type="dict"),
            display_name=dict(aliases=["name"], type="str"),
            freeform_tags=dict(type="dict"),
            vcn_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="vcn",
        service_client_class=VirtualNetworkClient,
        namespace="core",
    )

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()

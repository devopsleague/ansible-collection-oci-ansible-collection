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
module: oci_blockstorage_boot_volume_kms_key_facts
short_description: Fetches details about a BootVolumeKmsKey resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a BootVolumeKmsKey resource in Oracle Cloud Infrastructure
    - Gets the Vault service encryption key assigned to the specified boot volume.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    boot_volume_id:
        description:
            - The OCID of the boot volume.
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific boot_volume_kms_key
  oci_blockstorage_boot_volume_kms_key_facts:
    # required
    boot_volume_id: "ocid1.bootvolume.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
boot_volume_kms_key:
    description:
        - BootVolumeKmsKey resource
    returned: on success
    type: complex
    contains:
        kms_key_id:
            description:
                - The OCID of the Vault service key assigned to this volume. If the volume is not using Vault service, then the `kmsKeyId` will be a null
                  string.
            returned: on success
            type: str
            sample: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
    sample: {
        "kms_key_id": "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.core import BlockstorageClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class BootVolumeKmsKeyFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "boot_volume_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_boot_volume_kms_key,
            boot_volume_id=self.module.params.get("boot_volume_id"),
        )


BootVolumeKmsKeyFactsHelperCustom = get_custom_class(
    "BootVolumeKmsKeyFactsHelperCustom"
)


class ResourceFactsHelper(
    BootVolumeKmsKeyFactsHelperCustom, BootVolumeKmsKeyFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(boot_volume_id=dict(aliases=["id"], type="str", required=True),)
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="boot_volume_kms_key",
        service_client_class=BlockstorageClient,
        namespace="core",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(boot_volume_kms_key=result)


if __name__ == "__main__":
    main()

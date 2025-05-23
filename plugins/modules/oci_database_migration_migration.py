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
module: oci_database_migration_migration
short_description: Manage a Migration resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Migration resource in Oracle Cloud Infrastructure
    - For I(state=present), create a Migration resource that contains all the details to perform the
      database migration operation, such as source and destination database
      details, credentials, etc.
    - "This resource has the following action operations in the M(oracle.oci.oci_database_migration_migration_actions) module: add_migration_objects,
      change_compartment, remove_migration_objects."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the resource being referenced.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    exclude_objects:
        description:
            - Database objects to exclude from migration, cannot be specified alongside 'includeObjects'
        type: list
        elements: dict
        suboptions:
            schema:
                description:
                    - Schema of the object (regular expression is allowed)
                    - Required when database_combination is 'MYSQL'
                type: str
            owner:
                description:
                    - Owner of the object (regular expression is allowed)
                    - Required when database_combination is 'ORACLE'
                type: str
            object_name:
                description:
                    - Name of the object (regular expression is allowed)
                type: str
                required: true
            type:
                description:
                    - Type of object to exclude.
                      If not specified, matching owners and object names of type TABLE would be excluded.
                type: str
            is_omit_excluded_table_from_replication:
                description:
                    - Whether an excluded table should be omitted from replication. Only valid for database objects
                      that have are of type TABLE and object status EXCLUDE.
                    - Applicable when database_combination is 'ORACLE'
                type: bool
    include_objects:
        description:
            - Database objects to include from migration, cannot be specified alongside 'excludeObjects'
        type: list
        elements: dict
        suboptions:
            schema:
                description:
                    - Schema of the object (regular expression is allowed)
                    - Required when database_combination is 'MYSQL'
                type: str
            owner:
                description:
                    - Owner of the object (regular expression is allowed)
                    - Required when database_combination is 'ORACLE'
                type: str
            object_name:
                description:
                    - Name of the object (regular expression is allowed)
                type: str
                required: true
            type:
                description:
                    - Type of object to exclude.
                      If not specified, matching owners and object names of type TABLE would be excluded.
                type: str
            is_omit_excluded_table_from_replication:
                description:
                    - Whether an excluded table should be omitted from replication. Only valid for database objects
                      that have are of type TABLE and object status EXCLUDE.
                    - Applicable when database_combination is 'ORACLE'
                type: bool
    bulk_include_exclude_data:
        description:
            - Specifies the database objects to be excluded from the migration in bulk.
              The definition accepts input in a CSV format, newline separated for each entry.
              More details can be found in the documentation.
        type: str
    description:
        description:
            - A user-friendly description. Does not have to be unique, and it's changeable.
              Avoid entering confidential information.
            - This parameter is updatable.
        type: str
    database_combination:
        description:
            - "The combination of source and target databases participating in a migration.
              Example: ORACLE means the migration is meant for migrating Oracle source and target databases."
            - Required for create using I(state=present), update using I(state=present) with migration_id present.
        type: str
        choices:
            - "MYSQL"
            - "ORACLE"
    type:
        description:
            - "The type of the migration to be performed.
              Example: ONLINE if no downtime is preferred for a migration. This method uses Oracle GoldenGate for replication."
            - Required for create using I(state=present).
            - This parameter is updatable.
            - Applicable when database_combination is one of ['MYSQL', 'ORACLE']
        type: str
        choices:
            - "ONLINE"
            - "OFFLINE"
    display_name:
        description:
            - A user-friendly name. Does not have to be unique, and it's changeable.
              Avoid entering confidential information.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    source_database_connection_id:
        description:
            - The OCID of the resource being referenced.
            - Required for create using I(state=present).
            - This parameter is updatable.
            - Applicable when database_combination is one of ['MYSQL', 'ORACLE']
        type: str
    target_database_connection_id:
        description:
            - The OCID of the resource being referenced.
            - Required for create using I(state=present).
            - This parameter is updatable.
            - Applicable when database_combination is one of ['MYSQL', 'ORACLE']
        type: str
    freeform_tags:
        description:
            - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
              For more information, see Resource Tags. Example: {\\"Department\\": \\"Finance\\"}"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    data_transfer_medium_details:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            region:
                description:
                    - "AWS region code where the S3 bucket is located.
                      Region code should match the documented available regions:
                      https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions"
                    - This parameter is updatable.
                    - Applicable when type is 'AWS_S3'
                type: str
            access_key_id:
                description:
                    - "AWS access key credentials identifier
                      Details: https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys"
                    - This parameter is updatable.
                    - Applicable when type is 'AWS_S3'
                type: str
            secret_access_key:
                description:
                    - "AWS secret access key credentials
                      Details: https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys"
                    - This parameter is updatable.
                    - Applicable when type is 'AWS_S3'
                type: str
            shared_storage_mount_target_id:
                description:
                    - OCID of the shared storage mount target
                    - This parameter is updatable.
                    - Applicable when type is 'NFS'
                type: str
            source:
                description:
                    - ""
                    - Applicable when type is one of ['OBJECT_STORAGE', 'NFS']
                type: dict
                suboptions:
                    oci_home:
                        description:
                            - Path to the OCI CLI installation in the node.
                            - Applicable when kind is 'OCI_CLI'
                        type: str
                    wallet_location:
                        description:
                            - Directory path to OCI SSL wallet location on Db server node.
                        type: str
                    kind:
                        description:
                            - Type of dump transfer to use during migration in source or target host. Default kind is CURL
                        type: str
                        choices:
                            - "OCI_CLI"
                            - "CURL"
                        required: true
            target:
                description:
                    - ""
                    - Applicable when type is one of ['OBJECT_STORAGE', 'NFS']
                type: dict
                suboptions:
                    oci_home:
                        description:
                            - Path to the OCI CLI installation in the node.
                            - Applicable when kind is 'OCI_CLI'
                        type: str
                    wallet_location:
                        description:
                            - Directory path to OCI SSL wallet location on Db server node.
                        type: str
                    kind:
                        description:
                            - Type of dump transfer to use during migration in source or target host. Default kind is CURL
                        type: str
                        choices:
                            - "OCI_CLI"
                            - "CURL"
                        required: true
            type:
                description:
                    - Type of the data transfer medium to use.
                    - This parameter is updatable.
                type: str
                choices:
                    - "OBJECT_STORAGE"
                    - "DBLINK"
                    - "NFS"
                    - "AWS_S3"
                required: true
            object_storage_bucket:
                description:
                    - ""
                type: dict
                suboptions:
                    namespace_name:
                        description:
                            - Namespace name of the object store bucket.
                            - This parameter is updatable.
                            - Applicable when type is one of ['OBJECT_STORAGE', 'DBLINK', 'NFS']
                            - Required when type is one of ['OBJECT_STORAGE', 'AWS_S3']
                        type: str
                    bucket_name:
                        description:
                            - Bucket name.
                            - This parameter is updatable.
                            - Applicable when type is one of ['OBJECT_STORAGE', 'DBLINK', 'NFS']
                            - Required when type is one of ['OBJECT_STORAGE', 'AWS_S3']
                        type: str
            name:
                description:
                    - Name of database link from OCI database to on-premise database. ODMS will create link,
                      if the link does not already exist.
                    - This parameter is updatable.
                    - Applicable when type is one of ['DBLINK', 'AWS_S3']
                type: str
    initial_load_settings:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            is_consistent:
                description:
                    - Enable (true) or disable (false) consistent data dumps by locking the instance for backup during the dump.
                    - This parameter is updatable.
                    - Applicable when database_combination is 'MYSQL'
                type: bool
            is_tz_utc:
                description:
                    - Include a statement at the start of the dump to set the time zone to UTC.
                    - This parameter is updatable.
                    - Applicable when database_combination is 'MYSQL'
                type: bool
            compatibility:
                description:
                    - Apply the specified requirements for compatibility with MySQL Database Service for all tables in the dump
                      output, altering the dump files as necessary.
                    - This parameter is updatable.
                    - Applicable when database_combination is 'MYSQL'
                type: list
                elements: str
            primary_key_compatibility:
                description:
                    - Primary key compatibility option
                    - This parameter is updatable.
                    - Applicable when database_combination is 'MYSQL'
                type: str
                choices:
                    - "NONE"
                    - "IGNORE_MISSING_PKS"
                    - "CREATE_INVISIBLE_PKS"
            is_ignore_existing_objects:
                description:
                    - Import the dump even if it contains objects that already exist in the target schema in the MySQL instance.
                    - This parameter is updatable.
                    - Applicable when database_combination is 'MYSQL'
                type: bool
            handle_grant_errors:
                description:
                    - The action taken in the event of errors related to GRANT or REVOKE errors.
                    - This parameter is updatable.
                    - Applicable when database_combination is 'MYSQL'
                type: str
                choices:
                    - "ABORT"
                    - "DROP_ACCOUNT"
                    - "IGNORE"
            data_pump_parameters:
                description:
                    - ""
                    - Applicable when database_combination is 'ORACLE'
                type: dict
                suboptions:
                    is_cluster:
                        description:
                            - Set to false to force Data Pump worker process to run on one instance.
                            - This parameter is updatable.
                            - Applicable when database_combination is 'ORACLE'
                        type: bool
                    estimate:
                        description:
                            - Estimate size of dumps that will be generated.
                            - This parameter is updatable.
                            - Applicable when database_combination is 'ORACLE'
                        type: str
                        choices:
                            - "BLOCKS"
                            - "STATISTICS"
                    table_exists_action:
                        description:
                            - "IMPORT: Specifies the action to be performed when data is loaded into a preexisting table."
                            - This parameter is updatable.
                            - Applicable when database_combination is 'ORACLE'
                        type: str
                        choices:
                            - "TRUNCATE"
                            - "REPLACE"
                            - "APPEND"
                            - "SKIP"
                    exclude_parameters:
                        description:
                            - Exclude paratemers for Export and Import.
                            - This parameter is updatable.
                            - Applicable when database_combination is 'ORACLE'
                        type: list
                        elements: str
                    import_parallelism_degree:
                        description:
                            - Maximum number of worker processes that can be used for a Data Pump Import job.
                              For an Autonomous Database, ODMS will automatically query its CPU core count and set this property.
                            - This parameter is updatable.
                            - Applicable when database_combination is 'ORACLE'
                        type: int
                    export_parallelism_degree:
                        description:
                            - Maximum number of worker processes that can be used for a Data Pump Export job.
                            - This parameter is updatable.
                            - Applicable when database_combination is 'ORACLE'
                        type: int
            tablespace_details:
                description:
                    - ""
                    - Applicable when database_combination is 'ORACLE'
                type: dict
                suboptions:
                    remap_target:
                        description:
                            - Name of tablespace at target to which the source database tablespace need to be remapped.
                            - This parameter is updatable.
                            - Applicable when target_type is one of ['ADB_D_REMAP', 'NON_ADB_REMAP']
                        type: str
                    is_auto_create:
                        description:
                            - True to auto-create tablespace in the target Database.
                            - This parameter is updatable.
                            - Applicable when target_type is one of ['ADB_D_AUTOCREATE', 'NON_ADB_AUTOCREATE']
                        type: bool
                    is_big_file:
                        description:
                            - True set tablespace to big file.
                            - This parameter is updatable.
                            - Applicable when target_type is one of ['ADB_D_AUTOCREATE', 'NON_ADB_AUTOCREATE']
                        type: bool
                    extend_size_in_mbs:
                        description:
                            - Size of extend in MB. Can only be specified if 'isBigFile' property is set to true.
                            - This parameter is updatable.
                            - Applicable when target_type is one of ['ADB_D_AUTOCREATE', 'NON_ADB_AUTOCREATE']
                        type: int
                    block_size_in_kbs:
                        description:
                            - Size of Oracle database blocks in KB.
                            - This parameter is updatable.
                            - Applicable when target_type is one of ['ADB_D_AUTOCREATE', 'NON_ADB_AUTOCREATE']
                        type: str
                        choices:
                            - "SIZE_8K"
                            - "SIZE_16K"
                    target_type:
                        description:
                            - Type of Database Base Migration Target.
                            - This parameter is updatable.
                        type: str
                        choices:
                            - "NON_ADB_AUTOCREATE"
                            - "NON_ADB_REMAP"
                            - "ADB_D_REMAP"
                            - "ADB_S_REMAP"
                            - "ADB_D_AUTOCREATE"
                            - "TARGET_DEFAULTS_REMAP"
                            - "TARGET_DEFAULTS_AUTOCREATE"
                        required: true
            export_directory_object:
                description:
                    - ""
                    - Applicable when database_combination is 'ORACLE'
                type: dict
                suboptions:
                    name:
                        description:
                            - Name of directory object in database
                            - This parameter is updatable.
                            - Required when database_combination is 'ORACLE'
                        type: str
                    path:
                        description:
                            - Absolute path of directory on database server
                            - This parameter is updatable.
                            - Applicable when database_combination is 'ORACLE'
                        type: str
            import_directory_object:
                description:
                    - ""
                    - Applicable when database_combination is 'ORACLE'
                type: dict
                suboptions:
                    name:
                        description:
                            - Name of directory object in database
                            - This parameter is updatable.
                            - Required when database_combination is 'ORACLE'
                        type: str
                    path:
                        description:
                            - Absolute path of directory on database server
                            - This parameter is updatable.
                            - Applicable when database_combination is 'ORACLE'
                        type: str
            job_mode:
                description:
                    - MySql Job Mode
                    - This parameter is updatable.
                type: str
                choices:
                    - "FULL"
                    - "SCHEMA"
                    - "TABLE"
                    - "TABLESPACE"
                    - "TRANSPORTABLE"
                required: true
            metadata_remaps:
                description:
                    - Defines remapping to be applied to objects as they are processed.
                    - Applicable when database_combination is 'ORACLE'
                type: list
                elements: dict
                suboptions:
                    type:
                        description:
                            - Type of remap. Refer to L(METADATA_REMAP Procedure ,https://docs.oracle.com/en/database/oracle/oracle-
                              database/19/arpls/DBMS_DATAPUMP.html#GUID-0FC32790-91E6-4781-87A3-229DE024CB3D)
                            - Required when database_combination is 'ORACLE'
                        type: str
                        choices:
                            - "SCHEMA"
                            - "TABLESPACE"
                            - "DATAFILE"
                            - "TABLE"
                        required: true
                    old_value:
                        description:
                            - Specifies the value which needs to be reset.
                            - Required when database_combination is 'ORACLE'
                        type: str
                        required: true
                    new_value:
                        description:
                            - Specifies the new value that oldValue should be translated into.
                            - Required when database_combination is 'ORACLE'
                        type: str
                        required: true
    advisor_settings:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            is_skip_advisor:
                description:
                    - True to skip the Pre-Migration Advisor execution. Default is false.
                    - This parameter is updatable.
                type: bool
            is_ignore_errors:
                description:
                    - True to not interrupt migration execution due to Pre-Migration Advisor errors. Default is false.
                    - This parameter is updatable.
                type: bool
    hub_details:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            rest_admin_credentials:
                description:
                    - ""
                    - Required when database_combination is 'MYSQL'
                type: dict
                suboptions:
                    username:
                        description:
                            - Administrator username
                            - This parameter is updatable.
                            - Required when database_combination is 'MYSQL'
                        type: str
                    password:
                        description:
                            - Administrator password
                            - This parameter is updatable.
                            - Required when database_combination is 'MYSQL'
                        type: str
            url:
                description:
                    - Endpoint URL.
                    - This parameter is updatable.
                    - Required when database_combination is 'MYSQL'
                type: str
            compute_id:
                description:
                    - The OCID of the resource being referenced.
                    - This parameter is updatable.
                    - Applicable when database_combination is 'MYSQL'
                type: str
            vault_id:
                description:
                    - The OCID of the resource being referenced.
                    - This parameter is updatable.
                    - Required when database_combination is 'MYSQL'
                type: str
            key_id:
                description:
                    - The OCID of the resource being referenced.
                    - This parameter is updatable.
                    - Required when database_combination is 'MYSQL'
                type: str
            extract:
                description:
                    - ""
                    - Applicable when database_combination is 'MYSQL'
                type: dict
                suboptions:
                    performance_profile:
                        description:
                            - Extract performance.
                            - This parameter is updatable.
                            - Applicable when database_combination is 'MYSQL'
                        type: str
                        choices:
                            - "LOW"
                            - "MEDIUM"
                            - "HIGH"
                    long_trans_duration:
                        description:
                            - Length of time (in seconds) that a transaction can be open before Extract generates a warning message that the transaction is
                              long-running.
                              If not specified, Extract will not generate a warning on long-running transactions.
                            - This parameter is updatable.
                            - Applicable when database_combination is 'MYSQL'
                        type: int
            replicat:
                description:
                    - ""
                    - Applicable when database_combination is 'MYSQL'
                type: dict
                suboptions:
                    performance_profile:
                        description:
                            - Replicat performance.
                            - This parameter is updatable.
                            - Applicable when database_combination is 'MYSQL'
                        type: str
                        choices:
                            - "LOW"
                            - "HIGH"
            acceptable_lag:
                description:
                    - ODMS will monitor GoldenGate end-to-end latency until the lag time is lower than the specified value in seconds.
                    - This parameter is updatable.
                    - Applicable when database_combination is 'MYSQL'
                type: int
    ggs_details:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            extract:
                description:
                    - ""
                    - Applicable when database_combination is 'ORACLE'
                type: dict
                suboptions:
                    performance_profile:
                        description:
                            - Extract performance.
                            - This parameter is updatable.
                            - Applicable when database_combination is 'ORACLE'
                        type: str
                        choices:
                            - "LOW"
                            - "MEDIUM"
                            - "HIGH"
                    long_trans_duration:
                        description:
                            - Length of time (in seconds) that a transaction can be open before Extract generates a warning message that the transaction is
                              long-running.
                              If not specified, Extract will not generate a warning on long-running transactions.
                            - This parameter is updatable.
                            - Applicable when database_combination is 'ORACLE'
                        type: int
            replicat:
                description:
                    - ""
                type: dict
                suboptions:
                    performance_profile:
                        description:
                            - Replicat performance.
                            - This parameter is updatable.
                            - Applicable when database_combination is 'MYSQL'
                        type: str
                        choices:
                            - "LOW"
                            - "HIGH"
            acceptable_lag:
                description:
                    - ODMS will monitor GoldenGate end-to-end latency until the lag time is lower than the specified value in seconds.
                    - This parameter is updatable.
                type: int
    advanced_parameters:
        description:
            - List of Migration Parameter objects.
            - This parameter is updatable.
            - Applicable when database_combination is 'ORACLE'
        type: list
        elements: dict
        suboptions:
            value:
                description:
                    - If a STRING data type then the value should be an array of characters,
                      if a INTEGER data type then the value should be an integer value,
                      if a FLOAT data type then the value should be an float value,
                      if a BOOLEAN data type then the value should be TRUE or FALSE.
                    - Required when database_combination is 'ORACLE'
                type: str
                required: true
            name:
                description:
                    - Parameter name.
                    - Required when database_combination is 'ORACLE'
                type: str
                required: true
            data_type:
                description:
                    - Parameter data type.
                    - Required when database_combination is 'ORACLE'
                type: str
                choices:
                    - "STRING"
                    - "INTEGER"
                    - "FLOAT"
                    - "BOOLEAN"
                required: true
    source_container_database_connection_id:
        description:
            - The OCID of the resource being referenced.
            - This parameter is updatable.
            - Applicable when database_combination is 'ORACLE'
        type: str
    migration_id:
        description:
            - The OCID of the migration
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the Migration.
            - Use I(state=present) to create or update a Migration.
            - Use I(state=absent) to delete a Migration.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create migration with database_combination = MYSQL
  oci_database_migration_migration:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    database_combination: MYSQL

    # optional
    exclude_objects:
    - # required
      object_name: object_name_example

      # optional
      schema: schema_example
      owner: owner_example
      type: type_example
      is_omit_excluded_table_from_replication: true
    include_objects:
    - # required
      object_name: object_name_example

      # optional
      schema: schema_example
      owner: owner_example
      type: type_example
      is_omit_excluded_table_from_replication: true
    bulk_include_exclude_data: bulk_include_exclude_data_example
    description: description_example
    type: ONLINE
    display_name: display_name_example
    source_database_connection_id: "ocid1.sourcedatabaseconnection.oc1..xxxxxxEXAMPLExxxxxx"
    target_database_connection_id: "ocid1.targetdatabaseconnection.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    data_transfer_medium_details:
      # required
      type: OBJECT_STORAGE

      # optional
      source:
        # required
        kind: OCI_CLI

        # optional
        oci_home: oci_home_example
        wallet_location: wallet_location_example
      target:
        # required
        kind: OCI_CLI

        # optional
        oci_home: oci_home_example
        wallet_location: wallet_location_example
      object_storage_bucket:
        # optional
        namespace_name: namespace_name_example
        bucket_name: bucket_name_example
    initial_load_settings:
      # required
      job_mode: FULL

      # optional
      is_consistent: true
      is_tz_utc: true
      compatibility: [ "compatibility_example" ]
      primary_key_compatibility: NONE
      is_ignore_existing_objects: true
      handle_grant_errors: ABORT
      data_pump_parameters:
        # optional
        is_cluster: true
        estimate: BLOCKS
        table_exists_action: TRUNCATE
        exclude_parameters: [ "exclude_parameters_example" ]
        import_parallelism_degree: 56
        export_parallelism_degree: 56
      tablespace_details:
        # required
        target_type: NON_ADB_AUTOCREATE

        # optional
        is_auto_create: true
        is_big_file: true
        extend_size_in_mbs: 56
        block_size_in_kbs: SIZE_8K
      export_directory_object:
        # optional
        name: name_example
        path: path_example
      import_directory_object:
        # optional
        name: name_example
        path: path_example
      metadata_remaps:
      - # required
        type: SCHEMA
        old_value: old_value_example
        new_value: new_value_example
    advisor_settings:
      # optional
      is_skip_advisor: true
      is_ignore_errors: true
    hub_details:
      # optional
      rest_admin_credentials:
        # optional
        username: username_example
        password: example-password
      url: url_example
      compute_id: "ocid1.compute.oc1..xxxxxxEXAMPLExxxxxx"
      vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
      key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
      extract:
        # optional
        performance_profile: LOW
        long_trans_duration: 56
      replicat:
        # optional
        performance_profile: LOW
      acceptable_lag: 56
    ggs_details:
      # optional
      extract:
        # optional
        performance_profile: LOW
        long_trans_duration: 56
      replicat:
        # optional
        performance_profile: LOW
      acceptable_lag: 56

- name: Create migration with database_combination = ORACLE
  oci_database_migration_migration:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    database_combination: ORACLE

    # optional
    exclude_objects:
    - # required
      object_name: object_name_example

      # optional
      schema: schema_example
      owner: owner_example
      type: type_example
      is_omit_excluded_table_from_replication: true
    include_objects:
    - # required
      object_name: object_name_example

      # optional
      schema: schema_example
      owner: owner_example
      type: type_example
      is_omit_excluded_table_from_replication: true
    bulk_include_exclude_data: bulk_include_exclude_data_example
    description: description_example
    type: ONLINE
    display_name: display_name_example
    source_database_connection_id: "ocid1.sourcedatabaseconnection.oc1..xxxxxxEXAMPLExxxxxx"
    target_database_connection_id: "ocid1.targetdatabaseconnection.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    data_transfer_medium_details:
      # required
      type: OBJECT_STORAGE

      # optional
      source:
        # required
        kind: OCI_CLI

        # optional
        oci_home: oci_home_example
        wallet_location: wallet_location_example
      target:
        # required
        kind: OCI_CLI

        # optional
        oci_home: oci_home_example
        wallet_location: wallet_location_example
      object_storage_bucket:
        # optional
        namespace_name: namespace_name_example
        bucket_name: bucket_name_example
    initial_load_settings:
      # required
      job_mode: FULL

      # optional
      is_consistent: true
      is_tz_utc: true
      compatibility: [ "compatibility_example" ]
      primary_key_compatibility: NONE
      is_ignore_existing_objects: true
      handle_grant_errors: ABORT
      data_pump_parameters:
        # optional
        is_cluster: true
        estimate: BLOCKS
        table_exists_action: TRUNCATE
        exclude_parameters: [ "exclude_parameters_example" ]
        import_parallelism_degree: 56
        export_parallelism_degree: 56
      tablespace_details:
        # required
        target_type: NON_ADB_AUTOCREATE

        # optional
        is_auto_create: true
        is_big_file: true
        extend_size_in_mbs: 56
        block_size_in_kbs: SIZE_8K
      export_directory_object:
        # optional
        name: name_example
        path: path_example
      import_directory_object:
        # optional
        name: name_example
        path: path_example
      metadata_remaps:
      - # required
        type: SCHEMA
        old_value: old_value_example
        new_value: new_value_example
    advisor_settings:
      # optional
      is_skip_advisor: true
      is_ignore_errors: true
    hub_details:
      # optional
      rest_admin_credentials:
        # optional
        username: username_example
        password: example-password
      url: url_example
      compute_id: "ocid1.compute.oc1..xxxxxxEXAMPLExxxxxx"
      vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
      key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
      extract:
        # optional
        performance_profile: LOW
        long_trans_duration: 56
      replicat:
        # optional
        performance_profile: LOW
      acceptable_lag: 56
    ggs_details:
      # optional
      extract:
        # optional
        performance_profile: LOW
        long_trans_duration: 56
      replicat:
        # optional
        performance_profile: LOW
      acceptable_lag: 56
    advanced_parameters:
    - # required
      value: value_example
      name: name_example
      data_type: STRING
    source_container_database_connection_id: "ocid1.sourcecontainerdatabaseconnection.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update migration with database_combination = MYSQL
  oci_database_migration_migration:
    # required
    database_combination: MYSQL

    # optional
    description: description_example
    type: ONLINE
    display_name: display_name_example
    source_database_connection_id: "ocid1.sourcedatabaseconnection.oc1..xxxxxxEXAMPLExxxxxx"
    target_database_connection_id: "ocid1.targetdatabaseconnection.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    data_transfer_medium_details:
      # required
      type: OBJECT_STORAGE

      # optional
      source:
        # required
        kind: OCI_CLI

        # optional
        oci_home: oci_home_example
        wallet_location: wallet_location_example
      target:
        # required
        kind: OCI_CLI

        # optional
        oci_home: oci_home_example
        wallet_location: wallet_location_example
      object_storage_bucket:
        # optional
        namespace_name: namespace_name_example
        bucket_name: bucket_name_example
    initial_load_settings:
      # required
      job_mode: FULL

      # optional
      is_consistent: true
      is_tz_utc: true
      compatibility: [ "compatibility_example" ]
      primary_key_compatibility: NONE
      is_ignore_existing_objects: true
      handle_grant_errors: ABORT
      data_pump_parameters:
        # optional
        is_cluster: true
        estimate: BLOCKS
        table_exists_action: TRUNCATE
        exclude_parameters: [ "exclude_parameters_example" ]
        import_parallelism_degree: 56
        export_parallelism_degree: 56
      tablespace_details:
        # required
        target_type: NON_ADB_AUTOCREATE

        # optional
        is_auto_create: true
        is_big_file: true
        extend_size_in_mbs: 56
        block_size_in_kbs: SIZE_8K
      export_directory_object:
        # optional
        name: name_example
        path: path_example
      import_directory_object:
        # optional
        name: name_example
        path: path_example
      metadata_remaps:
      - # required
        type: SCHEMA
        old_value: old_value_example
        new_value: new_value_example
    advisor_settings:
      # optional
      is_skip_advisor: true
      is_ignore_errors: true
    hub_details:
      # optional
      rest_admin_credentials:
        # optional
        username: username_example
        password: example-password
      url: url_example
      compute_id: "ocid1.compute.oc1..xxxxxxEXAMPLExxxxxx"
      vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
      key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
      extract:
        # optional
        performance_profile: LOW
        long_trans_duration: 56
      replicat:
        # optional
        performance_profile: LOW
      acceptable_lag: 56
    ggs_details:
      # optional
      extract:
        # optional
        performance_profile: LOW
        long_trans_duration: 56
      replicat:
        # optional
        performance_profile: LOW
      acceptable_lag: 56

- name: Update migration with database_combination = ORACLE
  oci_database_migration_migration:
    # required
    database_combination: ORACLE

    # optional
    description: description_example
    type: ONLINE
    display_name: display_name_example
    source_database_connection_id: "ocid1.sourcedatabaseconnection.oc1..xxxxxxEXAMPLExxxxxx"
    target_database_connection_id: "ocid1.targetdatabaseconnection.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    data_transfer_medium_details:
      # required
      type: OBJECT_STORAGE

      # optional
      source:
        # required
        kind: OCI_CLI

        # optional
        oci_home: oci_home_example
        wallet_location: wallet_location_example
      target:
        # required
        kind: OCI_CLI

        # optional
        oci_home: oci_home_example
        wallet_location: wallet_location_example
      object_storage_bucket:
        # optional
        namespace_name: namespace_name_example
        bucket_name: bucket_name_example
    initial_load_settings:
      # required
      job_mode: FULL

      # optional
      is_consistent: true
      is_tz_utc: true
      compatibility: [ "compatibility_example" ]
      primary_key_compatibility: NONE
      is_ignore_existing_objects: true
      handle_grant_errors: ABORT
      data_pump_parameters:
        # optional
        is_cluster: true
        estimate: BLOCKS
        table_exists_action: TRUNCATE
        exclude_parameters: [ "exclude_parameters_example" ]
        import_parallelism_degree: 56
        export_parallelism_degree: 56
      tablespace_details:
        # required
        target_type: NON_ADB_AUTOCREATE

        # optional
        is_auto_create: true
        is_big_file: true
        extend_size_in_mbs: 56
        block_size_in_kbs: SIZE_8K
      export_directory_object:
        # optional
        name: name_example
        path: path_example
      import_directory_object:
        # optional
        name: name_example
        path: path_example
      metadata_remaps:
      - # required
        type: SCHEMA
        old_value: old_value_example
        new_value: new_value_example
    advisor_settings:
      # optional
      is_skip_advisor: true
      is_ignore_errors: true
    hub_details:
      # optional
      rest_admin_credentials:
        # optional
        username: username_example
        password: example-password
      url: url_example
      compute_id: "ocid1.compute.oc1..xxxxxxEXAMPLExxxxxx"
      vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
      key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
      extract:
        # optional
        performance_profile: LOW
        long_trans_duration: 56
      replicat:
        # optional
        performance_profile: LOW
      acceptable_lag: 56
    ggs_details:
      # optional
      extract:
        # optional
        performance_profile: LOW
        long_trans_duration: 56
      replicat:
        # optional
        performance_profile: LOW
      acceptable_lag: 56
    advanced_parameters:
    - # required
      value: value_example
      name: name_example
      data_type: STRING
    source_container_database_connection_id: "ocid1.sourcecontainerdatabaseconnection.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update migration using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with database_combination = MYSQL
  oci_database_migration_migration:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    database_combination: MYSQL

    # optional
    description: description_example
    type: ONLINE
    display_name: display_name_example
    source_database_connection_id: "ocid1.sourcedatabaseconnection.oc1..xxxxxxEXAMPLExxxxxx"
    target_database_connection_id: "ocid1.targetdatabaseconnection.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    data_transfer_medium_details:
      # required
      type: OBJECT_STORAGE

      # optional
      source:
        # required
        kind: OCI_CLI

        # optional
        oci_home: oci_home_example
        wallet_location: wallet_location_example
      target:
        # required
        kind: OCI_CLI

        # optional
        oci_home: oci_home_example
        wallet_location: wallet_location_example
      object_storage_bucket:
        # optional
        namespace_name: namespace_name_example
        bucket_name: bucket_name_example
    initial_load_settings:
      # required
      job_mode: FULL

      # optional
      is_consistent: true
      is_tz_utc: true
      compatibility: [ "compatibility_example" ]
      primary_key_compatibility: NONE
      is_ignore_existing_objects: true
      handle_grant_errors: ABORT
      data_pump_parameters:
        # optional
        is_cluster: true
        estimate: BLOCKS
        table_exists_action: TRUNCATE
        exclude_parameters: [ "exclude_parameters_example" ]
        import_parallelism_degree: 56
        export_parallelism_degree: 56
      tablespace_details:
        # required
        target_type: NON_ADB_AUTOCREATE

        # optional
        is_auto_create: true
        is_big_file: true
        extend_size_in_mbs: 56
        block_size_in_kbs: SIZE_8K
      export_directory_object:
        # optional
        name: name_example
        path: path_example
      import_directory_object:
        # optional
        name: name_example
        path: path_example
      metadata_remaps:
      - # required
        type: SCHEMA
        old_value: old_value_example
        new_value: new_value_example
    advisor_settings:
      # optional
      is_skip_advisor: true
      is_ignore_errors: true
    hub_details:
      # optional
      rest_admin_credentials:
        # optional
        username: username_example
        password: example-password
      url: url_example
      compute_id: "ocid1.compute.oc1..xxxxxxEXAMPLExxxxxx"
      vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
      key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
      extract:
        # optional
        performance_profile: LOW
        long_trans_duration: 56
      replicat:
        # optional
        performance_profile: LOW
      acceptable_lag: 56
    ggs_details:
      # optional
      extract:
        # optional
        performance_profile: LOW
        long_trans_duration: 56
      replicat:
        # optional
        performance_profile: LOW
      acceptable_lag: 56

- name: Update migration using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with database_combination = ORACLE
  oci_database_migration_migration:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    database_combination: ORACLE

    # optional
    description: description_example
    type: ONLINE
    display_name: display_name_example
    source_database_connection_id: "ocid1.sourcedatabaseconnection.oc1..xxxxxxEXAMPLExxxxxx"
    target_database_connection_id: "ocid1.targetdatabaseconnection.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    data_transfer_medium_details:
      # required
      type: OBJECT_STORAGE

      # optional
      source:
        # required
        kind: OCI_CLI

        # optional
        oci_home: oci_home_example
        wallet_location: wallet_location_example
      target:
        # required
        kind: OCI_CLI

        # optional
        oci_home: oci_home_example
        wallet_location: wallet_location_example
      object_storage_bucket:
        # optional
        namespace_name: namespace_name_example
        bucket_name: bucket_name_example
    initial_load_settings:
      # required
      job_mode: FULL

      # optional
      is_consistent: true
      is_tz_utc: true
      compatibility: [ "compatibility_example" ]
      primary_key_compatibility: NONE
      is_ignore_existing_objects: true
      handle_grant_errors: ABORT
      data_pump_parameters:
        # optional
        is_cluster: true
        estimate: BLOCKS
        table_exists_action: TRUNCATE
        exclude_parameters: [ "exclude_parameters_example" ]
        import_parallelism_degree: 56
        export_parallelism_degree: 56
      tablespace_details:
        # required
        target_type: NON_ADB_AUTOCREATE

        # optional
        is_auto_create: true
        is_big_file: true
        extend_size_in_mbs: 56
        block_size_in_kbs: SIZE_8K
      export_directory_object:
        # optional
        name: name_example
        path: path_example
      import_directory_object:
        # optional
        name: name_example
        path: path_example
      metadata_remaps:
      - # required
        type: SCHEMA
        old_value: old_value_example
        new_value: new_value_example
    advisor_settings:
      # optional
      is_skip_advisor: true
      is_ignore_errors: true
    hub_details:
      # optional
      rest_admin_credentials:
        # optional
        username: username_example
        password: example-password
      url: url_example
      compute_id: "ocid1.compute.oc1..xxxxxxEXAMPLExxxxxx"
      vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
      key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
      extract:
        # optional
        performance_profile: LOW
        long_trans_duration: 56
      replicat:
        # optional
        performance_profile: LOW
      acceptable_lag: 56
    ggs_details:
      # optional
      extract:
        # optional
        performance_profile: LOW
        long_trans_duration: 56
      replicat:
        # optional
        performance_profile: LOW
      acceptable_lag: 56
    advanced_parameters:
    - # required
      value: value_example
      name: name_example
      data_type: STRING
    source_container_database_connection_id: "ocid1.sourcecontainerdatabaseconnection.oc1..xxxxxxEXAMPLExxxxxx"

- name: Delete migration
  oci_database_migration_migration:
    # required
    migration_id: "ocid1.migration.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete migration using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_database_migration_migration:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
migration:
    description:
        - Details of the Migration resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the resource being referenced.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        description:
            description:
                - A user-friendly description. Does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
            returned: on success
            type: str
            sample: description_example
        database_combination:
            description:
                - "The combination of source and target databases participating in a migration.
                  Example: ORACLE means the migration is meant for migrating Oracle source and target databases."
            returned: on success
            type: str
            sample: MYSQL
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - The OCID of the resource being referenced.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        type:
            description:
                - "The type of the migration to be performed.
                  Example: ONLINE if no downtime is preferred for a migration. This method uses Oracle GoldenGate for replication."
            returned: on success
            type: str
            sample: ONLINE
        wait_after:
            description:
                - You can optionally pause a migration after a job phase.
                  This property allows you to optionally specify the phase after which you can pause the migration.
            returned: on success
            type: str
            sample: ODMS_VALIDATE_TGT
        source_database_connection_id:
            description:
                - The OCID of the resource being referenced.
            returned: on success
            type: str
            sample: "ocid1.sourcedatabaseconnection.oc1..xxxxxxEXAMPLExxxxxx"
        target_database_connection_id:
            description:
                - The OCID of the resource being referenced.
            returned: on success
            type: str
            sample: "ocid1.targetdatabaseconnection.oc1..xxxxxxEXAMPLExxxxxx"
        executing_job_id:
            description:
                - The OCID of the resource being referenced.
            returned: on success
            type: str
            sample: "ocid1.executingjob.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - An RFC3339 formatted datetime string such as `2016-08-25T21:10:29.600Z`.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - An RFC3339 formatted datetime string such as `2016-08-25T21:10:29.600Z`.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_last_migration:
            description:
                - An RFC3339 formatted datetime string such as `2016-08-25T21:10:29.600Z`.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the Migration resource.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - Additional status related to the execution and current state of the Migration.
            returned: on success
            type: str
            sample: READY
        freeform_tags:
            description:
                - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see Resource Tags. Example: {\\"Department\\": \\"Finance\\"}"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "Usage of system tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
        data_transfer_medium_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                type:
                    description:
                        - Type of the data transfer medium to use.
                    returned: on success
                    type: str
                    sample: OBJECT_STORAGE
                object_storage_bucket:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        namespace_name:
                            description:
                                - Namespace name of the object store bucket.
                            returned: on success
                            type: str
                            sample: namespace_name_example
                        bucket_name:
                            description:
                                - Bucket name.
                            returned: on success
                            type: str
                            sample: bucket_name_example
                region:
                    description:
                        - "AWS region code where the S3 bucket is located.
                          Region code should match the documented available regions:
                          https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions"
                    returned: on success
                    type: str
                    sample: us-phoenix-1
                access_key_id:
                    description:
                        - "AWS access key credentials identifier
                          Details: https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys"
                    returned: on success
                    type: str
                    sample: "ocid1.accesskey.oc1..xxxxxxEXAMPLExxxxxx"
                secret_access_key:
                    description:
                        - "AWS secret access key credentials
                          Details: https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys"
                    returned: on success
                    type: str
                    sample: secret_access_key_example
                name:
                    description:
                        - S3 bucket name.
                    returned: on success
                    type: str
                    sample: name_example
                shared_storage_mount_target_id:
                    description:
                        - OCID of the shared storage mount target
                    returned: on success
                    type: str
                    sample: "ocid1.sharedstoragemounttarget.oc1..xxxxxxEXAMPLExxxxxx"
                source:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        wallet_location:
                            description:
                                - Directory path to OCI SSL wallet location on Db server node.
                            returned: on success
                            type: str
                            sample: wallet_location_example
                        kind:
                            description:
                                - Type of dump transfer to use during migration in source or target host. Default kind is CURL
                            returned: on success
                            type: str
                            sample: CURL
                        oci_home:
                            description:
                                - Path to the OCI CLI installation in the node.
                            returned: on success
                            type: str
                            sample: oci_home_example
                target:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        wallet_location:
                            description:
                                - Directory path to OCI SSL wallet location on Db server node.
                            returned: on success
                            type: str
                            sample: wallet_location_example
                        kind:
                            description:
                                - Type of dump transfer to use during migration in source or target host. Default kind is CURL
                            returned: on success
                            type: str
                            sample: CURL
                        oci_home:
                            description:
                                - Path to the OCI CLI installation in the node.
                            returned: on success
                            type: str
                            sample: oci_home_example
        initial_load_settings:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                is_consistent:
                    description:
                        - Enable (true) or disable (false) consistent data dumps by locking the instance for backup during the dump.
                    returned: on success
                    type: bool
                    sample: true
                is_tz_utc:
                    description:
                        - Include a statement at the start of the dump to set the time zone to UTC.
                    returned: on success
                    type: bool
                    sample: true
                compatibility:
                    description:
                        - Apply the specified requirements for compatibility with MySQL Database Service for all tables in the dump
                          output, altering the dump files as necessary.
                    returned: on success
                    type: list
                    sample: []
                primary_key_compatibility:
                    description:
                        - Primary key compatibility option
                    returned: on success
                    type: str
                    sample: NONE
                is_ignore_existing_objects:
                    description:
                        - Import the dump even if it contains objects that already exist in the target schema in the MySQL instance.
                    returned: on success
                    type: bool
                    sample: true
                handle_grant_errors:
                    description:
                        - The action taken in the event of errors related to GRANT or REVOKE errors.
                    returned: on success
                    type: str
                    sample: ABORT
                job_mode:
                    description:
                        - MySql Job Mode
                    returned: on success
                    type: str
                    sample: FULL
                data_pump_parameters:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        is_cluster:
                            description:
                                - Set to false to force Data Pump worker process to run on one instance.
                            returned: on success
                            type: bool
                            sample: true
                        estimate:
                            description:
                                - Estimate size of dumps that will be generated.
                            returned: on success
                            type: str
                            sample: BLOCKS
                        table_exists_action:
                            description:
                                - "IMPORT: Specifies the action to be performed when data is loaded into a preexisting table."
                            returned: on success
                            type: str
                            sample: TRUNCATE
                        exclude_parameters:
                            description:
                                - Exclude paratemers for Export and Import.
                            returned: on success
                            type: list
                            sample: []
                        import_parallelism_degree:
                            description:
                                - Maximum number of worker processes that can be used for a Data Pump Import job.
                                  For an Autonomous Database, ODMS will automatically query its CPU core count and set this property.
                            returned: on success
                            type: int
                            sample: 56
                        export_parallelism_degree:
                            description:
                                - Maximum number of worker processes that can be used for a Data Pump Export job.
                            returned: on success
                            type: int
                            sample: 56
                tablespace_details:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        is_auto_create:
                            description:
                                - "Set this property to true to auto-create tablespaces in the target Database.
                                  Note: This is not applicable for Autonomous Database Serverless databases."
                            returned: on success
                            type: bool
                            sample: true
                        is_big_file:
                            description:
                                - Set this property to true to enable tablespace of the type big file.
                            returned: on success
                            type: bool
                            sample: true
                        extend_size_in_mbs:
                            description:
                                - "Size to extend the tablespace in MB.
                                  Note: Only applicable if 'isBigFile' property is set to true."
                            returned: on success
                            type: int
                            sample: 56
                        block_size_in_kbs:
                            description:
                                - Size of Oracle database blocks in KB.
                            returned: on success
                            type: str
                            sample: SIZE_8K
                        target_type:
                            description:
                                - Type of Database Base Migration Target.
                            returned: on success
                            type: str
                            sample: ADB_S_REMAP
                        remap_target:
                            description:
                                - Name of the tablespace on the target database to which the source database tablespace is to be remapped.
                            returned: on success
                            type: str
                            sample: remap_target_example
                export_directory_object:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - Name of directory object in database
                            returned: on success
                            type: str
                            sample: name_example
                        path:
                            description:
                                - Absolute path of directory on database server
                            returned: on success
                            type: str
                            sample: path_example
                import_directory_object:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - Name of directory object in database
                            returned: on success
                            type: str
                            sample: name_example
                        path:
                            description:
                                - Absolute path of directory on database server
                            returned: on success
                            type: str
                            sample: path_example
                metadata_remaps:
                    description:
                        - Defines remapping to be applied to objects as they are processed.
                    returned: on success
                    type: complex
                    contains:
                        type:
                            description:
                                - Type of remap. Refer to L(METADATA_REMAP Procedure ,https://docs.oracle.com/en/database/oracle/oracle-
                                  database/19/arpls/DBMS_DATAPUMP.html#GUID-0FC32790-91E6-4781-87A3-229DE024CB3D)
                            returned: on success
                            type: str
                            sample: SCHEMA
                        old_value:
                            description:
                                - Specifies the value which needs to be reset.
                            returned: on success
                            type: str
                            sample: old_value_example
                        new_value:
                            description:
                                - Specifies the new value that oldValue should be translated into.
                            returned: on success
                            type: str
                            sample: new_value_example
        advisor_settings:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                is_skip_advisor:
                    description:
                        - True to skip the Pre-Migration Advisor execution. Default is false.
                    returned: on success
                    type: bool
                    sample: true
                is_ignore_errors:
                    description:
                        - True to not interrupt migration execution due to Pre-Migration Advisor errors. Default is false.
                    returned: on success
                    type: bool
                    sample: true
        hub_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                rest_admin_credentials:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        username:
                            description:
                                - Administrator username
                            returned: on success
                            type: str
                            sample: username_example
                url:
                    description:
                        - Endpoint URL.
                    returned: on success
                    type: str
                    sample: url_example
                compute_id:
                    description:
                        - The OCID of the resource being referenced.
                    returned: on success
                    type: str
                    sample: "ocid1.compute.oc1..xxxxxxEXAMPLExxxxxx"
                vault_id:
                    description:
                        - The OCID of the resource being referenced.
                    returned: on success
                    type: str
                    sample: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
                key_id:
                    description:
                        - The OCID of the resource being referenced.
                    returned: on success
                    type: str
                    sample: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
                extract:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        performance_profile:
                            description:
                                - Extract performance.
                            returned: on success
                            type: str
                            sample: LOW
                        long_trans_duration:
                            description:
                                - Length of time (in seconds) that a transaction can be open before Extract generates a warning message that the transaction is
                                  long-running.
                                  If not specified, Extract will not generate a warning on long-running transactions.
                            returned: on success
                            type: int
                            sample: 56
                replicat:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        performance_profile:
                            description:
                                - Replicat performance.
                            returned: on success
                            type: str
                            sample: LOW
                acceptable_lag:
                    description:
                        - ODMS will monitor GoldenGate end-to-end latency until the lag time is lower than the specified value in seconds.
                    returned: on success
                    type: int
                    sample: 56
        ggs_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                ggs_deployment:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        deployment_id:
                            description:
                                - The OCID of the resource being referenced.
                            returned: on success
                            type: str
                            sample: "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx"
                        ggs_admin_credentials_secret_id:
                            description:
                                - The OCID of the resource being referenced.
                            returned: on success
                            type: str
                            sample: "ocid1.ggsadmincredentialssecret.oc1..xxxxxxEXAMPLExxxxxx"
                replicat:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        performance_profile:
                            description:
                                - Replicat performance.
                            returned: on success
                            type: str
                            sample: LOW
                acceptable_lag:
                    description:
                        - ODMS will monitor GoldenGate end-to-end latency until the lag time is lower than the specified value in seconds.
                    returned: on success
                    type: int
                    sample: 56
                extract:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        performance_profile:
                            description:
                                - Extract performance.
                            returned: on success
                            type: str
                            sample: LOW
                        long_trans_duration:
                            description:
                                - Length of time (in seconds) that a transaction can be open before Extract generates a warning message that the transaction is
                                  long-running.
                                  If not specified, Extract will not generate a warning on long-running transactions.
                            returned: on success
                            type: int
                            sample: 56
        source_container_database_connection_id:
            description:
                - The OCID of the resource being referenced.
            returned: on success
            type: str
            sample: "ocid1.sourcecontainerdatabaseconnection.oc1..xxxxxxEXAMPLExxxxxx"
        advanced_parameters:
            description:
                - List of Migration Parameter objects.
            returned: on success
            type: complex
            contains:
                value:
                    description:
                        - If a STRING data type then the value should be an array of characters,
                          if a INTEGER data type then the value should be an integer value,
                          if a FLOAT data type then the value should be an float value,
                          if a BOOLEAN data type then the value should be TRUE or FALSE.
                    returned: on success
                    type: str
                    sample: value_example
                name:
                    description:
                        - Parameter name.
                    returned: on success
                    type: str
                    sample: name_example
                data_type:
                    description:
                        - Parameter data type.
                    returned: on success
                    type: str
                    sample: STRING
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "description": "description_example",
        "database_combination": "MYSQL",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "type": "ONLINE",
        "wait_after": "ODMS_VALIDATE_TGT",
        "source_database_connection_id": "ocid1.sourcedatabaseconnection.oc1..xxxxxxEXAMPLExxxxxx",
        "target_database_connection_id": "ocid1.targetdatabaseconnection.oc1..xxxxxxEXAMPLExxxxxx",
        "executing_job_id": "ocid1.executingjob.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "time_last_migration": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "READY",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {},
        "data_transfer_medium_details": {
            "type": "OBJECT_STORAGE",
            "object_storage_bucket": {
                "namespace_name": "namespace_name_example",
                "bucket_name": "bucket_name_example"
            },
            "region": "us-phoenix-1",
            "access_key_id": "ocid1.accesskey.oc1..xxxxxxEXAMPLExxxxxx",
            "secret_access_key": "secret_access_key_example",
            "name": "name_example",
            "shared_storage_mount_target_id": "ocid1.sharedstoragemounttarget.oc1..xxxxxxEXAMPLExxxxxx",
            "source": {
                "wallet_location": "wallet_location_example",
                "kind": "CURL",
                "oci_home": "oci_home_example"
            },
            "target": {
                "wallet_location": "wallet_location_example",
                "kind": "CURL",
                "oci_home": "oci_home_example"
            }
        },
        "initial_load_settings": {
            "is_consistent": true,
            "is_tz_utc": true,
            "compatibility": [],
            "primary_key_compatibility": "NONE",
            "is_ignore_existing_objects": true,
            "handle_grant_errors": "ABORT",
            "job_mode": "FULL",
            "data_pump_parameters": {
                "is_cluster": true,
                "estimate": "BLOCKS",
                "table_exists_action": "TRUNCATE",
                "exclude_parameters": [],
                "import_parallelism_degree": 56,
                "export_parallelism_degree": 56
            },
            "tablespace_details": {
                "is_auto_create": true,
                "is_big_file": true,
                "extend_size_in_mbs": 56,
                "block_size_in_kbs": "SIZE_8K",
                "target_type": "ADB_S_REMAP",
                "remap_target": "remap_target_example"
            },
            "export_directory_object": {
                "name": "name_example",
                "path": "path_example"
            },
            "import_directory_object": {
                "name": "name_example",
                "path": "path_example"
            },
            "metadata_remaps": [{
                "type": "SCHEMA",
                "old_value": "old_value_example",
                "new_value": "new_value_example"
            }]
        },
        "advisor_settings": {
            "is_skip_advisor": true,
            "is_ignore_errors": true
        },
        "hub_details": {
            "rest_admin_credentials": {
                "username": "username_example"
            },
            "url": "url_example",
            "compute_id": "ocid1.compute.oc1..xxxxxxEXAMPLExxxxxx",
            "vault_id": "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx",
            "key_id": "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx",
            "extract": {
                "performance_profile": "LOW",
                "long_trans_duration": 56
            },
            "replicat": {
                "performance_profile": "LOW"
            },
            "acceptable_lag": 56
        },
        "ggs_details": {
            "ggs_deployment": {
                "deployment_id": "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx",
                "ggs_admin_credentials_secret_id": "ocid1.ggsadmincredentialssecret.oc1..xxxxxxEXAMPLExxxxxx"
            },
            "replicat": {
                "performance_profile": "LOW"
            },
            "acceptable_lag": 56,
            "extract": {
                "performance_profile": "LOW",
                "long_trans_duration": 56
            }
        },
        "source_container_database_connection_id": "ocid1.sourcecontainerdatabaseconnection.oc1..xxxxxxEXAMPLExxxxxx",
        "advanced_parameters": [{
            "value": "value_example",
            "name": "name_example",
            "data_type": "STRING"
        }]
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
    from oci.database_migration import DatabaseMigrationClient
    from oci.database_migration.models import CreateMigrationDetails
    from oci.database_migration.models import UpdateMigrationDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MigrationHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(MigrationHelperGen, self).get_possible_entity_types() + [
            "odmsmigration",
            "odmsmigrations",
            "databaseMigrationodmsmigration",
            "databaseMigrationodmsmigrations",
            "odmsmigrationresource",
            "odmsmigrationsresource",
            "migration",
            "migrations",
            "databaseMigrationmigration",
            "databaseMigrationmigrations",
            "migrationresource",
            "migrationsresource",
            "databasemigration",
        ]

    def get_module_resource_id_param(self):
        return "migration_id"

    def get_module_resource_id(self):
        return self.module.params.get("migration_id")

    def get_get_fn(self):
        return self.client.get_migration

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_migration, migration_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_migration,
            migration_id=self.module.params.get("migration_id"),
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
        return oci_common_utils.list_all_resources(
            self.client.list_migrations, **kwargs
        )

    def get_create_model_class(self):
        return CreateMigrationDetails

    def get_exclude_attributes(self):
        return [
            "exclude_objects",
            "hub_details.rest_admin_credentials.password",
            "include_objects",
            "bulk_include_exclude_data",
        ]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_migration,
            call_fn_args=(),
            call_fn_kwargs=dict(create_migration_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateMigrationDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_migration,
            call_fn_args=(),
            call_fn_kwargs=dict(
                migration_id=self.module.params.get("migration_id"),
                update_migration_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_migration,
            call_fn_args=(),
            call_fn_kwargs=dict(migration_id=self.module.params.get("migration_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


MigrationHelperCustom = get_custom_class("MigrationHelperCustom")


class ResourceHelper(MigrationHelperCustom, MigrationHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            exclude_objects=dict(
                type="list",
                elements="dict",
                options=dict(
                    schema=dict(type="str"),
                    owner=dict(type="str"),
                    object_name=dict(type="str", required=True),
                    type=dict(type="str"),
                    is_omit_excluded_table_from_replication=dict(type="bool"),
                ),
            ),
            include_objects=dict(
                type="list",
                elements="dict",
                options=dict(
                    schema=dict(type="str"),
                    owner=dict(type="str"),
                    object_name=dict(type="str", required=True),
                    type=dict(type="str"),
                    is_omit_excluded_table_from_replication=dict(type="bool"),
                ),
            ),
            bulk_include_exclude_data=dict(type="str"),
            description=dict(type="str"),
            database_combination=dict(type="str", choices=["MYSQL", "ORACLE"]),
            type=dict(type="str", choices=["ONLINE", "OFFLINE"]),
            display_name=dict(aliases=["name"], type="str"),
            source_database_connection_id=dict(type="str"),
            target_database_connection_id=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            data_transfer_medium_details=dict(
                type="dict",
                options=dict(
                    region=dict(type="str"),
                    access_key_id=dict(type="str"),
                    secret_access_key=dict(type="str", no_log=True),
                    shared_storage_mount_target_id=dict(type="str"),
                    source=dict(
                        type="dict",
                        options=dict(
                            oci_home=dict(type="str"),
                            wallet_location=dict(type="str"),
                            kind=dict(
                                type="str", required=True, choices=["OCI_CLI", "CURL"]
                            ),
                        ),
                    ),
                    target=dict(
                        type="dict",
                        options=dict(
                            oci_home=dict(type="str"),
                            wallet_location=dict(type="str"),
                            kind=dict(
                                type="str", required=True, choices=["OCI_CLI", "CURL"]
                            ),
                        ),
                    ),
                    type=dict(
                        type="str",
                        required=True,
                        choices=["OBJECT_STORAGE", "DBLINK", "NFS", "AWS_S3"],
                    ),
                    object_storage_bucket=dict(
                        type="dict",
                        options=dict(
                            namespace_name=dict(type="str"),
                            bucket_name=dict(type="str"),
                        ),
                    ),
                    name=dict(type="str"),
                ),
            ),
            initial_load_settings=dict(
                type="dict",
                options=dict(
                    is_consistent=dict(type="bool"),
                    is_tz_utc=dict(type="bool"),
                    compatibility=dict(type="list", elements="str"),
                    primary_key_compatibility=dict(
                        type="str",
                        choices=["NONE", "IGNORE_MISSING_PKS", "CREATE_INVISIBLE_PKS"],
                        no_log=True,
                    ),
                    is_ignore_existing_objects=dict(type="bool"),
                    handle_grant_errors=dict(
                        type="str", choices=["ABORT", "DROP_ACCOUNT", "IGNORE"]
                    ),
                    data_pump_parameters=dict(
                        type="dict",
                        options=dict(
                            is_cluster=dict(type="bool"),
                            estimate=dict(type="str", choices=["BLOCKS", "STATISTICS"]),
                            table_exists_action=dict(
                                type="str",
                                choices=["TRUNCATE", "REPLACE", "APPEND", "SKIP"],
                            ),
                            exclude_parameters=dict(type="list", elements="str"),
                            import_parallelism_degree=dict(type="int"),
                            export_parallelism_degree=dict(type="int"),
                        ),
                    ),
                    tablespace_details=dict(
                        type="dict",
                        options=dict(
                            remap_target=dict(type="str"),
                            is_auto_create=dict(type="bool"),
                            is_big_file=dict(type="bool"),
                            extend_size_in_mbs=dict(type="int"),
                            block_size_in_kbs=dict(
                                type="str", choices=["SIZE_8K", "SIZE_16K"]
                            ),
                            target_type=dict(
                                type="str",
                                required=True,
                                choices=[
                                    "NON_ADB_AUTOCREATE",
                                    "NON_ADB_REMAP",
                                    "ADB_D_REMAP",
                                    "ADB_S_REMAP",
                                    "ADB_D_AUTOCREATE",
                                    "TARGET_DEFAULTS_REMAP",
                                    "TARGET_DEFAULTS_AUTOCREATE",
                                ],
                            ),
                        ),
                    ),
                    export_directory_object=dict(
                        type="dict",
                        options=dict(name=dict(type="str"), path=dict(type="str")),
                    ),
                    import_directory_object=dict(
                        type="dict",
                        options=dict(name=dict(type="str"), path=dict(type="str")),
                    ),
                    job_mode=dict(
                        type="str",
                        required=True,
                        choices=[
                            "FULL",
                            "SCHEMA",
                            "TABLE",
                            "TABLESPACE",
                            "TRANSPORTABLE",
                        ],
                    ),
                    metadata_remaps=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            type=dict(
                                type="str",
                                required=True,
                                choices=["SCHEMA", "TABLESPACE", "DATAFILE", "TABLE"],
                            ),
                            old_value=dict(type="str", required=True),
                            new_value=dict(type="str", required=True),
                        ),
                    ),
                ),
            ),
            advisor_settings=dict(
                type="dict",
                options=dict(
                    is_skip_advisor=dict(type="bool"),
                    is_ignore_errors=dict(type="bool"),
                ),
            ),
            hub_details=dict(
                type="dict",
                options=dict(
                    rest_admin_credentials=dict(
                        type="dict",
                        options=dict(
                            username=dict(type="str"),
                            password=dict(type="str", no_log=True),
                        ),
                    ),
                    url=dict(type="str"),
                    compute_id=dict(type="str"),
                    vault_id=dict(type="str"),
                    key_id=dict(type="str"),
                    extract=dict(
                        type="dict",
                        options=dict(
                            performance_profile=dict(
                                type="str", choices=["LOW", "MEDIUM", "HIGH"]
                            ),
                            long_trans_duration=dict(type="int"),
                        ),
                    ),
                    replicat=dict(
                        type="dict",
                        options=dict(
                            performance_profile=dict(
                                type="str", choices=["LOW", "HIGH"]
                            )
                        ),
                    ),
                    acceptable_lag=dict(type="int"),
                ),
            ),
            ggs_details=dict(
                type="dict",
                options=dict(
                    extract=dict(
                        type="dict",
                        options=dict(
                            performance_profile=dict(
                                type="str", choices=["LOW", "MEDIUM", "HIGH"]
                            ),
                            long_trans_duration=dict(type="int"),
                        ),
                    ),
                    replicat=dict(
                        type="dict",
                        options=dict(
                            performance_profile=dict(
                                type="str", choices=["LOW", "HIGH"]
                            )
                        ),
                    ),
                    acceptable_lag=dict(type="int"),
                ),
            ),
            advanced_parameters=dict(
                type="list",
                elements="dict",
                options=dict(
                    value=dict(type="str", required=True),
                    name=dict(type="str", required=True),
                    data_type=dict(
                        type="str",
                        required=True,
                        choices=["STRING", "INTEGER", "FLOAT", "BOOLEAN"],
                    ),
                ),
            ),
            source_container_database_connection_id=dict(type="str"),
            migration_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="migration",
        service_client_class=DatabaseMigrationClient,
        namespace="database_migration",
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

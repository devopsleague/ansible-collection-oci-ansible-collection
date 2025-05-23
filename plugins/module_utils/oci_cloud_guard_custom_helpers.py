# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type


class DetectorRecipeHelperCustom:
    # excluding the responder_rules param from being used in idempotency as the detector_rules object is
    # not getting converted to dict format by the method to_dict which causes the idempotency check
    # to fail and create another resource with the same attributes
    def get_exclude_attributes(self):
        exclude_attributes = super(
            DetectorRecipeHelperCustom, self
        ).get_exclude_attributes()
        return exclude_attributes + [
            "detector_rules",
        ]


class ResponderRecipeHelperCustom:
    # excluding the responder_rules param from being used in idempotency as the responder_rules object is
    # not getting converted to dict format by the method to_dict which causes the idempotency check
    # to fail and create another resource with the same attributes
    def get_exclude_attributes(self):
        exclude_attributes = super(
            ResponderRecipeHelperCustom, self
        ).get_exclude_attributes()
        return exclude_attributes + [
            "responder_rules",
        ]


class TargetHelperCustom:
    # changing the name of the input parameter target_detector_recipe_id and target_responder_recipe_id to
    # detector_recipe_id and responder_recipe_id respectively as the get_resource() object changes the name
    #
    # removing the "details" suboption of the parameter target_detector_recipes.detector_rules and
    # target_responder_recipes.responder_rules as get_resource() contains too many rules for comparison and
    # has extra suboptions than that provided in the input parameter causing reource to be non-idempotent
    def get_update_model_dict_for_idempotence_check(self, update_model):
        update_model_dict = super(
            TargetHelperCustom, self
        ).get_update_model_dict_for_idempotence_check(update_model)

        if update_model_dict.get("target_detector_recipes") is not None:
            for recipes_list in update_model_dict.get("target_detector_recipes"):
                if "target_detector_recipe_id" in recipes_list:
                    recipes_list["detector_recipe_id"] = recipes_list.get(
                        "target_detector_recipe_id"
                    )
                    recipes_list.pop("target_detector_recipe_id", None)

                if recipes_list.get("detector_rules") is not None:
                    for rules_list in recipes_list.get("detector_rules"):
                        rules_list.pop("details", None)

        if update_model_dict.get("target_responder_recipes") is not None:
            for recipes_list in update_model_dict.get("target_responder_recipes"):
                if "target_responder_recipe_id" in recipes_list:
                    recipes_list["responder_recipe_id"] = recipes_list.get(
                        "target_responder_recipe_id"
                    )
                    recipes_list.pop("target_responder_recipe_id", None)

                if recipes_list.get("responder_rules") is not None:
                    for rules_list in recipes_list.get("responder_rules"):
                        rules_list.pop("details", None)

        return update_model_dict

    # changing the name of the input parameter target_detector_recipe_id and target_responder_recipe_id to
    # detector_recipe_id and responder_recipe_id respectively as the get_resource() object changes the name
    #
    # removing the "details" suboption of the parameter target_detector_recipes.detector_rules and
    # target_responder_recipes.responder_rules as get_resource() contains too many rules for comparison and
    # has extra suboptions than that provided in the input parameter causing reource to be non-idempotent
    def get_create_model_dict_for_idempotence_check(self, create_model):
        create_model_dict = super(
            TargetHelperCustom, self
        ).get_create_model_dict_for_idempotence_check(create_model)

        if create_model_dict.get("target_detector_recipes"):
            for recipes_list in create_model_dict["target_detector_recipes"]:
                if "target_detector_recipe_id" in recipes_list:
                    recipes_list["detector_recipe_id"] = recipes_list[
                        "target_detector_recipe_id"
                    ]
                    del recipes_list["target_detector_recipe_id"]

                for rules_list in recipes_list["detector_rules"]:
                    del rules_list["details"]

        if create_model_dict.get("target_responder_recipes"):
            for recipes_list in create_model_dict["target_responder_recipes"]:
                if "target_responder_recipe_id" in recipes_list:
                    recipes_list["responder_recipe_id"] = recipes_list[
                        "target_responder_recipe_id"
                    ]
                    del recipes_list["target_responder_recipe_id"]

                for rules_list in recipes_list["responder_rules"]:
                    del rules_list["details"]

        return create_model_dict


class SecurityZoneActionsHelperCustom:
    def is_action_necessary(self, action, resource=None):
        # this logic is decided by reading about api from the below link
        # https://docs.oracle.com/en-us/iaas/security-zone/using/managing-security-zones.htm

        if resource is not None:
            if action == "add_compartment":
                compartment_to_add = self.module.params.get("compartment_id")
                return (compartment_to_add != resource.compartment_id) and (
                    compartment_to_add not in resource.inherited_by_compartments
                )
            elif action == "remove_compartment":
                compartment_to_remove = self.module.params.get("compartment_id")
                return (compartment_to_remove != resource.compartment_id) and (
                    compartment_to_remove in resource.inherited_by_compartments
                )

        return super(SecurityZoneActionsHelperCustom, self).is_action_necessary(
            action, resource
        )

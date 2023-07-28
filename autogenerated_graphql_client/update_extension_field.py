# Generated by ariadne-codegen on 2023-07-28 09:56
# Source: queries.graphql

from uuid import UUID

from .base_model import BaseModel


class UpdateExtensionField(BaseModel):
    engagement_update: "UpdateExtensionFieldEngagementUpdate"


class UpdateExtensionFieldEngagementUpdate(BaseModel):
    uuid: UUID


UpdateExtensionField.update_forward_refs()
UpdateExtensionFieldEngagementUpdate.update_forward_refs()
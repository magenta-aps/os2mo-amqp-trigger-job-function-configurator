# Generated by ariadne-codegen on 2023-07-27 14:37
# Source: queries.graphql

from uuid import UUID

from .base_model import BaseModel


class MyMutation(BaseModel):
    engagement_update: "MyMutationEngagementUpdate"


class MyMutationEngagementUpdate(BaseModel):
    uuid: UUID


MyMutation.update_forward_refs()
MyMutationEngagementUpdate.update_forward_refs()

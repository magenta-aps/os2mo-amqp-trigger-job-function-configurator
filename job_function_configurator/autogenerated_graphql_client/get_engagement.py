# Generated by ariadne-codegen on 2023-10-31 17:44
# Source: queries.graphql

from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import Field

from .base_model import BaseModel


class GetEngagement(BaseModel):
    engagements: "GetEngagementEngagements"


class GetEngagementEngagements(BaseModel):
    objects: List["GetEngagementEngagementsObjects"]


class GetEngagementEngagementsObjects(BaseModel):
    current: Optional["GetEngagementEngagementsObjectsCurrent"]
    uuid: UUID


class GetEngagementEngagementsObjectsCurrent(BaseModel):
    validity: "GetEngagementEngagementsObjectsCurrentValidity"
    extension_2: Optional[str]
    extension_3: Optional[str]
    is_primary: bool
    job_function: "GetEngagementEngagementsObjectsCurrentJobFunction"
    primary: Optional["GetEngagementEngagementsObjectsCurrentPrimary"]
    person: List["GetEngagementEngagementsObjectsCurrentPerson"]


class GetEngagementEngagementsObjectsCurrentValidity(BaseModel):
    from_: datetime = Field(alias="from")
    to: Optional[datetime]


class GetEngagementEngagementsObjectsCurrentJobFunction(BaseModel):
    name: str
    user_key: str
    uuid: UUID


class GetEngagementEngagementsObjectsCurrentPrimary(BaseModel):
    name: str
    user_key: str
    uuid: UUID


class GetEngagementEngagementsObjectsCurrentPerson(BaseModel):
    uuid: UUID
    addresses: List["GetEngagementEngagementsObjectsCurrentPersonAddresses"]


class GetEngagementEngagementsObjectsCurrentPersonAddresses(BaseModel):
    name: Optional[str]
    user_key: str
    address_type: "GetEngagementEngagementsObjectsCurrentPersonAddressesAddressType"


class GetEngagementEngagementsObjectsCurrentPersonAddressesAddressType(BaseModel):
    scope: Optional[str]
    user_key: str
    name: str


GetEngagement.update_forward_refs()
GetEngagementEngagements.update_forward_refs()
GetEngagementEngagementsObjects.update_forward_refs()
GetEngagementEngagementsObjectsCurrent.update_forward_refs()
GetEngagementEngagementsObjectsCurrentValidity.update_forward_refs()
GetEngagementEngagementsObjectsCurrentJobFunction.update_forward_refs()
GetEngagementEngagementsObjectsCurrentPrimary.update_forward_refs()
GetEngagementEngagementsObjectsCurrentPerson.update_forward_refs()
GetEngagementEngagementsObjectsCurrentPersonAddresses.update_forward_refs()
GetEngagementEngagementsObjectsCurrentPersonAddressesAddressType.update_forward_refs()

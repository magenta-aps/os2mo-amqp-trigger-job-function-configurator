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


class GetEngagementEngagementsObjectsCurrent(BaseModel):
    validity: "GetEngagementEngagementsObjectsCurrentValidity"
    user_key: str
    extension_1: Optional[str]
    extension_2: Optional[str]
    extension_3: Optional[str]
    extension_4: Optional[str]
    extension_5: Optional[str]
    extension_6: Optional[str]
    extension_7: Optional[str]
    extension_8: Optional[str]
    extension_9: Optional[str]
    extension_10: Optional[str]
    is_primary: bool
    primary: Optional["GetEngagementEngagementsObjectsCurrentPrimary"]
    job_function: "GetEngagementEngagementsObjectsCurrentJobFunction"
    engagement_type: "GetEngagementEngagementsObjectsCurrentEngagementType"
    org_unit: List["GetEngagementEngagementsObjectsCurrentOrgUnit"]
    person: List["GetEngagementEngagementsObjectsCurrentPerson"]


class GetEngagementEngagementsObjectsCurrentValidity(BaseModel):
    from_: datetime = Field(alias="from")
    to: Optional[datetime]


class GetEngagementEngagementsObjectsCurrentPrimary(BaseModel):
    uuid: UUID


class GetEngagementEngagementsObjectsCurrentJobFunction(BaseModel):
    uuid: UUID
    name: str
    user_key: str


class GetEngagementEngagementsObjectsCurrentEngagementType(BaseModel):
    uuid: UUID


class GetEngagementEngagementsObjectsCurrentOrgUnit(BaseModel):
    uuid: UUID


class GetEngagementEngagementsObjectsCurrentPerson(BaseModel):
    uuid: UUID
    itusers: List["GetEngagementEngagementsObjectsCurrentPersonItusers"]


class GetEngagementEngagementsObjectsCurrentPersonItusers(BaseModel):
    user_key: str


GetEngagement.update_forward_refs()
GetEngagementEngagements.update_forward_refs()
GetEngagementEngagementsObjects.update_forward_refs()
GetEngagementEngagementsObjectsCurrent.update_forward_refs()
GetEngagementEngagementsObjectsCurrentValidity.update_forward_refs()
GetEngagementEngagementsObjectsCurrentPrimary.update_forward_refs()
GetEngagementEngagementsObjectsCurrentJobFunction.update_forward_refs()
GetEngagementEngagementsObjectsCurrentEngagementType.update_forward_refs()
GetEngagementEngagementsObjectsCurrentOrgUnit.update_forward_refs()
GetEngagementEngagementsObjectsCurrentPerson.update_forward_refs()
GetEngagementEngagementsObjectsCurrentPersonItusers.update_forward_refs()

from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import Field

from .base_model import BaseModel


class TestingGetEngagementTimeline(BaseModel):
    engagements: "TestingGetEngagementTimelineEngagements"


class TestingGetEngagementTimelineEngagements(BaseModel):
    objects: List["TestingGetEngagementTimelineEngagementsObjects"]


class TestingGetEngagementTimelineEngagementsObjects(BaseModel):
    objects: List["TestingGetEngagementTimelineEngagementsObjectsObjects"]


class TestingGetEngagementTimelineEngagementsObjectsObjects(BaseModel):
    uuid: UUID
    user_key: str
    validity: "TestingGetEngagementTimelineEngagementsObjectsObjectsValidity"
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
    fraction: Optional[int]
    is_primary: bool
    primary: Optional["TestingGetEngagementTimelineEngagementsObjectsObjectsPrimary"]
    job_function: "TestingGetEngagementTimelineEngagementsObjectsObjectsJobFunction"
    engagement_type: (
        "TestingGetEngagementTimelineEngagementsObjectsObjectsEngagementType"
    )
    person: List["TestingGetEngagementTimelineEngagementsObjectsObjectsPerson"]
    org_unit: List["TestingGetEngagementTimelineEngagementsObjectsObjectsOrgUnit"]


class TestingGetEngagementTimelineEngagementsObjectsObjectsValidity(BaseModel):
    from_: datetime = Field(alias="from")
    to: Optional[datetime]


class TestingGetEngagementTimelineEngagementsObjectsObjectsPrimary(BaseModel):
    uuid: UUID


class TestingGetEngagementTimelineEngagementsObjectsObjectsJobFunction(BaseModel):
    uuid: UUID


class TestingGetEngagementTimelineEngagementsObjectsObjectsEngagementType(BaseModel):
    uuid: UUID


class TestingGetEngagementTimelineEngagementsObjectsObjectsPerson(BaseModel):
    uuid: UUID


class TestingGetEngagementTimelineEngagementsObjectsObjectsOrgUnit(BaseModel):
    uuid: UUID


TestingGetEngagementTimeline.update_forward_refs()
TestingGetEngagementTimelineEngagements.update_forward_refs()
TestingGetEngagementTimelineEngagementsObjects.update_forward_refs()
TestingGetEngagementTimelineEngagementsObjectsObjects.update_forward_refs()
TestingGetEngagementTimelineEngagementsObjectsObjectsValidity.update_forward_refs()
TestingGetEngagementTimelineEngagementsObjectsObjectsPrimary.update_forward_refs()
TestingGetEngagementTimelineEngagementsObjectsObjectsJobFunction.update_forward_refs()
TestingGetEngagementTimelineEngagementsObjectsObjectsEngagementType.update_forward_refs()
TestingGetEngagementTimelineEngagementsObjectsObjectsPerson.update_forward_refs()
TestingGetEngagementTimelineEngagementsObjectsObjectsOrgUnit.update_forward_refs()

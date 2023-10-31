# Generated by ariadne-codegen on 2023-10-31 17:44
# Source: schema.graphql

from datetime import datetime
from typing import Any, List, Optional
from uuid import UUID

from pydantic import Field

from .base_model import BaseModel
from .enums import AuditLogModel, FileStore


class AddressCreateInput(BaseModel):
    uuid: Optional[UUID] = None
    org_unit: Optional[UUID] = None
    person: Optional[UUID] = None
    employee: Optional[UUID] = None
    engagement: Optional[UUID] = None
    visibility: Optional[UUID] = None
    validity: "RAValidityInput"
    user_key: Optional[str] = None
    value: str
    address_type: UUID


class AddressFilter(BaseModel):
    uuids: Optional[List[UUID]] = None
    user_keys: Optional[List[str]] = None
    from_date: Optional[datetime]
    to_date: Optional[datetime]
    address_types: Optional[List[UUID]] = None
    address_type_user_keys: Optional[List[str]] = None
    employees: Optional[List[UUID]] = None
    engagements: Optional[List[UUID]] = None
    org_units: Optional[List[UUID]] = None


class AddressTerminateInput(BaseModel):
    from_: Optional[datetime] = Field(alias="from", default=None)
    to: datetime
    uuid: UUID


class AddressUpdateInput(BaseModel):
    uuid: UUID
    org_unit: Optional[UUID] = None
    person: Optional[UUID] = None
    employee: Optional[UUID] = None
    engagement: Optional[UUID] = None
    visibility: Optional[UUID] = None
    validity: "RAValidityInput"
    user_key: Optional[str] = None
    value: Optional[str] = None
    address_type: Optional[UUID] = None


class AssociationCreateInput(BaseModel):
    uuid: Optional[UUID] = None
    user_key: Optional[str] = None
    primary: Optional[UUID] = None
    validity: "RAValidityInput"
    person: Optional[UUID] = None
    employee: Optional[UUID] = None
    org_unit: UUID
    association_type: UUID


class AssociationFilter(BaseModel):
    uuids: Optional[List[UUID]] = None
    user_keys: Optional[List[str]] = None
    from_date: Optional[datetime]
    to_date: Optional[datetime]
    employees: Optional[List[UUID]] = None
    org_units: Optional[List[UUID]] = None
    association_types: Optional[List[UUID]] = None
    association_type_user_keys: Optional[List[str]] = None
    it_association: Optional[bool] = None


class AssociationTerminateInput(BaseModel):
    from_: Optional[datetime] = Field(alias="from", default=None)
    to: datetime
    uuid: UUID


class AssociationUpdateInput(BaseModel):
    uuid: UUID
    user_key: Optional[str] = None
    primary: Optional[UUID] = None
    validity: "RAValidityInput"
    person: Optional[UUID] = None
    employee: Optional[UUID] = None
    org_unit: Optional[UUID] = None
    association_type: Optional[UUID] = None


class AuditLogFilter(BaseModel):
    ids: Optional[List[UUID]] = None
    uuids: Optional[List[UUID]] = None
    actors: Optional[List[UUID]] = None
    models: Optional[List[AuditLogModel]] = None
    start: Optional[datetime] = None
    end: Optional[datetime] = None


class ClassCreateInput(BaseModel):
    uuid: Optional[UUID] = None
    name: str
    user_key: str
    facet_uuid: UUID
    scope: Optional[str] = None
    published: str = "Publiceret"
    parent_uuid: Optional[UUID] = None
    example: Optional[str] = None
    owner: Optional[UUID] = None
    validity: "ValidityInput"


class ClassFilter(BaseModel):
    uuids: Optional[List[UUID]] = None
    user_keys: Optional[List[str]] = None
    from_date: Optional[datetime]
    to_date: Optional[datetime]
    facets: Optional[List[UUID]] = None
    facet_user_keys: Optional[List[str]] = None
    parents: Optional[List[UUID]] = None
    parent_user_keys: Optional[List[str]] = None


class ClassTerminateInput(BaseModel):
    from_: Optional[datetime] = Field(alias="from", default=None)
    to: datetime
    uuid: UUID


class ClassUpdateInput(BaseModel):
    uuid: UUID
    name: str
    user_key: str
    facet_uuid: UUID
    scope: Optional[str] = None
    published: str = "Publiceret"
    parent_uuid: Optional[UUID] = None
    example: Optional[str] = None
    owner: Optional[UUID] = None
    validity: "ValidityInput"


class ConfigurationFilter(BaseModel):
    identifiers: Optional[List[str]] = None


class EmployeeCreateInput(BaseModel):
    uuid: Optional[UUID] = None
    user_key: Optional[str] = None
    nickname_given_name: Optional[str] = None
    nickname_surname: Optional[str] = None
    seniority: Optional[Any] = None
    cpr_number: Optional[Any] = None
    given_name: str
    surname: str


class EmployeeFilter(BaseModel):
    uuids: Optional[List[UUID]] = None
    user_keys: Optional[List[str]] = None
    from_date: Optional[datetime]
    to_date: Optional[datetime]
    query: Optional[str]
    cpr_numbers: Optional[List[Any]] = None


class EmployeeTerminateInput(BaseModel):
    from_: Optional[datetime] = Field(alias="from", default=None)
    to: datetime
    uuid: UUID


class EmployeeUpdateInput(BaseModel):
    uuid: UUID
    user_key: Optional[str] = None
    nickname_given_name: Optional[str] = None
    nickname_surname: Optional[str] = None
    seniority: Optional[Any] = None
    cpr_number: Optional[Any] = None
    given_name: Optional[str] = None
    surname: Optional[str] = None
    validity: "RAValidityInput"


class EmployeesBoundAddressFilter(BaseModel):
    uuids: Optional[List[UUID]] = None
    user_keys: Optional[List[str]] = None
    from_date: Optional[datetime]
    to_date: Optional[datetime]
    address_types: Optional[List[UUID]] = None
    address_type_user_keys: Optional[List[str]] = None
    engagements: Optional[List[UUID]] = None
    org_units: Optional[List[UUID]] = None


class EmployeesBoundAssociationFilter(BaseModel):
    uuids: Optional[List[UUID]] = None
    user_keys: Optional[List[str]] = None
    from_date: Optional[datetime]
    to_date: Optional[datetime]
    org_units: Optional[List[UUID]] = None
    association_types: Optional[List[UUID]] = None
    association_type_user_keys: Optional[List[str]] = None
    it_association: Optional[bool] = None


class EmployeesBoundEngagementFilter(BaseModel):
    uuids: Optional[List[UUID]] = None
    user_keys: Optional[List[str]] = None
    from_date: Optional[datetime]
    to_date: Optional[datetime]
    org_units: Optional[List[UUID]] = None


class EmployeesBoundITUserFilter(BaseModel):
    uuids: Optional[List[UUID]] = None
    user_keys: Optional[List[str]] = None
    from_date: Optional[datetime]
    to_date: Optional[datetime]
    org_units: Optional[List[UUID]] = None
    itsystem_uuids: Optional[List[UUID]] = None


class EmployeesBoundLeaveFilter(BaseModel):
    uuids: Optional[List[UUID]] = None
    user_keys: Optional[List[str]] = None
    from_date: Optional[datetime]
    to_date: Optional[datetime]
    org_units: Optional[List[UUID]] = None


class EmployeesBoundManagerFilter(BaseModel):
    uuids: Optional[List[UUID]] = None
    user_keys: Optional[List[str]] = None
    from_date: Optional[datetime]
    to_date: Optional[datetime]
    org_units: Optional[List[UUID]] = None


class EmployeesBoundRoleFilter(BaseModel):
    uuids: Optional[List[UUID]] = None
    user_keys: Optional[List[str]] = None
    from_date: Optional[datetime]
    to_date: Optional[datetime]
    org_units: Optional[List[UUID]] = None


class EngagementCreateInput(BaseModel):
    uuid: Optional[UUID] = None
    user_key: Optional[str] = None
    primary: Optional[UUID] = None
    validity: "RAValidityInput"
    extension_1: Optional[str] = None
    extension_2: Optional[str] = None
    extension_3: Optional[str] = None
    extension_4: Optional[str] = None
    extension_5: Optional[str] = None
    extension_6: Optional[str] = None
    extension_7: Optional[str] = None
    extension_8: Optional[str] = None
    extension_9: Optional[str] = None
    extension_10: Optional[str] = None
    employee: Optional[UUID] = None
    person: Optional[UUID] = None
    org_unit: UUID
    engagement_type: UUID
    job_function: UUID


class EngagementFilter(BaseModel):
    uuids: Optional[List[UUID]] = None
    user_keys: Optional[List[str]] = None
    from_date: Optional[datetime]
    to_date: Optional[datetime]
    employees: Optional[List[UUID]] = None
    org_units: Optional[List[UUID]] = None


class EngagementTerminateInput(BaseModel):
    from_: Optional[datetime] = Field(alias="from", default=None)
    to: datetime
    uuid: UUID


class EngagementUpdateInput(BaseModel):
    uuid: UUID
    user_key: Optional[str] = None
    primary: Optional[UUID] = None
    validity: "RAValidityInput"
    extension_1: Optional[str] = None
    extension_2: Optional[str] = None
    extension_3: Optional[str] = None
    extension_4: Optional[str] = None
    extension_5: Optional[str] = None
    extension_6: Optional[str] = None
    extension_7: Optional[str] = None
    extension_8: Optional[str] = None
    extension_9: Optional[str] = None
    extension_10: Optional[str] = None
    employee: Optional[UUID] = None
    person: Optional[UUID] = None
    org_unit: Optional[UUID] = None
    engagement_type: Optional[UUID] = None
    job_function: Optional[UUID] = None


class FacetCreateInput(BaseModel):
    user_key: str
    published: str = "Publiceret"
    validity: "ValidityInput"


class FacetFilter(BaseModel):
    uuids: Optional[List[UUID]] = None
    user_keys: Optional[List[str]] = None
    from_date: Optional[datetime]
    to_date: Optional[datetime]
    parents: Optional[List[UUID]] = None
    parent_user_keys: Optional[List[str]] = None


class FacetTerminateInput(BaseModel):
    from_: Optional[datetime] = Field(alias="from", default=None)
    to: datetime
    uuid: UUID


class FacetUpdateInput(BaseModel):
    user_key: str
    published: str = "Publiceret"
    validity: "ValidityInput"
    uuid: UUID


class FacetsBoundClassFilter(BaseModel):
    uuids: Optional[List[UUID]] = None
    user_keys: Optional[List[str]] = None
    from_date: Optional[datetime]
    to_date: Optional[datetime]
    facet_user_keys: Optional[List[str]] = None
    parents: Optional[List[UUID]] = None
    parent_user_keys: Optional[List[str]] = None


class FileFilter(BaseModel):
    file_store: FileStore
    file_names: Optional[List[str]] = None


class HealthFilter(BaseModel):
    identifiers: Optional[List[str]] = None


class ITAssociationCreateInput(BaseModel):
    uuid: Optional[UUID] = None
    user_key: Optional[str] = None
    primary: Optional[UUID] = None
    validity: "RAValidityInput"
    org_unit: UUID
    person: UUID
    it_user: UUID
    job_function: UUID


class ITAssociationTerminateInput(BaseModel):
    from_: Optional[datetime] = Field(alias="from", default=None)
    to: datetime
    uuid: UUID


class ITAssociationUpdateInput(BaseModel):
    uuid: UUID
    user_key: Optional[str] = None
    primary: Optional[UUID] = None
    validity: "RAValidityInput"
    org_unit: Optional[UUID] = None
    it_user: Optional[UUID] = None
    job_function: Optional[UUID] = None


class ITSystemCreateInput(BaseModel):
    uuid: Optional[UUID] = None
    user_key: str
    name: str
    validity: "RAOpenValidityInput"


class ITSystemFilter(BaseModel):
    uuids: Optional[List[UUID]] = None
    user_keys: Optional[List[str]] = None
    from_date: Optional[datetime]
    to_date: Optional[datetime]


class ITSystemTerminateInput(BaseModel):
    from_: Optional[datetime] = Field(alias="from", default=None)
    to: datetime
    uuid: UUID


class ITSystemUpdateInput(BaseModel):
    uuid: UUID
    user_key: str
    name: str
    validity: "RAOpenValidityInput"


class ITUserCreateInput(BaseModel):
    uuid: Optional[UUID] = None
    primary: Optional[UUID] = None
    person: Optional[UUID] = None
    org_unit: Optional[UUID] = None
    engagement: Optional[UUID] = None
    validity: "RAValidityInput"
    user_key: str
    itsystem: UUID


class ITUserFilter(BaseModel):
    uuids: Optional[List[UUID]] = None
    user_keys: Optional[List[str]] = None
    from_date: Optional[datetime]
    to_date: Optional[datetime]
    employees: Optional[List[UUID]] = None
    org_units: Optional[List[UUID]] = None
    itsystem_uuids: Optional[List[UUID]] = None


class ITUserTerminateInput(BaseModel):
    from_: Optional[datetime] = Field(alias="from", default=None)
    to: datetime
    uuid: UUID


class ITUserUpdateInput(BaseModel):
    uuid: UUID
    primary: Optional[UUID] = None
    person: Optional[UUID] = None
    org_unit: Optional[UUID] = None
    engagement: Optional[UUID] = None
    validity: "RAValidityInput"
    user_key: Optional[str] = None
    itsystem: Optional[UUID] = None


class KLECreateInput(BaseModel):
    uuid: Optional[UUID] = None
    user_key: Optional[str] = None
    org_unit: UUID
    kle_aspects: List[UUID]
    kle_number: UUID
    validity: "RAValidityInput"


class KLEFilter(BaseModel):
    uuids: Optional[List[UUID]] = None
    user_keys: Optional[List[str]] = None
    from_date: Optional[datetime]
    to_date: Optional[datetime]
    org_units: Optional[List[UUID]] = None


class KLETerminateInput(BaseModel):
    from_: Optional[datetime] = Field(alias="from", default=None)
    to: datetime
    uuid: UUID


class KLEUpdateInput(BaseModel):
    uuid: UUID
    user_key: Optional[str] = None
    kle_number: Optional[UUID] = None
    kle_aspects: Optional[List[UUID]] = None
    org_unit: Optional[UUID] = None
    validity: "RAValidityInput"


class LeaveCreateInput(BaseModel):
    uuid: Optional[UUID] = None
    user_key: Optional[str] = None
    person: UUID
    engagement: UUID
    leave_type: UUID
    validity: "RAValidityInput"


class LeaveFilter(BaseModel):
    uuids: Optional[List[UUID]] = None
    user_keys: Optional[List[str]] = None
    from_date: Optional[datetime]
    to_date: Optional[datetime]
    employees: Optional[List[UUID]] = None
    org_units: Optional[List[UUID]] = None


class LeaveTerminateInput(BaseModel):
    from_: Optional[datetime] = Field(alias="from", default=None)
    to: datetime
    uuid: UUID


class LeaveUpdateInput(BaseModel):
    uuid: UUID
    user_key: Optional[str] = None
    person: Optional[UUID] = None
    engagement: Optional[UUID] = None
    leave_type: Optional[UUID] = None
    validity: "RAValidityInput"


class ManagerCreateInput(BaseModel):
    uuid: Optional[UUID] = None
    user_key: Optional[str] = None
    person: Optional[UUID] = None
    responsibility: List[UUID]
    org_unit: UUID
    manager_level: UUID
    manager_type: UUID
    validity: "RAValidityInput"


class ManagerFilter(BaseModel):
    uuids: Optional[List[UUID]] = None
    user_keys: Optional[List[str]] = None
    from_date: Optional[datetime]
    to_date: Optional[datetime]
    employees: Optional[List[UUID]] = None
    org_units: Optional[List[UUID]] = None


class ManagerTerminateInput(BaseModel):
    from_: Optional[datetime] = Field(alias="from", default=None)
    to: datetime
    uuid: UUID


class ManagerUpdateInput(BaseModel):
    uuid: UUID
    validity: "RAValidityInput"
    user_key: Optional[str] = None
    person: Optional[UUID] = None
    responsibility: Optional[List[UUID]] = None
    org_unit: Optional[UUID] = None
    manager_type: Optional[UUID] = None
    manager_level: Optional[UUID] = None


class ModelsUuidsBoundRegistrationFilter(BaseModel):
    actors: Optional[List[UUID]] = None
    start: Optional[datetime] = None
    end: Optional[datetime] = None


class OrgUnitsboundaddressfilter(BaseModel):
    uuids: Optional[List[UUID]] = None
    user_keys: Optional[List[str]] = None
    from_date: Optional[datetime]
    to_date: Optional[datetime]
    address_types: Optional[List[UUID]] = None
    address_type_user_keys: Optional[List[str]] = None
    employees: Optional[List[UUID]] = None
    engagements: Optional[List[UUID]] = None


class OrgUnitsboundassociationfilter(BaseModel):
    uuids: Optional[List[UUID]] = None
    user_keys: Optional[List[str]] = None
    from_date: Optional[datetime]
    to_date: Optional[datetime]
    employees: Optional[List[UUID]] = None
    association_types: Optional[List[UUID]] = None
    association_type_user_keys: Optional[List[str]] = None
    it_association: Optional[bool] = None


class OrgUnitsboundengagementfilter(BaseModel):
    uuids: Optional[List[UUID]] = None
    user_keys: Optional[List[str]] = None
    from_date: Optional[datetime]
    to_date: Optional[datetime]
    employees: Optional[List[UUID]] = None


class OrgUnitsboundituserfilter(BaseModel):
    uuids: Optional[List[UUID]] = None
    user_keys: Optional[List[str]] = None
    from_date: Optional[datetime]
    to_date: Optional[datetime]
    employees: Optional[List[UUID]] = None
    itsystem_uuids: Optional[List[UUID]] = None


class OrgUnitsboundklefilter(BaseModel):
    uuids: Optional[List[UUID]] = None
    user_keys: Optional[List[str]] = None
    from_date: Optional[datetime]
    to_date: Optional[datetime]


class OrgUnitsboundleavefilter(BaseModel):
    uuids: Optional[List[UUID]] = None
    user_keys: Optional[List[str]] = None
    from_date: Optional[datetime]
    to_date: Optional[datetime]
    employees: Optional[List[UUID]] = None


class OrgUnitsboundownerfilter(BaseModel):
    uuids: Optional[List[UUID]] = None
    user_keys: Optional[List[str]] = None
    from_date: Optional[datetime]
    to_date: Optional[datetime]
    employees: Optional[List[UUID]] = None


class OrgUnitsboundrelatedunitfilter(BaseModel):
    uuids: Optional[List[UUID]] = None
    user_keys: Optional[List[str]] = None
    from_date: Optional[datetime]
    to_date: Optional[datetime]


class OrgUnitsboundrolefilter(BaseModel):
    uuids: Optional[List[UUID]] = None
    user_keys: Optional[List[str]] = None
    from_date: Optional[datetime]
    to_date: Optional[datetime]
    employees: Optional[List[UUID]] = None


class OrganisationCreate(BaseModel):
    municipality_code: Optional[int]


class OrganisationUnitCreateInput(BaseModel):
    uuid: Optional[UUID] = None
    name: str
    user_key: Optional[str] = None
    parent: Optional[UUID] = None
    org_unit_type: UUID
    time_planning: Optional[UUID] = None
    org_unit_level: Optional[UUID] = None
    org_unit_hierarchy: Optional[UUID] = None
    validity: "RAValidityInput"


class OrganisationUnitFilter(BaseModel):
    uuids: Optional[List[UUID]] = None
    user_keys: Optional[List[str]] = None
    from_date: Optional[datetime]
    to_date: Optional[datetime]
    query: Optional[str]
    parents: Optional[List[UUID]]
    hierarchies: Optional[List[UUID]] = None


class OrganisationUnitTerminateInput(BaseModel):
    from_: Optional[datetime] = Field(alias="from", default=None)
    to: datetime
    uuid: UUID


class OrganisationUnitUpdateInput(BaseModel):
    uuid: UUID
    validity: "RAValidityInput"
    name: Optional[str] = None
    user_key: Optional[str] = None
    parent: Optional[UUID] = None
    org_unit_type: Optional[UUID] = None
    org_unit_level: Optional[UUID] = None
    org_unit_hierarchy: Optional[UUID] = None
    time_planning: Optional[UUID] = None


class OwnerFilter(BaseModel):
    uuids: Optional[List[UUID]] = None
    user_keys: Optional[List[str]] = None
    from_date: Optional[datetime]
    to_date: Optional[datetime]
    employees: Optional[List[UUID]] = None
    org_units: Optional[List[UUID]] = None


class ParentsBoundClassFilter(BaseModel):
    uuids: Optional[List[UUID]] = None
    user_keys: Optional[List[str]] = None
    from_date: Optional[datetime]
    to_date: Optional[datetime]
    facets: Optional[List[UUID]] = None
    facet_user_keys: Optional[List[str]] = None
    parent_user_keys: Optional[List[str]] = None


class ParentsBoundFacetFilter(BaseModel):
    uuids: Optional[List[UUID]] = None
    user_keys: Optional[List[str]] = None
    from_date: Optional[datetime]
    to_date: Optional[datetime]
    parent_user_keys: Optional[List[str]] = None


class ParentsBoundOrganisationUnitFilter(BaseModel):
    uuids: Optional[List[UUID]] = None
    user_keys: Optional[List[str]] = None
    from_date: Optional[datetime]
    to_date: Optional[datetime]
    query: Optional[str]
    hierarchies: Optional[List[UUID]] = None


class RAOpenValidityInput(BaseModel):
    from_: Optional[datetime] = Field(alias="from", default=None)
    to: Optional[datetime] = None


class RAValidityInput(BaseModel):
    from_: datetime = Field(alias="from")
    to: Optional[datetime] = None


class RegistrationFilter(BaseModel):
    uuids: Optional[List[UUID]] = None
    actors: Optional[List[UUID]] = None
    models: Optional[List[str]] = None
    start: Optional[datetime] = None
    end: Optional[datetime] = None


class RelatedUnitFilter(BaseModel):
    uuids: Optional[List[UUID]] = None
    user_keys: Optional[List[str]] = None
    from_date: Optional[datetime]
    to_date: Optional[datetime]
    org_units: Optional[List[UUID]] = None


class RelatedUnitsUpdateInput(BaseModel):
    uuid: Optional[UUID] = None
    origin: UUID
    destination: Optional[List[UUID]] = None
    validity: "RAValidityInput"


class RoleCreateInput(BaseModel):
    uuid: Optional[UUID] = None
    user_key: Optional[str] = None
    org_unit: UUID
    person: UUID
    role_type: UUID
    validity: "RAValidityInput"


class RoleFilter(BaseModel):
    uuids: Optional[List[UUID]] = None
    user_keys: Optional[List[str]] = None
    from_date: Optional[datetime]
    to_date: Optional[datetime]
    employees: Optional[List[UUID]] = None
    org_units: Optional[List[UUID]] = None


class RoleTerminateInput(BaseModel):
    from_: Optional[datetime] = Field(alias="from", default=None)
    to: datetime
    uuid: UUID


class RoleUpdateInput(BaseModel):
    uuid: UUID
    user_key: Optional[str] = None
    org_unit: Optional[UUID] = None
    role_type: Optional[UUID] = None
    validity: "RAValidityInput"


class UuidsBoundClassFilter(BaseModel):
    user_keys: Optional[List[str]] = None
    from_date: Optional[datetime]
    to_date: Optional[datetime]
    facets: Optional[List[UUID]] = None
    facet_user_keys: Optional[List[str]] = None
    parents: Optional[List[UUID]] = None
    parent_user_keys: Optional[List[str]] = None


class UuidsBoundEmployeeFilter(BaseModel):
    user_keys: Optional[List[str]] = None
    from_date: Optional[datetime]
    to_date: Optional[datetime]
    query: Optional[str]
    cpr_numbers: Optional[List[Any]] = None


class UuidsBoundEngagementFilter(BaseModel):
    user_keys: Optional[List[str]] = None
    from_date: Optional[datetime]
    to_date: Optional[datetime]
    employees: Optional[List[UUID]] = None
    org_units: Optional[List[UUID]] = None


class UuidsBoundFacetFilter(BaseModel):
    user_keys: Optional[List[str]] = None
    from_date: Optional[datetime]
    to_date: Optional[datetime]
    parents: Optional[List[UUID]] = None
    parent_user_keys: Optional[List[str]] = None


class UuidsBoundITSystemFilter(BaseModel):
    user_keys: Optional[List[str]] = None
    from_date: Optional[datetime]
    to_date: Optional[datetime]


class UuidsBoundITUserFilter(BaseModel):
    user_keys: Optional[List[str]] = None
    from_date: Optional[datetime]
    to_date: Optional[datetime]
    employees: Optional[List[UUID]] = None
    org_units: Optional[List[UUID]] = None
    itsystem_uuids: Optional[List[UUID]] = None


class UuidsBoundLeaveFilter(BaseModel):
    user_keys: Optional[List[str]] = None
    from_date: Optional[datetime]
    to_date: Optional[datetime]
    employees: Optional[List[UUID]] = None
    org_units: Optional[List[UUID]] = None


class UuidsBoundOrganisationUnitFilter(BaseModel):
    user_keys: Optional[List[str]] = None
    from_date: Optional[datetime]
    to_date: Optional[datetime]
    query: Optional[str]
    parents: Optional[List[UUID]]
    hierarchies: Optional[List[UUID]] = None


class ValidityInput(BaseModel):
    from_: Optional[datetime] = Field(alias="from", default=None)
    to: Optional[datetime] = None


AddressCreateInput.update_forward_refs()
AddressFilter.update_forward_refs()
AddressTerminateInput.update_forward_refs()
AddressUpdateInput.update_forward_refs()
AssociationCreateInput.update_forward_refs()
AssociationFilter.update_forward_refs()
AssociationTerminateInput.update_forward_refs()
AssociationUpdateInput.update_forward_refs()
AuditLogFilter.update_forward_refs()
ClassCreateInput.update_forward_refs()
ClassFilter.update_forward_refs()
ClassTerminateInput.update_forward_refs()
ClassUpdateInput.update_forward_refs()
ConfigurationFilter.update_forward_refs()
EmployeeCreateInput.update_forward_refs()
EmployeeFilter.update_forward_refs()
EmployeeTerminateInput.update_forward_refs()
EmployeeUpdateInput.update_forward_refs()
EmployeesBoundAddressFilter.update_forward_refs()
EmployeesBoundAssociationFilter.update_forward_refs()
EmployeesBoundEngagementFilter.update_forward_refs()
EmployeesBoundITUserFilter.update_forward_refs()
EmployeesBoundLeaveFilter.update_forward_refs()
EmployeesBoundManagerFilter.update_forward_refs()
EmployeesBoundRoleFilter.update_forward_refs()
EngagementCreateInput.update_forward_refs()
EngagementFilter.update_forward_refs()
EngagementTerminateInput.update_forward_refs()
EngagementUpdateInput.update_forward_refs()
FacetCreateInput.update_forward_refs()
FacetFilter.update_forward_refs()
FacetTerminateInput.update_forward_refs()
FacetUpdateInput.update_forward_refs()
FacetsBoundClassFilter.update_forward_refs()
FileFilter.update_forward_refs()
HealthFilter.update_forward_refs()
ITAssociationCreateInput.update_forward_refs()
ITAssociationTerminateInput.update_forward_refs()
ITAssociationUpdateInput.update_forward_refs()
ITSystemCreateInput.update_forward_refs()
ITSystemFilter.update_forward_refs()
ITSystemTerminateInput.update_forward_refs()
ITSystemUpdateInput.update_forward_refs()
ITUserCreateInput.update_forward_refs()
ITUserFilter.update_forward_refs()
ITUserTerminateInput.update_forward_refs()
ITUserUpdateInput.update_forward_refs()
KLECreateInput.update_forward_refs()
KLEFilter.update_forward_refs()
KLETerminateInput.update_forward_refs()
KLEUpdateInput.update_forward_refs()
LeaveCreateInput.update_forward_refs()
LeaveFilter.update_forward_refs()
LeaveTerminateInput.update_forward_refs()
LeaveUpdateInput.update_forward_refs()
ManagerCreateInput.update_forward_refs()
ManagerFilter.update_forward_refs()
ManagerTerminateInput.update_forward_refs()
ManagerUpdateInput.update_forward_refs()
ModelsUuidsBoundRegistrationFilter.update_forward_refs()
OrgUnitsboundaddressfilter.update_forward_refs()
OrgUnitsboundassociationfilter.update_forward_refs()
OrgUnitsboundengagementfilter.update_forward_refs()
OrgUnitsboundituserfilter.update_forward_refs()
OrgUnitsboundklefilter.update_forward_refs()
OrgUnitsboundleavefilter.update_forward_refs()
OrgUnitsboundownerfilter.update_forward_refs()
OrgUnitsboundrelatedunitfilter.update_forward_refs()
OrgUnitsboundrolefilter.update_forward_refs()
OrganisationCreate.update_forward_refs()
OrganisationUnitCreateInput.update_forward_refs()
OrganisationUnitFilter.update_forward_refs()
OrganisationUnitTerminateInput.update_forward_refs()
OrganisationUnitUpdateInput.update_forward_refs()
OwnerFilter.update_forward_refs()
ParentsBoundClassFilter.update_forward_refs()
ParentsBoundFacetFilter.update_forward_refs()
ParentsBoundOrganisationUnitFilter.update_forward_refs()
RAOpenValidityInput.update_forward_refs()
RAValidityInput.update_forward_refs()
RegistrationFilter.update_forward_refs()
RelatedUnitFilter.update_forward_refs()
RelatedUnitsUpdateInput.update_forward_refs()
RoleCreateInput.update_forward_refs()
RoleFilter.update_forward_refs()
RoleTerminateInput.update_forward_refs()
RoleUpdateInput.update_forward_refs()
UuidsBoundClassFilter.update_forward_refs()
UuidsBoundEmployeeFilter.update_forward_refs()
UuidsBoundEngagementFilter.update_forward_refs()
UuidsBoundFacetFilter.update_forward_refs()
UuidsBoundITSystemFilter.update_forward_refs()
UuidsBoundITUserFilter.update_forward_refs()
UuidsBoundLeaveFilter.update_forward_refs()
UuidsBoundOrganisationUnitFilter.update_forward_refs()
ValidityInput.update_forward_refs()

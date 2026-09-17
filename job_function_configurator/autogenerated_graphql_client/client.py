from uuid import UUID

from ._testing__create_class import TestingCreateClass, TestingCreateClassClassCreate
from ._testing__create_employee import (
    TestingCreateEmployee,
    TestingCreateEmployeeEmployeeCreate,
)
from ._testing__create_engagement import (
    TestingCreateEngagement,
    TestingCreateEngagementEngagementCreate,
)
from ._testing__create_facet import TestingCreateFacet, TestingCreateFacetFacetCreate
from ._testing__create_it_system import (
    TestingCreateItSystem,
    TestingCreateItSystemItsystemCreate,
)
from ._testing__create_it_user import (
    TestingCreateItUser,
    TestingCreateItUserItuserCreate,
)
from ._testing__create_org_unit import (
    TestingCreateOrgUnit,
    TestingCreateOrgUnitOrgUnitCreate,
)
from ._testing__get_engagement_timeline import (
    TestingGetEngagementTimeline,
    TestingGetEngagementTimelineEngagements,
)
from ._testing__update_engagement import (
    TestingUpdateEngagement,
    TestingUpdateEngagementEngagementUpdate,
)
from .async_base_client import AsyncBaseClient
from .get_engagement import GetEngagement, GetEngagementEngagements
from .input_types import (
    ClassCreateInput,
    EmployeeCreateInput,
    EngagementCreateInput,
    EngagementUpdateInput,
    FacetCreateInput,
    ITSystemCreateInput,
    ITUserCreateInput,
    OrganisationUnitCreateInput,
)
from .update_engagement import UpdateEngagement, UpdateEngagementEngagementUpdate


def gql(q: str) -> str:
    return q


class GraphQLClient(AsyncBaseClient):

    async def get_engagement(
        self, engagement_uuid: UUID, itsystem_user_key: str
    ) -> GetEngagementEngagements:
        query = gql("""
            query GetEngagement($engagement_uuid: UUID!, $itsystem_user_key: String!) {
              engagements(filter: {uuids: [$engagement_uuid]}) {
                objects {
                  current {
                    validity {
                      from
                      to
                    }
                    user_key
                    extension_1
                    extension_2
                    extension_3
                    extension_4
                    extension_5
                    extension_6
                    extension_7
                    extension_8
                    extension_9
                    extension_10
                    is_primary
                    primary {
                      uuid
                    }
                    job_function {
                      uuid
                      name
                      user_key
                    }
                    engagement_type {
                      uuid
                    }
                    org_unit {
                      uuid
                    }
                    person {
                      uuid
                      itusers(filter: {itsystem: {user_keys: [$itsystem_user_key]}}) {
                        user_key
                      }
                    }
                  }
                }
              }
            }
            """)
        variables: dict[str, object] = {
            "engagement_uuid": engagement_uuid,
            "itsystem_user_key": itsystem_user_key,
        }
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return GetEngagement.parse_obj(data).engagements

    async def update_engagement(
        self, input: EngagementUpdateInput
    ) -> UpdateEngagementEngagementUpdate:
        query = gql("""
            mutation UpdateEngagement($input: EngagementUpdateInput!) {
              engagement_update(input: $input) {
                uuid
              }
            }
            """)
        variables: dict[str, object] = {"input": input}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return UpdateEngagement.parse_obj(data).engagement_update

    async def _testing__create_facet(
        self, input: FacetCreateInput
    ) -> TestingCreateFacetFacetCreate:
        query = gql("""
            mutation _Testing_CreateFacet($input: FacetCreateInput!) {
              facet_create(input: $input) {
                uuid
              }
            }
            """)
        variables: dict[str, object] = {"input": input}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return TestingCreateFacet.parse_obj(data).facet_create

    async def _testing__create_class(
        self, input: ClassCreateInput
    ) -> TestingCreateClassClassCreate:
        query = gql("""
            mutation _Testing_CreateClass($input: ClassCreateInput!) {
              class_create(input: $input) {
                uuid
              }
            }
            """)
        variables: dict[str, object] = {"input": input}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return TestingCreateClass.parse_obj(data).class_create

    async def _testing__create_employee(
        self, input: EmployeeCreateInput
    ) -> TestingCreateEmployeeEmployeeCreate:
        query = gql("""
            mutation _Testing_CreateEmployee($input: EmployeeCreateInput!) {
              employee_create(input: $input) {
                uuid
              }
            }
            """)
        variables: dict[str, object] = {"input": input}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return TestingCreateEmployee.parse_obj(data).employee_create

    async def _testing__create_org_unit(
        self, input: OrganisationUnitCreateInput
    ) -> TestingCreateOrgUnitOrgUnitCreate:
        query = gql("""
            mutation _Testing_CreateOrgUnit($input: OrganisationUnitCreateInput!) {
              org_unit_create(input: $input) {
                uuid
              }
            }
            """)
        variables: dict[str, object] = {"input": input}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return TestingCreateOrgUnit.parse_obj(data).org_unit_create

    async def _testing__create_engagement(
        self, input: EngagementCreateInput
    ) -> TestingCreateEngagementEngagementCreate:
        query = gql("""
            mutation _Testing_CreateEngagement($input: EngagementCreateInput!) {
              engagement_create(input: $input) {
                uuid
              }
            }
            """)
        variables: dict[str, object] = {"input": input}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return TestingCreateEngagement.parse_obj(data).engagement_create

    async def _testing__create_it_system(
        self, input: ITSystemCreateInput
    ) -> TestingCreateItSystemItsystemCreate:
        query = gql("""
            mutation _Testing_CreateItSystem($input: ITSystemCreateInput!) {
              itsystem_create(input: $input) {
                uuid
              }
            }
            """)
        variables: dict[str, object] = {"input": input}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return TestingCreateItSystem.parse_obj(data).itsystem_create

    async def _testing__create_it_user(
        self, input: ITUserCreateInput
    ) -> TestingCreateItUserItuserCreate:
        query = gql("""
            mutation _Testing_CreateItUser($input: ITUserCreateInput!) {
              ituser_create(input: $input) {
                uuid
              }
            }
            """)
        variables: dict[str, object] = {"input": input}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return TestingCreateItUser.parse_obj(data).ituser_create

    async def _testing__update_engagement(
        self, input: EngagementUpdateInput
    ) -> TestingUpdateEngagementEngagementUpdate:
        query = gql("""
            mutation _Testing_UpdateEngagement($input: EngagementUpdateInput!) {
              engagement_update(input: $input) {
                uuid
              }
            }
            """)
        variables: dict[str, object] = {"input": input}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return TestingUpdateEngagement.parse_obj(data).engagement_update

    async def _testing__get_engagement_timeline(
        self, engagement_uuid: UUID
    ) -> TestingGetEngagementTimelineEngagements:
        query = gql("""
            query _Testing_GetEngagementTimeline($engagement_uuid: UUID!) {
              engagements(filter: {uuids: [$engagement_uuid], from_date: null, to_date: null}) {
                objects {
                  objects {
                    uuid
                    user_key
                    validity {
                      from
                      to
                    }
                    extension_1
                    extension_2
                    extension_3
                    extension_4
                    extension_5
                    extension_6
                    extension_7
                    extension_8
                    extension_9
                    extension_10
                    fraction
                    is_primary
                    primary {
                      uuid
                    }
                    job_function {
                      uuid
                    }
                    engagement_type {
                      uuid
                    }
                    person {
                      uuid
                    }
                    org_unit {
                      uuid
                    }
                  }
                }
              }
            }
            """)
        variables: dict[str, object] = {"engagement_uuid": engagement_uuid}
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return TestingGetEngagementTimeline.parse_obj(data).engagements

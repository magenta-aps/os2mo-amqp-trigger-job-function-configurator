# Generated by ariadne-codegen on 2023-11-02 16:16
# Source: queries.graphql

from datetime import datetime
from typing import Optional, Union
from uuid import UUID

from .async_base_client import AsyncBaseClient
from .base_model import UNSET, UnsetType
from .get_engagement import GetEngagement, GetEngagementEngagements
from .update_extension_field import (
    UpdateExtensionField,
    UpdateExtensionFieldEngagementUpdate,
)


def gql(q: str) -> str:
    return q


class GraphQLClient(AsyncBaseClient):
    async def get_engagement(
        self, engagement_uuid: UUID, itsystem_user_key: str
    ) -> GetEngagementEngagements:
        query = gql(
            """
            query GetEngagement($engagement_uuid: UUID!, $itsystem_user_key: String!) {
              engagements(filter: {uuids: [$engagement_uuid]}) {
                objects {
                  current {
                    validity {
                      from
                      to
                    }
                    extension_2
                    extension_3
                    is_primary
                    job_function {
                      name
                      user_key
                    }
                    person {
                      itusers(filter: {itsystem: {user_keys: [$itsystem_user_key]}}) {
                        user_key
                      }
                    }
                  }
                }
              }
            }
            """
        )
        variables: dict[str, object] = {
            "engagement_uuid": engagement_uuid,
            "itsystem_user_key": itsystem_user_key,
        }
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return GetEngagement.parse_obj(data).engagements

    async def update_extension_field(
        self,
        uuid: UUID,
        from_date: datetime,
        to_date: Union[Optional[datetime], UnsetType] = UNSET,
        extension_3: Union[Optional[str], UnsetType] = UNSET,
    ) -> UpdateExtensionFieldEngagementUpdate:
        query = gql(
            """
            mutation UpdateExtensionField($uuid: UUID!, $from_date: DateTime!, $to_date: DateTime, $extension_3: String) {
              engagement_update(
                input: {uuid: $uuid, validity: {from: $from_date, to: $to_date}, extension_3: $extension_3}
              ) {
                uuid
              }
            }
            """
        )
        variables: dict[str, object] = {
            "uuid": uuid,
            "from_date": from_date,
            "to_date": to_date,
            "extension_3": extension_3,
        }
        response = await self.execute(query=query, variables=variables)
        data = self.get_data(response)
        return UpdateExtensionField.parse_obj(data).engagement_update

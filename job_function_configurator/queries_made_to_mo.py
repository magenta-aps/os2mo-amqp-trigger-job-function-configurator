# SPDX-FileCopyrightText: 2022 Magenta ApS <https://magenta.dk>
# SPDX-License-Identifier: MPL-2.0
from uuid import UUID

import structlog
from gql import gql
from pydantic import parse_obj_as
from raclients.graph.client import PersistentGraphQLClient

from job_function_configurator.models.get_job_functions import GetJobFunctions

logger = structlog.get_logger()


async def get_engagement_object(
    gql_client: PersistentGraphQLClient, engagement_uuid: UUID, email_user_keys: list
) -> GetJobFunctions:
    """
    Get the engagement and related fields.

    Args:
        gql_client: The GraphQL client to perform the query.
        engagement_uuid: UUID of the engagement being edited or created.
        email_user_keys: User keys on the address types we want to find.

    Returns:
        Engagement object consisting of extension fields, job functions and
        all relevant information thereof.
    """
    query = gql(
        """
        query GetEngagement($engagement_uuids: [UUID!], $email_user_keys: [String!]) {
          engagements(uuids: $engagement_uuids) {
            objects {
              current {
                extension_2
                extension_3
                is_primary
                job_function {
                  name
                  user_key
                  uuid
                }
                primary {
                  name
                  user_key
                  name
                  uuid
                }
                employee {
                  uuid
                  addresses(address_type_user_keys: $email_user_keys) {
                    name
                    user_key
                    address_type {
                      scope
                      user_key
                      name
                    }
                  }
                }
              }
              uuid
            }
          }
        }
        """
    )
    response = await gql_client.execute(
        query,
        variable_values={
            "engagement_uuids": str(engagement_uuid),
            "email_user_keys": email_user_keys,
        },
    )
    return parse_obj_as(GetJobFunctions, {"data": response})

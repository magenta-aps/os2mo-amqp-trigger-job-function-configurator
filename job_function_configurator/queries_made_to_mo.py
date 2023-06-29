# SPDX-FileCopyrightText: 2022 Magenta ApS <https://magenta.dk>
# SPDX-License-Identifier: MPL-2.0
from uuid import UUID

import structlog
from gql import gql
from pydantic import parse_obj_as
from raclients.graph.client import PersistentGraphQLClient

from .models.get_job_functions import GetJobFunctions

logger = structlog.get_logger()


async def get_engagement_object(
    gql_client: PersistentGraphQLClient, engagement_uuid: UUID
) -> GetJobFunctions:
    """
    Get the engagement and related fields.

    Args:
        gql_client: The GraphQL client to perform the query.
        engagement_uuid: UUID of the engagement being edited or created.

    Returns:
        Engagement object consisting of extension fields, job functions and
        all relevant information thereof.
    """
    query = gql(
        """
        query GetEngagement($engagement_uuids: [UUID!]) {
          engagements(uuids: $engagement_uuids) {
            objects {
              current {
                extension_2
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
                  addresses {
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
        query, variable_values={"engagement_uuids": str(engagement_uuid)}
    )
    return parse_obj_as(GetJobFunctions, {"data": response})

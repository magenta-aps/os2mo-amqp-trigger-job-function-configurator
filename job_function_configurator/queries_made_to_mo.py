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
        engagement_uuid: UUID of the engagement being edited or created.
        gql_client: The GraphQL client to perform the query.

    Returns:
        Engagement object consisting of extension fields, job functions and
        all relevant information thereof.
    """
    query = gql(
        """
        query MyQuery($uuid_list: [UUID!]) {
          engagements(uuids: $uuid_list) {
            objects {
              current {
                extension_1
                extension_10
                extension_2
                extension_3
                extension_4
                extension_5
                extension_6
                extension_7
                extension_8
                extension_9
                fraction
                job_function {
                  full_name
                  user_key
                  uuid
                }
              }
              uuid
            }
          }
        }
        """
    )
    response = await gql_client.execute(
        query, variable_values={"uuid_list": str(engagement_uuid)}
    )
    print("!!!!!!!!!!!", response)
    return parse_obj_as(GetJobFunctions, {"data": response})

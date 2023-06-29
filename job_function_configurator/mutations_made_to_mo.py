import datetime
from uuid import UUID

import structlog
from gql import gql
from raclients.graph.client import PersistentGraphQLClient


logger = structlog.get_logger()


async def update_extension_field_for_engagement(
    gql_client: PersistentGraphQLClient,
    engagement_uuid: UUID,
    extension_: str,
    new_job_title: str,
):
    """
    Edit the engagements' job function to use the title found in the
    engagements' extension field to another extension field.

    Args:
        gql_client: The GraphQL client to perform the query.
        engagement_uuid: UUID of the engagement to perform an edit on.
        extension_: Name extension field to update.
        new_job_title: The title to edit the job function with.

    Returns:
        An engagements job function title successfully updated.
    """
    mutation = gql(
        """
        mutation UpdateJobFunction($input: EngagementUpdateInput!) {
          engagement_update(input: $input) {
            uuid
          }
        }
        """
    )
    update_engagement_variables = {
        "input": {
            "uuid": str(engagement_uuid),  # UUID of the engagement to be updated.
            extension_: new_job_title,
            "validity": {"from": datetime.date.today().isoformat()},  # From today.
        }
    }

    await gql_client.execute(mutation, variable_values=update_engagement_variables)

from uuid import UUID

import structlog
from raclients.graph.client import PersistentGraphQLClient

from .queries_made_to_mo import get_engagement_object

logger = structlog.get_logger(__name__)


async def process_engagement_events(
    gql_client: PersistentGraphQLClient, engagement_uuid: UUID
) -> None:
    """
    A function for handling the various events made involving an engagement.
    This involves checking whether the engagement has a job function containing
    sensitive information, and to potentially overwrite this information.
    Once the engagement satisfies our quota, we either create it, or update it
    accordingly.

    Args:
        gql_client: A GraphQL client to perform the various queries

        engagement_uuid: UUID of the engagement

    Returns:
        A successful creation, or update, of an engagement or None
    """
    logger.debug(
        "Starting event of engagement create/update, with uuid of:",
        engagement_uuid=engagement_uuid,
    )
    try:
        foo = await get_engagement_object(gql_client, engagement_uuid)
        print(foo)

    except ValueError:
        return None

    logger.info("An update was successfully made")

# SPDX-FileCopyrightText: 2022 Magenta ApS <https://magenta.dk>
# SPDX-License-Identifier: MPL-2.0
from uuid import UUID

import structlog
from more_itertools import one
from raclients.graph.client import PersistentGraphQLClient

from .config import get_settings
from .helper_functions import check_for_avoided_emails
from .helper_functions import check_for_blacklisted_engagement_job_function_user_keys
from .helper_functions import check_for_primary_engagement
from .helper_functions import get_email_address_type_uuid_from_gql
from .mutations_made_to_mo import update_extension_field_for_engagement
from .queries_made_to_mo import get_engagement_object

logger = structlog.get_logger(__name__)
settings = get_settings()


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
    print(")~&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& STARTING JOBSSSSS")
    logger.info(
        "Starting event of engagement create/update, with uuid of:",
        engagement_uuid=engagement_uuid,
    )
    try:  # Make a Graphql call to pull the engagement.
        engagement_object_parsed_as_model = await get_engagement_object(
            gql_client, engagement_uuid
        )

    except ValueError as exc:
        print(exc.args[0])
        logger.error("Engagement object not found, something went wrong:", exc.args[0])
        return None

    # Mypy insists on making sure "data" is not empty.
    assert engagement_object_parsed_as_model.data is not None

    engagement_fields = one(
        engagement_object_parsed_as_model.data.engagements.objects
    ).current

    if not engagement_fields:
        print("The engagement must have just been ended. Do nothing.")
        return None

    try:  # Check whether job functions codes are in blacklist.
        if check_for_blacklisted_engagement_job_function_user_keys(
            engagement_fields.job_function.user_key
        ):
            # Codes are blacklisted. Write empty values.
            await update_extension_field_for_engagement(
                gql_client,
                engagement_uuid,
                settings.name_of_extension_field_to_update,
                settings.emtpy_content_for_extension_field_update,
            )

            return None

    except ValueError as exc:
        print(exc.args[0])
        logger.error("A mutation was not made, error occurred:", exc.args[0])
        return None

    emails = None
    engagement_type = None

    try:
        # Get addresses to check for email values.
        addresses = one(engagement_fields.employee).addresses

        emails = get_email_address_type_uuid_from_gql(addresses)
        # Get whether the engagement is primary or not.
        engagement_type = engagement_fields.is_primary

    except ValueError as exc:
        print(exc.args[0])
        logger.error("Missing objects in engagement:", exc.args[0])

    try:
        # If the engagement is primary and the email is not of avoided type,
        # then go ahead and use the contents of extension_2.
        assert emails and engagement_type is not None  # For mypy
        if check_for_avoided_emails(emails) and check_for_primary_engagement(
            engagement_type
        ):
            new_job_function = engagement_fields.extension_2
            # Make a mutation, write the contents of extension_2, to extension_x.
            await update_extension_field_for_engagement(
                gql_client,
                engagement_uuid,
                settings.name_of_extension_field_to_update,
                new_job_function,
            )

        else:
            try:
                job_function_name_from_sd = engagement_fields.job_function.name
                await update_extension_field_for_engagement(
                    gql_client,
                    engagement_uuid,
                    settings.name_of_extension_field_to_update,
                    job_function_name_from_sd,
                )

            except ValueError as exc:
                print(exc.args[0])
                logger.error("Job function name apparently not found:", exc.args[0])
                return None

    except ValueError as exc:
        print(exc.args[0])

        logger.error("A mutation was not made, error occurred:", exc.args[0])

    logger.info("An update was successfully made")

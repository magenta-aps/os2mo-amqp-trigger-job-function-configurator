# SPDX-FileCopyrightText: 2022 Magenta ApS <https://magenta.dk>
# SPDX-License-Identifier: MPL-2.0
from uuid import UUID

import structlog
from more_itertools import one
from raclients.graph.client import PersistentGraphQLClient

from job_function_configurator.config import get_settings
from job_function_configurator.helper_functions import (
    check_for_blacklisted_engagement_job_function_user_keys,
)
from job_function_configurator.helper_functions import (
    check_for_email_not_in_avoided_list,
)
from job_function_configurator.mutations_made_to_mo import (
    update_extension_field_for_engagement,
)
from job_function_configurator.queries_made_to_mo import get_engagement_object

logger = structlog.get_logger(__name__)
settings = get_settings()


async def process_engagement_events(
    gql_client: PersistentGraphQLClient, engagement_uuid: UUID
) -> None:
    """
    A function for handling the various events made involving an engagement.
    This involves checking whether the engagement has a job function containing
    sensitive information, and to potentially overwrite this information.

    Args:
        gql_client: A GraphQL client to perform the various queries

        engagement_uuid: UUID of the engagement

    Returns:
        A successful creation, or update, of an engagement or None
    """
    print("LISTENING ON AN EVENT")
    logger.info(
        "Listening on a create/update/delete engagement event, with uuid of:",
        engagement_uuid=engagement_uuid,
    )
    try:  # Make a Graphql call to pull the engagement.
        engagement_object_parsed_as_model = await get_engagement_object(
            gql_client, engagement_uuid, settings.email_user_key_for_address_type
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
        logger.debug(f"No current engagements found for {engagement_uuid=}.")
        return None

    try:  # Check whether job functions codes are in blacklist.
        if check_for_blacklisted_engagement_job_function_user_keys(
            engagement_fields.job_function.user_key, settings.blacklisted_keys
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

    email = None
    primary_status = None

    try:
        # Get addresses to check for email values.
        if (
            one(one(engagement_fields.employee).addresses).address_type.scope
            == settings.address_type_scope
        ):
            email = one(one(engagement_fields.employee).addresses).name

            # Get whether the engagement is primary or not.
            primary_status = engagement_fields.is_primary

    except ValueError as exc:
        print(exc.args[0])
        logger.error("Missing objects in engagement:", exc.args[0])

    try:
        # If the engagement is primary and the email is not of avoided type,
        # then go ahead and use the contents of extension_2.
        # assert emails and primary_status is not None  # For mypy
        if email is not None:
            if (
                check_for_email_not_in_avoided_list(email, settings.avoided_emails)
                and primary_status
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
    print("FINISHED PROCESSING THE EVENT")
    logger.info("An update was successfully made")

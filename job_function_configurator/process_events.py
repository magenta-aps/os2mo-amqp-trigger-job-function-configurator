# SPDX-FileCopyrightText: 2023 Magenta ApS <https://magenta.dk>
# SPDX-License-Identifier: MPL-2.0
from uuid import UUID

import structlog
from more_itertools import one

from autogenerated_graphql_client import GraphQLClient
from job_function_configurator.config import get_settings
from job_function_configurator.helper_functions import (
    check_for_blacklisted_engagement_job_function_user_keys,
)


logger = structlog.get_logger(__name__)
settings = get_settings()


async def process_engagement_events(
    mo: GraphQLClient,
    engagement_uuid: UUID,
) -> None:
    """
    A function for handling the various events made involving an engagement.
    This involves checking whether the engagement has a job function containing
    sensitive information, and to potentially overwrite this information.

    Args:
        mo: A MO graphql client used to perform queries and mutations to MO.
        engagement_uuid: UUID of the engagement

    Returns:
        A successful creation, or update, of an engagement or None
    """
    print("LISTENING ON AN EVENT")
    logger.info(
        "Listening on a create/update/delete engagement event, with uuid of:",
        engagement_uuid=engagement_uuid,
    )
    try:
        engagement_object_parsed_as_model = await mo.get_engagement(
            engagement_uuid, settings.email_user_key_for_address_type
        )

    except ValueError as exc:
        print(exc.args[0])
        logger.error("Engagement object not found, something went wrong:", exc.args[0])
        return

    engagement_objects = one(engagement_object_parsed_as_model.objects).current

    if not engagement_objects:
        logger.debug(f"No current engagements found for: {engagement_uuid}.")
        return

    # Use the engagements current "from" date to avoid multiple entries in database.
    update_from_date = engagement_objects.validity.from_

    try:  # Check whether job functions codes are in blacklist.
        job_function_user_key = engagement_objects.job_function.user_key
        if check_for_blacklisted_engagement_job_function_user_keys(
            job_function_user_key, settings.blacklisted_keys
        ):
            # Job function code is blacklisted. Write empty values.
            await mo.update_extension_field(
                engagement_uuid,
                update_from_date,
                settings.emtpy_content_for_extension_field_update,
            )
            print("FINISHED PROCESSING THE EVENT - WROTE EMPTY VALUES")
            logger.info(
                "An update with with empty values was successfully made to the new extension field."
            )
            return

    except ValueError as exc:
        print(exc.args[0])
        logger.error("A mutation was not made, error occurred:", exc.args[0])
        return

    email = None
    email_user_key = None
    primary_status = None

    try:
        # Get addresses to check for email values.
        if (
            one(one(engagement_objects.employee).addresses).address_type.scope
            == settings.address_type_scope
        ):
            # Get the engagements primary status, retrieve the email and the emails user key.
            email = one(one(engagement_objects.employee).addresses).name
            email_user_key = one(one(engagement_objects.employee).addresses).user_key
            primary_status = engagement_objects.is_primary

    except ValueError as exc:
        print(exc.args[0])
        logger.error("Missing objects in engagement:", exc.args[0])

    # If the engagement is primary and the email is not of avoided type,
    # then go ahead and use the contents of extension_2.
    try:
        if email is not None:
            if (
                email_user_key not in settings.avoided_email_user_keys
                and primary_status
            ):
                new_job_function = engagement_objects.extension_2
                # Make a mutation, write the contents of extension_2, to extension_x.
                await mo.update_extension_field(
                    engagement_uuid, update_from_date, new_job_function
                )
                print("FINISHED PROCESSING THE EVENT - WROTE FROM EXISTING EXTENSION")
                logger.info(
                    "An update with the contents of extension_2 was successfully made to"
                    " the new extension field."
                )
                return
            else:
                # Make mutation, write what is the current job function name to the extension.
                job_function_name_from_sd = engagement_objects.job_function.name
                await mo.update_extension_field(
                    engagement_uuid, update_from_date, job_function_name_from_sd
                )
                print("FINISHED PROCESSING THE EVENT - WROTE FROM SD")
                logger.info(
                    "An update with the job function from SD was successfully made to"
                    " the new extension field."
                )
                return
    except ValueError as exc:
        print(exc.args[0])
        logger.error("An update was not made, error occurred:", exc.args[0])
        return

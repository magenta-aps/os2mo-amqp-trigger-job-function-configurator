# SPDX-FileCopyrightText: 2023 Magenta ApS <https://magenta.dk>
# SPDX-License-Identifier: MPL-2.0
from uuid import UUID

import structlog
from more_itertools import one

from job_function_configurator.autogenerated_graphql_client import GraphQLClient
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
    logger.info(
        "Listening on a create/update/delete engagement event, with uuid of:",
        engagement_uuid=engagement_uuid,
    )
    engagement_object_parsed_as_model = await mo.get_engagement(
        engagement_uuid, settings.email_user_key_for_address_type
    )

    if len(engagement_object_parsed_as_model.objects) == 0:
        # No objects were found in the GraphQL payload - might be a termination.
        logger.info("Engagement objects are missing")
        return

    engagement_objects = None
    try:
        engagement_objects = one(engagement_object_parsed_as_model.objects).current
    except ValueError:
        logger.debug(
            "No current engagement objects found",
        )

    if not engagement_objects:
        return

    # Use the engagements current "from" date to avoid multiple entries in database.
    update_from_date = engagement_objects.validity.from_
    update_to_date = engagement_objects.validity.to

    email = None
    email_user_key = None
    primary_status = None

    # Handle possibility of the person not having an email address.
    try:
        if one(engagement_objects.employee).addresses is None:
            logger.info(
                "Person does not have an email address",
            )
            job_function_name_from_sd = engagement_objects.job_function.name
            await mo.update_extension_field(
                engagement_uuid, update_from_date, update_to_date, job_function_name_from_sd
            )
            # We should have passed the check for blacklisted job function codes (user keys)
            # at this point.
            logger.info(
                "Made an update with the job function title from SD to"
                " the new extension field."
            )

    except ValueError:
        logger.error(
            "The person does not have a valid job function",
        )

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

    except ValueError:
        logger.error("Missing objects in employee")

    # If the engagement is primary and the email is not of avoided type,
    # then go ahead and use the contents of extension_2.

    if email is not None:
        if (  # If email is not blacklisted, and the engagement is the primary engagement
            # and there is content in the extension_2 field.
            email_user_key not in settings.avoided_email_user_keys
            and primary_status
            and engagement_objects.extension_2
        ):
            new_job_function = engagement_objects.extension_2
            # Make a mutation, write the contents of extension_2, to extension_x.
            await mo.update_extension_field(
                engagement_uuid, update_from_date, update_to_date, new_job_function
            )
            logger.info(
                "An update with the contents of extension_2 was successfully made to"
                " the new extension field."
            )
            return
        else:
            # Make mutation, write what is the current job function name to the extension.
            job_function_name_from_sd = engagement_objects.job_function.name
            await mo.update_extension_field(
                engagement_uuid, update_from_date, update_to_date, job_function_name_from_sd
            )
            logger.info(
                "An update with the job function from SD was successfully made to"
                " the new extension field."
            )
            return

    # Check whether job functions codes are in blacklist.
    job_function_user_key = engagement_objects.job_function.user_key
    if check_for_blacklisted_engagement_job_function_user_keys(
        job_function_user_key, settings.blacklisted_keys
    ):
        # Job function code is blacklisted. Write empty values.
        await mo.update_extension_field(
            engagement_uuid,
            update_from_date,
            update_to_date,
            settings.empty_content_for_extension_field_update,
        )

        logger.info(
            "An update with with empty values was successfully made to the new extension field."
        )
        return

    if email is None:
        # There is no email, and/or the extension_2 field is empty - write the
        # job functions name to the new extension.
        job_function_name_from_sd = engagement_objects.job_function.name
        await mo.update_extension_field(
            engagement_uuid, update_from_date, update_to_date, job_function_name_from_sd
        )
        logger.info(
            "An update with the job function from SD was successfully made to"
            " the new extension field."
        )

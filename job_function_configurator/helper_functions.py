# SPDX-FileCopyrightText: 2022 Magenta ApS <https://magenta.dk>
# SPDX-License-Identifier: MPL-2.0
from .config import get_settings

settings = get_settings()


def check_for_avoided_emails(emails: list) -> bool:
    """
    A helper function used to check for emails to
    avoid from the persons engagement object.
    Args:
        emails: the persons email, if any.

    Returns:
        False - if the person has an email not allowed
        True - if the persons email is not blacklisted

    Example:
        ['@avoided_email', '@may_not_use', '@bad_email']
    """
    # TODO Get these avoided words from settings rather
    # avoided_emails = ["@viborgskoler", "@scviborg.dk"]
    avoided_emails = settings.avoided_emails
    for email in emails:
        if email not in avoided_emails:
            return False

    return True


def check_for_primary_engagement(engagement: bool) -> bool:
    """
    A helper function used to check for the persons
    primary engagement.
    Args:
        engagement: the persons' engagement.

    Returns:
        False - if this is not the primary engagement.
        True - if this is the persons' primary engagement.

    Example:
        'is_primary: True'
    """
    if not engagement:
        return False

    return True


def get_email_address_type_uuid_from_gql(address_list: list) -> list:
    """
    Filtering through all address types to only extract emails.

    Args:
        address_list: - A payload with all address types.

    Returns:
        A list of all possible emails.

    Example:
        ['onetwo@three.com']
    """
    extracted_emails = [
        address.name
        for address in address_list
        if address.address_type.scope == settings.address_type_scope
    ]

    return extracted_emails


def check_for_blacklisted_engagement_job_function_user_keys(job_function: str) -> bool:
    """
    A helper function used to check for banned user keys
    from the engagements' job functions user key.

    Args:
        job_function: The value to check for in the blacklist.

    Returns:
        False - if the user key is not blacklisted
        True - if the user key is in the blacklist
    """
    blacklisted_user_keys = settings.blacklisted_keys
    if job_function in blacklisted_user_keys:
        return True

    return False

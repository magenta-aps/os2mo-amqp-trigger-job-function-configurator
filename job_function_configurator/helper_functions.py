# SPDX-FileCopyrightText: 2023 Magenta ApS <https://magenta.dk>
# SPDX-License-Identifier: MPL-2.0
def filter_out_avoided_email_user_keys(
    email: str, avoided_email_user_keys: list
) -> bool:
    """
    A helper function used to check whether the persons
    email is allowed or is in the list to be avoided.
    Args:
        email: The persons email, if any.
        avoided_email_user_keys: List of banned email from customer settings.

    Returns:
        True - if the persons email is eligible, and is not blacklisted.
        False - if the persons email is not allowed, and exists in the list of avoided emails.

    Example:
        ['onetwothree@avoided_email', 'heyhow@may_not_use', 'notagentsmith@bad_email']
    """
    return email not in avoided_email_user_keys


def check_for_blacklisted_engagement_job_function_user_keys(
    job_function: str, blacklisted_user_keys: list
) -> bool:
    """
    A helper function used to check for banned user keys
    from the engagements' job functions user key.

    Args:
        job_function: The value to check for in the blacklist.
        blacklisted_user_keys: A list of blacklisted user keys.

    Returns:
        False - if the user key is not blacklisted.
        True - if the user key is in the blacklist.
    """
    return job_function in blacklisted_user_keys

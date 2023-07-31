# SPDX-FileCopyrightText: 2023 Magenta ApS <https://magenta.dk>
# SPDX-License-Identifier: MPL-2.0
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

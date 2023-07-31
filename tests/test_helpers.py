# SPDX-FileCopyrightText: 2023 Magenta ApS <https://magenta.dk>
# SPDX-License-Identifier: MPL-2.0
import pytest

from job_function_configurator.helper_functions import (
    check_for_blacklisted_engagement_job_function_user_keys,
)
from job_function_configurator.helper_functions import (
    filter_out_avoided_email_user_keys,
)


@pytest.mark.parametrize(
    "test_emails, expected_result",
    [
        ("sprogcenter-email", False),
        ("email", True),
        (
            "EmailEmployee",
            True,
        ),
        (
            "skole-mail",
            False,
        ),
    ],
)
def test_check_for_avoided_emails(test_emails, expected_result):
    avoided_emails = ["sprogcenter-email", "skole-mail"]

    result = filter_out_avoided_email_user_keys(test_emails, avoided_emails)
    print("!!!!!!!", result)
    assert result == expected_result


@pytest.mark.parametrize(
    "test_job_function_user_keys, expected_result",
    [
        ("1550", True),
        ("Udvikler", False),
        ("1555", True),
        ("1558", True),
        ("1600", False),
        ("Skolepsykolog", False),
        ("Lønkonsulent", False),
        ("9000", False),
        ("3000", True),
        ("1551", True),
        ("extension_2", False),
    ],
)
def test_black_listed_engagement_job_function_user_keys(
    test_job_function_user_keys, expected_result
):
    blacklist = [
        "1550",
        "1551",
        "1552",
        "1553",
        "1554",
        "1555",
        "1556",
        "1557",
        "1558",
        "1559",
        "3000",
    ]
    result = check_for_blacklisted_engagement_job_function_user_keys(
        test_job_function_user_keys, blacklist
    )
    assert result == expected_result

# SPDX-FileCopyrightText: Magenta ApS
#
# SPDX-License-Identifier: MPL-2.0
import pytest

from job_function_configurator.helper_functions import (
    check_for_blacklisted_engagement_job_function_user_keys,
)
from job_function_configurator.helper_functions import (
    check_for_email_not_in_avoided_list,
)
from job_function_configurator.helper_functions import get_email_from_all_address_types


@pytest.mark.parametrize(
    "test_emails, expected_result",
    [
        (["forbudt@viborgskoler.dk", "entotre@hep.hey"], False),
        (["somethingcool@gmail.com", "alsocool@hotmail.com", "no@one.com"], True),
        (
            [
                "morpheus@matrix.com",
                "trinity@matrix.com",
                "neo@matrix.dk",
                "smith@matrix.com",
            ],
            True,
        ),
        (
            [
                "goats@horses.com",
                "yubyyl@yahoo.com",
                "neo@scviborg.dk",
                "not@illegal.com",
            ],
            False,
        ),
    ],
)
def test_check_for_avoided_emails(test_emails, expected_result):
    avoided_emails = ["viborgskoler.dk", "scviborg.dk"]

    result = check_for_email_not_in_avoided_list(test_emails, avoided_emails)
    assert result == expected_result


@pytest.mark.parametrize(
    "test_address_types, expected_result",
    [
        (
            [
                {
                    "user_key": "0a3f50aa-e81b-32b8-e044-0003ba298018",
                    "address_type": {
                        "user_key": "AdressePostEmployee",
                        "name": "Postadresse",
                        "scope": "DAR",
                    },
                    "name": "Damhaven 7, 2670 Greve",
                },
                {
                    "user_key": "allowed@stuff.com",
                    "address_type": {
                        "user_key": "EmailEmployee",
                        "name": "Email",
                        "scope": "EMAIL",
                    },
                    "name": "allowed@stuff.com",
                },
                {
                    "user_key": "76824598",
                    "address_type": {
                        "user_key": "PhoneEmployee",
                        "name": "Telefon",
                        "scope": "PHONE",
                    },
                    "name": "76824598",
                },
            ],
            ["allowed@stuff.com"],
        ),
        (
            [
                {
                    "user_key": "forbudt@viborgskoler.dk",
                    "address_type": {
                        "user_key": "EmailEmployee",
                        "name": "Email",
                        "scope": "EMAIL",
                    },
                    "name": "forbudt@viborgskoler.dk",
                }
            ],
            ["forbudt@viborgskoler.dk"],
        ),
        (
            [
                {
                    "user_key": "bad@scviborg.dk",
                    "address_type": {
                        "user_key": "EmailEmployee",
                        "name": "Email",
                        "scope": "EMAIL",
                    },
                    "name": "bad@scviborg.dk",
                },
                {
                    "user_key": "niceemail@gmail.com",
                    "address_type": {
                        "user_key": "EmailEmployee",
                        "name": "Email",
                        "scope": "EMAIL",
                    },
                    "name": "niceemail@gmail.com",
                },
                {
                    "user_key": "notallowed@viborgskoler.dk",
                    "address_type": {
                        "user_key": "EmailEmployee",
                        "name": "Email",
                        "scope": "EMAIL",
                    },
                    "name": "notallowed@viborgskoler.dk",
                },
            ],
            ["bad@scviborg.dk", "niceemail@gmail.com", "notallowed@viborgskoler.dk"],
        ),
    ],
)
def test_retrieve_emails_from_address_type_payload(test_address_types, expected_result):
    emails = get_email_from_all_address_types(test_address_types, "EMAIL")
    assert emails == expected_result


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

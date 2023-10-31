# SPDX-FileCopyrightText: 2023 Magenta ApS <https://magenta.dk>
# SPDX-License-Identifier: MPL-2.0
from fastramqpi.config import Settings as FastRAMQPISettings
from pydantic import PositiveInt


class JobFunctionSettings(FastRAMQPISettings):
    """Settings for the engagement elevator AMQP trigger."""

    log_level: str = "INFO"

    mo_graphql_version: PositiveInt = 19

    # HELPERS
    email_user_key_for_address_type: list = []
    address_type_scope: str
    avoided_email_user_keys: list = []
    blacklisted_keys: list = []

    # MUTATORS
    empty_content_for_extension_field_update: str = " "

    class Config:
        """Settings are frozen."""

        frozen = True
        env_nested_delimiter = "__"
        env_file_encoding = "utf-8"


def get_settings(*args, **kwargs) -> JobFunctionSettings:
    return JobFunctionSettings(*args, **kwargs)

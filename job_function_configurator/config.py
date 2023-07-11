# SPDX-FileCopyrightText: 2022 Magenta ApS <https://magenta.dk>
# SPDX-License-Identifier: MPL-2.0
from fastramqpi.config import Settings as FastRAMQPISettings


class Settings(FastRAMQPISettings):
    """Settings for the engagement elevator AMQP trigger."""

    log_level: str = "INFO"

    # HELPERS
    # Do not use "@" in emails, as we're splitting on it in the helper function.
    email_user_key_for_address_type: list = []
    address_type_scope: str
    avoided_emails: list = []
    blacklisted_keys: list = []

    # MUTATORS
    emtpy_content_for_extension_field_update: str = " "
    name_of_extension_field_to_update: str

    class Config:
        """Settings are frozen."""

        frozen = True
        env_nested_delimiter = "__"
        env_file_encoding = "utf-8"


def get_settings(*args, **kwargs) -> Settings:
    return Settings(*args, **kwargs)

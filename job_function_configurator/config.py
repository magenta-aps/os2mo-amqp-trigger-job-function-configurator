# SPDX-FileCopyrightText: 2022 Magenta ApS <https://magenta.dk>
# SPDX-License-Identifier: MPL-2.0
from fastramqpi.config import Settings as FastRAMQPISettings


class Settings(FastRAMQPISettings):
    """Settings for the engagement elevator AMQP trigger."""

    log_level: str = "INFO"

    # HELPERS
    avoided_emails: list = ["@viborgskoler", "@scviborg.dk"]  # DOES THIS WORK???
    address_type_scope: str = "EMAIL"
    blacklisted_keys: list = [
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

    # MUTATORS
    emtpy_content_for_extension_field_update: str = " "
    name_of_extension_field_to_update: str = "extension_3"

    class Config:
        """Settings are frozen."""

        frozen = True
        env_nested_delimiter = "__"


def get_settings(*args, **kwargs) -> Settings:
    return Settings(*args, **kwargs)

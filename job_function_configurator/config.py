# SPDX-FileCopyrightText: 2023 Magenta ApS <https://magenta.dk>
# SPDX-License-Identifier: MPL-2.0
from fastramqpi.config import Settings as FastRAMQPISettings
from pydantic import BaseSettings


class JobFunctionSettings(BaseSettings):
    """Settings for the job function configurator."""

    # The settings FastRAMQPI needs, such as the OS2mo URL and the client
    # credentials. They are read from FASTRAMQPI__-prefixed environment
    # variables, i.e. FASTRAMQPI__MO_URL.
    fastramqpi: FastRAMQPISettings

    itsystem_user_key: str = "Active Directory"
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

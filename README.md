# SPDX-FileCopyrightText: 2023 Magenta ApS <https://magenta.dk>
# SPDX-License-Identifier: MPL-2.0

OS2mo-amqp-trigger-job-function-configurator
=====================================================================================
This is an OS2mo AMQP trigger receiver that allows for configuration of job functions

This integration has the sole responsibility of maintaining and writing the contents of the `extension_3` field in MO.

The integration listens on changes made to engagements in MO, which will trigger a chain of events. If the contents of
the `job_function` field are of sensitive nature, or if it contains any information the user wants to filter out, we
edit the field with any configured information, and send it back to MO to be displayed as the new `job_function`.

## Prerequisites
You will need a functioning MO instance running on your host machine.

## How do you run it
To run this integration firstly you will need to pull the project from the upstream git repository and running it as:
`docker compose up -d` to start the integration.

## Custom configurations
Currently, we may configure following settings:
- `email_user_key_for_address_type` - A list of address type user keys used to find address types for, i.e. "EmailEmployee".
- `address_type_scope` - Scope on address types to search for, i.e "EMAIL".
- `avoided_email_user_keys` - A list of email user keys used to exclude when writing to the new extension field.
- `blacklisted_keys` - A list of job function user keys to exclude when writing to the new extension field.
- `emtpy_content_for_extension_field_update` - Empty content to write to the new extension field.

## Tests
Tests can be run by the following command:
`poetry run pytest tests/`. This will run all tests in the `tests/` directory.

If needed, you may run the tests as more verbose by: `poetry run pytest tests/ --verbose`. This will output which tests
are run, and may prove to be more useful in case of failing tests.

# SPDX-FileCopyrightText: 2023 Magenta ApS <https://magenta.dk>
# SPDX-License-Identifier: MPL-2.0

OS2mo-amqp-trigger-job-function-configurator
=====================================================================================
This is an OS2mo AMQP trigger receiver that allows for configuration of job functions

This integration has the sole responsibility of validating the contents of the `job_function` field found in MO.

The integration listens on changes made to engagements in MO, which will trigger a chain of events. If the contents of
the `job_function` field are of sensitive nature, or if it contains any information the user wants to filter out, we
edit the field with any configured information, and send it back to MO to be displayed as the new `job_function`.

## Prerequisites
You will need a functioning MO instance running on your host machine.

## How do you run it
Running this integration is as simple as pulling down the project from the upstream git repository and running it as:
`docker compose up --build --detach` to start in detached mode.
Build the application without the `--detach` flag, if you want to view the containers output.

## Custom configurations
Currently, we may configure following settings:
- Address type user keys
- Address type scope
- Emails user keys to exclude
- Job function user keys to exclude
- Content to write to the new extension field

## Tests
Tests can be run by the following command:
`poetry run pytest tests/`. This will simply run all tests in the `tests/` directory.

If needed, you may run the tests as more verbose by: `poetry run pytest tests/ --verbose`. This will output which tests
are run, and may prove to be more useful in case of failing tests.

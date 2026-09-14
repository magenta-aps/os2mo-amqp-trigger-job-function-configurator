# SPDX-FileCopyrightText: 2023 Magenta ApS <https://magenta.dk>
# SPDX-License-Identifier: MPL-2.0

OS2mo-amqp-trigger-job-function-configurator
=====================================================================================
This is an OS2mo integration that allows for configuration of job functions

This integration has the sole responsibility of maintaining and writing the contents of the `extension_3` field in MO.

The integration listens on changes made to engagements in MO, which will trigger a chain of events. If the contents of
the `job_function` field are of sensitive nature, or if it contains any information the user wants to filter out, we
edit the field with any configured information, and send it back to MO to be displayed as the new `job_function`.

## Events
The integration uses the GraphQL event system in MO. On startup it declares an
event listener in MO, and MO then delivers engagement events as HTTP POSTs to
`/events/mo/engagement`.

## Prerequisites
You will need a functioning MO instance running on your host machine.

## How do you run it
To run this integration firstly you will need to pull the project from the upstream git repository and running it as:
`docker compose up -d` to start the integration.

## Custom configurations
The integration is configured through environment variables.

The connection to MO is configured through FastRAMQPI, whose settings are nested under `fastramqpi`:
- `FASTRAMQPI__MO_URL` - Base URL of the MO instance to integrate with.
- `FASTRAMQPI__CLIENT_ID` - Client ID to authenticate with.
- `FASTRAMQPI__CLIENT_SECRET` - Client secret to authenticate with.
- `FASTRAMQPI__AUTH_SERVER` - Base URL of the Keycloak to authenticate against.
- `FASTRAMQPI__LOG_LEVEL` - Log level to configure.

The integration's own settings are:
- `BLACKLISTED_KEYS` - A list of job function user keys to exclude when writing to the new extension field.
- `EMPTY_CONTENT_FOR_EXTENSION_FIELD_UPDATE` - Empty content to write to the new extension field.
- `ITSYSTEM_USER_KEY` - User key of the IT system to look for the employee's IT user in, i.e. "Active Directory".

## Tests
The unit tests are in `tests/`, and the integration tests are in `tests/integration/`. The integration tests are run
against a real MO instance, so you will need the MO stack (https://github.com/OS2mo/os2mo) running before you run them.

Tests are run in the integration's own container:
- `docker compose run --rm configurator pytest` runs all tests
- `docker compose run --rm configurator pytest -m 'not integration_test'` runs only the unit tests, which do not need
  MO to be running
- `docker compose run --rm configurator pytest tests/integration` runs only the integration tests

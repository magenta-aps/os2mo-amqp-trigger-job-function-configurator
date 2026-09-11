# SPDX-FileCopyrightText: 2023 Magenta ApS <https://magenta.dk>
# SPDX-License-Identifier: MPL-2.0
from uuid import UUID

import structlog
from fastapi import APIRouter
from fastramqpi.events import Event
from structlog.contextvars import bound_contextvars

from job_function_configurator import depends
from job_function_configurator.process_events import process_engagement_events

logger = structlog.get_logger(__name__)

events_router = APIRouter()


@events_router.post("/events/mo/engagement")
async def engagement_event(
    mo: depends.GraphQLClient, settings: depends.Settings, event: Event[UUID]
) -> None:
    """
    Handle changes made to engagements in MO.

    The event subject is the UUID of the changed engagement.

    Args:
        mo: A GraphQL client to perform the various queries
        settings: The integration settings
        event: The engagement event received from MO
    """
    logger.info("Received engagement event", engagement_event=event.dict())

    with bound_contextvars(engagement_uuid=event.subject):
        await process_engagement_events(mo, settings, event.subject)

# SPDX-FileCopyrightText: 2022 Magenta ApS <https://magenta.dk>
# SPDX-License-Identifier: MPL-2.0
import structlog
from fastapi import APIRouter
from fastapi import FastAPI
from fastramqpi.main import FastRAMQPI
from ramqp.depends import Context
from ramqp.depends import RateLimit
from ramqp.mo import MORouter
from ramqp.mo import PayloadUUID

from .config import get_settings
from .log import setup_logging
from .process_events import process_engagement_events

amqp_router = MORouter()
fastapi_router = APIRouter()

logger = structlog.get_logger(__name__)


@amqp_router.register("engagement")
async def listener(
    context: Context, engagement_uuid: PayloadUUID, _: RateLimit
) -> None:
    """
    This function listens on changes made to:
    ServiceType - engagements
    ObjectType - job function

    We receive a payload, of type PayloadUUID, with content of:
    engagement_uuid - UUID of the engagement.

    Args:
    gql_client: A GraphQL client to perform the various queries

    engagement_uuid: UUID of the engagement

    Returns:
        A successful creation, or update, of an engagement or None
    """
    gql_session = context["graphql_session"]
    print("$$$$$$$$$$$$$$$$", gql_session)
    print("%%%%%%%%%%%%%%%%%%%%%%", context)
    print("^^^^^^^^^^^^^^^^^^^^^^^^^", context["graphql_session"])
    print("@@@@@@@@@@@@@@@@@@@@@@", engagement_uuid)
    await process_engagement_events(gql_session, engagement_uuid)


def create_fastramqpi(**kwargs) -> FastRAMQPI:
    settings = get_settings()
    setup_logging(settings.log_level)

    fastramqpi = FastRAMQPI(
        application_name="os2mo-job-function-configurator", settings=settings
    )

    amqpsystem = fastramqpi.get_amqpsystem()
    amqpsystem.router.registry.update(amqp_router.registry)

    app = fastramqpi.get_app()
    app.include_router(fastapi_router)

    return fastramqpi


def create_app(**kwargs) -> FastAPI:
    fastramqpi = create_fastramqpi(**kwargs)
    return fastramqpi.get_app()

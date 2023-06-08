# SPDX-FileCopyrightText: 2022 Magenta ApS <https://magenta.dk>
# SPDX-License-Identifier: MPL-2.0
from typing import Any

import structlog
from fastapi import APIRouter
from fastapi import FastAPI
from fastramqpi.main import FastRAMQPI  # type: ignore
from ramqp.depends import Context
from ramqp.depends import RateLimit
from ramqp.mo import MORouter  # type: ignore
from ramqp.mo import PayloadType

from .config import get_settings
from .log import setup_logging

amqp_router = MORouter()
fastapi_router = APIRouter()

logger = structlog.get_logger(__name__)


@amqp_router.register("*.engagement.*")
@amqp_router.register("employee.engagements.create")
@amqp_router.register("employee.engagements.edit")
async def listener(context: Context, payload: PayloadType, _: RateLimit) -> None:
    """
    This function listens on changes made to:
    ServiceType - engagements
    ObjectType - job function
    RequestType - create/edit

    We receive a payload, of type Payload, with content of:
    Organisation Units uuid - payload.uuid
    Manager uuid - payload.object_uuid
    """

    gql_client = context["graphql_session"]
    print("!!!!!!!!!", context)

    print("@@@@@@@@@@@@@", payload)
    print("%%%%%% DONE!")


@fastapi_router.post("/dum/dum")
async def dummy() -> dict[str, str]:
    return {"everything": "42"}


def create_fastramqpi(**kwargs) -> FastRAMQPI:
    settings = get_settings()
    setup_logging(settings.log_level)

    fastramqpi = FastRAMQPI(
        application_name="os2mo-job-function-configurator", settings=settings.fastramqpi
    )

    amqpsystem = fastramqpi.get_amqpsystem()
    amqpsystem.router.registry.update(amqp_router.registry)

    app = fastramqpi.get_app()
    app.include_router(fastapi_router)

    return fastramqpi


def create_app(**kwargs) -> FastAPI:
    fastramqpi = create_fastramqpi(**kwargs)
    return fastramqpi.get_app()

import logging
from fastapi import Depends
from ....dependencies import permission
from ....app.base import AuthenticatedAPIRouter
from pyispyb.core.schemas import ssx as schema
from pyispyb.core.schemas import events as schema_events

import pyispyb.core.modules.ssx as crud
from ispyb import models


router = AuthenticatedAPIRouter(
    prefix="/webservices/ssx",
    tags=["Webservices - Serial crystallography"],
    dependencies=[Depends(permission("ssx_sync"))],
)

logger = logging.getLogger("ispyb")


@router.post(
    "/datacollection",
    response_model=schema_events.Event,
)
def create_datacollection(
    ssx_datacollection_create: schema.SSXDataCollectionCreate,
) -> models.SSXDataCollection:
    return crud.create_ssx_datacollection(ssx_datacollection_create)


@router.post(
    "/datacollectiongroup",
    response_model=int,
)
def create_datacollectiongroup(
    ssx_datacollectiongroup_create: schema.SSXDataCollectionGroupCreate,
) -> models.DataCollectionGroup:
    return crud.create_ssx_datacollectiongroup(ssx_datacollectiongroup_create)


@router.post(
    "/datacollection/{dataCollectionId:int}/processing",
    response_model=int,
)
def create_ssx_datacollection_processing(
    data: schema.SSXDataCollectionProcessingCreate, dataCollectionId: int
) -> int:
    return crud.create_ssx_datacollection_processing(dataCollectionId, data)

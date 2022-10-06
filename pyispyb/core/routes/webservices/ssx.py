import logging
from fastapi import Depends
from ....dependencies import permission
from ....app.base import AuthenticatedAPIRouter
from pyispyb.core.schemas import ssx as schema
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
    response_model=schema.SSXDataCollectionResponse,
)
def create_datacollection(
    ssx_datacollection_create: schema.SSXDataCollectionCreate,
) -> models.SSXDataCollection:
    return crud.create_ssx_datacollection(ssx_datacollection_create)


@router.post(
    "/datacollectiongroup",
    response_model=schema.DataCollectionGroupResponse,
)
def create_datacollectiongroup(
    ssx_datacollectiongroup_create: schema.SSXDataCollectionGroupCreate,
) -> models.DataCollectionGroup:
    return crud.create_ssx_datacollectiongroup(ssx_datacollectiongroup_create)


@router.post(
    "/datacollection/{dataCollectionId:int}/processing",
    response_model=schema.SSXDataCollectionProcessingResponse,
)
def create_ssx_datacollection_processing(
    ssx_hits_create: schema.SSXDataCollectionProcessingCreate, dataCollectionId: int
) -> models.SSXDataCollectionProcessing:
    return crud.create_ssx_datacollection_processing(dataCollectionId, ssx_hits_create)

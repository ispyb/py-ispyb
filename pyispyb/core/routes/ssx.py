from fastapi import HTTPException
from pydantic import conint
from pyispyb.app.base import AuthenticatedAPIRouter
from pyispyb.core import models
import pyispyb.core.modules.ssx as crud
from fastapi.responses import FileResponse
import os


from pyispyb.core.schemas import ssx as schema

router = AuthenticatedAPIRouter(prefix="/ssx", tags=["Serial crystallography"])


@router.get(
    "/datacollection",
    response_model=list[schema.SSXDataCollectionResponse],
    responses={404: {"description": "Entity not found"}},
)
def get_datacollections(sessionId: int) -> list[models.SSXDataCollection]:
    return crud.get_ssx_datacollections(sessionId)


@router.get(
    "/datacollection/{ssxDataCollectionId:int}",
    response_model=schema.SSXDataCollectionResponse,
    responses={404: {"description": "Entity not found"}},
)
def get_datacollection(ssxDataCollectionId: int) -> models.SSXDataCollection:
    return crud.get_ssx_datacollection(ssxDataCollectionId)


@router.get(
    "/datacollection/{ssxDataCollectionId:int}/sample",
    response_model=schema.SSXSpecimenResponse,
    responses={404: {"description": "Entity not found"}},
)
def get_datacollection_sample(ssxDataCollectionId: int) -> models.SSXDataCollection:
    return crud.get_ssx_datacollection_sample(ssxDataCollectionId)


@router.post(
    "/datacollection",
    response_model=schema.SSXDataCollectionResponse,
    responses={404: {"description": "Entity not found"}},
)
def create_datacollection(
    ssx_data_collection_create: schema.SSXDataCollectionCreate,
) -> models.SSXDataCollection:
    return crud.create_ssx_datacollection(ssx_data_collection_create)


@router.get(
    "/datacollection/{ssxDataCollectionId:int}/sample/thumbnail/{thumbnailNumber:int}",
    response_class=FileResponse,
    responses={404: {"description": "Entity not found"}},
)
def get_datacollection_sample_thumbnail(
    ssxDataCollectionId: int, thumbnailNumber: conint(ge=1, le=3)
) -> str:
    dc = crud.get_ssx_datacollection(ssxDataCollectionId)
    if dc is None:
        raise HTTPException(status_code=404, detail="Data collection not found")
    res = None
    if thumbnailNumber == 1:
        res = dc.DataCollection.xtalSnapshotFullPath1
    if thumbnailNumber == 2:
        res = dc.DataCollection.xtalSnapshotFullPath2
    if thumbnailNumber == 3:
        res = dc.DataCollection.xtalSnapshotFullPath3
    if res is not None and os.path.isfile(res):
        return res
    raise HTTPException(status_code=404, detail="Thumbnail not found")

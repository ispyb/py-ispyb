from pyispyb.app.base import AuthenticatedAPIRouter
from pyispyb.core import models
import pyispyb.core.modules.ssx as crud


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
    "/datacollection/{dataCollectionId:int}",
    response_model=schema.SSXDataCollectionResponse,
    responses={404: {"description": "Entity not found"}},
)
def get_datacollection(dataCollectionId: int) -> models.SSXDataCollection:
    return crud.get_ssx_datacollection(dataCollectionId)


@router.get(
    "/datacollection/{dataCollectionId:int}/sample",
    response_model=schema.SSXSampleResponse,
    responses={404: {"description": "Entity not found"}},
)
def get_datacollection_sample(dataCollectionId: int) -> models.BLSample:
    return crud.get_ssx_datacollection_sample(dataCollectionId)

    
@router.get(
    "/datacollection/{dataCollectionId:int}/sequences",
    response_model=list[schema.SSXSequenceResponse],
    responses={404: {"description": "Entity not found"}},
)
def get_datacollection_sequences(dataCollectionId: int) -> list[models.Sequence]:
    return crud.get_ssx_datacollection_sequences(dataCollectionId)

@router.post(
    "/datacollection",
    response_model=schema.SSXDataCollectionResponse,
    responses={404: {"description": "Entity not found"}},
)
def create_datacollection(
    ssx_data_collection_create: schema.SSXDataCollectionCreate,
) -> models.SSXDataCollection:
    return crud.create_ssx_datacollection(ssx_data_collection_create)

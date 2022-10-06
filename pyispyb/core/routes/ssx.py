from pyispyb.app.base import AuthenticatedAPIRouter
from ispyb import models
import pyispyb.core.modules.ssx as crud


from pyispyb.core.schemas import ssx as schema

router = AuthenticatedAPIRouter(prefix="/ssx", tags=["Serial crystallography"])


@router.get(
    "/datacollection",
    response_model=list[schema.SSXDataCollectionResponse],
    responses={404: {"description": "Entity not found"}},
)
def get_datacollections(
    sessionId: int, dataCollectionGroupId: int
) -> list[models.SSXDataCollection]:
    return crud.get_ssx_datacollections(sessionId, dataCollectionGroupId)


@router.get(
    "/datacollectiongroup",
    response_model=list[schema.DataCollectionGroupResponse],
    responses={404: {"description": "Entity not found"}},
)
def get_datacollectiongroups(sessionId: int) -> list[models.DataCollectionGroup]:
    results = crud.get_ssx_datacollectiongroups(sessionId)
    results = [r.__dict__ for r in results]
    for r in results:
        r["nbDataCollection"] = crud.count_datacollections(r["dataCollectionGroupId"])
    return results


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
    "/datacollection/{dataCollectionId:int}/events",
    response_model=list[schema.EventChainResponse],
    responses={404: {"description": "Entity not found"}},
)
def get_datacollection_event_chains(dataCollectionId: int) -> list[models.EventChain]:
    return crud.get_ssx_datacollection_event_chains(dataCollectionId)


@router.get(
    "/datacollectiongroup/{dataCollectionGroupId:int}",
    response_model=schema.DataCollectionGroupResponse,
)
def get_datacollectiongroup(
    dataCollectionGroupId: int,
) -> models.DataCollectionGroup:
    r = crud.get_ssx_datacollectiongroup(dataCollectionGroupId).__dict__
    r["nbDataCollection"] = crud.count_datacollections(r["dataCollectionGroupId"])
    return r


@router.get(
    "/datacollectiongroup/{dataCollectionGroupId:int}/sample",
    response_model=schema.SSXSampleResponse,
    responses={404: {"description": "Entity not found"}},
)
def get_datacollectiongroup_sample(dataCollectionGroupId: int) -> models.BLSample:
    return crud.get_ssx_datacollectiongroup_sample(dataCollectionGroupId)


@router.get(
    "/datacollection/{dataCollectionId:int}/processing",
    response_model=schema.SSXDataCollectionProcessingResponse,
)
def get_ssx_datacollection_processing(
    dataCollectionId: int,
) -> models.SSXDataCollectionProcessing:
    return crud.get_ssx_datacollection_processing(dataCollectionId)

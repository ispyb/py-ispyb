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
    "/datacollection/{dataCollectionId:int}/sequences",
    response_model=list[schema.SSXSequenceResponse],
    responses={404: {"description": "Entity not found"}},
)
def get_datacollection_sequences(dataCollectionId: int) -> list[models.Sequence]:
    return crud.get_ssx_datacollection_sequences(dataCollectionId)


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


@router.post(
    "/datacollection/{dataCollectionId:int}/hits",
    response_model=schema.SSXHitsResponse,
)
def create_ssx_hits(
    ssx_hits_create: schema.SSXHitsCreate, dataCollectionId: int
) -> models.SSXHits:
    return crud.create_ssx_hits(dataCollectionId, ssx_hits_create)


@router.get(
    "/datacollection/{dataCollectionId:int}/hits",
    response_model=schema.SSXHitsResponse,
)
def get_ssx_hits(dataCollectionId: int) -> models.SSXHits:
    return crud.get_ssx_hits(dataCollectionId)


@router.get(
    "/datacollection/{dataCollectionId:int}/graphs",
    response_model=list[schema.GraphResponse],
)
def get_graphs(dataCollectionId: int) -> list[models.Graph]:
    return crud.get_graphs(dataCollectionId)


@router.get(
    "/graph/{graphId:int}/data",
    response_model=list[schema.GraphDataResponse],
)
def get_graph_data(graphId: int) -> list[models.GraphData]:
    return crud.get_graph_data(graphId)

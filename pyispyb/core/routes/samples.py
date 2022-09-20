from fastapi import Depends, HTTPException, Request
from ispyb import models

from ...dependencies import pagination, order_by_factory
from ...app.extensions.database.utils import Paged
from ... import filters
from ...app.base import AuthenticatedAPIRouter

from ..modules import samples as crud
from ..schemas import samples as schema
from ..schemas.utils import paginated


router = AuthenticatedAPIRouter(prefix="/samples", tags=["Samples"])


@router.get("/sub", response_model=paginated(schema.SubSample))
def get_subsamples(
    request: Request,
    page: dict[str, int] = Depends(pagination),
    blSampleId: int = Depends(filters.blSampleId),
    proteinId: int = Depends(filters.proteinId),
    proposal: str = Depends(filters.proposal),
    containerId: int = Depends(filters.containerId),
    sort_order: dict = Depends(
        order_by_factory(crud.SUBSAMPLE_ORDER_BY_MAP, "SubSampleOrder")
    ),
) -> Paged[models.BLSubSample]:
    """Get a list of sub samples"""
    return crud.get_subsamples(
        blSampleId=blSampleId,
        proteinId=proteinId,
        proposal=proposal,
        containerId=containerId,
        sort_order=sort_order,
        beamlineGroups=request.app.db_options.beamlineGroups,
        **page
    )


@router.get(
    "/sub/{blSubSampleId}",
    response_model=schema.SubSample,
    responses={404: {"description": "No such sub sample"}},
)
def get_subsample(
    request: Request,
    blSubSampleId: int = Depends(filters.blSubSampleId),
) -> models.BLSubSample:
    """Get a sub sample"""
    subsamples = crud.get_subsamples(
        blSubSampleId=blSubSampleId,
        beamlineGroups=request.app.db_options.beamlineGroups,
        skip=0,
        limit=1,
    )

    try:
        return subsamples.first
    except IndexError:
        raise HTTPException(status_code=404, detail="Sub sample not found")


@router.get("/", response_model=paginated(schema.Sample))
def get_samples(
    request: Request,
    page: dict[str, int] = Depends(pagination),
    proteinId: int = Depends(filters.proteinId),
    proposal: str = Depends(filters.proposal),
    containerId: int = Depends(filters.containerId),
    sort_order: dict = Depends(
        order_by_factory(crud.SAMPLE_ORDER_BY_MAP, "SampleOrder")
    ),
) -> Paged[models.BLSample]:
    """Get a list of samples"""
    return crud.get_samples(
        proteinId=proteinId,
        proposal=proposal,
        containerId=containerId,
        sort_order=sort_order,
        beamlineGroups=request.app.db_options.beamlineGroups,
        **page
    )


@router.get(
    "/{blSampleId}",
    response_model=schema.Sample,
    responses={404: {"description": "No such sample"}},
)
def get_sample(
    request: Request,
    blSampleId: int = Depends(filters.blSampleId),
) -> models.BLSample:
    """Get a sample"""
    samples = crud.get_samples(
        blSampleId=blSampleId,
        beamlineGroups=request.app.db_options.beamlineGroups,
        skip=0,
        limit=1,
    )

    try:
        return samples.first
    except IndexError:
        raise HTTPException(status_code=404, detail="Sample not found")

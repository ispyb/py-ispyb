import logging
import os
from typing import Optional

from fastapi import Depends, HTTPException, Request
from fastapi.responses import FileResponse
from ispyb import models

from ...config import settings
from ...dependencies import pagination, order_by_factory
from ...app.extensions.database.utils import Paged
from ... import filters
from ...app.base import AuthenticatedAPIRouter
from ..modules import samples as crud
from ..schemas import samples as schema
from ..schemas.utils import paginated

logger = logging.getLogger(__name__)
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
        beamLineGroups=request.app.db_options.beamLineGroups,
        **page,
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
        beamLineGroups=request.app.db_options.beamLineGroups,
        skip=0,
        limit=1,
    )

    try:
        return subsamples.first
    except IndexError:
        raise HTTPException(status_code=404, detail="Sub sample not found")


@router.get("/images", response_model=paginated(schema.SampleImage))
def get_sample_images(
    request: Request,
    page: dict[str, int] = Depends(pagination),
    blSampleId: int = Depends(filters.blSampleId),
) -> Paged[models.BLSampleImage]:
    """Get a list of sample images"""
    return crud.get_sample_images(
        blSampleId=blSampleId,
        beamLineGroups=request.app.db_options.beamLineGroups,
        **page,
    )


@router.get("/images/{blSampleImageId}", response_class=FileResponse)
def get_sample_image(
    request: Request,
    blSampleImageId: int,
):
    """Get a sample image"""
    sampleimages = crud.get_sample_images(
        blSampleImageId=blSampleImageId,
        beamLineGroups=request.app.db_options.beamLineGroups,
        limit=1,
        skip=0,
    )

    try:
        sampleimage = sampleimages.first
        image_path = sampleimage.imageFullPath
        if settings.path_map:
            image_path = settings.path_map + image_path

        if not os.path.exists(image_path):
            logger.warning(
                f"blSampleImageId `{sampleimage.blSampleImageId}` file `{image_path}` does not exist on disk"
            )
            raise IndexError
        return image_path

    except IndexError:
        raise HTTPException(status_code=404, detail="Sample image not found")


@router.get("", response_model=paginated(schema.Sample))
def get_samples(
    request: Request,
    page: dict[str, int] = Depends(pagination),
    search: str = Depends(filters.search),
    proteinId: int = Depends(filters.proteinId),
    proposal: str = Depends(filters.proposal),
    containerId: int = Depends(filters.containerId),
    beamLineName: str = Depends(filters.beamLineName),
    status: Optional[crud.SAMPLE_STATUS_ENUM] = None,
    sort_order: dict = Depends(
        order_by_factory(crud.SAMPLE_ORDER_BY_MAP, "SampleOrder")
    ),
) -> Paged[models.BLSample]:
    """Get a list of samples"""
    return crud.get_samples(
        search=search,
        proteinId=proteinId,
        proposal=proposal,
        containerId=containerId,
        beamLineName=beamLineName,
        status=status,
        sort_order=sort_order,
        beamLineGroups=request.app.db_options.beamLineGroups,
        **page,
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
        beamLineGroups=request.app.db_options.beamLineGroups,
        skip=0,
        limit=1,
    )

    try:
        return samples.first
    except IndexError:
        raise HTTPException(status_code=404, detail="Sample not found")

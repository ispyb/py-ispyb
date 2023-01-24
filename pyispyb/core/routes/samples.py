import logging
import os
from typing import Optional

from fastapi import Depends, HTTPException
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
        **page,
    )


@router.get(
    "/sub/{blSubSampleId}",
    response_model=schema.SubSample,
    responses={404: {"description": "No such sub sample"}},
)
def get_subsample(
    blSubSampleId: int = Depends(filters.blSubSampleId),
) -> models.BLSubSample:
    """Get a sub sample"""
    subsamples = crud.get_subsamples(
        blSubSampleId=blSubSampleId,
        skip=0,
        limit=1,
    )

    try:
        return subsamples.first
    except IndexError:
        raise HTTPException(status_code=404, detail="Sub sample not found")


@router.get("/images", response_model=paginated(schema.SampleImage))
def get_sample_images(
    page: dict[str, int] = Depends(pagination),
    blSampleId: int = Depends(filters.blSampleId),
) -> Paged[models.BLSampleImage]:
    """Get a list of sample images"""
    return crud.get_sample_images(
        blSampleId=blSampleId,
        **page,
    )


@router.get("/images/{blSampleImageId}", response_class=FileResponse)
def get_sample_image(
    blSampleImageId: int,
):
    """Get a sample image"""
    sampleimages = crud.get_sample_images(
        blSampleImageId=blSampleImageId,
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
        **page,
    )


@router.get("/components", response_model=paginated(schema.Component))
def get_components(
    page: dict[str, int] = Depends(pagination),
    proposal: str = Depends(filters.proposal),
) -> Paged[models.BLSample]:
    """Get a list of available components"""
    return crud.get_components(
        proposal=proposal,
        **page,
    )


@router.get("/components/types", response_model=list[schema.ComponentType])
def get_components_types() -> Paged[models.BLSample]:
    """Get a list of available component types"""
    return crud.get_component_types()


@router.get("/concentration/types", response_model=list[schema.ConcentrationType])
def get_concentration_types() -> list[models.ConcentrationType]:
    """Get a list of available concentration types"""
    return crud.get_concentration_types()


@router.get(
    "/{blSampleId}",
    response_model=schema.Sample,
    responses={404: {"description": "No such sample"}},
)
def get_sample(
    blSampleId: int = Depends(filters.blSampleId),
) -> models.BLSample:
    """Get a sample"""
    samples = crud.get_samples(
        blSampleId=blSampleId,
        skip=0,
        limit=1,
    )

    try:
        return samples.first
    except IndexError:
        raise HTTPException(status_code=404, detail="Sample not found")


@router.patch(
    "/{blSampleId}",
    response_model=schema.Sample,
    responses={404: {"description": "No such sample"}},
)
def update_sample(
    sample: schema.SampleUpdate,
    blSampleId: int = Depends(filters.blSampleId),
) -> models.BLSample:
    """update a sample"""
    try:
        sample = crud.update_sample(blSampleId=blSampleId, sample=sample)
        return sample
    except IndexError:
        raise HTTPException(status_code=404, detail="Sample not found")


@router.post(
    "",
    response_model=schema.Sample,
)
def create_sample(
    sample: schema.SampleCreate,
) -> models.BLSample:
    """create a sample"""
    sample = crud.create_sample(sample=sample)
    return sample


@router.delete(
    "/{blSampleId}",
    responses={404: {"description": "No such sample"}},
)
def delete_sample(
    blSampleId: int = Depends(filters.blSampleId),
) -> None:
    """delete a sample"""
    try:
        crud.delete_sample(blSampleId=blSampleId)
    except IndexError:
        raise HTTPException(status_code=404, detail="Sample not found")

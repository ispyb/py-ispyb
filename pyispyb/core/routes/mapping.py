import logging
from typing import Optional

from fastapi import Depends, HTTPException, Query
from fastapi.responses import StreamingResponse
from ispyb import models

from ...dependencies import pagination
from ...app.extensions.database.utils import Paged
from ...app.base import AuthenticatedAPIRouter
from ... import filters

from ..modules import mapping as crud
from ..schemas import mapping as schema
from ..schemas.utils import paginated


logger = logging.getLogger(__name__)
router = AuthenticatedAPIRouter(prefix="/mapping", tags=["Mapping"])


@router.get("/rois", response_model=paginated(schema.MapROI))
def get_map_rois(
    blSampleId: str = Depends(filters.blSampleId),
    xrfFluorescenceMappingROIId: Optional[int] = Query(
        None, title="xrfFluorescenceMapping ROI id"
    ),
    page: dict[str, int] = Depends(pagination),
) -> Paged[models.XRFFluorescenceMappingROI]:
    """Get a list of map rois"""
    return crud.get_map_rois(
        blSampleId=blSampleId,
        xrfFluorescenceMappingROIId=xrfFluorescenceMappingROIId,
        **page
    )


@router.get("", response_model=paginated(schema.Map))
def get_maps(
    dataCollectionId: int = Depends(filters.dataCollectionId),
    blSampleId: int = Depends(filters.blSampleId),
    blSubSampleId: int = Depends(filters.blSubSampleId),
    xrfFluorescenceMappingId: int = Query(None, title="XrfFluorescenceMapping id"),
    page: dict[str, int] = Depends(pagination),
) -> Paged[models.XRFFluorescenceMapping]:
    """Get a list of maps"""
    return crud.get_maps(
        blSampleId=blSampleId,
        blSubSampleId=blSubSampleId,
        dataCollectionId=dataCollectionId,
        xrfFluorescenceMappingId=xrfFluorescenceMappingId,
        **page
    )


@router.get("/histogram/{xrfFluorescenceMappingId}", response_model=schema.MapHistogram)
def get_map_histogram(
    xrfFluorescenceMappingId: int,
):
    """Get a map histogram"""
    maps = crud.get_maps(
        xrfFluorescenceMappingId=xrfFluorescenceMappingId, skip=0, limit=1
    )
    try:
        map_ = maps.first
    except IndexError:
        raise HTTPException(status_code=404, detail="Map not found")

    return crud.generate_histogram(map_)


@router.get("/pixel/{xrfFluorescenceMappingId}", response_model=schema.MapPixelValue)
def get_map_pixel_value(
    xrfFluorescenceMappingId: int,
    x: int = Query(None, title="Y position"),
    y: int = Query(None, title="Y position"),
):
    """Get a map histogram"""
    maps = crud.get_maps(
        xrfFluorescenceMappingId=xrfFluorescenceMappingId, skip=0, limit=1
    )
    try:
        map_ = maps.first
    except IndexError:
        raise HTTPException(status_code=404, detail="Map not found")

    data = crud.shape_map(map_)

    if y < len(data):
        if x < len(data[y]):
            return {
                "xrfFluorescenceMappingId": map_.xrfFluorescenceMappingId,
                "x": x,
                "y": y,
                "value": data[y][x],
            }


@router.get("/{xrfFluorescenceMappingId}")
def get_map(
    xrfFluorescenceMappingId: int,
):
    """Get a map in image format"""
    maps = crud.get_maps(
        xrfFluorescenceMappingId=xrfFluorescenceMappingId, skip=0, limit=1
    )
    try:
        map_ = maps.first
    except IndexError:
        raise HTTPException(status_code=404, detail="Map not found")

    image = crud.generate_map_image(map_)
    return StreamingResponse(image, media_type="image/png")

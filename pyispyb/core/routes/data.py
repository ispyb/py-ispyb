import logging
from fastapi import Depends, HTTPException, Response
from pydantic import conint

from ... import filters
from ...app.base import AuthenticatedAPIRouter
from ..modules import data as crud
from ..schemas import data as schema

logger = logging.getLogger(__name__)
router = AuthenticatedAPIRouter(prefix="/data", tags=["Data"])


@router.get("/images")
def get_image(
    imageNumber: conint(gt=0),
    dataCollectionId: int = Depends(filters.dataCollectionId),
):
    """Get raw image data"""
    image = crud.get_image(
        dataCollectionId=dataCollectionId,
        imageNumber=imageNumber,
    )

    if image is None:
        raise HTTPException(status_code=404, detail="Image not found")

    return Response(image.tobytes(), media_type="application/octet-stream")


@router.get("/images/header")
def get_image_header(
    imageNumber: int,
    dataCollectionId: int = Depends(filters.dataCollectionId),
):
    """Get image header"""
    header = crud.get_image(
        dataCollectionId=dataCollectionId, imageNumber=imageNumber, header=True
    )

    if not header:
        raise HTTPException(status_code=404, detail="Image not found")

    return header


@router.get("/images/histogram", response_model=schema.ImageHistogram)
def get_image_histogram(
    imageNumber: int,
    dataCollectionId: int = Depends(filters.dataCollectionId),
):
    """Get image histogram data"""
    histogram = crud.get_image_histogram(
        dataCollectionId=dataCollectionId,
        imageNumber=imageNumber,
    )

    if not histogram:
        raise HTTPException(status_code=404, detail="Image not found")

    return histogram

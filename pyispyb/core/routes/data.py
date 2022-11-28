import logging
from typing import Optional

from fastapi import Depends, HTTPException, Response, Query
from h5grove.content import (
    DatasetContent,
    ResolvedEntityContent,
    get_content_from_file,
)
from h5grove.encoders import encode
from h5grove.models import LinkResolution
from h5grove.utils import parse_link_resolution_arg
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


class H5GroveException(Exception):
    def __init__(self, status_code: int, message: str) -> None:
        self.status_code = status_code
        self.message = message


def create_error(status_code, message):
    return H5GroveException(status_code, message)


@router.get("/h5grove/attr/")
async def get_attr(
    path: str = "/",
    attr_keys: Optional[list[str]] = Query(default=None),
    dataCollectionId: Optional[int] = Depends(filters.dataCollectionId),
    autoProcProgramAttachmentId: Optional[int] = Query(
        None, title="AutoProcProgramAttachment id"
    ),
    robotActionId: Optional[int] = Query(None, title="RobotAction id"),
):
    """h5grove `/attr/` endpoint handler"""
    file = crud.get_h5_path_mapped(
        dataCollectionId=dataCollectionId,
        autoProcProgramAttachmentId=autoProcProgramAttachmentId,
        robotActionId=robotActionId,
    )
    if file is None:
        raise HTTPException(status_code=404, detail="File not found")

    with get_content_from_file(file, path, create_error) as content:
        if not isinstance(content, ResolvedEntityContent):
            raise HTTPException(status_code=500, detail="Wrong file type")
        h5grove_response = encode(content.attributes(attr_keys), "json")
        return Response(
            content=h5grove_response.content, headers=h5grove_response.headers
        )


@router.get("/h5grove/data/")
async def get_data(
    path: str = "/",
    dtype: str = "origin",
    format: str = "json",
    flatten: bool = False,
    selection=None,
    dataCollectionId: Optional[int] = Depends(filters.dataCollectionId),
    autoProcProgramAttachmentId: Optional[int] = Query(
        None, title="AutoProcProgramAttachment id"
    ),
    robotActionId: Optional[int] = Query(None, title="RobotAction id"),
):
    """h5grove `/data/` endpoint handler"""
    file = crud.get_h5_path_mapped(
        dataCollectionId=dataCollectionId,
        autoProcProgramAttachmentId=autoProcProgramAttachmentId,
        robotActionId=robotActionId,
    )
    if file is None:
        raise HTTPException(status_code=404, detail="File not found")

    with get_content_from_file(file, path, create_error) as content:
        if not isinstance(content, DatasetContent):
            raise HTTPException(status_code=500, detail="Wrong file type")
        data = content.data(selection, flatten, dtype)
        h5grove_response = encode(data, format)
        return Response(
            content=h5grove_response.content, headers=h5grove_response.headers
        )


@router.get("/h5grove/meta/")
async def get_meta(
    path: str = "/",
    resolve_links: str = "only_valid",
    dataCollectionId: Optional[int] = Depends(filters.dataCollectionId),
    autoProcProgramAttachmentId: Optional[int] = Query(
        None, title="AutoProcProgramAttachment id"
    ),
    robotActionId: Optional[int] = Query(None, title="RobotAction id"),
):
    """h5grove `/meta/` endpoint handler"""
    file = crud.get_h5_path_mapped(
        dataCollectionId=dataCollectionId,
        autoProcProgramAttachmentId=autoProcProgramAttachmentId,
        robotActionId=robotActionId,
    )
    if file is None:
        raise HTTPException(status_code=404, detail="File not found")

    resolve_links = parse_link_resolution_arg(
        resolve_links,
        fallback=LinkResolution.ONLY_VALID,
    )
    with get_content_from_file(file, path, create_error, resolve_links) as content:
        h5grove_response = encode(content.metadata(), "json")
        return Response(
            content=h5grove_response.content, headers=h5grove_response.headers
        )


@router.get("/h5grove/stats/")
async def get_stats(
    path: str = "/",
    selection=None,
    dataCollectionId: Optional[int] = Depends(filters.dataCollectionId),
    autoProcProgramAttachmentId: Optional[int] = Query(
        None, title="AutoProcProgramAttachment id"
    ),
    robotActionId: Optional[int] = Query(None, title="RobotAction id"),
):
    """h5grove `/stats/` endpoint handler"""
    file = crud.get_h5_path_mapped(
        dataCollectionId=dataCollectionId,
        autoProcProgramAttachmentId=autoProcProgramAttachmentId,
        robotActionId=robotActionId,
    )
    if file is None:
        raise HTTPException(status_code=404, detail="File not found")

    with get_content_from_file(file, path, create_error) as content:
        if not isinstance(content, DatasetContent):
            raise HTTPException(status_code=500, detail="Wrong file type")
        h5grove_response = encode(content.data_stats(selection), "json")
        return Response(
            content=h5grove_response.content, headers=h5grove_response.headers
        )

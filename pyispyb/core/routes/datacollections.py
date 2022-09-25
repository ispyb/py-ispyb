import logging
import os

from fastapi import Depends, HTTPException, Request, Query
from fastapi.responses import FileResponse
from pydantic import conint
from ispyb import models

from ...dependencies import pagination
from ...app.extensions.database.utils import Paged
from ... import filters
from ...app.base import AuthenticatedAPIRouter

from ..modules import datacollections as crud
from ..schemas import datacollections as schema
from ..schemas.utils import paginated


logger = logging.getLogger(__name__)
router = AuthenticatedAPIRouter(prefix="/datacollections", tags=["Data Collections"])


@router.get("/images/{dataCollectionId}", response_class=FileResponse)
def get_datacollection_image(
    request: Request,
    dataCollectionId: int,
    imageId: conint(ge=1, le=4) = Query(1, description="Image 1-4 to return"),
    snapshot: bool = Query(False, description="Get snapshot image"),
) -> str:
    """Get a data collection image"""
    path = crud.get_datacollection_snapshot_path(
        dataCollectionId,
        imageId,
        snapshot,
        beamLineGroups=request.app.db_options.beamLineGroups,
    )
    if not path:
        raise HTTPException(status_code=404, detail="Image not found")

    return path


@router.get(
    "/attachments", response_model=paginated(schema.DataCollectionFileAttachment)
)
def get_datacollection_attachments(
    request: Request,
    page: dict[str, int] = Depends(pagination),
    dataCollectionId: int = Depends(filters.dataCollectionId),
    dataCollectionGroupId: int = Depends(filters.dataCollectionGroupId),
) -> Paged[models.DataCollectionFileAttachment]:
    """Get a list of data collection attachments"""
    return crud.get_datacollection_attachments(
        dataCollectionId=dataCollectionId,
        dataCollectionGroupId=dataCollectionGroupId,
        beamLineGroups=request.app.db_options.beamLineGroups,
        **page,
    )


@router.get(
    "/attachments/{dataCollectionFileAttachmentId}",
    response_class=FileResponse,
    responses={404: {"description": "No such data collection attachment"}},
)
def get_datacollection_attachment(
    request: Request,
    dataCollectionFileAttachmentId: int,
):
    """Get a data collection attachment"""
    attachments = crud.get_datacollection_attachments(
        dataCollectionFileAttachmentId=dataCollectionFileAttachmentId,
        beamLineGroups=request.app.db_options.beamLineGroups,
        skip=0,
        limit=1,
    )

    try:
        attachment = attachments.first
        if not os.path.exists(attachment.fileFullPath):
            logger.warning(
                f"dataCollectionFileAttachmentId `{attachment.dataCollectionFileAttachmentId}` file `{attachment.fileFullPath}` does not exist on disk"
            )
            raise IndexError
        return attachment.fileFullPath
    except IndexError:
        raise HTTPException(
            status_code=404, detail="Data collection attachment not found"
        )

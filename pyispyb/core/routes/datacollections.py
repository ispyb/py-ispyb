import logging
import os
from typing import Optional

from fastapi import Depends, HTTPException, Query
from fastapi.responses import FileResponse
from pydantic import conint
from ispyb import models

from ...config import settings
from ...dependencies import pagination
from ...app.extensions.database.utils import Paged
from ... import filters
from ...app.base import AuthenticatedAPIRouter

from ..modules import datacollections as crud
from ..schemas import datacollections as schema
from ..schemas.utils import paginated


logger = logging.getLogger(__name__)
router = AuthenticatedAPIRouter(prefix="/datacollections", tags=["Data Collections"])


@router.get("/images/diffraction/{dataCollectionId}", response_class=FileResponse)
def get_datacollection_diffraction_image(
    dataCollectionId: int,
    snapshot: bool = Query(False, description="Get snapshot image"),
) -> str:
    """Get a data collection diffraction image"""
    path = crud.get_datacollection_diffraction_image_path(
        dataCollectionId,
        snapshot,
    )
    if not path:
        raise HTTPException(status_code=404, detail="Image not found")

    return path


@router.get("/images/quality/{dataCollectionId}", response_class=FileResponse)
def get_datacollection_anaylsis_image(
    dataCollectionId: int,
) -> str:
    """Get a data collection per image analysis image"""
    path = crud.get_datacollection_analysis_image_path(
        dataCollectionId,
    )
    if not path:
        raise HTTPException(status_code=404, detail="Image not found")

    return path


@router.get("/images/{dataCollectionId}", response_class=FileResponse)
def get_datacollection_image(
    dataCollectionId: int,
    imageId: conint(ge=1, le=4) = Query(1, description="Image 1-4 to return"),
    snapshot: bool = Query(False, description="Get snapshot image"),
) -> str:
    """Get a data collection image"""
    path = crud.get_datacollection_snapshot_path(
        dataCollectionId,
        imageId,
        snapshot,
    )
    if not path:
        raise HTTPException(status_code=404, detail="Image not found")

    return path


@router.get(
    "/attachments", response_model=paginated(schema.DataCollectionFileAttachment)
)
def get_datacollection_attachments(
    page: dict[str, int] = Depends(pagination),
    dataCollectionId: int = Depends(filters.dataCollectionId),
    dataCollectionGroupId: int = Depends(filters.dataCollectionGroupId),
) -> Paged[models.DataCollectionFileAttachment]:
    """Get a list of data collection attachments"""
    return crud.get_datacollection_attachments(
        dataCollectionId=dataCollectionId,
        dataCollectionGroupId=dataCollectionGroupId,
        **page,
    )


@router.get(
    "/attachments/{dataCollectionFileAttachmentId}",
    response_class=FileResponse,
    responses={404: {"description": "No such data collection attachment"}},
)
def get_datacollection_attachment(
    dataCollectionFileAttachmentId: int,
):
    """Get a data collection attachment"""
    attachments = crud.get_datacollection_attachments(
        dataCollectionFileAttachmentId=dataCollectionFileAttachmentId,
        skip=0,
        limit=1,
    )

    try:
        attachment = attachments.first
        file_path = attachment.fileFullPath
        if settings.path_map:
            file_path = settings.path_map + file_path

        if not os.path.exists(file_path):
            logger.warning(
                f"dataCollectionFileAttachmentId `{attachment.dataCollectionFileAttachmentId}` file `{file_path}` does not exist on disk"
            )
            raise IndexError
        return FileResponse(file_path, filename=attachment._metadata["fileName"])
    except IndexError:
        raise HTTPException(
            status_code=404, detail="Data collection attachment not found"
        )


@router.get(
    "/quality",
    response_model=paginated(schema.PerImageAnalysis),
    responses={404: {"description": "A list of per image/point analysis"}},
)
def get_per_image_analysis(
    page: dict[str, int] = Depends(pagination),
    dataCollectionId: int = Depends(filters.dataCollectionId),
    dataCollectionGroupId: int = Depends(filters.dataCollectionGroupId),
) -> Paged[schema.PerImageAnalysis]:
    """Get a list of per image/point analysis"""
    return crud.get_per_image_analysis(
        dataCollectionId=dataCollectionId,
        dataCollectionGroupId=dataCollectionGroupId,
        **page,
    )


@router.get("/workflows/steps", response_model=paginated(schema.WorkflowStep))
def get_workflow_steps(
    page: dict[str, int] = Depends(pagination),
    workflowId: Optional[int] = Query(None, title="Workflow id"),
    workflowStepId: Optional[int] = Query(None, title="Workflow step id"),
) -> Paged[models.WorkflowStep]:
    """Get a list of workflow steps"""
    return crud.get_workflow_steps(
        workflowId=workflowId,
        workflowStepId=workflowStepId,
        **page,
    )


@router.get(
    "/workflows/steps/{workflowStepId}",
    response_class=FileResponse,
    responses={404: {"description": "No such workflow step attachment"}},
)
def get_workflow_step_attachment(
    workflowStepId: int, attachmentType: schema.WorkflowStepAttachment
):
    """Get a workflow step attachment"""
    steps = crud.get_workflow_steps(
        workflowStepId=workflowStepId,
        skip=0,
        limit=1,
    )

    try:
        steps: models.WorkflowStep = steps.first
        file_path = getattr(steps, attachmentType)
        if settings.path_map:
            file_path = settings.path_map + file_path

        if not os.path.exists(file_path):
            logger.warning(
                f"workflowStep.{attachmentType} `{workflowStepId}` file `{file_path}` does not exist on disk"
            )
            raise IndexError
        return FileResponse(file_path, filename=os.path.basename(file_path))
    except IndexError:
        raise HTTPException(
            status_code=404, detail="Workflow step attachment not found"
        )

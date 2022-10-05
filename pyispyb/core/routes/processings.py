import logging
import os
from typing import Optional

from fastapi import Depends, Request, HTTPException, Query
from fastapi.responses import FileResponse
from ispyb import models
from pydantic import BaseModel, parse_obj_as
from pydantic.types import Json

from ...config import settings
from ...app.base import AuthenticatedAPIRouter
from ...app.extensions.database.utils import Paged
from ..schemas.utils import paginated
from ...dependencies import pagination
from ... import filters

from ..modules import processings as crud
from ..schemas import processings as schema


logger = logging.getLogger(__name__)
router = AuthenticatedAPIRouter(
    prefix="/processings", tags=["Processing Status and Results"]
)


class DataCollectionIds(BaseModel):
    dataCollectionIds: list[int]


def dataCollectionIds(
    dataCollectionIds: Json = Query(
        "", title="List of data collection ids (JSON encoded)"
    )
) -> list[int]:
    try:
        obj: DataCollectionIds = parse_obj_as(
            DataCollectionIds, {"dataCollectionIds": dataCollectionIds}
        )
        if not len(obj.dataCollectionIds):
            raise

        return obj.dataCollectionIds
    except Exception:
        logger.exception("Couldn't parse dataCollectionIds")
        raise HTTPException(status_code=422, detail="Couldn't parse dataCollectionIds")


@router.get("/status", response_model=schema.ProcessingStatusesList)
def get_processing_statuses(
    request: Request,
    dataCollectionIds: list[int] = Depends(dataCollectionIds),
) -> schema.ProcessingStatusesList:
    """Get processing statuses for a group of data collections"""
    return crud.get_processing_status(
        dataCollectionIds=dataCollectionIds,
        beamLineGroups=request.app.db_options.beamLineGroups,
    )


@router.get("/screenings", response_model=paginated(schema.Screening))
def get_screening_results(
    request: Request,
    dataCollectionId: int = Depends(filters.dataCollectionId),
    page: dict[str, int] = Depends(pagination),
) -> Paged[models.Screening]:
    """Get a list of screening results from `Screening`"""
    return crud.get_screening_results(
        dataCollectionId=dataCollectionId,
        beamLineGroups=request.app.db_options.beamLineGroups,
        **page,
    )


@router.get("", response_model=paginated(schema.AutoProcProgram))
def get_processing_results(
    request: Request,
    dataCollectionId: int = Depends(filters.dataCollectionId),
    page: dict[str, int] = Depends(pagination),
) -> Paged[models.AutoProcProgram]:
    """Get a list of processing results from `ProcessingJob`"""
    return crud.get_processing_results(
        dataCollectionId=dataCollectionId,
        beamLineGroups=request.app.db_options.beamLineGroups,
        **page,
    )


@router.get(
    "/auto-integrations", response_model=paginated(schema.AutoProcProgramIntegration)
)
def get_auto_integration_results(
    request: Request,
    dataCollectionId: int = Depends(filters.dataCollectionId),
    page: dict[str, int] = Depends(pagination),
) -> Paged[models.AutoProcProgram]:
    """Get a list of auto-integration results from `AutoProcIntegration`"""
    return crud.get_autointegration_results(
        dataCollectionId=dataCollectionId,
        beamLineGroups=request.app.db_options.beamLineGroups,
        **page,
    )


@router.get("/messages", response_model=paginated(schema.AutoProcProgramMessage))
def get_processing_messages(
    request: Request,
    dataCollectionId: int = Depends(filters.dataCollectionId),
    autoProcProgramMessageId: int = None,
    page: dict[str, int] = Depends(pagination),
) -> Paged[schema.AutoProcProgramMessage]:
    """Get a list of processing messages"""
    return crud.get_processing_messages(
        dataCollectionId=dataCollectionId,
        autoProcProgramMessageId=autoProcProgramMessageId,
        beamLineGroups=request.app.db_options.beamLineGroups,
        **page,
    )


@router.get("/messages/status", response_model=schema.AutoProcProgramMessageStatuses)
def get_processing_messages_status(
    request: Request,
    dataCollectionIds: list[int] = Depends(dataCollectionIds),
) -> schema.AutoProcProgramMessageStatuses:
    """Get the processing messages status"""
    return crud.get_processing_message_status(
        dataCollectionIds=dataCollectionIds,
        beamLineGroups=request.app.db_options.beamLineGroups,
    )


@router.get("/attachments", response_model=paginated(schema.AutoProcProgramAttachment))
def get_processing_attachments(
    request: Request,
    autoProcProgramId: int = None,
    autoProcProgramAttachmentId: int = None,
    page: dict[str, int] = Depends(pagination),
) -> Paged[models.AutoProcProgramAttachment]:
    """Get a list of auto processing attachments"""
    return crud.get_processing_attachments(
        autoProcProgramId=autoProcProgramId,
        autoProcProgramAttachmentId=autoProcProgramAttachmentId,
        beamLineGroups=request.app.db_options.beamLineGroups,
        **page,
    )


@router.get("/attachments/{autoProcProgramAttachmentId}", response_class=FileResponse)
def get_processing_attachment(
    request: Request,
    autoProcProgramAttachmentId: int,
):
    """Get an auto processing attachment"""
    attachments = crud.get_processing_attachments(
        autoProcProgramAttachmentId=autoProcProgramAttachmentId,
        beamLineGroups=request.app.db_options.beamLineGroups,
        skip=0,
        limit=1,
    )

    try:
        attachment = attachments.first
        file_path = os.path.join(attachment.filePath, attachment.fileName)

        if settings.path_map:
            file_path = settings.path_map + file_path

        if not os.path.exists(file_path):
            logger.warning(
                f"autoProcProgramAttachmentId `{attachment.autoProcProgramAttachmentId}` file `{file_path}` does not exist on disk"
            )
            raise IndexError
        return FileResponse(file_path, filename=attachment.fileName)
    except IndexError:
        raise HTTPException(
            status_code=404, detail="Autoproc program attachment not found"
        )

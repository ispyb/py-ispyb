from typing import Optional
from fastapi import Depends, Request

from ...app.extensions.database.utils import Paged
from ...dependencies import pagination
from ... import filters
from ...app.base import AuthenticatedAPIRouter

from ..modules import events as crud
from ..schemas import events as schema
from ..schemas.utils import paginated

router = AuthenticatedAPIRouter(prefix="/events", tags=["Events"])


@router.get(
    "",
    response_model=paginated(schema.Event),
    responses={404: {"description": "Entity not found"}},
)
def get_events(
    request: Request,
    page: dict[str, int] = Depends(pagination),
    session: str = Depends(filters.session),
    proposal: str = Depends(filters.proposal),
    beamLineName: str = Depends(filters.beamLineName),
    dataCollectionId: int = Depends(filters.dataCollectionId),
    dataCollectionGroupId: int = Depends(filters.dataCollectionGroupId),
    blSampleId: int = Depends(filters.blSampleId),
    proteinId: int = Depends(filters.proteinId),
    status: crud.EventStatus = None,
    eventType: Optional[str] = None,
) -> Paged[schema.Event]:
    """Get a list of events"""
    return crud.get_events(
        session=session,
        proposal=proposal,
        beamLineName=beamLineName,
        dataCollectionId=dataCollectionId,
        dataCollectionGroupId=dataCollectionGroupId,
        blSampleId=blSampleId,
        proteinId=proteinId,
        status=status,
        eventType=eventType,
        beamLineGroups=request.app.db_options.beamLineGroups,
        **page
    )


@router.get(
    "/types",
    response_model=paginated(schema.EventType),
)
def get_event_types(
    request: Request,
    session: str = Depends(filters.session),
    blSampleId: int = Depends(filters.blSampleId),
) -> Paged[schema.EventType]:
    """Get a list of event types"""
    return crud.get_event_types(
        session=session,
        blSampleId=blSampleId,
        beamLineGroups=request.app.db_options.beamLineGroups,
    )

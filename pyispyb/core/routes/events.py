from typing import Optional
from fastapi import Depends

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
    page: dict[str, int] = Depends(pagination),
    session: str = Depends(filters.session),
    sessionId: int = Depends(filters.sessionId),
    proposal: str = Depends(filters.proposal),
    proposalId: str = Depends(filters.proposalId),
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
        sessionId=sessionId,
        proposal=proposal,
        proposalId=proposalId,
        beamLineName=beamLineName,
        dataCollectionId=dataCollectionId,
        dataCollectionGroupId=dataCollectionGroupId,
        blSampleId=blSampleId,
        proteinId=proteinId,
        status=status,
        eventType=eventType,
        **page
    )


@router.get(
    "/types",
    response_model=paginated(schema.EventType),
)
def get_event_types(
    session: str = Depends(filters.session),
    sessionId: int = Depends(filters.sessionId),
    blSampleId: int = Depends(filters.blSampleId),
    proteinId: int = Depends(filters.proteinId),
) -> Paged[schema.EventType]:
    """Get a list of event types"""
    return crud.get_event_types(
        session=session,
        sessionId=sessionId,
        blSampleId=blSampleId,
        proteinId=proteinId,
    )

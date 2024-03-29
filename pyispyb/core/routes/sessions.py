from typing import Optional

from fastapi import Depends, HTTPException, Query
from ispyb import models

from pyispyb.dependencies import pagination
from pyispyb.app.extensions.database.utils import Paged
from pyispyb import filters
from pyispyb.app.base import AuthenticatedAPIRouter

from ..modules import sessions as crud
from ..schemas import sessions as schema
from ..schemas.utils import paginated


router = AuthenticatedAPIRouter(prefix="/sessions", tags=["Sessions"])
PaginatedSession = paginated(schema.Session)


@router.get("", response_model=PaginatedSession)
def get_sessions(
    proposal: str = Depends(filters.proposal),
    beamLineName: str = Depends(filters.beamLineName),
    beamLineGroup: Optional[str] = Query(
        None, description="Show sessions for a beamLineGroup"
    ),
    scheduled: bool = Query(None, description="Get scheduled sessions only"),
    upcoming: Optional[bool] = Query(False, description="Get the upcoming sessions"),
    previous: Optional[bool] = Query(
        False, description="Get the recently finished sessions"
    ),
    sessionType=Query(
        None, description="Filter by session type, i.e. commissioning, remote"
    ),
    month: int = Depends(filters.month),
    year: int = Depends(filters.year),
    page: dict[str, int] = Depends(pagination),
) -> Paged[models.BLSession]:
    """Get a list of sessions"""
    return crud.get_sessions(
        proposal=proposal,
        beamLineName=beamLineName,
        beamLineGroup=beamLineGroup,
        scheduled=scheduled,
        upcoming=upcoming,
        previous=previous,
        sessionType=sessionType,
        month=month,
        year=year,
        **page
    )


@router.get("/group", response_model=PaginatedSession)
def get_sessions_for_beamline_group(
    beamLineGroup: str = Query(
        None, description="Beamline group to display session for"
    ),
    upcoming: Optional[bool] = Query(False, description="Get the upcoming sessions"),
    previous: Optional[bool] = Query(
        False, description="Get the recently finished sessions"
    ),
    sessionType=Query(
        None, description="Filter by session type, i.e. commissioning, remote"
    ),
):
    """Get a list of sessions for a beamline group
    Displays one session per beamline
    """
    return crud.get_sessions_for_beamline_group(
        beamLineGroup=beamLineGroup,
        upcoming=upcoming,
        previous=previous,
        sessionType=sessionType,
    )


@router.get(
    "/{sessionId}",
    response_model=schema.Session,
    responses={404: {"description": "No such session"}},
)
def get_session(
    sessionId: str = Depends(filters.sessionId),
) -> models.BLSession:
    """Get a session"""
    sessions = crud.get_sessions(
        sessionId=sessionId,
        skip=0,
        limit=1,
    )

    try:
        return sessions.first
    except IndexError:
        raise HTTPException(status_code=404, detail="Session not found")

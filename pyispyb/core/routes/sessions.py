from typing import Optional

from fastapi import Depends, HTTPException, Request
from ispyb import models

from pyispyb.dependencies import pagination
from pyispyb.app.extensions.database.utils import Paged
from pyispyb import filters
from pyispyb.app.base import AuthenticatedAPIRouter

from ..modules import sessions as crud
from ..schemas import sessions as schema
from ..schemas.utils import paginated


router = AuthenticatedAPIRouter(prefix="/sessions", tags=["Sessions"])


@router.get("/", response_model=paginated(schema.Session))
def get_sessions(
    request: Request,
    proposal: str = Depends(filters.proposal),
    page: dict[str, int] = Depends(pagination),
) -> Paged[models.BLSession]:
    """Get a list of sessions"""
    return crud.get_sessions(
        sessionHasPerson=True,
        proposal=proposal,
        beamLineGroups=request.app.db_options.beamLineGroups,
        **page
    )


@router.get(
    "/{session}",
    response_model=schema.Session,
    responses={404: {"description": "No such session"}},
)
def get_session(
    request: Request,
    session: str = Depends(filters.session),
    beamLineName: str = Depends(filters.beamLineName),
    beamLineGroup: Optional[str] = None,
) -> models.BLSession:
    """Get a session"""
    sessions = crud.get_sessions(
        session=session,
        beamLineName=beamLineName,
        beamLineGroup=beamLineGroup
        beamLineGroups=request.app.db_options.beamLineGroups,
        skip=0,
        limit=1,
    )

    try:
        return sessions.first
    except IndexError:
        raise HTTPException(status_code=404, detail="Session not found")

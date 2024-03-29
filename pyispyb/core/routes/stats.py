from fastapi import Depends, HTTPException

from ...app.base import AuthenticatedAPIRouter
from ...app.extensions.database.utils import Paged
from ...core.schemas.utils import paginated
from ...dependencies import pagination
from ... import filters

from ..modules import stats as crud
from ..schemas import stats as schema


router = AuthenticatedAPIRouter(prefix="/stats", tags=["Stats"])


@router.get("/breakdown", response_model=schema.Breakdown)
def get_breakdown(
    beamLineName: str = Depends(filters.beamLineName),
    session: str = Depends(filters.session),
    sessionId: str = Depends(filters.sessionId),
    runId: str = Depends(filters.runId),
) -> schema.Breakdown:
    """Get stats breakdown for a session or run"""
    if not (sessionId or session or (beamLineName and runId)):
        raise HTTPException(
            status_code=422,
            detail="Please provide either `session` or (`beamLineName` and `runId`)",
        )

    return crud.get_breakdown(
        session=session,
        sessionId=sessionId,
        beamLineName=beamLineName,
        runId=runId,
    )


@router.get("/times", response_model=schema.Times)
def get_times(
    beamLineName: str = Depends(filters.beamLineName),
    session: str = Depends(filters.session),
    sessionId: str = Depends(filters.sessionId),
    proposal: str = Depends(filters.proposal),
    runId: str = Depends(filters.runId),
) -> schema.Times:
    """Get total times for a session, proposal, or run"""
    if not (proposal or sessionId or session or (beamLineName and runId)):
        raise HTTPException(
            status_code=422,
            detail="Please provide either `proposal` or `session` or (`beamLineName` and `runId`)",
        )

    return crud.get_times(
        session=session,
        sessionId=sessionId,
        proposal=proposal,
        beamLineName=beamLineName,
        runId=runId,
    )


@router.get("/errors", response_model=schema.Errors)
def get_errors(
    beamLineName: str = Depends(filters.beamLineName),
    session: str = Depends(filters.session),
    sessionId: str = Depends(filters.sessionId),
    runId: str = Depends(filters.runId),
) -> schema.Errors:
    """Get the errors for a session or run"""
    if not (sessionId or session or (beamLineName and runId)):
        raise HTTPException(
            status_code=422,
            detail="Please provide either `session` or (`beamLineName` and `runId`)",
        )

    return crud.get_errors(
        session=session,
        sessionId=sessionId,
        beamLineName=beamLineName,
        runId=runId,
    )


@router.get("/hourlies", response_model=schema.Hourlies)
def get_hourlies(
    beamLineName: str = Depends(filters.beamLineName),
    session: str = Depends(filters.session),
    sessionId: str = Depends(filters.sessionId),
    proposal: str = Depends(filters.proposal),
    runId: str = Depends(filters.runId),
) -> schema.Hourlies:
    """Get the hourly stats for a session or run"""
    if not (proposal or sessionId or session or (beamLineName and runId)):
        raise HTTPException(
            status_code=422,
            detail="Please provide either `proposal` or `session` or (`beamLineName` and `runId`)",
        )

    return crud.get_hourlies(
        session=session,
        sessionId=sessionId,
        proposal=proposal,
        beamLineName=beamLineName,
        runId=runId,
    )


@router.get("/parameters/histogram", response_model=schema.ParameterHistograms)
def get_parameter_histogram(
    beamLineName: str = Depends(filters.beamLineName),
    session: str = Depends(filters.session),
    sessionId: str = Depends(filters.sessionId),
    runId: str = Depends(filters.runId),
) -> schema.ParameterHistograms:
    """Get histogram of parameters for a session or run"""
    if not (sessionId or session or (beamLineName and runId)):
        raise HTTPException(
            status_code=422, detail="Please provide either `session` or `runId`"
        )

    return crud.get_parameter_histogram(
        session=session,
        sessionId=sessionId,
        beamLineName=beamLineName,
        runId=runId,
    )


@router.get("/runs", response_model=paginated(schema.VRun))
def get_runs(
    page: dict[str, int] = Depends(pagination),
) -> Paged[schema.VRun]:
    """Get a list of runs"""
    return crud.get_runs(
        **page,
    )

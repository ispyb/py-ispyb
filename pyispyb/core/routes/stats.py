from fastapi import Depends, Request, HTTPException
from ispyb import models

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
    request: Request,
    beamLineName: str = Depends(filters.beamLineName),
    session: str = Depends(filters.session),
    runId: str = Depends(filters.runId),
) -> schema.Breakdown:
    """Get stats breakdown for a session or run"""
    if not (session or (beamLineName and runId)):
        raise HTTPException(
            status_code=422,
            detail="Please provide either `session` or (`beamLineName` and `runId`)",
        )

    return crud.get_breakdown(
        session=session,
        beamLineName=beamLineName,
        runId=runId,
        beamLineGroups=request.app.db_options.beamLineGroups,
    )


@router.get("/times", response_model=schema.Times)
def get_times(
    request: Request,
    beamLineName: str = Depends(filters.beamLineName),
    session: str = Depends(filters.session),
    proposal: str = Depends(filters.proposal),
    runId: str = Depends(filters.runId),
) -> schema.Times:
    """Get total times for a session, proposal, or run"""
    if not (proposal or session or (beamLineName and runId)):
        raise HTTPException(
            status_code=422,
            detail="Please provide either `proposal` or `session` or (`beamLineName` and `runId`)",
        )

    return crud.get_times(
        session=session,
        proposal=proposal,
        beamLineName=beamLineName,
        runId=runId,
        beamLineGroups=request.app.db_options.beamLineGroups,
    )


@router.get("/errors", response_model=schema.Errors)
def get_errors(
    request: Request,
    beamLineName: str = Depends(filters.beamLineName),
    session: str = Depends(filters.session),
    runId: str = Depends(filters.runId),
) -> schema.Errors:
    """Get the errors for a session or run"""
    if not (session or (beamLineName and runId)):
        raise HTTPException(
            status_code=422,
            detail="Please provide either `session` or (`beamLineName` and `runId`)",
        )

    return crud.get_errors(
        session=session,
        beamLineName=beamLineName,
        runId=runId,
        beamLineGroups=request.app.db_options.beamLineGroups,
    )


@router.get("/hourlies", response_model=schema.Hourlies)
def get_hourlies(
    request: Request,
    beamLineName: str = Depends(filters.beamLineName),
    session: str = Depends(filters.session),
    proposal: str = Depends(filters.proposal),
    runId: str = Depends(filters.runId),
) -> schema.Hourlies:
    """Get the hourly stats for a session or run"""
    if not (proposal or session or (beamLineName and runId)):
        raise HTTPException(
            status_code=422,
            detail="Please provide either `proposal` or `session` or (`beamLineName` and `runId`)",
        )

    return crud.get_hourlies(
        session=session,
        proposal=proposal,
        beamLineName=beamLineName,
        runId=runId,
        beamLineGroups=request.app.db_options.beamLineGroups,
    )


@router.get("/parameters/histogram", response_model=schema.ParameterHistograms)
def get_parameter_histogram(
    request: Request,
    beamLineName: str = Depends(filters.beamLineName),
    beamLineGroup: str = None,
    session: str = Depends(filters.session),
    runId: str = Depends(filters.runId),
) -> schema.ParameterHistograms:
    """Get histogram of parameters for a session or run"""
    if not (session or (beamLineName and runId)):
        raise HTTPException(
            status_code=422, detail="Please provide either `session` or `runId`"
        )

    return crud.get_parameter_histogram(
        session=session,
        beamLineName=beamLineName,
        beamLineGroup=beamLineGroup,
        runId=runId,
        beamLineGroups=request.app.db_options.beamLineGroups,
    )


@router.get("/runs", response_model=paginated(schema.VRun))
def get_runs(
    page: dict[str, int] = Depends(pagination),
) -> Paged[schema.VRun]:
    """Get a list of runs"""
    return crud.get_runs(
        **page,
    )

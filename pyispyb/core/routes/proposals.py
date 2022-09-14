from fastapi import Depends, HTTPException, Request
from ispyb import models

from pyispyb.dependencies import pagination
from pyispyb.app.extensions.database.utils import Paged
from pyispyb import filters
from pyispyb.app.base import AuthenticatedAPIRouter

from ..modules import proposals as crud
from ..schemas import proposals as schema
from ..schemas.utils import paginated


router = AuthenticatedAPIRouter(prefix="/proposals", tags=["Proposals"])


@router.get("/", response_model=paginated(schema.Proposal))
def get_proposals(
    request: Request,
    search: str = Depends(filters.search),
    page: dict[str, int] = Depends(pagination),
) -> Paged[models.Proposal]:
    """Get a list of proposals"""
    return crud.get_proposals(
        search=search, beamlineGroups=request.app.db_options.beamlineGroups, **page
    )


@router.get(
    "/{proposal}",
    response_model=schema.Proposal,
    responses={404: {"description": "No such proposal"}},
)
def get_proposal(
    request: Request,
    proposal: str = Depends(filters.proposal),
) -> models.Proposal:
    """Get a proposal"""
    proposals = crud.get_proposals(
        proposal=proposal,
        beamlineGroups=request.app.db_options.beamlineGroups,
        skip=0,
        limit=1,
    )

    try:
        return proposals.first
    except IndexError:
        raise HTTPException(status_code=404, detail="Proposal not found")

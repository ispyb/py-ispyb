from fastapi import Depends, HTTPException, Request
from ispyb import models

from pyispyb.dependencies import pagination
from pyispyb.app.extensions.database.utils import Paged
from pyispyb import filters
from pyispyb.app.base import AuthenticatedAPIRouter

from ..modules import samples as crud
from ..schemas import samples as schema
from ..schemas.utils import paginated


router = AuthenticatedAPIRouter(prefix="/samples", tags=["Samples"])


@router.get("/", response_model=paginated(schema.Sample))
def get_samples(
    request: Request,
    page: dict[str, int] = Depends(pagination),
    proteinId: int = Depends(filters.proteinId),
    proposal: str = Depends(filters.proposal),
    containerId: int = Depends(filters.containerId),
) -> Paged[models.BLSample]:
    """Get a list of samples"""
    return crud.get_samples(
        proteinId=proteinId,
        proposal=proposal,
        containerId=containerId,
        beamlineGroups=request.app.db_options.beamlineGroups,
        **page
    )


@router.get(
    "/{blSampleId}",
    response_model=schema.Sample,
    responses={404: {"description": "No such sample"}},
)
def get_sample(
    request: Request,
    blSampleId: int = Depends(filters.blSampleId),
) -> models.BLSample:
    """Get a sample"""
    samples = crud.get_samples(
        blSampleId=blSampleId,
        beamlineGroups=request.app.db_options.beamlineGroups,
        skip=0,
        limit=1,
    )

    try:
        return samples.first
    except IndexError:
        raise HTTPException(status_code=404, detail="Sample not found")

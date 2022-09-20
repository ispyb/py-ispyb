from fastapi import Depends, Query, HTTPException, Request
from fastapi.responses import FileResponse
from pydantic import conint

from ...app.extensions.database.utils import Paged
from ...dependencies import pagination
from ... import filters
from ...app.base import AuthenticatedAPIRouter

from ..modules import events as crud
from ..schemas import events as schema
from ..schemas.utils import paginated

router = AuthenticatedAPIRouter(prefix="/events", tags=["Events"])


@router.get(
    "/",
    response_model=paginated(schema.Event),
    responses={404: {"description": "Entity not found"}},
)
def get_events(
    request: Request,
    page: dict[str, int] = Depends(pagination),
    session: str = Depends(filters.session),
    proposal: str = Depends(filters.proposal),
    beamlineName: str = Depends(filters.beamlineName),
    dataCollectionId: int = Depends(filters.dataCollectionId),
    dataCollectionGroupId: int = Depends(filters.dataCollectionGroupId),
    blSampleId: int = Depends(filters.blSampleId),
    proteinId: int = Depends(filters.proteinId),
    status: crud.EventStatus = None,
) -> Paged[schema.Event]:
    """Get a list of events"""
    return crud.get_events(
        session=session,
        proposal=proposal,
        beamlineName=beamlineName,
        dataCollectionId=dataCollectionId,
        dataCollectionGroupId=dataCollectionGroupId,
        blSampleId=blSampleId,
        proteinId=proteinId,
        status=status,
        beamlineGroups=request.app.db_options.beamlineGroups,
        **page
    )


@router.get("/image/{dataCollectionId}", response_class=FileResponse)
def get_datacollection_image(
    dataCollectionId: int,
    imageId: conint(ge=1, le=4) = Query(0, description="Image 1-4 to return"),
    snapshot: bool = Query(False, description="Get snapshot image"),
) -> str:
    """Get a data collection image"""
    path = crud.get_datacollection_snapshot_path(dataCollectionId, imageId, snapshot)
    if not path:
        raise HTTPException(status_code=404, detail="Image not found")

    return path

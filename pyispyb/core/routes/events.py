from fastapi import Depends, Query, HTTPException
from fastapi.responses import FileResponse
from pydantic import conint

from pyispyb.app.extensions.database.definitions import get_blsession
from pyispyb.app.extensions.database.utils import Paged
from pyispyb.dependencies import pagination
from pyispyb import filters
from pyispyb.app.base import AuthenticatedAPIRouter

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
    page: dict[str, int] = Depends(pagination),
    session: str = Depends(filters.session),
    dataCollectionGroupId: int = Depends(filters.dataCollectionGroupId),
    blSampleId: int = Depends(filters.blSampleId),
    proteinId: int = Depends(filters.proteinId),
) -> Paged[schema.Event]:
    """Get a list of events"""
    sessionId = None
    if session:
        blSession = get_blsession(session)
        if not blSession:
            raise HTTPException(status_code=404, detail="Session not found")
        sessionId = blSession.sessionId

    return crud.get_events(
        # sessionId is an int
        sessionId=sessionId,  # type: ignore
        dataCollectionGroupId=dataCollectionGroupId,
        blSampleId=blSampleId,
        proteinId=proteinId,
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

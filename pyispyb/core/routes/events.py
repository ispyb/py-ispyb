from fastapi import APIRouter, Depends, Query, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from pyispyb.app.extensions.database.session import get_session
from pyispyb.app.extensions.database.definitions import get_blsession
from ..database.utils import Paged
from ..dependencies import pagination
from ..modules import events as crud
from ..schemas import events as schema
from ..schemas.utils import paginated
from ispyb.app import filters

_router = APIRouter(prefix="/events", tags=["Events"])


@router.get(
    "/",
    response_model=paginated(schema.Event),
    responses={404: {"description": "Entity not found"}},
)
def get_events(
    db: Session = Depends(get_session),
    page: dict[str, int] = Depends(pagination),
    session: str = Depends(filters.session),
    dataCollectionGroupId: int = Depends(filters.dataCollectionGroupId),
    blSampleId: int = Depends(filters.blSampleId),
    proteinId: int = Depends(filters.proteinId),
) -> Paged[schema.Event]:
    """Get a list of events"""
    sessionId = None
    if session:
        blSession = get_blsession(db, session)
        if not blSession:
            raise HTTPException(status_code=404, detail="Session not found")
        sessionId = blSession.sessionId

    return crud.get_events(
        db,
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
    db: Session = Depends(get_session),
    imageId: int = Query(0, description="Image 1-4 to return"),
    fullSize: bool = Query(False, description="Get full size image"),
) -> str:
    """Get a data collection image"""
    path = crud.get_datacollection_snapshot_path(
        db, dataCollectionId, imageId, fullSize
    )
    if not path:
        raise HTTPException(status_code=404, detail="Image not found")

    return path

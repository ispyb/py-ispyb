from fastapi import Depends, Query, HTTPException
from fastapi.responses import FileResponse

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
    data_collection_group_id: int = Depends(filters.data_collection_group_id),
    bl_sample_id: int = Depends(filters.bl_sample_id),
    protein_id: int = Depends(filters.protein_id),
) -> Paged[schema.Event]:
    """Get a list of events"""
    session_id = None
    if session:
        bl_session = get_blsession(session)
        if not bl_session:
            raise HTTPException(status_code=404, detail="Session not found")
        session_id = bl_session.sessionId

    return crud.get_events(
        # sessionId is an int
        session_id=session_id,  # type: ignore
        data_collection_group_id=data_collection_group_id,
        bl_sample_id=bl_sample_id,
        protein_id=protein_id,
        **page
    )


@router.get("/image/{data_collection_id}", response_class=FileResponse)
def get_datacollection_image(
    data_collection_id: int,
    image_id: int = Query(0, description="Image 1-4 to return"),
    full_size: bool = Query(False, description="Get full size image"),
) -> str:
    """Get a data collection image"""
    path = crud.get_datacollection_snapshot_path(
        data_collection_id, image_id, full_size
    )
    if not path:
        raise HTTPException(status_code=404, detail="Image not found")

    return path

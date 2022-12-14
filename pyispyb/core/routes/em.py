import logging

from fastapi import Depends, HTTPException
from fastapi.responses import FileResponse

from ...dependencies import pagination
from ...app.extensions.database.utils import Paged
from ... import filters
from ...app.base import AuthenticatedAPIRouter

from ..modules import em as crud
from ..schemas import em as schema
from ..schemas.utils import paginated


logger = logging.getLogger(__name__)
router = AuthenticatedAPIRouter(prefix="/em", tags=["EM"])


@router.get("/snapshot/micrograph", response_class=FileResponse)
def get_micrograph_snapshot(movieId: int = Depends(filters.movieId)) -> str:
    """Get micrograph snapshot"""
    path = crud.get_micrograph_snapshot_path(movieId=movieId)

    if not path:
        raise HTTPException(status_code=404, detail="Image not found")

    return path


@router.get("/thumbnail/fft", response_class=FileResponse)
def get_fft_thumbnail(movieId: int = Depends(filters.movieId)) -> str:
    """Get FFT thumbnail"""
    path = crud.get_fft_thumbnail_path(movieId=movieId)

    if not path:
        raise HTTPException(status_code=404, detail="Image not found")

    return path


@router.get("/movies", response_model=paginated(schema.FullMovie))
def get_movies(
    dataCollectionId: int = Depends(filters.dataCollectionId),
    page: dict[str, int] = Depends(pagination),
) -> Paged[schema.FullMovie]:
    """Get movies for a data collection"""
    return crud.get_movies(dataCollectionId=dataCollectionId, **page)

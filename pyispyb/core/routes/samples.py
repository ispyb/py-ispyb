from fastapi import Depends, HTTPException

from pyispyb.dependencies import pagination
from pyispyb.app.extensions.database.utils import Paged
from pyispyb.core import models
from pyispyb import filters
from pyispyb.app.base import AuthenticatedAPIRouter

from ..modules import samples as crud
from ..schemas import samples as schema
from ..schemas.utils import paginated


router = AuthenticatedAPIRouter(prefix="/samples", tags=["Samples"])


@router.get("/", response_model=paginated(schema.Sample))
def get_samples(
    page: dict[str, int] = Depends(pagination),
    protein_id: int = Depends(filters.protein_id),
) -> Paged[models.BLSample]:
    """Get a list of samples"""
    return crud.get_samples(protein_id=protein_id, **page)


@router.get(
    "/{bl_sample_id}",
    response_model=schema.Sample,
    responses={404: {"description": "No such sample"}},
)
def get_sample(
    bl_sample_id: int = Depends(filters.bl_sample_id),
) -> models.BLSample:
    """Get a samples"""
    samples = crud.get_samples(bl_sample_id=bl_sample_id, skip=0, limit=1)

    try:
        return samples.first
    except IndexError:
        raise HTTPException(status_code=404, detail="Sample not found")

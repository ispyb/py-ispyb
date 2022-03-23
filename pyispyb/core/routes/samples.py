from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from pyispyb.app.extensions.database.session import get_session
from pyispyb.dependencies import pagination
from ..modules import samples as crud
from ..schemas import samples as schema
from ..schemas.utils import paginated
from pyispyb.app.extensions.database.utils import Paged
from pyispyb.core import models
from pyispyb import filters
from pyispyb.app.base import AuthenticatedAPIRouter

from pyispyb.app.extensions.auth.bearer import JWTBearer

router = AuthenticatedAPIRouter(prefix="/samples", tags=["Samples"])


@router.get("/", response_model=paginated(schema.Sample))
def get_samples(
    db: Session = Depends(get_session),
    page: dict[str, int] = Depends(pagination),
    proteinId: int = Depends(filters.proteinId),
) -> Paged[models.BLSample]:
    """Get a list of samples"""
    return crud.get_samples(db, proteinId=proteinId, **page)


@router.get(
    "/{blSampleId}",
    response_model=schema.Sample,
    responses={404: {"description": "No such sample"}},
)
def get_sample(
    db: Session = Depends(get_session),
    blSampleId: int = Depends(filters.blSampleId),
) -> models.BLSample:
    """Get a samples"""
    samples = crud.get_samples(db, blSampleId=blSampleId, skip=0, limit=1)

    try:
        return samples.first
    except IndexError:
        raise HTTPException(status_code=404, detail="Sample not found")

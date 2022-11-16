import logging

from fastapi import Depends
from ispyb import models

from ...dependencies import pagination
from ...app.extensions.database.utils import Paged
from ...app.base import AuthenticatedAPIRouter
from ... import filters

from ..modules import persons as crud
from ..schemas import persons as schema
from ..schemas.utils import paginated


logger = logging.getLogger(__name__)
router = AuthenticatedAPIRouter(prefix="/persons", tags=["People"])


@router.get("", response_model=paginated(schema.Person))
def get_persons(
    proposal: str = Depends(filters.proposal),
    sessionId: int = Depends(filters.sessionId),
    page: dict[str, int] = Depends(pagination),
) -> Paged[models.Person]:
    """Get a list of people"""
    return crud.get_persons(
        proposal=proposal, sessionId=sessionId, withAuthorization=True, **page
    )

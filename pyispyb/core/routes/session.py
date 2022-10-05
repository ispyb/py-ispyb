from pyispyb.app.base import AuthenticatedAPIRouter
from ispyb import models
import pyispyb.core.modules.session as crud

from pyispyb.core.schemas import session as schema

router = AuthenticatedAPIRouter(prefix="/session", tags=["Session"])


@router.get(
    "/{sessionId:int}",
    response_model=schema.SessionResponse,
    responses={404: {"description": "Entity not found"}},
)
def get_session(sessionId: int) -> list[models.BLSession]:
    return crud.get_session(sessionId)

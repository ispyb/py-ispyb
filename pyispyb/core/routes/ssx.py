from pyispyb.app.base import AuthenticatedAPIRouter
from pyispyb.core import models
import pyispyb.core.modules.ssx as crud

from ..schemas import ssx as schema

router = AuthenticatedAPIRouter(prefix="/ssx", tags=["Serial crystallography"])


@router.get(
    "/datacollection/{ssxDataCollectionId:int}",
    response_model=schema.SSXDataCollectionResponse,
    responses={404: {"description": "Entity not found"}},
)
def get_datacollection(ssxDataCollectionId: int) -> models.SSXDataCollection:
    return crud.get_ssx_datacollection(ssxDataCollectionId)

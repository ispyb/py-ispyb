from fastapi import Depends
from pyispyb.app.base import AuthenticatedAPIRouter
from pyispyb.app.extensions.database.utils import Paged
import pyispyb.core.modules.eventchains as crud
import pyispyb.core.schemas.eventchains as schema
from pyispyb.dependencies import pagination

router = AuthenticatedAPIRouter(prefix="/eventchains", tags=["Event chains"])


@router.get(
    "",
    response_model=Paged[schema.EventChainResponse],
)
def get_datacollection_eventchains(
    dataCollectionId: int,
    page: dict[str, int] = Depends(pagination),
) -> list[schema.EventChainResponse]:
    return crud.get_datacollection_eventchains(dataCollectionId, **page)

from pyispyb.app.base import AuthenticatedAPIRouter
import pyispyb.core.modules.eventchain as crud
import pyispyb.core.schemas.eventchain as schema

router = AuthenticatedAPIRouter(prefix="/eventchain", tags=["Event chains"])


@router.get(
    "",
    response_model=list[schema.EventChainResponse],
)
def get_ssx_datacollection_eventchains(
    dataCollectionId: int,
) -> list[schema.EventChainResponse]:
    return crud.get_ssx_datacollection_eventchains(dataCollectionId)

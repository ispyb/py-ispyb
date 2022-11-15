import json
from fastapi import HTTPException
from pydantic import constr
from pyispyb.app.base import AuthenticatedAPIRouter
import pyispyb.core.modules.ssx as crud
import pyispyb.core.schemas.ssx as schema

router = AuthenticatedAPIRouter(prefix="/ssx", tags=["Serial crystallography"])


IdList = constr(regex=r"^\d+(,\d+)*$")


@router.get(
    "/datacollection/processing/stats",
    response_model=list[schema.SSXDataCollectionProcessingStats],
)
async def get_ssx_datacollection_processing_stats(
    dataCollectionIds: IdList,
) -> list[schema.SSXDataCollectionProcessingStats]:
    result = await crud.get_ssx_datacollection_processing_stats(
        dataCollectionIds.split(",")
    )
    return result


@router.get(
    "/datacollection/processing/cells",
)
async def get_ssx_datacollection_processing_cells(
    dataCollectionId: int,
):
    result = crud.get_ssx_datacollection_processing_cells(dataCollectionId)
    if result is not None:
        res = json.loads(result)
        return res
    raise HTTPException(status_code=404, detail="Item not found")

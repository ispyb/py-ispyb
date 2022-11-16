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
    response_model=schema.SSXDataCollectionProcessingCells,
)
async def get_ssx_datacollection_processing_cells(
    dataCollectionId: int,
):
    result = await crud.get_ssx_datacollection_processing_cells(dataCollectionId)
    if result is not None:
        return result
    raise HTTPException(status_code=404, detail="Item not found")


@router.get(
    "/datacollection/processing/cells/histogram",
    response_model=schema.SSXDataCollectionProcessingCellsHistogram,
)
async def get_ssx_datacollection_processing_cells_histogram(
    dataCollectionIds: IdList,
):
    result = await crud.get_ssx_datacollection_processing_cells_histogram(
        dataCollectionIds.split(",")
    )
    return result

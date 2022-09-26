from fastapi import Depends, HTTPException, Request
from ispyb import models

from ...dependencies import order_by_factory, pagination
from ...app.extensions.database.utils import Paged
from ... import filters
from ...app.base import AuthenticatedAPIRouter

from ..modules import proteins as crud
from ..schemas import protein as schema
from ..schemas.utils import paginated


router = AuthenticatedAPIRouter(prefix="/proteins", tags=["Proteins"])


@router.get("", response_model=paginated(schema.Protein))
def get_proteins(
    request: Request,
    page: dict[str, int] = Depends(pagination),
    proteinId: int = Depends(filters.proteinId),
    proposal: str = Depends(filters.proposal),
    search: str = Depends(filters.search),
    sort_order: dict = Depends(order_by_factory(crud.ORDER_BY_MAP, "ProteinOrder")),
) -> Paged[models.BLSample]:
    """Get a list of proteins"""
    return crud.get_proteins(
        proteinId=proteinId,
        proposal=proposal,
        search=search,
        sort_order=sort_order,
        beamLineGroups=request.app.db_options.beamLineGroups,
        **page
    )


@router.get(
    "/{proteinId}",
    response_model=schema.Protein,
    responses={404: {"description": "No such protein"}},
)
def get_protein(
    request: Request,
    proteinId: int = Depends(filters.proteinId),
) -> models.Protein:
    """Get a protein"""
    proteins = crud.get_proteins(
        proteinId=proteinId,
        beamLineGroups=request.app.db_options.beamLineGroups,
        skip=0,
        limit=1,
    )

    try:
        return proteins.first
    except IndexError:
        raise HTTPException(status_code=404, detail="Protein not found")

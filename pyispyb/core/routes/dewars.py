import logging

from fastapi import Depends, HTTPException, status
from ispyb import models

from ...dependencies import pagination
from ...app.extensions.database.utils import Paged
from ...app.base import AuthenticatedAPIRouter
from ... import filters

from ..modules import dewars as crud
from ..schemas import dewars as schema
from ..schemas.utils import paginated, make_optional


logger = logging.getLogger(__name__)
router = AuthenticatedAPIRouter(prefix="/dewars", tags=["Dewars"])


@router.get("", response_model=paginated(schema.Dewar))
def get_dewars(
    shippingId: int = Depends(filters.shippingId),
    proposal: str = Depends(filters.proposal),
    page: dict[str, int] = Depends(pagination),
) -> Paged[models.Dewar]:
    """Get a list of dewars"""
    return crud.get_dewars(proposal=proposal, shippingId=shippingId, **page)


@router.get(
    "/{dewarId}",
    response_model=schema.Dewar,
    responses={404: {"description": "No such dewar"}},
)
def get_dewar(dewarId: int) -> models.Dewar:
    """Get a dewar"""
    dewar = crud.get_dewars(
        dewarId=dewarId,
        skip=0,
        limit=1,
    )
    try:
        return dewar.first
    except IndexError:
        raise HTTPException(status_code=404, detail="Dewar not found")


@router.post(
    "",
    response_model=schema.Dewar,
    status_code=status.HTTP_201_CREATED,
)
def create_dewar(dewar: schema.DewarCreate) -> models.Dewar:
    """Create a new dewar"""
    return crud.create_dewar(
        dewar=dewar,
    )


DEWAR_UPDATE_EXCLUDED = {"shippingId": True}


@router.patch(
    "/{dewarId}",
    response_model=schema.Dewar,
    responses={
        404: {"description": "No such dewar"},
        400: {"description": "Could not update dewar"},
    },
)
def update_dewar(
    dewarId: int,
    dewar: make_optional(
        schema.DewarCreate,
        exclude=DEWAR_UPDATE_EXCLUDED,
    ),
):
    """Update a Dewar"""
    try:
        return crud.update_dewar(dewarId, dewar)
    except IndexError:
        raise HTTPException(status_code=404, detail="Dewar not found")
    except Exception:
        logger.exception(f"Could not update dewar `{dewarId}` with payload `{dewar}`")
        raise HTTPException(status_code=400, detail="Could not update dewar")

import logging

from fastapi import Depends, HTTPException, status
from ispyb import models

from pyispyb.dependencies import pagination
from pyispyb.app.extensions.database.utils import Paged
from pyispyb.app.base import AuthenticatedAPIRouter
from pyispyb import filters

from ..modules import shipping as crud
from ..schemas import shipping as schema
from ..schemas.utils import paginated, make_optional


logger = logging.getLogger(__name__)
router = AuthenticatedAPIRouter(prefix="/shippings", tags=["Shipping"])


@router.get("", response_model=paginated(schema.Shipping))
def get_shippings(
    proposal: str = Depends(filters.proposal),
    page: dict[str, int] = Depends(pagination),
) -> Paged[models.Shipping]:
    """Get a list of shipments"""
    return crud.get_shippings(proposal=proposal, **page)


@router.get(
    "/{shippingId}",
    response_model=schema.Shipping,
    responses={404: {"description": "No such shipment"}},
)
def get_shipping(shippingId: int) -> models.Shipping:
    """Get a shipment"""
    shipping = crud.get_shippings(
        shippingId=shippingId,
        skip=0,
        limit=1,
    )
    try:
        return shipping.first
    except IndexError:
        raise HTTPException(status_code=404, detail="Shipment not found")


@router.post(
    "",
    response_model=schema.Shipping,
    status_code=status.HTTP_201_CREATED,
)
def create_shipping(shipping: schema.ShippingCreate) -> models.Shipping:
    """Create a new shipment"""
    return crud.create_shipping(
        shipping=shipping,
    )


SHIPPING_UPDATE_EXCLUDED = {}


@router.patch(
    "/{shippingId}",
    response_model=schema.Shipping,
    responses={
        404: {"description": "No such shipment"},
        400: {"description": "Could not update shipment"},
    },
)
def update_shipping(
    shippingId: int,
    shipping: make_optional(
        schema.ShippingCreate,
        exclude=SHIPPING_UPDATE_EXCLUDED,
    ),
):
    """Update a Shipment"""
    try:
        return crud.update_shipping(shippingId, shipping)
    except IndexError:
        raise HTTPException(status_code=404, detail="Shipment not found")
    except Exception:
        logger.exception(
            f"Could not update shipping `{shippingId}` with payload `{shipping}`"
        )
        raise HTTPException(status_code=400, detail="Could not update shipment")

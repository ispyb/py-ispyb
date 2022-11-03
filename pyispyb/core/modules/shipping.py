from datetime import datetime
from typing import Optional

from sqlalchemy import distinct, func
from sqlalchemy.orm import joinedload
from ispyb import models

from ...app.extensions.database.definitions import with_authorization
from ...app.extensions.database.utils import Paged, page, update_model, with_metadata
from ...app.extensions.database.middleware import db
from ..schemas import shipping as schema


def get_shippings(
    skip: int,
    limit: int,
    shippingId: Optional[int] = None,
    proposal: str = None,
    proposalId: Optional[int] = None,
    withAuthorization: bool = True,
) -> Paged[models.Shipping]:
    metadata = {"dewars": func.count(distinct(models.Dewar.dewarId))}

    query = (
        db.session.query(models.Shipping, *metadata.values())
        .options(joinedload(models.Shipping.LabContact))
        .options(joinedload(models.Shipping.LabContact1))
        .join(models.Proposal, models.Proposal.proposalId == models.Shipping.proposalId)
        .outerjoin(models.Dewar)
        .group_by(models.Shipping.shippingId)
    )

    if shippingId:
        query = query.filter(models.Shipping.shippingId == shippingId)

    if proposal:
        query = query.filter(models.Proposal.proposal == proposal)

    if proposalId:
        query = query.filter(models.Proposal.proposalId == proposalId)

    if withAuthorization:
        query = with_authorization(query)

    total = query.count()
    query = page(query, skip=skip, limit=limit)
    results = with_metadata(query.all(), list(metadata.keys()))

    return Paged(total=total, results=results, skip=skip, limit=limit)


def create_shipping(shipping: schema.ShippingCreate) -> models.Shipping:
    shipping_dict = shipping.dict()
    shipping_dict["safetyLevel"] = shipping.safetyLevel.value
    shipping_dict["bltimeStamp"] = datetime.now()

    shipping = models.Shipping(**shipping_dict)
    db.session.add(shipping)
    db.session.commit()

    new_shipping = get_shippings(shippingId=shipping.shippingId, skip=0, limit=1)
    return new_shipping.first


def update_shipping(
    shippingId: int, shipping: schema.ShippingCreate
) -> models.Shipping:
    shipping_dict = shipping.dict(exclude_unset=True)
    new_shipping = get_shippings(shippingId=shippingId, skip=0, limit=1).first

    update_model(new_shipping, shipping_dict)
    db.session.commit()

    return get_shippings(shippingId=shippingId, skip=0, limit=1).first

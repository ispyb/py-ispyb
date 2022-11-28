from typing import Optional

from sqlalchemy import distinct, func
from sqlalchemy.orm import joinedload
from ispyb import models

from ...app.extensions.database.definitions import with_authorization
from ...app.extensions.database.utils import Paged, page, update_model, with_metadata
from ...app.extensions.database.middleware import db
from ..schemas import dewars as schema


def get_dewars(
    skip: int,
    limit: int,
    dewarId: Optional[int] = None,
    shippingId: Optional[int] = None,
    proposal: str = None,
    proposalId: Optional[int] = None,
    withAuthorization: bool = True,
) -> Paged[models.Dewar]:
    metadata = {"containers": func.count(distinct(models.Container.containerId))}

    query = (
        db.session.query(models.Dewar, *metadata.values())
        .join(models.Dewar.Shipping)
        .options(joinedload(models.Dewar.Shipping))
        .join(models.Proposal, models.Proposal.proposalId == models.Shipping.proposalId)
        .outerjoin(models.Container)
        .group_by(models.Dewar.dewarId)
        .order_by(models.Dewar.dewarId)
    )

    if dewarId:
        query = query.filter(models.Dewar.dewarId == dewarId)

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


def create_dewar(dewar: schema.DewarCreate) -> models.Dewar:
    dewar_dict = dewar.dict()
    dewar = models.Dewar(**dewar_dict)
    db.session.add(dewar)
    db.session.commit()

    new_dewar = get_dewars(dewarId=dewar.dewarId, skip=0, limit=1)
    return new_dewar.first


def update_dewar(dewarId: int, dewar: schema.DewarCreate) -> models.Dewar:
    dewar_dict = dewar.dict(exclude_unset=True)
    new_dewar = get_dewars(dewarId=dewarId, skip=0, limit=1).first

    update_model(new_dewar, dewar_dict)
    db.session.commit()

    return get_dewars(dewarId=dewarId, skip=0, limit=1).first

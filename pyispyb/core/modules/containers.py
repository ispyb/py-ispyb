from typing import Optional

from sqlalchemy import distinct, func
from sqlalchemy.orm import joinedload
from ispyb import models

from ...app.extensions.database.definitions import with_authorization
from ...app.extensions.database.utils import Paged, page, update_model, with_metadata
from ...app.extensions.database.middleware import db
from ..schemas import containers as schema


def get_containers(
    skip: int,
    limit: int,
    proteinId: Optional[int] = None,
    containerId: Optional[int] = None,
    dewarId: Optional[int] = None,
    proposal: str = None,
    proposalId: Optional[int] = None,
    withAuthorization: bool = True,
) -> Paged[models.Container]:
    metadata = {"samples": func.count(distinct(models.BLSample.blSampleId))}

    query = (
        db.session.query(models.Container, *metadata.values())
        .join(models.Dewar)
        .options(joinedload(models.Container.Dewar))
        .join(models.Shipping)
        .join(models.BLSample)
        .join(models.Crystal)
        .join(models.Proposal, models.Proposal.proposalId == models.Shipping.proposalId)
        .group_by(models.Container.containerId)
    )

    if containerId:
        query = query.filter(models.Continer.containerId == containerId)

    if dewarId:
        query = query.filter(models.Continer.dewarId == dewarId)

    if proteinId:
        query = query.filter(models.Crystal.proteinId == proteinId)

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


def create_container(container: schema.ContainerCreate) -> models.Container:
    container_dict = container.dict()
    container = models.Container(**container_dict)
    db.session.add(container)
    db.session.commit()

    new_container = get_containers(containerId=container.containerId, skip=0, limit=1)
    return new_container.first


def update_container(
    containerId: int, container: schema.ContainerCreate
) -> models.Container:
    container_dict = container.dict(exclude_unset=True)
    new_container = get_containers(containerId=containerId, skip=0, limit=1).first

    update_model(new_container, container_dict)
    db.session.commit()

    return get_containers(containerId=containerId, skip=0, limit=1).first

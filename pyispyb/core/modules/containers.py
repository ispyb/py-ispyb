import enum
from typing import Optional

from sqlalchemy import distinct, func, and_
from sqlalchemy.orm import joinedload
from ispyb import models

from ...app.extensions.database.definitions import with_authorization
from ...app.extensions.database.utils import (
    Paged,
    page,
    update_model,
    with_metadata,
    order,
)
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
        query = query.filter(models.Container.containerId == containerId)

    if dewarId:
        query = query.filter(models.Container.dewarId == dewarId)

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


def get_queued_containers(
    skip: int,
    limit: int,
    proposal: Optional[str] = None,
    beamLineName: Optional[str] = None,
    containerId: Optional[int] = None,
    containerQueueId: Optional[int] = None,
) -> Paged[models.ContainerQueue]:
    metadata = {
        "samples": func.count(
            distinct(models.ContainerQueueSample.containerQueueSampleId)
        )
    }
    query = (
        db.session.query(models.ContainerQueue, *metadata.values())
        .select_from(models.ContainerQueue)
        .join(models.ContainerQueueSample)
        .join(models.Container)
        .options(joinedload(models.ContainerQueue.Container))
        .join(models.Dewar)
        .options(joinedload(models.ContainerQueue.Container, models.Container.Dewar))
        .join(models.Shipping)
        .options(
            joinedload(
                models.ContainerQueue.Container,
                models.Container.Dewar,
                models.Dewar.Shipping,
            )
        )
        .join(models.Proposal, models.Proposal.proposalId == models.Shipping.proposalId)
        .group_by(models.ContainerQueue.containerQueueId)
    )

    if containerQueueId:
        query = query.filter(models.ContainerQueue.containerQueueId == containerQueueId)

    if proposal:
        query = query.filter(models.Proposal.proposal == proposal)

    if beamLineName:
        query = query.filter(models.Container.beamlineLocation == beamLineName)

    if containerId:
        query = query.filter(models.Container.containerId == containerId)

    query = with_authorization(query, proposal)
    total = query.count()
    query = page(query, skip=skip, limit=limit)
    results = with_metadata(query.all(), list(metadata.keys()))

    return Paged(total=total, results=results, skip=skip, limit=limit)


def update_queued_container(
    containerQueueId: int, containerQueue: schema.ContainerQueueUpdate
) -> models.ContainerQueue:
    new_container_queue = get_queued_containers(
        containerQueueId=containerQueueId, skip=0, limit=1
    ).first

    if containerQueue.completed:
        new_container_queue.completedTimeStamp = func.now()
    db.session.commit()

    return get_queued_containers(
        containerQueueId=containerQueueId, skip=0, limit=1
    ).first


QUEUED_SAMPLE_STATUS_FILTERS = {
    "Queued": func.count(distinct(models.DataCollection.dataCollectionId)) == 0,
    "Completed": func.count(distinct(models.DataCollection.dataCollectionId)) > 0,
    "Failed": func.sum(
        func.IF(
            and_(
                models.DataCollection.runStatus.notlike("%success%"),
                models.DataCollection.runStatus != None,  # noqa
            ),
            1,
            0,
        )
    )
    > 0,
}

QUEUED_SAMPLE_STATUS_ENUM = enum.Enum(
    "QueuedSampleStatus", {k: k for k in QUEUED_SAMPLE_STATUS_FILTERS.keys()}
)

QUEUED_SAMPLE_ORDER_BY_MAP = {
    "containerQueueSampleId": models.ContainerQueueSample.containerQueueSampleId,
    "started": func.min(models.DataCollection.startTime),
    "finished": func.max(models.DataCollection.endTime),
}


def get_queued_samples(
    skip: int,
    limit: int,
    proposal: Optional[str] = None,
    blSampleId: Optional[int] = None,
    beamLineName: Optional[str] = None,
    containerId: Optional[int] = None,
    containerQueueSampleId: Optional[int] = None,
    status: Optional[QUEUED_SAMPLE_STATUS_ENUM] = None,
    sort_order: Optional[dict[str, str]] = None,
) -> Paged[models.ContainerQueueSample]:
    metadata = {
        "datacollections": func.group_concat(
            distinct(
                func.concat(
                    models.DataCollection.dataCollectionId,
                    ":",
                    models.DataCollection.runStatus,
                )
            )
        ),
        "dataCollectionGroupId": models.DataCollectionGroup.dataCollectionGroupId,
        "sessionId": models.DataCollectionGroup.sessionId,
        "proposal": models.Proposal.proposal,
        "started": func.min(models.DataCollection.startTime),
        "finished": func.max(models.DataCollection.endTime),
        "types": func.group_concat(distinct(models.DataCollectionGroup.experimentType)),
    }

    query = (
        db.session.query(models.ContainerQueueSample, *metadata.values())
        .select_from(models.ContainerQueueSample)
        .join(models.DiffractionPlan)
        .options(
            joinedload(
                models.ContainerQueueSample.DiffractionPlan,
            )
        )
        .outerjoin(
            models.BLSubSample,
            models.BLSubSample.blSubSampleId
            == models.ContainerQueueSample.blSubSampleId,
        )
        .options(
            joinedload(
                models.ContainerQueueSample.BLSubSample,
            )
        )
        .options(
            joinedload(
                models.ContainerQueueSample.BLSample,
            )
        )
        .outerjoin(
            models.BLSample,
            models.BLSample.blSampleId == models.BLSubSample.blSampleId,
        )
        .options(
            joinedload(
                models.ContainerQueueSample.BLSubSample,
                models.BLSubSample.BLSample,
            )
        )
        .outerjoin(
            models.DataCollection,
            models.DataCollection.dataCollectionPlanId
            == models.ContainerQueueSample.dataCollectionPlanId,
        )
        .outerjoin(models.DataCollectionGroup)
        .join(models.ContainerQueue)
        .join(models.Container)
        .join(models.Dewar)
        .join(models.Shipping)
        .join(models.Proposal, models.Proposal.proposalId == models.Shipping.proposalId)
        .group_by(models.ContainerQueueSample.containerQueueSampleId)
    )

    if containerQueueSampleId:
        query = query.filter(
            models.ContainerQueueSample.containerQueueSampleId == containerQueueSampleId
        )

    if proposal:
        query = query.filter(models.Proposal.proposal == proposal)

    if beamLineName:
        query = query.filter(models.Container.beamlineLocation == beamLineName)

    if containerId:
        query = query.filter(models.Container.containerId == containerId)

    if blSampleId:
        query = query.filter(models.BLSample.blSampleId == blSampleId)

    if status:
        query = query.having(QUEUED_SAMPLE_STATUS_FILTERS[status.value])

    if sort_order:
        query = order(
            query,
            QUEUED_SAMPLE_ORDER_BY_MAP,
            sort_order,
            default={"order_by": "containerQueueSampleId", "order": "desc"},
        )

    query = with_authorization(query)
    total = query.count()
    query = page(query, skip=skip, limit=limit)
    results = with_metadata(query.all(), list(metadata.keys()))
    dc_keys = ["dataCollectionId", "runStatus"]

    for result in results:
        if result._metadata["types"]:
            result._metadata["types"] = result._metadata["types"].split(",")
        else:
            result._metadata["types"] = []

        if result._metadata["datacollections"]:
            result._metadata["datacollections"] = [
                {dc_keys[i]: value for i, value in enumerate(dc.split(":"))}
                for dc in result._metadata["datacollections"].split(",")
            ]
        else:
            result._metadata["datacollections"] = []

    return Paged(total=total, results=results, skip=skip, limit=limit)


def delete_queued_sample(containerQueueSampleId: int) -> None:
    queued_sample = get_queued_samples(
        containerQueueSampleId=containerQueueSampleId, skip=0, limit=1
    ).first

    if len(queued_sample._metadata["datacollections"]) > 0:
        raise RuntimeError(
            "Queued sample has related data collections so cannot be removed"
        )

    if queued_sample.DiffractionPlan:
        db.session.delete(queued_sample.DiffractionPlan)

    db.session.delete(queued_sample)
    db.session.commit()

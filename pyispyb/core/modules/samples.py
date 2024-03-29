import enum
from typing import Optional

from sqlalchemy.orm import contains_eager, aliased, joinedload
from sqlalchemy.sql.expression import func, distinct, and_, literal_column
from ispyb import models

from ...config import settings
from ...app.extensions.database.definitions import with_authorization
from ...app.extensions.database.middleware import db
from ...app.extensions.database.utils import (
    Paged,
    page,
    with_metadata,
    order,
    update_model,
)

from ..schemas import samples as schema


SAMPLE_ORDER_BY_MAP = {
    "blSampleId": models.BLSample.blSampleId,
    "name": models.BLSample.name,
    "location": models.BLSample.location,
    "datacollections": func.count(distinct(models.DataCollection.dataCollectionId)),
}


SAMPLE_STATUS_FILTERS = {
    "Sample Action": func.count(models.RobotAction.robotActionId),
    "Data Collected": func.count(models.DataCollection.dataCollectionId),
    "Strategy": func.count(models.Screening.screeningId),
    "Auto Integrated": func.count(models.AutoProcIntegration.autoProcIntegrationId),
}

if hasattr(models, "ProcessingJob"):
    SAMPLE_STATUS_FILTERS["Processed"] = func.count(
        models.ProcessingJob.processingJobId
    )

SAMPLE_STATUS_ENUM = enum.Enum(
    "SampleStatus", {k: k for k in SAMPLE_STATUS_FILTERS.keys()}
)


def get_samples(
    skip: int,
    limit: int,
    search: Optional[str] = None,
    blSampleId: Optional[int] = None,
    proteinId: Optional[int] = None,
    proposal: Optional[str] = None,
    containerId: Optional[int] = None,
    beamLineName: Optional[str] = None,
    sort_order: Optional[dict[str, str]] = None,
    status: Optional[SAMPLE_STATUS_ENUM] = None,
) -> Paged[models.BLSample]:
    metadata = {
        "subsamples": func.count(distinct(models.BLSubSample.blSubSampleId)),
        "datacollections": func.count(distinct(models.DataCollection.dataCollectionId)),
        "types": func.group_concat(distinct(models.DataCollectionGroup.experimentType)),
        "strategies": func.count(distinct(models.ScreeningOutput.screeningOutputId)),
        "autoIntegrations": func.count(
            distinct(models.AutoProcIntegration.autoProcIntegrationId)
        ),
        "integratedResolution": func.min(
            models.AutoProcScalingStatistics.resolutionLimitHigh
        ),
        "proposal": models.Proposal.proposal,
    }

    query = (
        db.session.query(models.BLSample, *metadata.values())
        .join(models.BLSample.Crystal)
        .options(
            contains_eager(models.BLSample.Crystal).load_only(
                models.Crystal.cell_a,
                models.Crystal.cell_b,
                models.Crystal.cell_c,
                models.Crystal.cell_alpha,
                models.Crystal.cell_beta,
                models.Crystal.cell_gamma,
            )
        )
        .join(models.Crystal.Protein)
        .options(
            contains_eager(models.BLSample.Crystal, models.Crystal.Protein).load_only(
                "name", "acronym"
            ),
        )
        .outerjoin(
            models.BLSubSample,
            models.BLSubSample.blSampleId == models.BLSample.blSampleId,
        )
        .outerjoin(
            models.DataCollectionGroup,
            models.DataCollectionGroup.blSampleId == models.BLSample.blSampleId,
        )
        .outerjoin(
            models.DataCollection,
            models.DataCollectionGroup.dataCollectionGroupId
            == models.DataCollection.dataCollectionGroupId,
        )
        .outerjoin(models.Screening)
        .outerjoin(
            models.ScreeningOutput,
            and_(
                models.Screening.screeningId == models.ScreeningOutput.screeningId,
                models.ScreeningOutput.strategySuccess == 1,
            ),
        )
        .outerjoin(models.AutoProcIntegration)
        .outerjoin(models.AutoProcScalingHasInt)
        .outerjoin(
            models.AutoProcScalingStatistics,
            models.AutoProcScalingHasInt.autoProcScalingId
            == models.AutoProcScalingStatistics.autoProcScalingId,
        )
        .join(
            models.Container,
            models.BLSample.containerId == models.Container.containerId,
        )
        .options(
            contains_eager(models.BLSample.Container).load_only(
                models.Container.code,
            )
        )
        .join(models.Dewar, models.Container.dewarId == models.Dewar.dewarId)
        .options(
            contains_eager(
                models.BLSample.Container,
                models.Container.Dewar,
            ).load_only(
                models.Dewar.code,
            )
        )
        .join(models.Shipping, models.Dewar.shippingId == models.Shipping.shippingId)
        .options(
            contains_eager(
                models.BLSample.Container, models.Container.Dewar, models.Dewar.Shipping
            ).load_only(
                models.Shipping.shippingName,
            )
        )
        .join(models.Proposal, models.Proposal.proposalId == models.Shipping.proposalId)
        .group_by(models.BLSample.blSampleId)
    )

    if hasattr(models.ContainerQueueSample, "dataCollectionPlanId") and hasattr(
        models.ContainerQueueSample, "blSampleId"
    ):
        query = query.outerjoin(
            models.ContainerQueueSample,
            models.BLSample.blSampleId == models.ContainerQueueSample.blSampleId,
        )
        DataCollectionQueued: models.DataCollection = aliased(models.DataCollection)
        query = query.outerjoin(
            DataCollectionQueued,
            models.ContainerQueueSample.dataCollectionPlanId
            == DataCollectionQueued.dataCollectionPlanId,
        )
        metadata["queued"] = func.IF(
            func.count(models.ContainerQueueSample.containerQueueSampleId)
            > func.count(DataCollectionQueued.dataCollectionId),
            True,
            False,
        )

        query = query.add_columns(metadata["queued"])
    else:
        metadata["queued"] = literal_column("0")
        query = query.add_columns(metadata["queued"])

    if search:
        query = query.filter(
            models.BLSample.name.like(f"%{search}%"),
        )

    query = with_authorization(query)

    if blSampleId:
        query = query.filter(models.BLSample.blSampleId == blSampleId)

    if proteinId:
        query = query.filter(models.Protein.proteinId == proteinId)

    if containerId:
        query = query.filter(models.Container.containerId == containerId)

    if proposal:
        proposal_row = (
            db.session.query(models.Proposal)
            .filter(models.Proposal.proposal == proposal)
            .first()
        )
        if proposal_row:
            query = query.filter(models.Proposal.proposalId == proposal_row.proposalId)

    if beamLineName:
        query = query.filter(
            and_(
                models.Dewar.dewarStatus == "processing",
                models.Container.beamlineLocation == beamLineName,
                models.Container.sampleChangerLocation != "",
            )
        )

    if status:
        if hasattr(models, "ProcessingJob"):
            if status == SAMPLE_STATUS_ENUM.Processed:
                query = query.join(models.ProcessingJob)

        if status.value == "Sample Action":
            query = query.join(
                models.RobotAction,
                models.RobotAction.blsampleId == models.BLSample.blSampleId,
            )

        query = query.having(SAMPLE_STATUS_FILTERS[status.value] > 0)

    if sort_order:
        query = order(
            query,
            SAMPLE_ORDER_BY_MAP,
            sort_order,
            {"order_by": "blSampleId", "order": "desc"},
        )

    total = query.count()
    query = page(query, skip=skip, limit=limit)
    results = with_metadata(query.all(), list(metadata.keys()))

    for result in results:
        if result._metadata["types"]:
            result._metadata["types"] = result._metadata["types"].split(",")

    return Paged(total=total, results=results, skip=skip, limit=limit)


def create_sample(sample: schema.SampleCreate) -> models.BLSample:
    sample_dict = sample.dict()
    sample = models.BLSample(**sample_dict)
    db.session.add(sample)
    db.session.commit()

    new_sample = get_samples(sampleId=sample.sampleId, skip=0, limit=1)
    return new_sample.first


def update_sample(sampleId: int, sample: schema.SampleCreate) -> models.BLSample:
    sample_dict = sample.dict(exclude_unset=True)
    new_sample = get_samples(sampleId=sampleId, skip=0, limit=1).first

    update_model(new_sample, sample_dict)
    db.session.commit()

    return get_samples(sampleId=sampleId, skip=0, limit=1).first


SUBSAMPLE_ORDER_BY_MAP = {
    "blSubSampleId": models.BLSubSample.blSubSampleId,
    "datacollections": func.count(distinct(models.DataCollection.dataCollectionId)),
}

if hasattr(models.BLSubSample, "type"):
    SUBSAMPLE_ORDER_BY_MAP["type"] = models.BLSubSample.type


def get_subsamples(
    skip: int,
    limit: int,
    blSubSampleId: Optional[int] = None,
    blSampleId: Optional[int] = None,
    proteinId: Optional[int] = None,
    proposal: Optional[str] = None,
    containerId: Optional[int] = None,
    sort_order: Optional[dict[str, str]] = None,
) -> Paged[models.BLSubSample]:
    metadata = {
        "datacollections": func.count(distinct(models.DataCollection.dataCollectionId)),
        "types": func.group_concat(distinct(models.DataCollectionGroup.experimentType)),
    }

    query = (
        db.session.query(models.BLSubSample, *metadata.values())
        .join(models.BLSubSample.BLSample)
        .join(models.BLSample.Crystal)
        .options(
            contains_eager(models.BLSubSample.BLSample).load_only(
                models.BLSample.name,
            )
        )
        .join(models.Crystal.Protein)
        .options(
            contains_eager(
                models.BLSubSample.BLSample,
                models.BLSample.Crystal,
                models.Crystal.Protein,
            ).load_only("name", "acronym"),
        )
        .outerjoin(
            models.DataCollection,
            models.DataCollection.blSubSampleId == models.BLSubSample.blSubSampleId,
        )
        .outerjoin(
            models.DataCollectionGroup,
            models.DataCollectionGroup.dataCollectionGroupId
            == models.DataCollection.dataCollectionGroupId,
        )
        .options(
            joinedload(models.BLSubSample.Position1).load_only(
                models.Position.posX,
                models.Position.posY,
            )
        )
        .options(
            joinedload(models.BLSubSample.Position2).load_only(
                models.Position.posX,
                models.Position.posY,
            )
        )
        .join(
            models.Container,
            models.BLSample.containerId == models.Container.containerId,
        )
        .join(models.Dewar, models.Container.dewarId == models.Dewar.dewarId)
        .join(models.Shipping, models.Dewar.shippingId == models.Shipping.shippingId)
        .join(models.Proposal, models.Proposal.proposalId == models.Protein.proposalId)
        .group_by(models.BLSubSample.blSubSampleId)
    )

    if hasattr(models.ContainerQueueSample, "dataCollectionPlanId"):
        query = query.outerjoin(
            models.ContainerQueueSample,
            models.BLSubSample.blSubSampleId
            == models.ContainerQueueSample.blSubSampleId,
        )
        DataCollectionQueued: models.DataCollection = aliased(models.DataCollection)
        query = query.outerjoin(
            DataCollectionQueued,
            models.ContainerQueueSample.dataCollectionPlanId
            == DataCollectionQueued.dataCollectionPlanId,
        )
        metadata["queued"] = func.IF(
            func.count(models.ContainerQueueSample.containerQueueSampleId)
            > func.count(DataCollectionQueued.dataCollectionId),
            True,
            False,
        )
        query = query.add_columns(metadata["queued"])
    else:
        metadata["queued"] = literal_column("0")
        query = query.add_columns(metadata["queued"])

    query = with_authorization(query)

    if blSubSampleId:
        query = query.filter(models.BLSubSample.blSubSampleId == blSubSampleId)

    if blSampleId:
        query = query.filter(models.BLSample.blSampleId == blSampleId)

    if proteinId:
        query = query.filter(models.Protein.proteinId == proteinId)

    if containerId:
        query = query.filter(models.Container.containerId == containerId)

    if proposal:
        query = query.filter(models.Proposal.proposal == proposal)

    query = order(query, SUBSAMPLE_ORDER_BY_MAP, sort_order)

    total = query.count()
    query = page(query, skip=skip, limit=limit)
    results = with_metadata(query.all(), list(metadata.keys()))

    for result in results:
        if result._metadata["types"]:
            result._metadata["types"] = result._metadata["types"].split(",")
        else:
            result._metadata["types"] = []

    return Paged(total=total, results=results, skip=skip, limit=limit)


def get_sample_images(
    skip: int,
    limit: int,
    blSampleId: Optional[int] = None,
    blSampleImageId: Optional[int] = None,
) -> Paged[models.BLSampleImage]:
    metadata = {
        "url": func.concat(
            f"{settings.api_root}/samples/images/",
            models.BLSampleImage.blSampleImageId,
        )
    }

    query = (
        db.session.query(models.BLSampleImage, *metadata.values())
        .join(models.BLSample)
        .join(
            models.Container,
            models.BLSample.containerId == models.Container.containerId,
        )
        .join(models.Dewar, models.Container.dewarId == models.Dewar.dewarId)
        .join(models.Shipping, models.Dewar.shippingId == models.Shipping.shippingId)
    )

    if blSampleId:
        query = query.filter(models.BLSample.blSampleId == blSampleId)

    if blSampleImageId:
        query = query.filter(models.BLSampleImage.blSampleImageId == blSampleImageId)

    query = with_authorization(query, proposalColumn=models.Shipping.proposalId)

    total = query.count()
    query = page(query, skip=skip, limit=limit)
    results = with_metadata(query.all(), list(metadata.keys()))

    return Paged(total=total, results=results, skip=skip, limit=limit)

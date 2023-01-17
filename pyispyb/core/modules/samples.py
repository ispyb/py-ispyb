import enum
from typing import Optional
from fastapi import HTTPException

from sqlalchemy.orm import contains_eager, aliased, joinedload
from sqlalchemy.sql.expression import func, distinct, and_, literal_column
from ispyb import models

from ...config import settings
from ...app.extensions.database.definitions import (
    authorize_for_proposal,
    with_authorization,
)
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
        .outerjoin(
            models.Container,
            models.BLSample.containerId == models.Container.containerId,
        )
        .options(
            contains_eager(models.BLSample.Container).load_only(
                models.Container.code,
            )
        )
        .outerjoin(models.Dewar, models.Container.dewarId == models.Dewar.dewarId)
        .options(
            contains_eager(
                models.BLSample.Container,
                models.Container.Dewar,
            ).load_only(
                models.Dewar.code,
            )
        )
        .outerjoin(
            models.Shipping, models.Dewar.shippingId == models.Shipping.shippingId
        )
        .options(
            contains_eager(
                models.BLSample.Container, models.Container.Dewar, models.Dewar.Shipping
            ).load_only(
                models.Shipping.shippingName,
            )
        )
        .join(models.Proposal, models.Proposal.proposalId == models.Protein.proposalId)
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


def build_compositions(
    composition_model,
    compositions: list[schema.CompositionCreate | schema.Composition | None] | None,
    proposal: models.Proposal,
):
    res = []
    if compositions is None:
        return res
    for c in compositions:
        if c is not None:
            component: models.Component = None
            # Try to find component in DB
            if isinstance(c.Component, schema.Component):
                component = (
                    db.session.query(models.Component)
                    .filter(models.Component.componentId == c.Component.componentId)
                    .first()
                )
            # If c.Component is ComponentCreate, try to find same component to avoid duplicate
            else:
                # Try to find component type in DB
                component_type: models.ComponentType = (
                    db.session.query(models.ComponentType)
                    .filter(models.ComponentType.name == c.Component.ComponentType.name)
                    .first()
                )
                # If component_type found, try to find component
                if component_type is not None:
                    component = (
                        db.session.query(models.Component)
                        .filter(models.Component.name == c.Component.name)
                        .filter(models.Component.ComponentType == component_type)
                        .filter(models.Component.Proposal == proposal)
                        .first()
                    )
                # If no component type found, create
                else:
                    component_type = models.ComponentType(
                        **c.Component.ComponentType.dict()
                    )

                # If no component found, create
                if component is None:
                    component = models.Component(
                        **{
                            **c.Component.dict(),
                            "ComponentType": component_type,
                            "Proposal": proposal,
                            "componentId": None,
                        }
                    )

            # find concentration type in DB
            concentration_type = None
            if c.ConcentrationType is not None:
                concentration_type = (
                    db.session.query(models.ConcentrationType)
                    .filter(
                        models.ConcentrationType.concentrationTypeId
                        == c.ConcentrationType.concentrationTypeId
                    )
                    .first()
                )

            # create final composition object
            composition = composition_model(
                **{
                    **c.dict(),
                    "Component": component,
                    "ConcentrationType": concentration_type,
                }
            )
            res.append(composition)
    return res


def build_crystal(sample: schema.SampleCreate | schema.SampleUpdate) -> models.Crystal:
    crystal: models.Crystal = None
    if isinstance(sample.Crystal, schema.SampleCrystalUpdate):
        crystal = (
            db.session.query(models.Crystal)
            .filter(models.Crystal.crystalId == sample.Crystal.crystalId)
            .first()
        )
        update_model(crystal, sample.Crystal.dict(exclude_unset=True), nested=False)
    else:
        # Create new crystal
        protein = (
            db.session.query(models.Protein)
            .filter(models.Protein.proteinId == sample.Crystal.Protein.proteinId)
            .first()
        )
        crystal = models.Crystal(
            **{**sample.Crystal.dict(), "Protein": protein, "crystal_compositions": []}
        )

    proposal = crystal.Protein.Proposal

    crystal.crystal_compositions = build_compositions(
        models.CrystalComposition, sample.Crystal.crystal_compositions, proposal
    )

    return crystal


def create_sample(sample: schema.SampleCreate) -> models.BLSample:
    sample_dict = sample.dict()
    crystal = build_crystal(sample)

    proposal = crystal.Protein.Proposal

    authorize_for_proposal(proposal.proposalId)

    sample_compositions = build_compositions(
        models.SampleComposition, sample.sample_compositions, proposal
    )

    new_sample = models.BLSample(
        **{
            **sample_dict,
            "Crystal": crystal,
            "sample_compositions": sample_compositions,
        }
    )

    db.session.add(new_sample)
    db.session.commit()

    new_sample = get_samples(blSampleId=new_sample.blSampleId, skip=0, limit=1)
    return new_sample.first


def update_sample(blSampleId: int, sample: schema.SampleUpdate) -> models.BLSample:
    sample_dict = sample.dict(exclude_unset=True)
    old_sample = get_samples(blSampleId=blSampleId, skip=0, limit=1).first
    update_model(old_sample, sample_dict, nested=False)

    crystal = build_crystal(sample)
    old_sample.Crystal = crystal

    proposal = crystal.Protein.Proposal
    authorize_for_proposal(proposal.proposalId)

    old_sample.sample_compositions = build_compositions(
        models.SampleComposition, sample.sample_compositions, proposal
    )

    db.session.commit()

    return get_samples(blSampleId=sample.blSampleId, skip=0, limit=1).first


def delete_sample(
    blSampleId: int,
) -> None:
    sample = get_samples(blSampleId=blSampleId, skip=0, limit=1).first
    if sample._metadata["datacollections"] > 0:
        raise HTTPException(
            status_code=409,
            detail="Sample cannot be deleted because it is associated with data collections",
        )

    if sample._metadata["subsamples"] > 0:
        raise HTTPException(
            status_code=409,
            detail="Sample cannot be deleted because it is associated with sub samples",
        )

    if sample._metadata["autoIntegrations"] > 0:
        raise HTTPException(
            status_code=409,
            detail="Sample cannot be deleted because it is associated autoIntegrations",
        )

    db.session.delete(sample)
    db.session.commit()


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
            models.DataCollectionGroup,
            models.DataCollectionGroup.blSampleId == models.BLSample.blSampleId,
        )
        .outerjoin(
            models.DataCollection,
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


def get_components(
    skip: int,
    limit: int,
    proposal: Optional[str] = None,
) -> Paged[models.Component]:

    query = db.session.query(models.Component).join(models.Proposal)

    if proposal:
        proposal_row = (
            db.session.query(models.Proposal)
            .filter(models.Proposal.proposal == proposal)
            .first()
        )
        if proposal_row:
            query = query.filter(models.Proposal.proposalId == proposal_row.proposalId)

    query = with_authorization(query)

    total = query.count()
    query = page(query, skip=skip, limit=limit)
    results = query.all()

    return Paged(total=total, results=results, skip=skip, limit=limit)


def get_concentration_types() -> Paged[models.ConcentrationType]:
    query = db.session.query(models.ConcentrationType)
    results = query.all()
    return results

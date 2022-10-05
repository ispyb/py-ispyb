from typing import Any, Optional

from sqlalchemy import func, and_, distinct
from sqlalchemy.sql.expression import literal_column
from sqlalchemy.orm import contains_eager, aliased
from ispyb import models

from ...config import settings
from ...app.extensions.database.utils import Paged, page, with_metadata
from ...app.extensions.database.definitions import (
    with_authorization,
)
from ...app.extensions.database.middleware import db
from ..schemas import processings as schema


def get_processing_status(
    dataCollectionIds: list[int],
    beamLineGroups: Optional[dict[str, Any]] = None,
) -> schema.ProcessingStatusesList:
    queries = {}
    queries["screening"] = (
        db.session.query(
            models.DataCollection.dataCollectionId,
            models.Screening.programVersion.label("program"),
            models.ScreeningOutput.indexingSuccess,
            models.ScreeningOutput.strategySuccess.label("status"),
            models.ScreeningOutput.alignmentSuccess,
        )
        .join(models.ScreeningOutput)
        .join(models.DataCollection)
        .join(models.DataCollectionGroup)
        .group_by(models.DataCollection.dataCollectionId, models.Screening.screeningId)
    )

    queries["xrc"] = (
        db.session.query(
            models.DataCollection.dataCollectionId,
            models.XrayCentringResult.status,
            literal_column("'xrc'").label("program"),
        )
        .join(models.DataCollectionGroup)
        .join(
            models.GridInfo,
            models.GridInfo.dataCollectionId == models.DataCollection.dataCollectionId,
        )
        .join(models.XrayCentringResult)
    )

    queries["autoIntegration"] = (
        db.session.query(
            models.DataCollection.dataCollectionId,
            models.AutoProcProgram.autoProcProgramId,
            models.AutoProcProgram.processingPrograms.label("program"),
            models.AutoProcProgram.processingStatus.label("status"),
        )
        .select_from(models.DataCollection)
        .join(models.DataCollectionGroup)
        .join(models.AutoProcIntegration)
        .join(models.AutoProcProgram)
    )

    queries["processing"] = (
        db.session.query(
            models.DataCollection.dataCollectionId,
            models.AutoProcProgram.autoProcProgramId,
            models.AutoProcProgram.processingPrograms.label("program"),
            models.AutoProcProgram.processingStatus.label("status"),
        )
        .select_from(models.DataCollection)
        .join(models.DataCollectionGroup)
        .join(models.ProcessingJob)
        .join(models.AutoProcProgram)
        .outerjoin(models.AutoProcIntegration)
        .filter(
            and_(
                models.AutoProcIntegration.autoProcIntegrationId == None,  # noqa
                models.ProcessingJob.automatic == 1,
            )
        )
    )

    for key in queries.keys():
        queries[key] = queries[key].filter(
            models.DataCollection.dataCollectionId.in_(dataCollectionIds)
        )
        queries[key] = queries[key].join(models.BLSession).join(models.Proposal)
        queries[key] = with_authorization(
            queries[key], beamLineGroups, joinBLSession=False
        )

    results = {}
    for key in queries.keys():
        results[key] = [r._asdict() for r in queries[key].all()]

    statuses = {}
    for key, rows in results.items():
        for row in rows:
            if row["dataCollectionId"] not in statuses:
                statuses[row["dataCollectionId"]] = {}

            if key not in statuses[row["dataCollectionId"]]:
                statuses[row["dataCollectionId"]][key] = {}

            if row["program"] not in statuses[row["dataCollectionId"]][key]:
                statuses[row["dataCollectionId"]][key][row["program"]] = []

            statuses[row["dataCollectionId"]][key][row["program"]].append(row)

    return {"statuses": statuses}


def get_processing_message_status(
    dataCollectionIds: list[int],
    beamLineGroups: Optional[dict[str, Any]] = None,
) -> schema.AutoProcProgramMessageStatuses:
    queries = {}
    columns = [
        models.DataCollection.dataCollectionId.label("dataCollectionId"),
        func.sum(
            func.IF(models.AutoProcProgramMessage.severity == "ERROR", 1, 0)
        ).label("errors"),
        func.sum(
            func.IF(models.AutoProcProgramMessage.severity == "WARNING", 1, 0)
        ).label("warnings"),
        func.sum(func.IF(models.AutoProcProgramMessage.severity == "INFO", 1, 0)).label(
            "info"
        ),
    ]

    queries["autoIntegration"] = (
        db.session.query(*columns)
        .select_from(models.AutoProcProgramMessage)
        .join(models.AutoProcProgram)
        .join(models.AutoProcIntegration)
        .join(models.DataCollection)
        .join(models.DataCollectionGroup)
        .group_by(models.DataCollection.dataCollectionId)
    )

    queries["processing"] = (
        db.session.query(*columns)
        .select_from(models.AutoProcProgramMessage)
        .join(models.AutoProcProgram)
        .join(
            models.ProcessingJob,
            models.ProcessingJob.processingJobId
            == models.AutoProcProgram.processingJobId,
        )
        .join(
            models.DataCollection,
            models.ProcessingJob.dataCollectionId
            == models.DataCollection.dataCollectionId,
        )
        .join(models.DataCollectionGroup)
        .outerjoin(
            models.AutoProcIntegration,
            models.AutoProcIntegration.dataCollectionId
            == models.DataCollection.dataCollectionId,
        )
        .filter(
            and_(
                models.AutoProcIntegration.autoProcIntegrationId == None,  # noqa
                models.ProcessingJob.automatic == 1,
            )
        )
        .group_by(models.DataCollection.dataCollectionId)
    )

    for key in queries.keys():
        queries[key] = queries[key].filter(
            models.DataCollection.dataCollectionId.in_(dataCollectionIds)
        )
        queries[key] = queries[key].join(models.BLSession).join(models.Proposal)
        queries[key] = with_authorization(
            queries[key], beamLineGroups, joinBLSession=False
        )

    subquery = queries["autoIntegration"].union_all(queries["processing"]).subquery()
    query = db.session.query(
        subquery.c.dataCollectionId,
        subquery.c.errors,
        subquery.c.warnings,
        subquery.c.info,
    ).group_by(subquery.c.dataCollectionId)

    results = [r._asdict() for r in query.all()]
    return {"statuses": {row["dataCollectionId"]: row for (row) in results}}


def get_processing_messages(
    skip: 0,
    limit: 25,
    dataCollectionId: int = None,
    autoProcProgramId: int = None,
    autoProcProgramMessageId: int = None,
    beamLineGroups: Optional[dict[str, Any]] = None,
) -> Paged[models.AutoProcProgramMessage]:
    queries = {}
    queries["autoIntegration"] = (
        db.session.query(models.AutoProcProgramMessage)
        .join(models.AutoProcProgram)
        .join(models.AutoProcIntegration)
        .join(models.DataCollection)
        .join(models.DataCollectionGroup)
    )

    queries["processing"] = (
        db.session.query(models.AutoProcProgramMessage)
        .join(models.AutoProcProgram)
        .join(models.ProcessingJob)
        .join(models.DataCollection)
        .join(models.DataCollectionGroup)
    )

    for key in queries.keys():
        queries[key] = queries[key].join(models.BLSession).join(models.Proposal)
        queries[key] = with_authorization(
            queries[key], beamLineGroups, joinBLSession=False
        )

        if autoProcProgramMessageId:
            queries[key] = queries[key].filter(
                models.AutoProcProgramMessage.autoProcProgramMessageId
                == autoProcProgramMessageId
            )

        if dataCollectionId:
            queries[key] = queries[key].filter(
                models.DataCollection.dataCollectionId == dataCollectionId
            )

        if autoProcProgramId:
            queries[key] = queries[key].filter(
                models.AutoProcProgram.autoProcProgramId == autoProcProgramId
            )

    query = (
        queries["autoIntegration"]
        .union_all(queries["processing"])
        .group_by(models.AutoProcProgramMessage.autoProcProgramMessageId)
    )
    query = page(query, skip=skip, limit=limit)

    total = query.count()
    return Paged(total=total, results=query.all(), skip=skip, limit=limit)


def get_screening_results(
    skip: 0,
    limit: 25,
    dataCollectionId: int = None,
    screeningId: int = None,
    beamLineGroups: Optional[dict[str, Any]] = None,
) -> Paged[models.Screening]:
    query = (
        db.session.query(models.Screening)
        .join(models.ScreeningOutput)
        .options(contains_eager(models.Screening.ScreeningOutput))
        .join(models.ScreeningStrategy)
        .options(
            contains_eager(
                models.Screening.ScreeningOutput,
                models.ScreeningOutput.ScreeningStrategy,
            )
        )
        .join(models.ScreeningStrategyWedge)
        .options(
            contains_eager(
                models.Screening.ScreeningOutput,
                models.ScreeningOutput.ScreeningStrategy,
                models.ScreeningStrategy.ScreeningStrategyWedge,
            )
        )
        .outerjoin(models.ScreeningStrategySubWedge)
        .options(
            contains_eager(
                models.Screening.ScreeningOutput,
                models.ScreeningOutput.ScreeningStrategy,
                models.ScreeningStrategy.ScreeningStrategyWedge,
                models.ScreeningStrategyWedge.ScreeningStrategySubWedge,
            )
        )
        .outerjoin(models.ScreeningOutputLattice)
        .options(
            contains_eager(
                models.Screening.ScreeningOutput,
                models.ScreeningOutput.ScreeningStrategy,
                models.ScreeningStrategy.ScreeningOutput,
                models.ScreeningOutput.ScreeningOutputLattice,
            )
        )
        .join(models.DataCollection)
        .join(models.DataCollectionGroup)
        .join(models.BLSession)
        .join(models.Proposal)
    )

    if dataCollectionId:
        query = query.filter(models.Screening.dataCollectionId == dataCollectionId)

    if screeningId:
        query = query.filter(models.Screening.screeningId == screeningId)

    if beamLineGroups:
        query = with_authorization(query, beamLineGroups, joinBLSession=False)

    total = query.count()
    results = query.all()
    return Paged(total=total, results=results, skip=skip, limit=limit)


def get_processing_results(
    skip: 0,
    limit: 25,
    dataCollectionId: int = None,
    autoProcProgramId: int = None,
    beamLineGroups: Optional[dict[str, Any]] = None,
) -> Paged[models.AutoProcProgram]:
    metadata = {
        "attachments": func.count(
            distinct(models.AutoProcProgramAttachment.autoProcProgramAttachmentId)
        )
    }

    query = (
        db.session.query(models.AutoProcProgram, *metadata.values())
        .join(models.ProcessingJob)
        .options(contains_eager(models.AutoProcProgram.ProcessingJob))
        .outerjoin(models.ProcessingJobParameter)
        .options(
            contains_eager(
                models.AutoProcProgram.ProcessingJob,
                models.ProcessingJob.ProcessingJobParameters,
            )
        )
        .outerjoin(models.AutoProcProgramAttachment)
        .join(models.DataCollection)
        .join(models.DataCollectionGroup)
        .join(models.BLSession)
        .join(models.Proposal)
        .outerjoin(
            models.AutoProcIntegration,
            models.AutoProcIntegration.autoProcProgramId
            == models.AutoProcProgram.autoProcProgramId,
        )
        .group_by(models.AutoProcProgram.autoProcProgramId)
        .filter(models.AutoProcIntegration.autoProcIntegrationId == None)
    )

    if dataCollectionId:
        query = query.filter(models.ProcessingJob.dataCollectionId == dataCollectionId)

    if autoProcProgramId:
        query = query.filter(
            models.AutoProcProgram.autoProcProgramId == autoProcProgramId
        )

    if beamLineGroups:
        query = with_authorization(query, beamLineGroups, joinBLSession=False)

    query = page(query, skip=skip, limit=limit)
    total = query.count()
    results = with_metadata(query.all(), list(metadata.keys()))

    messages = get_processing_messages(
        skip=0,
        limit=9999,
        dataCollectionId=dataCollectionId,
        beamLineGroups=beamLineGroups,
    )

    for result in results:
        result._metadata["autoProcProgramMessages"] = [
            message
            for message in messages.results
            if message.autoProcProgramId == result.autoProcProgramId
        ]

    return Paged(total=total, results=results, skip=skip, limit=limit)


def get_processing_attachments(
    skip: 0,
    limit: 25,
    autoProcProgramId: int = None,
    autoProcProgramAttachmentId: int = None,
    beamLineGroups: Optional[dict[str, Any]] = None,
) -> Paged[models.AutoProcProgramAttachment]:
    metadata = {
        "url": func.concat(
            f"{settings.api_root}/processings/attachments/",
            models.AutoProcProgramAttachment.autoProcProgramAttachmentId,
        )
    }

    queries = {}
    queries["api"] = (
        db.session.query(models.AutoProcProgramAttachment, *metadata.values())
        .join(models.AutoProcProgram)
        .join(models.AutoProcIntegration)
    )
    queries["pj"] = (
        db.session.query(models.AutoProcProgramAttachment, *metadata.values())
        .join(models.AutoProcProgram)
        .join(models.ProcessingJob)
    )

    for key in queries.keys():
        queries
        if autoProcProgramAttachmentId:
            queries[key] = queries[key].filter(
                models.AutoProcProgramAttachment.autoProcProgramAttachmentId
                == autoProcProgramAttachmentId
            )

        if autoProcProgramId:
            queries[key] = queries[key].filter(
                models.AutoProcProgramAttachment.autoProcProgramId == autoProcProgramId
            )

        queries[key] = (
            queries[key]
            .join(models.DataCollection)
            .join(models.DataCollectionGroup)
            .join(models.BLSession)
            .join(models.Proposal)
        )
        queries[key] = with_authorization(
            queries[key], beamLineGroups, joinBLSession=False
        )
        queries[key] = page(queries[key], skip=skip, limit=limit)

    query_all = queries["api"].union_all(queries["pj"])
    total = query_all.count()
    results = with_metadata(query_all.all(), list(metadata.keys()))

    return Paged(total=total, results=results, skip=skip, limit=limit)


def get_autointegration_results(
    skip: 0,
    limit: 25,
    dataCollectionId: int = None,
    autoProcProgramId: int = None,
    beamLineGroups: Optional[dict[str, Any]] = None,
) -> Paged[models.AutoProcProgram]:
    # api2 = aliased(models.AutoProcIntegration)
    # subquery = (
    #     db.session.query(
    #         func.count(api2.autoProcIntegrationId).label("imageSweepCount")
    #     )
    #     .filter(api2.autoProcProgramId == models.AutoProcProgram.autoProcProgramId)
    #     .subquery()
    # )
    metadata = {
        # "imageSweepCount": subquery.c.imageSweepCount,
        "attachments": func.count(
            distinct(models.AutoProcProgramAttachment.autoProcProgramAttachmentId)
        ),
    }
    query = (
        db.session.query(models.AutoProcProgram, *metadata.values())
        .outerjoin(models.AutoProcProgramAttachment)
        .join(models.AutoProcIntegration)
        .options(contains_eager(models.AutoProcProgram.AutoProcIntegration))
        .outerjoin(models.AutoProcScalingHasInt)
        .options(
            contains_eager(
                models.AutoProcProgram.AutoProcIntegration,
                models.AutoProcIntegration.AutoProcScalingHasInt,
            )
        )
        .outerjoin(models.AutoProcScaling)
        .options(
            contains_eager(
                models.AutoProcProgram.AutoProcIntegration,
                models.AutoProcIntegration.AutoProcScalingHasInt,
                models.AutoProcScalingHasInt.AutoProcScaling,
            )
        )
        .outerjoin(models.AutoProc)
        .options(
            contains_eager(
                models.AutoProcProgram.AutoProcIntegration,
                models.AutoProcIntegration.AutoProcScalingHasInt,
                models.AutoProcScalingHasInt.AutoProcScaling,
                models.AutoProcScaling.AutoProc,
            )
        )
        .outerjoin(models.AutoProcScalingStatistics)
        .options(
            contains_eager(
                models.AutoProcProgram.AutoProcIntegration,
                models.AutoProcIntegration.AutoProcScalingHasInt,
                models.AutoProcScalingHasInt.AutoProcScaling,
                models.AutoProcScaling.AutoProcScalingStatistics,
            )
        )
        .outerjoin(
            models.ProcessingJob,
            models.ProcessingJob.processingJobId
            == models.AutoProcProgram.processingJobId,
        )
        .outerjoin(models.ProcessingJobImageSweep)
        .join(
            models.DataCollection,
            models.DataCollection.dataCollectionId
            == models.AutoProcIntegration.dataCollectionId,
        )
        .options(
            contains_eager(
                models.AutoProcProgram.AutoProcIntegration,
                models.AutoProcIntegration.DataCollection,
            )
        )
        .join(models.DataCollectionGroup)
        .join(models.BLSession)
        .join(models.Proposal)
        .group_by(
            models.AutoProcProgram.autoProcProgramId,
            models.AutoProcScalingStatistics.autoProcScalingStatisticsId,
        )
    )

    if dataCollectionId:
        query = query.filter(models.ProcessingJob.dataCollectionId == dataCollectionId)

    if autoProcProgramId:
        query = query.filter(
            models.AutoProcProgram.autoProcProgramId == autoProcProgramId
        )

    if beamLineGroups:
        query = with_authorization(query, beamLineGroups, joinBLSession=False)

    query = page(query, skip=skip, limit=limit)
    total = query.count()
    results = with_metadata(query.all(), list(metadata.keys()))

    messages = get_processing_messages(
        skip=0,
        limit=9999,
        dataCollectionId=dataCollectionId,
        beamLineGroups=beamLineGroups,
    )

    for result in results:
        result._metadata["autoProcProgramMessages"] = [
            message
            for message in messages.results
            if message.autoProcProgramId == result.autoProcProgramId
        ]

    return Paged(total=total, results=results, skip=skip, limit=limit)

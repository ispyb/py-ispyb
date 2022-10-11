from dataclasses import dataclass, field
import enum
from typing import Any, List, Optional
import os
from fastapi import HTTPException

import sqlalchemy
from sqlalchemy import or_
from sqlalchemy.orm import contains_eager
from sqlalchemy.sql.expression import literal_column
from ispyb import models

from ...app.extensions.database.definitions import (
    with_authorization,
    _session,
    _proposal,
)
from ...app.extensions.database.utils import Paged, page
from ...app.extensions.database.middleware import db
from ..schemas import events as schema
from ...config import settings


@dataclass
class EntityType:
    # The entity `DataCollection` or `EnergyScan`
    entity: sqlalchemy.orm.decl_api.DeclarativeMeta
    # How the entity joins to `BLSample` i.e. `DataCollection.blSampleId`
    sampleId: "sqlalchemy.Column[Any]"
    # Its primary key `dataCollectionId`
    key: str
    # Any joined entities i.e. `DataCollectionGroup``
    joined: Optional[List[sqlalchemy.orm.decl_api.DeclarativeMeta]] = field(
        default_factory=list
    )


ENTITY_TYPES: dict[str, EntityType] = {
    "dc": EntityType(
        models.DataCollection,
        models.DataCollectionGroup.blSampleId,
        "dataCollectionId",
        [
            models.DataCollection.DataCollectionGroup,
            models.DataCollection.GridInfo,
            [
                models.DataCollection.DataCollectionGroup,
                models.DataCollectionGroup.Workflow,
            ],
        ],
    ),
    "robot": EntityType(
        models.RobotAction, models.RobotAction.blsampleId, "robotActionId"
    ),
    "xrf": EntityType(
        models.XFEFluorescenceSpectrum,
        models.XFEFluorescenceSpectrum.blSampleId,
        "xfeFluorescenceSpectrumId",
    ),
    "es": EntityType(models.EnergyScan, models.EnergyScan.blSampleId, "energyScanId"),
}


def with_sample(
    query: "sqlalchemy.orm.Query[Any]",
    column: "sqlalchemy.Column[Any]",
    blSampleId: Optional[int] = None,
    proteinId: Optional[int] = None,
) -> "sqlalchemy.orm.Query[Any]":
    query = (
        query.outerjoin(models.BLSample, models.BLSample.blSampleId == column)
        .add_columns(models.BLSample.name.label("blSample"))
        .add_columns(models.BLSample.blSampleId.label("blSampleId"))
    )

    if blSampleId:
        query = query.filter(column == blSampleId)

    if proteinId:
        query = (
            query.join(models.Crystal)
            .join(models.Protein)
            .filter(models.Protein.proteinId == proteinId)
        )

    return query


class EventStatus(str, enum.Enum):
    success = "success"
    failed = "failed"
    processed = "processed"
    processerror = "processerror"


def get_events(
    skip: int,
    limit: int,
    session: Optional[str] = None,
    proposal: Optional[str] = None,
    beamLineName: Optional[str] = None,
    dataCollectionId: Optional[int] = None,
    dataCollectionGroupId: Optional[int] = None,
    blSampleId: Optional[int] = None,
    proteinId: Optional[int] = None,
    status: Optional[EventStatus] = None,
    eventType: Optional[str] = None,
    beamLineGroups: Optional[dict[str, Any]] = None,
) -> Paged[schema.Event]:
    queries = {}

    _dataCollectionId = models.DataCollection.dataCollectionId
    startTime = models.DataCollection.startTime
    endTime = models.DataCollection.endTime
    duration = (
        sqlalchemy.func.timestampdiff(
            sqlalchemy.text("SECOND"),
            models.DataCollection.startTime,
            models.DataCollection.endTime,
        )
        / 60
    )
    dataCollectionCount = literal_column("1")

    if dataCollectionGroupId is None:
        duration = sqlalchemy.func.sum(duration) / (
            sqlalchemy.func.count(models.DataCollection.dataCollectionId)
            / sqlalchemy.func.count(
                sqlalchemy.distinct(models.DataCollection.dataCollectionId)
            )
        )
        # Return the first dataCollectionId in a group
        _dataCollectionId = sqlalchemy.func.min(models.DataCollection.dataCollectionId)
        startTime = sqlalchemy.func.min(models.DataCollection.startTime)
        endTime = sqlalchemy.func.max(models.DataCollection.endTime)
        dataCollectionCount = sqlalchemy.func.count(
            sqlalchemy.func.distinct(models.DataCollection.dataCollectionId)
        )

    queries["dc"] = (
        db.session.query(
            _dataCollectionId.label("id"),
            startTime.label("startTime"),
            endTime.label("endTime"),
            duration.label("duration"),
            literal_column("'dc'").label("type"),
            dataCollectionCount.label("count"),
            sqlalchemy.func.count(
                sqlalchemy.distinct(
                    models.DataCollectionFileAttachment.dataCollectionFileAttachmentId
                )
            ).label("attachments"),
            _session,
            _proposal,
        )
        .join(
            models.DataCollectionGroup,
            models.DataCollectionGroup.dataCollectionGroupId
            == models.DataCollection.dataCollectionGroupId,
        )
        .join(
            models.BLSession,
            models.BLSession.sessionId == models.DataCollectionGroup.sessionId,
        )
        .join(
            models.Proposal, models.Proposal.proposalId == models.BLSession.proposalId
        )
        .outerjoin(models.DataCollectionFileAttachment)
    )

    queries["robot"] = (
        db.session.query(
            models.RobotAction.robotActionId.label("id"),
            models.RobotAction.startTimestamp.label("startTime"),
            models.RobotAction.endTimestamp.label("endTime"),
            (
                sqlalchemy.func.timestampdiff(
                    sqlalchemy.text("SECOND"),
                    models.RobotAction.startTimestamp,
                    models.RobotAction.endTimestamp,
                )
                / 60
            ).label("duration"),
            literal_column("'robot'").label("type"),
            literal_column("1").label("count"),
            literal_column("0").label("attachments"),
            _session,
            _proposal,
        )
        .join(
            models.BLSession,
            models.BLSession.sessionId == models.RobotAction.blsessionId,
        )
        .join(
            models.Proposal, models.Proposal.proposalId == models.BLSession.proposalId
        )
        .group_by(models.RobotAction.robotActionId)
    )
    queries["xrf"] = (
        db.session.query(
            models.XFEFluorescenceSpectrum.xfeFluorescenceSpectrumId.label("id"),
            models.XFEFluorescenceSpectrum.startTime.label("startTime"),
            models.XFEFluorescenceSpectrum.endTime.label("endTime"),
            (
                sqlalchemy.func.timestampdiff(
                    sqlalchemy.text("SECOND"),
                    models.XFEFluorescenceSpectrum.startTime,
                    models.XFEFluorescenceSpectrum.endTime,
                )
                / 60
            ).label("duration"),
            literal_column("'xrf'").label("type"),
            literal_column("1").label("count"),
            literal_column("0").label("attachments"),
            _session,
            _proposal,
        )
        .join(
            models.BLSession,
            models.BLSession.sessionId == models.XFEFluorescenceSpectrum.sessionId,
        )
        .join(
            models.Proposal, models.Proposal.proposalId == models.BLSession.proposalId
        )
        .group_by(models.XFEFluorescenceSpectrum.xfeFluorescenceSpectrumId)
    )
    queries["es"] = (
        db.session.query(
            models.EnergyScan.energyScanId.label("id"),
            models.EnergyScan.startTime.label("startTime"),
            models.EnergyScan.endTime.label("endTime"),
            (
                sqlalchemy.func.timestampdiff(
                    sqlalchemy.text("SECOND"),
                    models.EnergyScan.startTime,
                    models.EnergyScan.endTime,
                )
                / 60
            ).label("duration"),
            literal_column("'es'").label("type"),
            literal_column("1").label("count"),
            literal_column("0").label("attachments"),
            _session,
            _proposal,
        )
        .join(
            models.BLSession, models.BLSession.sessionId == models.EnergyScan.sessionId
        )
        .join(
            models.Proposal, models.Proposal.proposalId == models.BLSession.proposalId
        )
        .group_by(models.EnergyScan.energyScanId)
    )

    if session:
        session_row = (
            db.session.query(models.BLSession)
            .join(models.Proposal)
            .filter(models.BLSession.session == session)
            .first()
        )

    if proposal:
        proposal_row = (
            db.session.query(models.Proposal)
            .filter(models.Proposal.proposal == proposal)
            .first()
        )

    # Join sample information
    for key, _query in queries.items():
        queries[key] = with_sample(
            _query, ENTITY_TYPES[key].sampleId, blSampleId, proteinId
        )

        # Apply permissions
        if beamLineGroups:
            queries[key] = with_authorization(
                queries[key], beamLineGroups, joinBLSession=False
            )

        # Filter by session
        if session:
            if session_row:
                queries[key] = queries[key].filter(
                    models.BLSession.sessionId == session_row.sessionId
                )

        # Filter by proposal
        if proposal:
            if proposal_row:
                queries[key] = queries[key].filter(
                    models.Proposal.proposalId == proposal_row.proposalId
                )

        # Filter by beamLineName
        if beamLineName:
            queries[key] = queries[key].filter(
                models.BLSession.beamLineName == beamLineName
            )

    # Filter a single dataColleciton
    if dataCollectionId:
        queries["dc"] = queries["dc"].filter(
            models.DataCollection.dataCollectionId == dataCollectionId
        )
        queries["robot"] = queries["robot"].filter(
            models.RobotAction.robotActionId == 0
        )
        queries["xrf"] = queries["xrf"].filter(
            models.XFEFluorescenceSpectrum.xfeFluorescenceSpectrumId == 0
        )
        queries["es"] = queries["es"].filter(models.EnergyScan.energyScanId == 0)

    # Ungroup a dataCollectionGroup
    if dataCollectionGroupId:
        queries["dc"] = (
            queries["dc"]
            .filter(
                models.DataCollectionGroup.dataCollectionGroupId
                == dataCollectionGroupId
            )
            .group_by(models.DataCollection.dataCollectionId)
        )
        queries["robot"] = queries["robot"].filter(
            models.RobotAction.robotActionId == 0
        )
        queries["xrf"] = queries["xrf"].filter(
            models.XFEFluorescenceSpectrum.xfeFluorescenceSpectrumId == 0
        )
        queries["es"] = queries["es"].filter(models.EnergyScan.energyScanId == 0)
    else:
        queries["dc"] = queries["dc"].group_by(
            models.DataCollectionGroup.dataCollectionGroupId
        )

    # Filter by status
    if status:
        if status == EventStatus.success:
            queries["dc"] = queries["dc"].filter(
                models.DataCollection.runStatus.like("%success%")
            )
            queries["robot"] = queries["robot"].filter(
                models.RobotAction.status.like("%success%")
            )
        elif status == EventStatus.failed:
            queries["dc"] = queries["dc"].filter(
                models.DataCollection.runStatus.notlike("%success%")
            )
            queries["robot"] = queries["robot"].filter(
                models.RobotAction.status.notlike("%success%")
            )
        elif status == EventStatus.processed:
            queries["dc"] = (
                queries["dc"]
                .join(models.AutoProcIntegration)
                .join(models.AutoProcProgram)
                .filter(models.AutoProcProgram.processingStatus == 1)
            )
            queries["robot"] = queries["robot"].filter(
                models.RobotAction.robotActionId == 0
            )
        elif status == EventStatus.processerror:
            if not hasattr(models, "AutoProcProgramMessage"):
                raise HTTPException(
                    status_code=500,
                    detail="Database does not have `AutoProcProgramMessage`",
                )
            queries["dc"] = (
                queries["dc"]
                .join(models.AutoProcIntegration)
                # .outerjoin(models.ProcessingJob)
                .join(
                    models.AutoProcProgram,
                    or_(
                        # models.ProcessingJob.processingJobId
                        # == models.AutoProcProgram.processingJobId,
                        models.AutoProcIntegration.autoProcProgramId
                        == models.AutoProcProgram.autoProcProgramId,
                    ),
                )
                .join(models.AutoProcProgramMessage)
                .filter(
                    or_(
                        models.AutoProcProgramMessage.severity == "WARNING",
                        models.AutoProcProgramMessage.severity == "ERROR",
                    )
                )
            )
            queries["robot"] = queries["robot"].filter(
                models.RobotAction.robotActionId == 0
            )

        queries["xrf"] = queries["xrf"].filter(
            models.XFEFluorescenceSpectrum.xfeFluorescenceSpectrumId == 0
        )
        queries["es"] = queries["es"].filter(models.EnergyScan.energyScanId == 0)

    # Filter by eventType
    if eventType:
        filters = {
            "dc": queries["dc"].filter(models.DataCollection.dataCollectionId == 0),
            "robot": queries["robot"].filter(models.RobotAction.robotActionId == 0),
            "xrf": queries["xrf"].filter(
                models.XFEFluorescenceSpectrum.xfeFluorescenceSpectrumId == 0
            ),
            "es": queries["es"].filter(models.EnergyScan.energyScanId == 0),
        }

        tableFilters = ["robot", "es", "xrf"]
        if eventType in tableFilters:
            for query in tableFilters:
                if eventType == query:
                    filters[query] = queries[query]
        else:
            filters["dc"] = queries["dc"].filter(
                models.DataCollectionGroup.experimentType == eventType
            )

        for key, query_filter in filters.items():
            queries[key] = query_filter

    # Now union the four queries
    query: sqlalchemy.orm.Query[Any] = queries["dc"].union(
        queries["robot"], queries["xrf"], queries["es"]
    )

    total = query.count()
    query = query.order_by(sqlalchemy.desc("endTime"))
    query = page(query, skip=skip, limit=limit)

    # Results contains an index of type / id
    results = query.all()
    results = [r._asdict() for r in results]

    # Build a  list of ids to load based on type, i.e. a list of `dataCollectionId`s
    entity_ids: dict[str, list[int]] = {}
    for result in results:
        for name in ENTITY_TYPES.keys():
            if result["type"] == name:
                if name not in entity_ids:
                    entity_ids[name] = []
                entity_ids[name].append(result["id"])

    # Now load the related entities, i.e. load the `DataCollection` or `EnergyScan`
    entity_type_map = {}
    for name, entity_type in ENTITY_TYPES.items():
        if name in entity_ids:
            column = getattr(entity_type.entity, entity_type.key)
            query = db.session.query(entity_type.entity).filter(
                column.in_(entity_ids[name])
            )

            # If there are joined entities load those too
            if entity_type.joined:
                for joined_entity in entity_type.joined:
                    if isinstance(joined_entity, list):
                        query = query.outerjoin(joined_entity[-1]).options(
                            contains_eager(*joined_entity)
                        )
                    else:
                        query = query.outerjoin(joined_entity).options(
                            contains_eager(joined_entity)
                        )

            entity_type_map[name] = {
                getattr(entity, entity_type.key): entity for entity in query.all()
            }

    # Merge the loaded entities back into the index's `Item`
    for result in results:
        for entity_type_name in ENTITY_TYPES.keys():
            if result["type"] == entity_type_name:
                if entity_type_name in entity_type_map:
                    result["Item"] = entity_type_map[entity_type_name][result["id"]]

                    if entity_type_name == "dc":
                        _check_snapshots(result["Item"])

    return Paged(total=total, results=results, skip=skip, limit=limit)


def _check_snapshots(datacollection: models.DataCollection) -> models.DataCollection:
    snapshot_statuses = {}
    for i, snapshot in enumerate(
        [
            "xtalSnapshotFullPath1",
            "xtalSnapshotFullPath2",
            "xtalSnapshotFullPath3",
            "xtalSnapshotFullPath4",
        ]
    ):
        snapshot_path = getattr(datacollection, snapshot)
        if snapshot_path:
            if settings.path_map:
                snapshot_path = settings.path_map + snapshot_path
            snapshot_statuses[i + 1] = (
                os.path.exists(snapshot_path) if snapshot_path is not None else False
            )
        else:
            snapshot_statuses[i + 1] = False

    datacollection._metadata["snapshots"] = snapshot_statuses
    return datacollection


def get_event_types(
    session: Optional[str] = None,
    blSampleId: Optional[int] = None,
    beamLineGroups: Optional[dict[str, Any]] = None,
) -> Paged[schema.EventType]:
    queries = {}
    queries["dc"] = db.session.query(
        sqlalchemy.distinct(models.DataCollectionGroup.experimentType).label(
            "experimentType"
        ),
    ).join(
        models.BLSession,
        models.BLSession.sessionId == models.DataCollectionGroup.sessionId,
    )

    queries["robot"] = db.session.query(
        sqlalchemy.func.count(models.RobotAction.robotActionId).label("count")
    ).join(
        models.BLSession,
        models.BLSession.sessionId == models.RobotAction.blsessionId,
    )
    queries["xrf"] = db.session.query(
        sqlalchemy.func.count(
            models.XFEFluorescenceSpectrum.xfeFluorescenceSpectrumId
        ).label("count")
    ).join(
        models.BLSession,
        models.BLSession.sessionId == models.XFEFluorescenceSpectrum.sessionId,
    )
    queries["es"] = db.session.query(
        sqlalchemy.func.count(models.EnergyScan.energyScanId).label("count")
    ).join(models.BLSession, models.BLSession.sessionId == models.EnergyScan.sessionId)

    if session:
        session_row = (
            db.session.query(models.BLSession)
            .join(models.Proposal)
            .filter(models.BLSession.session == session)
            .first()
        )

    for key in queries.keys():
        queries[key] = queries[key].join(
            models.Proposal,
            models.Proposal.proposalId == models.BLSession.proposalId,
        )

        if session:
            if session_row:
                queries[key] = queries[key].filter(
                    models.BLSession.sessionId == session_row.sessionId
                )

        if blSampleId:
            queries[key] = queries[key].filter(
                models.DataCollectionGroup.blSampleId == blSampleId
            )

        if beamLineGroups:
            queries[key] = with_authorization(
                queries[key], beamLineGroups, joinBLSession=False
            )

        queries[key] = [result._asdict() for result in queries[key].all()]

    eventTypes = []
    for eventType in queries["dc"]:
        if eventType["experimentType"]:
            eventTypes.append(
                {
                    "eventType": eventType["experimentType"],
                    "eventTypeName": eventType["experimentType"],
                }
            )

    for table, name in {
        "robot": "Sample Actions",
        "xrf": "XRF Spectrum",
        "es": "Energy Scan",
    }.items():
        if queries[table][0]["count"] > 0:
            eventTypes.append({"eventType": table, "eventTypeName": name})

    return Paged(
        total=len(eventTypes), results=eventTypes, skip=0, limit=len(eventTypes)
    )

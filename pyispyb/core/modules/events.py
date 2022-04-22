from typing import Optional, Any
import os

import sqlalchemy
from sqlalchemy.orm import contains_eager
from sqlalchemy.sql.expression import literal_column

from pyispyb.core import models
from pyispyb.app.extensions.database.utils import Paged, page
from pyispyb.app.extensions.database.middleware import db
from ..schemas import events as schema


def with_sample(
    query: "sqlalchemy.orm.Query[Any]",
    column: "sqlalchemy.Column[Any]",
    bl_sample_id: Optional[int] = None,
    protein_id: Optional[int] = None,
) -> "sqlalchemy.orm.Query[Any]":
    query = (
        query.outerjoin(models.BLSample, models.BLSample.blSampleId == column)
        .add_columns(models.BLSample.name.label("blSample"))
        .add_columns(models.BLSample.blSampleId.label("blSampleId"))
    )

    if bl_sample_id:
        query = query.filter(column == bl_sample_id)

    if protein_id:
        query = (
            query.join(models.Crystal)
            .join(models.Protein)
            .filter(models.Protein.proteinId == protein_id)
        )

    return query


def get_events(
    skip: int,
    limit: int,
    session_id: Optional[int] = None,
    data_collection_group_id: Optional[int] = None,
    bl_sample_id: Optional[int] = None,
    protein_id: Optional[int] = None,
) -> Paged[schema.Event]:
    queries = {}

    data_collection_id = models.DataCollection.dataCollectionId
    start_time = models.DataCollection.startTime
    end_time = models.DataCollection.endTime
    duration = sqlalchemy.func.time_to_sec(
        sqlalchemy.func.timediff(
            models.DataCollection.endTime,
            models.DataCollection.startTime,
        )
    )
    data_collection_count = literal_column("1")

    if data_collection_group_id is None:
        duration = sqlalchemy.func.sum(duration)
        # Return the first dataCollectionId in a group
        data_collection_id = sqlalchemy.func.min(models.DataCollection.dataCollectionId)  # type: ignore
        start_time = sqlalchemy.func.min(models.DataCollection.startTime)  # type: ignore
        end_time = sqlalchemy.func.max(models.DataCollection.endTime)  # type: ignore
        data_collection_count = sqlalchemy.func.count(
            sqlalchemy.func.distinct(models.DataCollection.dataCollectionId)
        )  # type: ignore

    queries["dc"] = db.session.query(
        data_collection_id.label("id"),
        start_time.label("startTime"),
        end_time.label("endTime"),
        literal_column("'dc'").label("type"),
        data_collection_count.label("count"),
    ).join(
        models.DataCollectionGroup,
        models.DataCollectionGroup.dataCollectionGroupId
        == models.DataCollection.dataCollectionGroupId,
    )
    queries["robot"] = db.session.query(
        models.RobotAction.robotActionId.label("id"),
        models.RobotAction.startTimestamp.label("startTime"),
        models.RobotAction.endTimestamp.label("endTime"),
        literal_column("'robot'").label("type"),
        literal_column("1").label("count"),
    )
    queries["xrf"] = db.session.query(
        models.XFEFluorescenceSpectrum.xfeFluorescenceSpectrumId.label("id"),
        models.XFEFluorescenceSpectrum.startTime.label("startTime"),
        models.XFEFluorescenceSpectrum.endTime.label("endTime"),
        literal_column("'xrf'").label("type"),
        literal_column("1").label("count"),
    )
    queries["es"] = db.session.query(
        models.EnergyScan.energyScanId.label("id"),
        models.EnergyScan.startTime.label("startTime"),
        models.EnergyScan.endTime.label("endTime"),
        literal_column("'es'").label("type"),
        literal_column("1").label("count"),
    )

    # Join sample information
    _mapper = {
        "dc": models.DataCollectionGroup.blSampleId,
        "robot": models.RobotAction.blsampleId,
        "xrf": models.XFEFluorescenceSpectrum.blSampleId,
        "es": models.EnergyScan.blSampleId,
    }
    for key, _query in queries.items():
        queries[key] = with_sample(_query, _mapper[key], bl_sample_id, protein_id)

    # Filter by sessionid
    if session_id:
        queries["dc"] = queries["dc"].filter(
            models.DataCollectionGroup.sessionId == session_id
        )
        queries["robot"] = queries["robot"].filter(
            models.RobotAction.blsessionId == session_id
        )
        queries["xrf"] = queries["xrf"].filter(
            models.XFEFluorescenceSpectrum.sessionId == session_id
        )
        queries["es"] = queries["es"].filter(models.EnergyScan.sessionId == session_id)

    # Ungroup a dataCollectionGroup
    if data_collection_group_id:
        queries["dc"] = queries["dc"].filter(
            models.DataCollectionGroup.dataCollectionGroupId == data_collection_group_id
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

    query: sqlalchemy.orm.Query[Any] = queries["dc"].union_all(
        queries["robot"], queries["xrf"], queries["es"]
    )

    total = query.count()
    query = query.order_by(sqlalchemy.desc("startTime"))
    query = page(query, skip=skip, limit=limit)

    results = query.all()
    results = [r._asdict() for r in results]

    ids: dict[str, list[int]] = {}
    types: dict[str, list[Any]] = {
        "dc": [
            models.DataCollection,
            "dataCollectionId",
            models.DataCollection.DataCollectionGroup,
        ],
        "robot": [models.RobotAction, "robotActionId"],
        "xrf": [models.XFEFluorescenceSpectrum, "xfeFluorescenceSpectrumId"],
        "es": [models.EnergyScan, "energyScanId"],
    }
    for result in results:
        for name in types.keys():
            if result["type"] == name:
                if name not in ids:
                    ids[name] = []
                ids[name].append(result["id"])

    type_map = {}
    for name, ty in types.items():
        if name in ids:
            column = getattr(ty[0], ty[1])
            if len(ty) > 2:
                items = (
                    db.session.query(ty[0])
                    .join(ty[2])
                    .options(contains_eager(ty[2]))
                    .filter(column.in_(ids[name]))
                    .all()
                )
            else:
                items = (
                    db.session.query(ty[0]).filter(column.in_(ids[name])).all()
                )
            type_map[name] = {getattr(item, ty[1]): item for item in items}

    for result in results:
        for name, _ty in types.items():
            if result["type"] == name:
                if name in type_map:
                    result["Item"] = type_map[name][result["id"]]

                    if name == "dc":
                        _check_snapshots(result["Item"])

    return Paged(total=total, results=results, skip=skip, limit=limit)


def get_datacollection(
    data_collection_id: int
) -> Optional[models.DataCollection]:
    dc = (
        db.session.query(models.DataCollection)
        .filter(models.DataCollection.dataCollectionId == data_collection_id)
        .first()
    )

    return dc


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
            # snapshot_path = snapshot_path.replace("/data", "/Users/Shared/data")
            snapshot_statuses[i + 1] = (
                os.path.exists(snapshot_path) if snapshot_path is not None else False
            )
        else:
            snapshot_statuses[i + 1] = False

    datacollection._metadata["snapshots"] = snapshot_statuses
    return datacollection


def get_datacollection_snapshot_path(
    data_collection_id: int, image_id: int = 0, full_size: bool = False
) -> Optional[str]:
    dc = get_datacollection(data_collection_id)
    if not dc:
        return None

    images = [
        "xtalSnapshotFullPath1",
        "xtalSnapshotFullPath2",
        "xtalSnapshotFullPath3",
        "xtalSnapshotFullPath4",
    ]

    image_path: str = getattr(dc, images[image_id])
    if image_path is None:
        return None

    if not full_size:
        ext = os.path.splitext(image_path)[1][1:].strip()
        image_path = image_path.replace(f".{ext}", f"t.{ext}")

    # image_path = image_path.replace("/data", "/Users/Shared/data")
    if os.path.exists(image_path):
        return image_path

    return None

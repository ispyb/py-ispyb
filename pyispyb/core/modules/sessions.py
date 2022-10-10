from datetime import datetime, timedelta
from typing import Any, Optional

from ispyb import models
from sqlalchemy import func, and_, or_, extract, distinct
from sqlalchemy.orm import joinedload, contains_eager

from ...app.extensions.database.definitions import (
    groups_from_beamlines,
    with_authorization,
)
from ...app.extensions.options.schema import BeamLineGroup
from ...app.extensions.database.utils import Paged, page, with_metadata
from ...app.extensions.database.middleware import db
from ...core.modules.utils import encode_external_id


def get_sessions(
    skip: int,
    limit: int,
    sessionId: Optional[int] = None,
    externalId: Optional[int] = None,
    expSessionPk: Optional[int] = None,
    proposalId: Optional[int] = None,
    proposal: Optional[str] = None,
    session: Optional[str] = None,
    beamLineName: Optional[str] = None,
    beamLineGroup: Optional[str] = None,
    scheduled: Optional[bool] = None,
    upcoming: Optional[bool] = None,
    previous: Optional[bool] = None,
    sessionType: Optional[str] = None,
    month: Optional[int] = None,
    year: Optional[int] = None,
    beamLineGroups: Optional[dict[str, Any]] = None,
) -> Paged[models.BLSession]:
    metadata = {
        "active": func.IF(
            and_(
                models.BLSession.startDate <= datetime.now(),
                models.BLSession.endDate >= datetime.now(),
            ),
            True,
            False,
        ),
        "active_soon": func.IF(
            and_(
                models.BLSession.startDate <= datetime.now() - timedelta(minutes=20),
                models.BLSession.endDate >= datetime.now() + timedelta(minutes=20),
            ),
            True,
            False,
        ),
        "sessionTypes": func.group_concat(distinct(models.SessionType.typeName)),
        "persons": func.count(models.SessionHasPerson.personId),
    }

    query = (
        db.session.query(models.BLSession, *metadata.values())
        .outerjoin(models.SessionType)
        .join(models.Proposal)
        .outerjoin(models.SessionHasPerson)
        .options(contains_eager(models.BLSession.Proposal))
        .order_by(models.BLSession.startDate.desc())
        .group_by(models.BLSession.sessionId)
    )

    if sessionId:
        query = query.filter(models.BLSession.sessionId == sessionId)

    if session:
        query = query.filter(models.BLSession.session == session)

    if externalId:
        externalId = encode_external_id(externalId)
        query = query.filter(models.BLSession.externalId == externalId)

    if expSessionPk:
        query = query.filter(models.BLSession.expSessionPk == expSessionPk)

    if proposalId:
        query = query.filter(models.BLSession.proposalId == proposalId)

    if proposal:
        query = query.filter(models.Proposal.proposal == proposal)

    if beamLineName:
        query = query.filter(models.BLSession.beamLineName == beamLineName)

    if scheduled:
        query = query.filter(models.BLSession.scheduled == 1)

    if upcoming:
        query = query.filter(models.BLSession.endDate >= datetime.now())
        query = query.order_by(models.BLSession.startDate)

    if previous:
        query = query.filter(models.BLSession.endDate < datetime.now())

    if sessionType:
        query = query.filter(models.SessionType.typeName == sessionType)

    if month:
        query = query.filter(
            or_(
                extract("month", models.BLSession.startDate) == month,
                extract("month", models.BLSession.endDate) == month,
            )
        )

    if year:
        query = query.filter(
            or_(
                extract("year", models.BLSession.startDate) == year,
                extract("year", models.BLSession.endDate) == year,
            )
        )

    if beamLineGroups:
        if beamLineGroup:
            for group in beamLineGroups:
                if group.groupName == beamLineGroup:
                    query = query.filter(
                        models.BLSession.beamLineName.in_(
                            [beamline.beamLineName for beamline in group.beamLines]
                        )
                    )

        query = with_authorization(
            query,
            beamLineGroups,
            joinBLSession=False,
            joinSessionHasPerson=False,
        )

    total = query.count()
    query = page(query, skip=skip, limit=limit)
    results = with_metadata(query.all(), list(metadata.keys()))

    dataCollections = (
        db.session.query(
            func.count(models.DataCollection.dataCollectionId).label("count"),
            models.DataCollectionGroup.sessionId,
        )
        .join(models.DataCollectionGroup)
        .filter(
            models.DataCollectionGroup.sessionId.in_(
                [result.sessionId for result in results]
            )
        )
        .group_by(models.DataCollectionGroup.sessionId)
        .all()
    )
    dataCollectionCount = {}
    for dataCollection in dataCollections:
        dataCollectionDict = dataCollection._asdict()
        dataCollectionCount[dataCollectionDict["sessionId"]] = dataCollectionDict[
            "count"
        ]

    for result in results:
        if beamLineGroups:
            result._metadata["uiGroups"] = groups_from_beamlines(
                beamLineGroups, [result.beamLineName]
            )
        result._metadata["datacollections"] = dataCollectionCount.get(
            result.sessionId, 0
        )
        result._metadata["sessionTypes"] = (
            result._metadata["sessionTypes"].split(",")
            if result._metadata["sessionTypes"]
            else []
        )

    return Paged(total=total, results=results, skip=skip, limit=limit)


def get_sessions_for_beamline_group(
    beamLineGroup: Optional[str],
    upcoming: Optional[bool] = None,
    previous: Optional[bool] = None,
    sessionType: Optional[str] = None,
    beamLineGroups: Optional[dict[str, Any]] = None,
) -> Paged[models.BLSession]:
    group: BeamLineGroup = None
    for groupBeamLine in beamLineGroups:
        if groupBeamLine.groupName == beamLineGroup:
            group = groupBeamLine

    if not group:
        return Paged(total=0, results=[], skip=0, limit=0)

    sessions = []
    for beamLine in group.beamLines:
        beamline_sessions = get_sessions(
            skip=0,
            limit=1,
            beamLineName=beamLine.beamLineName,
            upcoming=upcoming,
            previous=previous,
            sessionType=sessionType,
            beamLineGroups=beamLineGroups,
        )

        sessions.extend(beamline_sessions.results)

    return Paged(total=len(sessions), results=sessions, skip=0, limit=len(sessions))


def get_sessionHasPerson(
    skip: int,
    limit: int,
    sessionId: Optional[int] = None,
) -> Paged[models.SessionHasPerson]:

    query = db.session.query(models.SessionHasPerson).options(
        joinedload(models.SessionHasPerson.Person)
    )

    if sessionId:
        query = query.filter(models.SessionHasPerson.sessionId == sessionId)

    query_distinct = query.distinct()
    total = query_distinct.count()

    query = page(query_distinct, skip=skip, limit=limit)

    return Paged(total=total, results=query.all(), skip=skip, limit=limit)

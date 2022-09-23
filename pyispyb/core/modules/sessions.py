from datetime import datetime, timedelta
from typing import Any, Optional

from ispyb import models
from sqlalchemy import func, and_, or_, extract
from sqlalchemy.orm import joinedload, contains_eager

from ...app.extensions.database.definitions import (
    groups_from_beamlines,
    with_beamline_groups,
)
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
    sessionHasPerson: Optional[bool] = False,
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
    }

    query = (
        db.session.query(models.BLSession, *metadata.values())
        .outerjoin(models.SessionType)
        .options(contains_eager(models.BLSession.SessionType))
        .join(models.Proposal)
        .options(contains_eager(models.BLSession.Proposal))
    )

    if sessionHasPerson:
        query = (
            query.outerjoin(
                models.SessionHasPerson,
                models.BLSession.sessionId == models.SessionHasPerson.sessionId,
            )
            .options(contains_eager(models.BLSession.SessionHasPerson))
            .outerjoin(
                models.Person,
                models.SessionHasPerson.personId == models.Person.personId,
            )
            .options(
                contains_eager(
                    models.BLSession.SessionHasPerson, models.SessionHasPerson.Person
                )
            )
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

    beamLineName: Optional[str] = (None,)
    beamLineGroup: Optional[str] = (None,)
    scheduled: Optional[bool] = (None,)
    upcoming: Optional[bool] = (None,)
    previous: Optional[bool] = (None,)
    sessionType: Optional[str] = (None,)
    month: Optional[int] = (None,)
    year: Optional[int] = (None,)

    if beamLineName:
        query = query.filter(models.BLSession.beamLineName == beamLineName)

    if scheduled:
        query = query.filter(models.BLSession.scheduled == 1)

    if upcoming:
        query = query.filter(models.BLSession.startDate > datetime.now())

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

        query = with_beamline_groups(
            query, beamLineGroups, joinBLSession=False, joinSessionHasPerson=False
        )

    query = query.distinct()
    total = query.count()
    query = page(query, skip=skip, limit=limit)

    results = query.all()
    results = with_metadata(query.all(), list(metadata.keys()))
    for result in results:
        if beamLineGroups:
            result._metadata["groups"] = groups_from_beamlines(
                beamLineGroups, [result.beamLineName]
            )
        result._metadata["persons"] = len(result.SessionHasPerson)

    return Paged(total=total, results=results, skip=skip, limit=limit)


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

from typing import Optional
from ispyb import models
from sqlalchemy.orm import joinedload, contains_eager
from pyispyb.app.extensions.database.utils import Paged, page
from pyispyb.app.extensions.database.middleware import db
from pyispyb.core.modules.utils import encode_external_id


def get_sessions(
    skip: int,
    limit: int,
    sessionId: Optional[int] = None,
    externalId: Optional[int] = None,
    expSessionPk: Optional[int] = None,
    proposalId: Optional[int] = None,
    sessionHasPerson: Optional[bool] = False,
) -> Paged[models.BLSession]:

    query = db.session.query(models.BLSession)

    if sessionHasPerson:
        query = (
            query.outerjoin(
                models.SessionHasPerson,
                models.BLSession.sessionId == models.SessionHasPerson.sessionId,
            )
            .options(contains_eager("SessionHasPerson"))
            .outerjoin(
                models.Person,
                models.SessionHasPerson.personId == models.Person.personId,
            )
            .options(contains_eager("SessionHasPerson.Person"))
            .distinct()
        )

    if sessionId:
        query = query.filter(models.BLSession.sessionId == sessionId)

    if externalId:
        externalId = encode_external_id(externalId)
        query = query.filter(models.BLSession.externalId == externalId)

    if expSessionPk:
        query = query.filter(models.BLSession.expSessionPk == expSessionPk)

    if proposalId:
        query = query.filter(models.BLSession.proposalId == proposalId)

    total = query.count()
    query = page(query, skip=skip, limit=limit)

    return Paged(total=total, results=query.all(), skip=skip, limit=limit)


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

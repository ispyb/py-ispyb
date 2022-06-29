from typing import Optional
from sqlalchemy.orm import contains_eager
from pyispyb.core import models
from pyispyb.app.extensions.database.utils import Paged, page
from pyispyb.app.extensions.database.middleware import db


def get_sessions(
    skip: int,
    limit: int,
    sessionId: Optional[int] = None,
    externalId: Optional[int] = None,
    expSessionPk: Optional[int] = None,
    proposalId: Optional[int] = None,
    sessionHasPerson: Optional[bool] = False,
) -> Paged[models.Proposal]:

    if sessionHasPerson:
        query = (
            db.session.query(models.BLSession)
            .join(models.BLSession.session_has_people)
            .options(
                contains_eager(models.BLSession.session_has_people),
            )
            .populate_existing()
        )
    else:
        query = db.session.query(models.BLSession)

    if sessionId:
        query = query.filter(models.BLSession.sessionId == sessionId)

    if externalId:
        externalId = externalId.to_bytes(16, byteorder="big")
        query = query.filter(models.BLSession.externalId == externalId)

    if expSessionPk:
        query = query.filter(models.BLSession.expSessionPk == expSessionPk)

    if proposalId:
        query = query.filter(models.BLSession.proposalId == proposalId)

    # https://github.com/aiidateam/aiida-core/issues/1600
    query_distinct = query.distinct()
    total = query_distinct.count()
    query = page(query_distinct, skip=skip, limit=limit)

    return Paged(total=total, results=query.all(), skip=skip, limit=limit)

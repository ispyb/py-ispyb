from typing import Optional, Any
import sqlalchemy
from sqlalchemy.orm import Session

from pyispyb.core import models
from pyispyb.app.globals import g

_session = sqlalchemy.func.concat(
    models.Proposal.proposalCode,
    models.Proposal.proposalNumber,
    "-",
    models.BLSession.visit_number,
).label("session")


def get_blsession(db: Session, session: str) -> Optional[models.BLSession]:
    return (
        db.query(models.BLSession)
        .join(models.Proposal)
        .filter(_session == session)
        .first()
    )


def with_auth_to_session(query: "sqlalchemy.orm.Query[Any]", column: "sqlalchemy.Column[Any]"):
    """Join relevant tables to authorise right through to SessionHasPerson

    in case of not being admin, can be reused"""
    return (
        query.join(models.Proposal, column == models.Proposal.proposalId)
        .join(
            models.BLSession, models.BLSession.proposalId == models.Proposal.proposalId
        )
        .join(
            models.SessionHasPerson,
            models.BLSession.sessionId == models.SessionHasPerson.sessionId,
        )
        .filter(models.SessionHasPerson.personId == g.person.personId)
    )

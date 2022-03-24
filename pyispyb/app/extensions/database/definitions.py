from typing import Optional, Any
import sqlalchemy
from sqlalchemy.orm import joinedload

from pyispyb.core import models
from pyispyb.app.globals import g
from pyispyb.app.extensions.database.middleware import db

_session = sqlalchemy.func.concat(
    models.Proposal.proposalCode,
    models.Proposal.proposalNumber,
    "-",
    models.BLSession.visit_number,
).label("session")


def get_blsession(session: str) -> Optional[models.BLSession]:
    return (
        db.session.query(models.BLSession)
        .join(models.Proposal)
        .filter(_session == session)
        .first()
    )


def with_auth_to_session(
    query: "sqlalchemy.orm.Query[Any]", column: "sqlalchemy.Column[Any]"
) -> "sqlalchemy.orm.Query[Any]":
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


def get_current_person() -> Optional[models.Person]:
    person = (
        db.session.query(models.Person)
        .options(joinedload(models.Person.UserGroup))
        .options(joinedload(models.Person.UserGroup, models.UserGroup.Permission))
        .filter(models.Person.login == g.login)
        .first()
    )

    if not person:
        return

    permissions = []
    for group in person.UserGroup:
        for permission in group.Permission:
            permissions.append(permission.type)
    person._metadata["permissions"] = permissions

    return person

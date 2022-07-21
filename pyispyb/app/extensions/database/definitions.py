from typing import Optional, Any

import sqlalchemy
from sqlalchemy.orm import joinedload
from ispyb import models

from pyispyb.app.globals import g
from pyispyb.app.extensions.database.middleware import db
from ...extensions.options.schema import BeamlineGroup

_session = sqlalchemy.func.concat(
    models.Proposal.proposalCode,
    models.Proposal.proposalNumber,
    "-",
    models.BLSession.visit_number,
).label("session")

_proposal = sqlalchemy.func.concat(
    models.Proposal.proposalCode, models.Proposal.proposalNumber
).label("proposal")


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
        .join(
            models.Person,
            models.SessionHasPerson.personId == models.Person.personId,
        )
        .filter(models.Person.login == g.login)
    )


def with_auth_to_session_has_person(
    query: "sqlalchemy.orm.Query[Any]",
) -> "sqlalchemy.orm.Query[Any]":
    """Join relevant tables to authorise right through to SessionHasPerson"""
    return (
        query.join(
            models.SessionHasPerson,
            models.BLSession.sessionId == models.SessionHasPerson.sessionId,
        )
        .join(
            models.Person,
            models.SessionHasPerson.personId == models.Person.personId,
        )
        .filter(models.Person.login == g.username)
    )


def get_current_person(login: str) -> Optional[models.Person]:
    person = (
        db.session.query(models.Person)
        .options(joinedload(models.Person.UserGroup))
        .options(joinedload(models.Person.UserGroup, models.UserGroup.Permission))
        .filter(models.Person.login == login)
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


def with_beamline_groups(
    query: "sqlalchemy.orm.Query[Any]",
    beamlineGroups: list[BeamlineGroup],
    includeArchived: bool = False,
) -> "sqlalchemy.orm.Query[Any]":
    # super_admin can access all sessions
    if "all_proposals" in g.permissions:
        print("user has `all_proposals`")
        return query

    # Iterate through users permissions and match them to the relevant groups
    beamlines = []
    permissions_applied = []
    for group in beamlineGroups:
        if group.permission in g.permissions:
            permissions_applied.append(group.permission)
            for beamline in group.beamlines:
                if (beamline.archived and includeArchived) or not includeArchived:
                    beamlines.append(beamline.beamlineName)

    if beamlines:
        print(
            f"filtered to beamlines `{beamlines}` with permissions `{permissions_applied}`"
        )
        return query.filter(models.BLSession.beamLineName.in_(beamlines))
    else:
        print("No beamline groups, filtering by session_has_person")
        return with_auth_to_session_has_person(query)

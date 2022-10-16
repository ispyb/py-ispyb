import logging
from typing import Optional, Any

import sqlalchemy
from sqlalchemy.orm import joinedload
from ispyb import models

from pyispyb.app.globals import g
from pyispyb.app.extensions.database.middleware import db
from ...extensions.options.schema import BeamLineGroup

logger = logging.getLogger(__name__)

_session = sqlalchemy.func.concat(
    models.Proposal.proposalCode,
    models.Proposal.proposalNumber,
    "-",
    models.BLSession.visit_number,
).label("session")

_proposal = sqlalchemy.func.concat(
    models.Proposal.proposalCode, models.Proposal.proposalNumber
).label("proposal")


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


def with_authorization(
    query: "sqlalchemy.orm.Query[Any]",
    includeArchived: bool = False,
    proposalColumn: "sqlalchemy.Column[Any]" = None,
    joinBLSession: bool = True,
) -> "sqlalchemy.orm.Query[Any]":
    """Apply authorization to a query

    Checks in the following order:
        * `all_proposals` allowing access to everything
        * checks if the user is in a beamLineGroup to allow access to all proposals on a beamline
        * checks ProposalHasPerson
        * falls back to SessionHasPerson allowing access to entities related to where the
            user is registered on a session

    Kwargs:
        includeArchived: whether to exclude archived beamlines
        proposalColumn: the column used to join to `models.Proposal`, will force a join with `models.Proposal`
        joinBLSession: whether to join `models.BLSession`
        joinSessionHasPerson: whether to join `models.SessionHasPerson`
    """
    # Avoid circular import
    from pyispyb.app.main import app

    # `all_proposals`` can access all sessions
    if "all_proposals" in g.permissions:
        logger.info("user has `all_proposals`")
        return query

    # Iterate through users permissions and match them to the relevant groups
    beamLines = []
    permissions_applied = []
    for group in app.db_options.beamLineGroups:
        if group.permission in g.permissions:
            permissions_applied.append(group.permission)
            for beamLine in group.beamLines:
                if (beamLine.archived and includeArchived) or not includeArchived:
                    beamLines.append(beamLine.beamLineName)

    if proposalColumn:
        query = query.join(
            models.Proposal, models.Proposal.proposalId == proposalColumn
        )

    if joinBLSession:
        query = query.outerjoin(
            models.BLSession, models.BLSession.proposalId == models.Proposal.proposalId
        )

    conditions = []
    if beamLines:
        logger.info(
            f"filtered to beamlines `{beamLines}` with permissions `{permissions_applied}`"
        )

        conditions.append(models.BLSession.beamLineName.in_(beamLines))

    # Sessions
    sessions = db.session.query(models.SessionHasPerson.sessionId).filter(
        models.SessionHasPerson.personId == g.personId
    )
    sessions = [r._asdict()["sessionId"] for r in sessions.all()]
    conditions.append(models.BLSession.sessionId.in_(sessions if sessions else []))

    # Proposals
    proposals = db.session.query(models.ProposalHasPerson.proposalId).filter(
        models.ProposalHasPerson.personId == g.personId
    )
    proposals = [r._asdict()["proposalId"] for r in proposals.all()]
    conditions.append(models.Proposal.proposalId.in_(proposals if proposals else []))

    query = query.filter(sqlalchemy.or_(*conditions))
    return query


def groups_from_beamlines(beamLines: list[str]) -> list[list]:
    """Get uiGroups from a list of beamlines"""
    from pyispyb.app.main import app

    groups = []
    for beamline in beamLines:
        for group in app.db_options.beamLineGroups:
            for groupBeamline in group.beamLines:
                if beamline == groupBeamline.beamLineName:
                    groups.append(group.uiGroup)

    return list(set(groups))


def beamlines_from_group(beamLineGroup: str) -> list[str]:
    """Get a list of beamlines from a groupName"""
    from pyispyb.app.main import app

    for group in app.db_options.beamLineGroups:
        if group.groupName == beamLineGroup:
            return [beamline.beamLineName for beamline in group.beamLines]

    return []

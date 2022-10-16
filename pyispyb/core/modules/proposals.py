from typing import Optional

from sqlalchemy import or_, func, distinct
from sqlalchemy.orm import joinedload
from ispyb import models

from ...app.extensions.database.utils import Paged, page, with_metadata
from ...app.extensions.database.middleware import db
from ...app.extensions.database.definitions import (
    groups_from_beamlines,
    with_authorization,
)


def get_proposals(
    skip: int,
    limit: int,
    proposalId: Optional[int] = None,
    proposalCode: Optional[str] = None,
    proposalNumber: Optional[str] = None,
    proposal: Optional[str] = None,
    search: Optional[str] = None,
    withAuthorization: bool = True,
) -> Paged[models.Proposal]:
    metadata = {
        "persons": func.count(distinct(models.ProposalHasPerson.personId)),
        "sessions": func.count(distinct(models.BLSession.sessionId)),
        "beamLines": func.group_concat(distinct(models.BLSession.beamLineName)),
    }

    query = (
        db.session.query(models.Proposal, *metadata.values())
        .options(joinedload(models.Proposal.Person))
        .outerjoin(models.BLSession)
        .outerjoin(models.ProposalHasPerson)
        .order_by(models.Proposal.proposalId.desc())
        .group_by(models.Proposal.proposalId)
    )

    if proposalId:
        query = query.filter(models.Proposal.proposalId == proposalId)

    if proposal:
        query = query.filter(models.Proposal.proposal == proposal)

    if proposalCode and proposalNumber:
        query = query.filter(models.Proposal.proposalCode == proposalCode)
        query = query.filter(models.Proposal.proposalNumber == proposalNumber)

    if search:
        query = query.filter(
            or_(
                models.Proposal.title.like(f"%{search}%"),
                models.BLSession.beamLineName.like(search),
                models.Proposal.proposal.like(f"%{search}%"),
            )
        )

    if withAuthorization:
        query = with_authorization(query, joinBLSession=False)

    total = query.count()
    query = page(query, skip=skip, limit=limit)
    results = with_metadata(query.all(), list(metadata.keys()))

    for result in results:
        result._metadata["beamLines"] = (
            result._metadata["beamLines"].split(",")
            if result._metadata["beamLines"]
            else []
        )

        result._metadata["uiGroups"] = groups_from_beamlines(
            result._metadata["beamLines"]
        )

    return Paged(total=total, results=results, skip=skip, limit=limit)


def get_proposalHasPerson(
    skip: int,
    limit: int,
    proposalId: Optional[int] = None,
) -> Paged[models.ProposalHasPerson]:

    query = db.session.query(models.ProposalHasPerson).options(
        joinedload(models.ProposalHasPerson.Person)
    )

    if proposalId:
        query = query.filter(models.ProposalHasPerson.proposalId == proposalId)

    query_distinct = query.distinct()
    total = query_distinct.count()
    query = page(query_distinct, skip=skip, limit=limit)

    return Paged(total=total, results=query.all(), skip=skip, limit=limit)

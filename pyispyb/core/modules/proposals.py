from typing import Any, Optional

from sqlalchemy import or_
from sqlalchemy.orm import joinedload, contains_eager
from ispyb import models

from ...app.extensions.database.utils import Paged, page
from ...app.extensions.database.middleware import db
from ...app.extensions.database.definitions import (
    groups_from_beamlines,
    with_beamline_groups,
)


def get_proposals(
    skip: int,
    limit: int,
    proposalId: Optional[int] = None,
    proposalCode: Optional[str] = None,
    proposalNumber: Optional[str] = None,
    proposalHasPerson: Optional[bool] = False,
    proposal: Optional[str] = None,
    search: Optional[str] = None,
    beamlineGroups: Optional[dict[str, Any]] = None,
) -> Paged[models.Proposal]:
    query = (
        db.session.query(models.Proposal)
        .options(joinedload(models.Proposal.Person))
        .outerjoin(models.BLSession)
        .options(
            contains_eager(models.Proposal.BLSession).load_only(
                models.BLSession.beamLineName
            )
        )
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

    if proposalHasPerson:
        query = (
            query.outerjoin(
                models.ProposalHasPerson,
                models.Proposal.proposalId == models.ProposalHasPerson.proposalId,
            )
            .options(contains_eager("ProposalHasPerson"))
            .outerjoin(
                models.Person,
                models.ProposalHasPerson.personId == models.Person.personId,
            )
            .options(contains_eager("ProposalHasPerson.Person"))
            .distinct()
        )

    if beamlineGroups:
        query = with_beamline_groups(query, beamlineGroups, joinBLSession=False)

    total = query.count()
    query = page(query, skip=skip, limit=limit)
    results = query.all()

    for result in results:
        result._metadata["sessions"] = len(result.BLSession)
        result._metadata["beamlines"] = list(
            set([session.beamLineName for session in result.BLSession])
        )
        if beamlineGroups:
            result._metadata["groups"] = groups_from_beamlines(
                beamlineGroups, result._metadata["beamlines"]
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

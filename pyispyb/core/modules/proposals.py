from typing import Optional
from sqlalchemy.orm import joinedload
from ispyb import models
from pyispyb.app.extensions.database.utils import Paged, page
from pyispyb.app.extensions.database.middleware import db


def get_proposals(
    skip: int,
    limit: int,
    proposalId: Optional[int] = None,
    proposalCode: Optional[str] = None,
    proposalNumber: Optional[str] = None,
) -> Paged[models.Proposal]:

    query = db.session.query(models.Proposal).options(
        joinedload(models.Proposal.Person)
    )

    if proposalId:
        query = query.filter(models.Proposal.proposalId == proposalId)

    if proposalCode and proposalNumber:
        query = query.filter(models.Proposal.proposalCode == proposalCode)
        query = query.filter(models.Proposal.proposalNumber == proposalNumber)

    # https://github.com/aiidateam/aiida-core/issues/1600
    query_distinct = query.distinct()
    total = query_distinct.count()
    query = page(query_distinct, skip=skip, limit=limit)

    return Paged(total=total, results=query.all(), skip=skip, limit=limit)


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

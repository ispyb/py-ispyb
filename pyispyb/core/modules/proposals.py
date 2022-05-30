from typing import Optional
from sqlalchemy.orm import joinedload
from pyispyb.core import models
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

    total = query.count()
    query = page(query, skip=skip, limit=limit)

    return Paged(total=total, results=query.all(), skip=skip, limit=limit)

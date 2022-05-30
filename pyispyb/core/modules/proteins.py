from typing import Optional
from sqlalchemy.orm import joinedload
from pyispyb.core import models
from pyispyb.app.extensions.database.utils import Paged, page
from pyispyb.app.extensions.database.middleware import db


def get_proteins(
    skip: int,
    limit: int,
    proteinId: Optional[int] = None,
    proposalId: Optional[int] = None,
    name: Optional[str] = None,
) -> Paged[models.Protein]:
    query = db.session.query(models.Protein).options(
        joinedload(models.Protein.Proposal)
    )

    if proteinId:
        query = query.filter(models.Protein.proteinId == proteinId)

    if name:
        query = query.filter(models.Protein.name == name)

    if proposalId:
        query = query.filter(models.Protein.proposalId == proposalId)

    total = query.count()
    query = page(query, skip=skip, limit=limit)

    return Paged(total=total, results=query.all(), skip=skip, limit=limit)

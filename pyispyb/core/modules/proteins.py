from typing import Optional
from sqlalchemy.orm import joinedload
from ispyb import models
from pyispyb.app.extensions.database.utils import Paged, page
from pyispyb.app.extensions.database.middleware import db
from pyispyb.core.modules.utils import encode_external_id


def get_proteins(
    skip: int,
    limit: int,
    proteinId: Optional[int] = None,
    proposalId: Optional[int] = None,
    externalId: Optional[int] = None,
    name: Optional[str] = None,
    acronym: Optional[str] = None,
) -> Paged[models.Protein]:
    query = db.session.query(models.Protein).options(
        joinedload(models.Protein.Proposal)
    )

    if proteinId:
        query = query.filter(models.Protein.proteinId == proteinId)

    if name:
        query = query.filter(models.Protein.name == name)

    if acronym:
        query = query.filter(models.Protein.acronym == acronym)

    if proposalId:
        query = query.filter(models.Protein.proposalId == proposalId)

    if externalId:
        externalId = encode_external_id(externalId)
        query = query.filter(models.Protein.externalId == externalId)

    total = query.count()
    query = page(query, skip=skip, limit=limit)

    return Paged(total=total, results=query.all(), skip=skip, limit=limit)

from typing import Any, Optional

from sqlalchemy import or_, func
from sqlalchemy.orm import joinedload, contains_eager
from ispyb import models


from ...app.extensions.database.utils import Paged, page, with_metadata, order
from ...app.extensions.database.middleware import db
from ...app.extensions.database.definitions import with_beamline_groups
from ...core.modules.utils import encode_external_id


ORDER_BY_MAP = {
    "proteinId": models.Protein.proteinId,
    "acronym": models.Protein.acronym,
    "name": models.Protein.name,
}


def get_proteins(
    skip: int,
    limit: int,
    proteinId: Optional[int] = None,
    proposalId: Optional[int] = None,
    proposal: Optional[str] = None,
    externalId: Optional[int] = None,
    name: Optional[str] = None,
    acronym: Optional[str] = None,
    search: Optional[str] = None,
    sort_order: Optional[dict[str, str]] = None,
    beamlineGroups: Optional[dict[str, Any]] = None,
) -> Paged[models.Protein]:
    metadata = {
        "pdbs": func.count(models.ProteinHasPDB.proteinid),
        "samples": func.count(models.BLSample.blSampleId),
        "crystals": func.count(models.Crystal.crystalId),
    }

    query = (
        db.session.query(models.Protein, *metadata.values())
        .options(joinedload(models.Protein.Proposal))
        .join(models.Proposal)
        # .outerjoin(
        #     models.ConcentrationType,
        #     models.ConcentrationType.concentrationTypeId
        #     == models.Protein.concentrationTypeId,
        # )
        # .options(contains_eager(models.Protein.ConcentrationType))
        .outerjoin(models.ComponentType)
        .options(contains_eager(models.Protein.ComponentType))
        .outerjoin(models.ProteinHasPDB)
        .outerjoin(models.Crystal)
        .outerjoin(models.BLSample)
        .group_by(models.Protein.proteinId)
    )

    if beamlineGroups:
        query = with_beamline_groups(query, beamlineGroups)

    if proteinId:
        query = query.filter(models.Protein.proteinId == proteinId)

    if name:
        query = query.filter(models.Protein.name == name)

    if acronym:
        query = query.filter(models.Protein.acronym == acronym)

    if proposalId:
        query = query.filter(models.Protein.proposalId == proposalId)

    if proposal:
        query = query.filter(models.Proposal.proposal == proposal)

    if externalId:
        externalId = encode_external_id(externalId)
        query = query.filter(models.Protein.externalId == externalId)

    if search:
        query = query.filter(
            or_(
                models.Protein.name.like(f"%{search}%"),
                models.Protein.acronym.like(f"%{search}%"),
            )
        )

    if sort_order:
        query = order(query, ORDER_BY_MAP, sort_order)

    total = query.count()
    query = page(query, skip=skip, limit=limit)

    results = with_metadata(query.all(), list(metadata.keys()))
    return Paged(total=total, results=results, skip=skip, limit=limit)

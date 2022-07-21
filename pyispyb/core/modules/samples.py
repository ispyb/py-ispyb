from typing import Any, Optional

from sqlalchemy.orm import contains_eager
from sqlalchemy.sql.expression import func, distinct
from ispyb import models

from ...app.extensions.database.definitions import with_beamline_groups, _session
from ...app.extensions.database.middleware import db
from ...app.extensions.database.utils import Paged, page, with_metadata


def get_samples(
    skip: int,
    limit: int,
    blSampleId: Optional[int] = None,
    proteinId: Optional[int] = None,
    session: Optional[str] = None,
    containerId: Optional[int] = None,
    beamlineGroups: Optional[dict[str, Any]] = None,
) -> Paged[models.BLSample]:
    metadata = {
        "subsamples": func.count(distinct(models.BLSubSample.blSubSampleId)),
        "datacollections": func.count(distinct(models.DataCollection.dataCollectionId)),
    }

    query = (
        db.session.query(models.BLSample, *metadata.values())
        .join(models.BLSample.Crystal)
        .options(
            contains_eager(models.BLSample.Crystal).load_only(
                models.Crystal.cell_a,
                models.Crystal.cell_b,
                models.Crystal.cell_c,
                models.Crystal.cell_alpha,
                models.Crystal.cell_beta,
                models.Crystal.cell_gamma,
            )
        )
        .join(models.Crystal.Protein)
        .options(
            contains_eager("Crystal.Protein").load_only("name", "acronym"),
        )
        .outerjoin(
            models.BLSubSample,
            models.BLSubSample.blSampleId == models.BLSample.blSampleId,
        )
        .outerjoin(
            models.DataCollectionGroup,
            models.DataCollectionGroup.blSampleId == models.BLSample.blSampleId,
        )
        .outerjoin(
            models.DataCollection,
            models.DataCollectionGroup.dataCollectionGroupId
            == models.DataCollection.dataCollectionGroupId,
        )
        .join(
            models.Container,
            models.BLSample.containerId == models.Container.containerId,
        )
        .join(models.Dewar, models.Container.dewarId == models.Dewar.dewarId)
        .join(models.Shipping, models.Dewar.shippingId == models.Shipping.shippingId)
        .group_by(models.BLSample.blSampleId)
    )

    if beamlineGroups:
        query = with_beamline_groups(
            query, beamlineGroups, proposalColumn=models.Shipping.proposalId
        )

    if blSampleId:
        query = query.filter(models.BLSample.blSampleId == blSampleId)

    if proteinId:
        query = query.filter(models.Protein.proteinId == proteinId)

    if containerId:
        query = query.filter(models.Container.containerId == containerId)

    if session:
        query = query.filter(_session == session)

    total = query.count()
    query = page(query, skip=skip, limit=limit)
    results = with_metadata(query.all(), list(metadata.keys()))

    return Paged(total=total, results=results, skip=skip, limit=limit)

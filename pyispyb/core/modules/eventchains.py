from sqlalchemy.orm import joinedload

from ispyb import models

from pyispyb.app.extensions.database.middleware import db
from pyispyb.app.extensions.database.definitions import with_authorization
from pyispyb.app.extensions.database.utils import Paged, page


def get_datacollection_eventchains(
    dataCollectionId: int,
    skip: int,
    limit: int,
) -> list[models.EventChain]:
    query = (
        db.session.query(models.EventChain)
        .filter(models.EventChain.dataCollectionId == dataCollectionId)
        .options(joinedload(models.EventChain.events))
        .join(
            models.DataCollection,
            models.EventChain.dataCollectionId
            == models.DataCollection.dataCollectionId,
        )
        .join(
            models.DataCollectionGroup,
            models.DataCollection.dataCollectionGroupId
            == models.DataCollectionGroup.dataCollectionGroupId,
        )
        .join(
            models.BLSession,
            models.DataCollectionGroup.sessionId == models.BLSession.sessionId,
        )
        .join(
            models.Proposal, models.BLSession.proposalId == models.Proposal.proposalId
        )
    )

    query = with_authorization(query, joinBLSession=False)

    total = query.count()
    query = page(query, skip=skip, limit=limit)

    return Paged(total=total, results=query.all(), skip=skip, limit=limit)

from sqlalchemy.orm import joinedload

from ispyb import models

from pyispyb.app.extensions.database.middleware import db
from pyispyb.app.extensions.database.definitions import with_authorization


def get_ssx_datacollection_eventchains(
    dataCollectionId: int,
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
            models.BLSession,
            models.DataCollection.sessionId == models.BLSession.sessionId,
        )
        .join(
            models.Proposal, models.BLSession.proposalId == models.Proposal.proposalId
        )
    )

    query = with_authorization(query, joinBLSession=False)

    return query.all()

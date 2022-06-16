from typing import Optional


from pyispyb.core import models
from pyispyb.app.extensions.database.middleware import db

from sqlalchemy.orm import joinedload


def get_ssx_datacollection(
    ssxDataCollectionId: int,
) -> Optional[models.SSXDataCollection]:
    dc = (
        db.session.query(models.SSXDataCollection)
        .options(joinedload(models.SSXDataCollection.DataCollection))
        .filter(models.SSXDataCollection.ssxDataCollectionId == ssxDataCollectionId)
        .first()
    )

    return dc

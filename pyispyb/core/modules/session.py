from ispyb import models
from pyispyb.app.extensions.database.middleware import db

from sqlalchemy.orm import joinedload


def get_session(
    sessionId: int,
) -> list[models.BLSession]:
    dc = (
        db.session.query(models.BLSession)
        .options(joinedload(models.BLSession.BeamLineSetup))
        .filter(models.BLSession.sessionId == sessionId)
        .first()
    )

    return dc

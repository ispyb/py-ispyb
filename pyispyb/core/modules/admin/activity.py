from typing import Optional

from ispyb import models

from ....app.extensions.database.middleware import db
from ....app.extensions.database.utils import Paged, page
from ...schemas.admin.activity import ActionType


def get_activity(
    skip: int, limit: int, action_type: Optional[ActionType] = None
) -> Paged[models.AdminActivity]:
    """Get admin activity"""
    query = db.session.query(models.AdminActivity).order_by(
        models.AdminActivity.dateTime.desc()
    )

    if action_type:
        query = query.filter(models.AdminActivity.action == action_type.value)

    total = query.count()
    query = page(query, skip=skip, limit=limit)

    return Paged(total=total, results=query.all(), skip=skip, limit=limit)

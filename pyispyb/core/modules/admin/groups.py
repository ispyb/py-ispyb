from typing import Optional

from ispyb import models

from ....app.extensions.database.utils import Paged, page
from ....app.extensions.database.middleware import db
from ...schemas.admin import groups as schema


def get_groups(
    skip: int,
    limit: int,
) -> Paged[models.UserGroup]:
    query = db.session.query(models.UserGroup)

    total = query.count()
    query = page(query, skip=skip, limit=limit)

    return Paged(total=total, results=query.all(), skip=skip, limit=limit)


def add_group(group: schema.UserGroup):
    pass


def update_group(group: schema.UserGroup):
    pass


def get_permissions(skip: int, limit: int, userGroupId: Optional[int] = None):
    pass


def add_permission(permission: schema.Permission):
    pass


def update_permission(permissionId: int, permission: schema.Permission):
    pass

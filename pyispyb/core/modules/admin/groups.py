from typing import Optional

from sqlalchemy import func, distinct
from ispyb import models

from ....app.extensions.database.utils import Paged, page, with_metadata
from ....app.extensions.database.middleware import db
from ...schemas.admin import groups as schema


def get_groups(
    skip: int,
    limit: int,
) -> Paged[models.UserGroup]:
    metadata = {
        "permissions": func.count(distinct(models.Permission.permissionId)),
        "people": func.count(distinct(models.Person.personId)),
    }

    query = (
        db.session.query(models.UserGroup, *metadata.values())
        .outerjoin(models.UserGroup.Permission)
        .outerjoin(models.UserGroup.Person)
        .group_by(models.UserGroup.userGroupId)
    )

    total = query.count()
    query = page(query, skip=skip, limit=limit)
    results = with_metadata(query.all(), list(metadata.keys()))

    return Paged(total=total, results=results, skip=skip, limit=limit)


def add_group(group: schema.UserGroup):
    pass


def update_group(group: schema.UserGroup):
    pass


def get_permissions(
    skip: int,
    limit: int,
    userGroupId: Optional[int] = None,
    search: Optional[str] = None,
):
    query = db.session.query(models.Permission)

    if userGroupId:
        query = query.join(models.UserGroup).filter(
            models.UserGroup.userGroupId == userGroupId
        )

    if search:
        query = query.filter(models.Permission.type.like(f"%{search}%"))

    total = query.count()
    query = page(query, skip=skip, limit=limit)

    return Paged(total=total, results=query.all(), skip=skip, limit=limit)


def add_permission(permission: schema.Permission):
    pass


def update_permission(permissionId: int, permission: schema.Permission):
    pass

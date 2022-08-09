from typing import Optional

from sqlalchemy import func, distinct
from sqlalchemy.orm import joinedload
from ispyb import models

from ....app.extensions.database.utils import Paged, page, with_metadata
from ....app.extensions.database.middleware import db
from ...schemas.admin import groups as schema


def get_groups(
    skip: int,
    limit: int,
    userGroupId: Optional[int] = None,
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

    if userGroupId:
        query = query.filter(models.UserGroup.userGroupId == userGroupId)

    total = query.count()
    query = page(query, skip=skip, limit=limit)
    results = with_metadata(query.all(), list(metadata.keys()))

    return Paged(total=total, results=results, skip=skip, limit=limit)


def add_group(group: schema.NewUserGroup) -> Optional[models.UserGroup]:
    check = (
        db.session.query(models.UserGroup)
        .filter(models.UserGroup.name == group.name)
        .first()
    )
    if check:
        raise AttributeError(f"UserGroup `{group.name}` already exists")

    userGroup = models.UserGroup(**group.dict())
    db.session.add(userGroup)
    db.session.commit()

    userGroups = get_groups(userGroupId=userGroup.userGroupId, skip=0, limit=1)
    return userGroups.first


def update_group(userGroupId: int, group: schema.UserGroup):
    userGroup = (
        db.session.query(models.UserGroup)
        .filter(models.UserGroup.userGroupId == userGroupId)
        .first()
    )

    if not userGroup:
        raise FileNotFoundError()

    group_dict = group.dict(exclude_unset=True)
    for key in ["name"]:
        if key in group_dict:
            setattr(userGroup, key, group_dict[key])

    db.session.commit()

    updatedUserGroups = get_groups(userGroupId=userGroup.userGroupId, skip=0, limit=1)
    return updatedUserGroups.first


def add_person_to_group(personId: int, userGroupId: int) -> None:
    person = (
        db.session.query(models.Person)
        .filter(models.Person.personId == personId)
        .first()
    )
    userGroup = (
        db.session.query(models.UserGroup)
        .options(joinedload(models.UserGroup.Person))
        .filter(models.UserGroup.userGroupId == userGroupId)
        .first()
    )

    if not person:
        raise AttributeError(f"Person `{personId}` does not exist")

    if not userGroup:
        raise AttributeError(f"UserGroup `{userGroupId}` does not exist")

    if person in userGroup.Person:
        raise AttributeError(
            f"UserGroup `{userGroupId}` already contains person `{personId}`"
        )

    userGroup.Person.append(person)
    db.session.commit()


def remove_person_from_group(personId: int, userGroupId: int) -> None:
    person = (
        db.session.query(models.Person)
        .filter(models.Person.personId == personId)
        .first()
    )
    userGroup = (
        db.session.query(models.UserGroup)
        .options(joinedload(models.UserGroup.Person))
        .filter(models.UserGroup.userGroupId == userGroupId)
        .first()
    )

    if not person:
        raise AttributeError(f"Person `{personId}` does not exist")

    if not userGroup:
        raise AttributeError(f"UserGroup `{userGroupId}` does not exist")

    userGroup.Person.remove(person)
    db.session.commit()


def add_permission_to_group(permissionId: int, userGroupId: int) -> None:
    permission = (
        db.session.query(models.Permission)
        .filter(models.Permission.permissionId == permissionId)
        .first()
    )
    userGroup = (
        db.session.query(models.UserGroup)
        .options(joinedload(models.UserGroup.Permission))
        .filter(models.UserGroup.userGroupId == userGroupId)
        .first()
    )

    if not permission:
        raise AttributeError(f"Permission `{permissionId}` does not exist")

    if not userGroup:
        raise AttributeError(f"UserGroup `{userGroupId}` does not exist")

    if permission in userGroup.Permission:
        raise AttributeError(
            f"UserGroup `{userGroupId}` already contains permission `{permissionId}`"
        )

    userGroup.Permission.append(permission)
    db.session.commit()


def remove_permission_from_group(permissionId: int, userGroupId: int) -> None:
    permission = (
        db.session.query(models.Permission)
        .filter(models.Permission.permissionId == permissionId)
        .first()
    )
    userGroup = (
        db.session.query(models.UserGroup)
        .options(joinedload(models.UserGroup.Permission))
        .filter(models.UserGroup.userGroupId == userGroupId)
        .first()
    )

    if not permission:
        raise AttributeError(f"Permission `{permissionId}` does not exist")

    if not userGroup:
        raise AttributeError(f"UserGroup `{userGroupId}` does not exist")

    userGroup.Person.remove(permission)
    db.session.commit()


def get_permissions(
    skip: int,
    limit: int,
    permissionId: Optional[int] = None,
    userGroupId: Optional[int] = None,
    search: Optional[str] = None,
):
    query = db.session.query(models.Permission)

    if permissionId:
        query = query.filter(models.Permission.permissionId == permissionId)

    if userGroupId:
        query = query.join(models.Permission.UserGroup).filter(
            models.UserGroup.userGroupId == userGroupId
        )

    if search:
        query = query.filter(models.Permission.type.like(f"%{search}%"))

    total = query.count()
    query = page(query, skip=skip, limit=limit)

    return Paged(total=total, results=query.all(), skip=skip, limit=limit)


def add_permission(permission: schema.NewPermission) -> models.Permission:
    check = (
        db.session.query(models.Permission)
        .filter(models.Permission.type == permission.type)
        .first()
    )
    if check:
        raise AttributeError(f"Permission type `{permission.type}` already exists")

    permissionModel = models.Permission(**permission.dict())
    db.session.add(permissionModel)
    db.session.commit()

    return permissionModel


def update_permission(
    permissionId: int, permission: schema.Permission
) -> models.Permission:
    permissionModel = (
        db.session.query(models.Permission)
        .filter(models.Permission.permissionId == permissionId)
        .first()
    )

    if not permissionModel:
        raise FileNotFoundError()

    permission_dict = permission.dict(exclude_unset=True)
    for key in ["type", "description"]:
        if key in permission_dict:
            setattr(permissionModel, key, permission_dict[key])

    db.session.commit()

    return permissionModel

from fastapi import Depends, status

from ....dependencies import pagination, permission
from ....core.schemas.utils import paginated
from ...modules.admin import groups as crud
from ...schemas.admin import groups as schema
from .... import filters
from .base import router


# Groups
@router.get(
    "/groups",
    response_model=paginated(schema.UserGroup),
)
def get_groups(
    page: dict[str, int] = Depends(pagination),
    depends=Depends(permission("manage_groups")),
):
    return crud.get_groups(**page)


@router.post(
    "/groups",
    response_model=schema.UserGroup,
)
def add_group(group: schema.NewUserGroup, depends=Depends(permission("manage_groups"))):
    return crud.add_group(group)


@router.patch(
    "/groups/{userGroupId}",
    response_model=schema.UserGroup,
)
def update_group(group: schema.UserGroup, depends=Depends(permission("manage_groups"))):
    pass


# Group Permissions
@router.post(
    "/groups/{userGroupId}/permission/{permissionId}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        204: {"description": "Added permission to group"},
        400: {"description": "Could not add permission to group"},
    },
)
def add_permission_to_group(depends=Depends(permission("manage_groups"))):
    pass


@router.delete(
    "/groups/{userGroupId}/permission/{permissionId}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        204: {"description": "Permission removed from group"},
        400: {"description": "Could not remove permission from group"},
    },
)
def remove_permission_from_group(depends=Depends(permission("manage_groups"))):
    pass


# Group People
@router.post(
    "/groups/{userGroupId}/person",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        204: {"description": "Added person to group"},
        400: {"description": "Could not add person to group"},
    },
)
def add_person_to_group(depends=Depends(permission("manage_groups"))):
    pass


@router.delete(
    "/groups/{userGroupId}/person/{personId}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        204: {"description": "Person removed from group"},
        400: {"description": "Could not remove person from group"},
    },
)
def remove_person_from_group(depends=Depends(permission("manage_groups"))):
    pass


# Permissions
@router.get(
    "/permissions",
    response_model=paginated(schema.Permission),
)
def get_permissions(
    userGroupId: int = Depends(filters.userGroupId),
    search: int = Depends(filters.search),
    page: dict[str, int] = Depends(pagination),
    depends=Depends(permission("manage_perms")),
):
    return crud.get_permissions(userGroupId=userGroupId, search=search, **page)


@router.post(
    "/permissions",
    response_model=schema.NewPermission,
)
def add_permission(
    permission: schema.Permission, depends=Depends(permission("manage_perms"))
):
    pass


@router.patch(
    "/permissions/{permissionId}",
    response_model=schema.Permission,
)
def update_permission(
    permission: schema.Permission, depends=Depends(permission("manage_perms"))
):
    pass

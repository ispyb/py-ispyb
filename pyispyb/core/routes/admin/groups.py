from fastapi import Depends, HTTPException, status

from ....dependencies import pagination, permission
from ....core.schemas.utils import paginated
from ...modules.admin import groups as crud
from ...schemas.admin import groups as schema
from ...schemas.utils import make_optional
from .... import filters
from .base import router

# eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImVmZ2giLCJncm91cHMiOlsibWFuYWdlX2dyb3VwcyIsIm1hbmFnZV9wZXJtcyJdLCJwZXJtaXNzaW9ucyI6WyJtYW5hZ2VfZ3JvdXBzIiwibWFuYWdlX3Blcm1zIl0sImlhdCI6MTY1ODQwNTk1MiwiZXhwIjoxNjU4NDIzOTUyfQ.B67vMH2BvAVhwd5ZyaagmjtV8O5ydWnPVlZgwjQbpS0

# Groups
@router.get(
    "/groups",
    response_model=paginated(schema.UserGroup),
)
def get_groups(
    userGroupId: int = Depends(filters.userGroupId),
    page: dict[str, int] = Depends(pagination),
    depends=Depends(permission("manage_groups")),
):
    """Get a list of UserGroups"""
    return crud.get_groups(userGroupId=userGroupId, **page)


@router.post(
    "/groups",
    response_model=schema.UserGroup,
)
def add_group(group: schema.NewUserGroup, depends=Depends(permission("manage_groups"))):
    """Add a new UserGroup"""
    try:
        return crud.add_group(group)
    except Exception as e:
        raise HTTPException(
            status_code=400, detail=f"Could not add new group: `{str(e)}`"
        )


@router.patch(
    "/groups/{userGroupId}",
    response_model=schema.UserGroup,
)
def update_group(
    userGroupId: int,
    userGroup: make_optional(schema.NewUserGroup),
    depends=Depends(permission("manage_groups")),
):
    """Update a UserGroup"""
    try:
        return crud.update_group(userGroupId, userGroup)
    except Exception as e:
        raise HTTPException(
            status_code=400, detail=f"Could not update group: `{str(e)}`"
        )


# Group Permissions
@router.post(
    "/groups/{userGroupId}/permission/{permissionId}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        204: {"description": "Added permission to group"},
        400: {"description": "Could not add permission to group"},
    },
)
def add_permission_to_group(
    userGroupId: int, permissionId: int, depends=Depends(permission("manage_groups"))
):
    """Add a Permission to a UserGroup"""
    try:
        crud.add_permission_to_group(permissionId, userGroupId)
        return status.HTTP_204_NO_CONTENT
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Could not add permission `{permissionId}` to group `{userGroupId}`: `{str(e)}`",
        )


@router.delete(
    "/groups/{userGroupId}/permission/{permissionId}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        204: {"description": "Permission removed from group"},
        400: {"description": "Could not remove permission from group"},
    },
)
def remove_permission_from_group(
    userGroupId: int, permissionId: int, depends=Depends(permission("manage_groups"))
):
    """Remove a Permission from a UserGroup"""
    try:
        crud.remove_permission_from_group(permissionId, userGroupId)
        return status.HTTP_204_NO_CONTENT
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Could not remove permission `{permissionId}` from group `{userGroupId}`: `{str(e)}`",
        )


# Group People
@router.post(
    "/groups/{userGroupId}/person/{personId}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        204: {"description": "Added person to group"},
        400: {"description": "Could not add person to group"},
    },
)
def add_person_to_group(
    userGroupId: int, personId: int, depends=Depends(permission("manage_groups"))
):
    """Add a Person to a UserGroup"""
    try:
        crud.add_person_to_group(personId, userGroupId)
        return status.HTTP_204_NO_CONTENT
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Could not add person `{personId}` to group `{userGroupId}`: `{str(e)}`",
        )


@router.delete(
    "/groups/{userGroupId}/person/{personId}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        204: {"description": "Person removed from group"},
        400: {"description": "Could not remove person from group"},
    },
)
def remove_person_from_group(
    userGroupId: int, personId: int, depends=Depends(permission("manage_groups"))
):
    """Remove a Person from a UserGroup"""
    try:
        crud.remove_person_from_group(personId, userGroupId)
        return status.HTTP_204_NO_CONTENT
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Could not remove person `{personId}` from group `{userGroupId}`: `{str(e)}`",
        )


# Permissions
@router.get(
    "/permissions",
    response_model=paginated(schema.Permission),
)
def get_permissions(
    permissionId: int = Depends(filters.permissionId),
    userGroupId: int = Depends(filters.userGroupId),
    search: int = Depends(filters.search),
    page: dict[str, int] = Depends(pagination),
    depends=Depends(permission("manage_perms")),
):
    """Get a list of Permissions"""
    return crud.get_permissions(
        permissionId=permissionId, userGroupId=userGroupId, search=search, **page
    )


@router.post(
    "/permissions",
    response_model=schema.Permission,
)
def add_permission(
    permission: schema.NewPermission, depends=Depends(permission("manage_perms"))
):
    """Add a new Permission"""
    try:
        return crud.add_permission(permission)
    except Exception as e:
        raise HTTPException(
            status_code=400, detail=f"Could not add new permission: `{str(e)}`"
        )


@router.patch(
    "/permissions/{permissionId}",
    response_model=schema.Permission,
)
def update_permission(
    permissionId: int,
    permission: make_optional(schema.NewPermission),
    depends=Depends(permission("manage_perms")),
):
    """Update a Permission"""
    try:
        return crud.update_permission(permissionId, permission)
    except Exception as e:
        raise HTTPException(
            status_code=400, detail=f"Could not update group: `{str(e)}`"
        )

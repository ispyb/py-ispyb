from typing import Optional

from pydantic import BaseModel, Field, constr


class UserGroupMetaData(BaseModel):
    permissions: int = Field(description="Number of permissions")
    people: int = Field(description="Number of people")


class NewUserGroup(BaseModel):
    name: str = Field(title="Name", description="The name of the group")


class UserGroup(NewUserGroup):
    userGroupId: int

    metadata: UserGroupMetaData = Field(alias="_metadata")

    class Config:
        orm_mode = True


class NewUserGroupPermission(BaseModel):
    permissionId: int = Field(title="Permission")


class NewUserGroupPerson(BaseModel):
    personId: int = Field(title="Person")


class NewPermission(BaseModel):
    type: constr(max_length=15) = Field(
        title="Permission", description="The permission identifier"
    )
    description: Optional[constr(max_length=100)] = Field(
        title="Description", description="Description of this permission"
    )


class Permission(NewPermission):
    permissionId: int

    class Config:
        orm_mode = True

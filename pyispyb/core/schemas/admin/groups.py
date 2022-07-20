from typing import Optional

from pydantic import BaseModel, Field, constr


class UserGroup(BaseModel):
    name: str = Field(title="Name", description="The name of the group")


class Permission(BaseModel):
    type: constr(max_length=15) = Field(
        title="Permission", description="The permission identifier"
    )
    description: Optional[constr(max_length=100)] = Field(
        title="Description", description="Description of this permission"
    )

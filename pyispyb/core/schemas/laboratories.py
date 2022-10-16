import datetime
from typing import Optional

# from pyispyb.core.schemas.validators import WordDashSpace
from pydantic import BaseModel, Field


class LaboratoryCreate(BaseModel):
    name: str = Field(title="Laboratory Name", description="The Laboratory name")
    address: str = Field(title="Address", description="The Laboratory Address")
    city: str = Field(title="City", description="The Laboratory City")
    country: str = Field(title="Country", description="The Laboratory Country")
    url: Optional[str] = Field(title="URL", description="The Laboratory optional URL")
    laboratoryExtPk: Optional[int] = Field(
        title="laboratoryExtPk", description="External Id from the User Portal"
    )
    recordTimeStamp: Optional[datetime.datetime] = Field(
        title="recordTimeStamp", description="Time Laboratory was created"
    )


class Laboratory(LaboratoryCreate):
    laboratoryId: int

    # Could be missing in db
    name: Optional[str] = Field(
        None, title="Laboratory Name", description="The Laboratory name"
    )
    address: Optional[str] = Field(
        None, title="Address", description="The Laboratory Address"
    )
    city: Optional[str] = Field(None, title="City", description="The Laboratory City")
    country: Optional[str] = Field(
        None, title="Country", description="The Laboratory Country"
    )

    class Config:
        orm_mode = True

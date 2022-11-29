from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class PersonMetaData(BaseModel):
    sessions: Optional[int] = Field(
        description="Number of sessions this person has been on"
    )
    lastSession: Optional[datetime] = Field(description="Last session date")
    role: Optional[str]
    remote: Optional[bool]


class Person(BaseModel):
    personId: int
    givenName: str
    familyName: str

    metadata: Optional[PersonMetaData] = Field(alias="_metadata")

    class Config:
        orm_mode = True

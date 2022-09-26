# import datetime
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class SessionType(BaseModel):
    typeName: str

    class Config:
        orm_mode = True


class SessionMetaData(BaseModel):
    datacollections: Optional[int] = Field(description="Number of datacollections")
    uiGroups: Optional[list[str]] = Field(description="UI groups for this session")
    persons: int = Field(description="Number of people registered on this session")
    active: bool = Field(description="Whether this session is active")
    active_soon: bool = Field(
        description="Whether this session is due to start soon or has ended recently (+/-20 min)"
    )


class SessionBase(BaseModel):
    proposalId: int
    session: str
    proposal: str
    visit_number: Optional[int]
    startDate: datetime
    endDate: datetime
    beamLineName: str
    beamLineOperator: Optional[str]
    scheduled: Optional[bool]


class Session(SessionBase):
    sessionId: int

    SessionType: list[SessionType]

    metadata: SessionMetaData = Field(alias="_metadata")

    class Config:
        orm_mode = True

# import datetime
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

from ispyb import models

s = models.BLSession


class SessionMetaData(BaseModel):
    datacollections: Optional[int] = Field(description="Number of datacollections")
    groups: Optional[list[str]] = Field(description="Beamline group for this session")
    persons: int = Field(description="Number of people registered on this session")
    active: bool = Field(description="Whether this session is active")
    active_soon: bool = Field(
        description="Whether this session is due to start soon or has ended recently (+/-20 min)"
    )


class SessionBase(BaseModel):
    proposalId: int
    session: str
    visit_number: Optional[int]
    startDate: datetime
    endDate: datetime
    beamLineName: str
    beamLineOperator: Optional[str]
    scheduled: bool

    metadata: SessionMetaData = Field(alias="_metadata")


class Session(SessionBase):
    sessionId: int

    class Config:
        orm_mode = True

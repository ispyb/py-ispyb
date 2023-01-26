# import datetime
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class SessionMetaData(BaseModel):
    datacollections: Optional[int] = Field(description="Number of datacollections")
    uiGroups: Optional[list[str]] = Field(description="UI groups for this session")
    persons: int = Field(
        description="Number of people registered on this session (via SessionHasPerson)"
    )
    active: bool = Field(description="Whether this session is active")
    active_soon: bool = Field(
        description="Whether this session is due to start soon or has ended recently (+/-20 min)"
    )
    sessionTypes: list[str] = Field(description="Session types for this session")


class BeamLineSetup(BaseModel):
    beamLineSetupId: int
    synchrotronMode: Optional[str]
    undulatorType1: Optional[str]
    undulatorType2: Optional[str]
    undulatorType3: Optional[str]
    focalSpotSizeAtSample: Optional[float]
    focusingOptic: Optional[str]
    beamDivergenceHorizontal: Optional[float]
    beamDivergenceVertical: Optional[float]
    polarisation: Optional[float]
    monochromatorType: Optional[str]
    setupDate: Optional[datetime]
    synchrotronName: Optional[str]
    maxExpTimePerDataCollection: Optional[float]
    minExposureTimePerImage: Optional[float]
    goniostatMaxOscillationSpeed: Optional[float]
    goniostatMinOscillationWidth: Optional[float]
    minTransmission: Optional[float]
    CS: Optional[float]

    class Config:
        orm_mode = True


class SessionBase(BaseModel):
    sessionId: int
    proposalId: int
    session: str
    proposal: str

    BeamLineSetup: Optional[BeamLineSetup]

    visit_number: Optional[int]
    startDate: datetime
    endDate: datetime
    beamLineName: str
    beamLineOperator: Optional[str]
    scheduled: Optional[bool]
    comments: Optional[str]
    nbReimbDewars: Optional[int]

    class Config:
        orm_mode = True


class Session(SessionBase):
    sessionId: int

    metadata: SessionMetaData = Field(alias="_metadata")

    class Config:
        orm_mode = True

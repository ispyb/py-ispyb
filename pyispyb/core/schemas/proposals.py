# import datetime
import enum
from typing import Optional

from pydantic import BaseModel, Field


class ProposalState(str, enum.Enum):
    Open = "Open"
    Closed = "Closed"
    Cancelled = "Cancelled"


class ProposalMetaData(BaseModel):
    sessions: int = Field(description="Number of sessions")
    beamlines: list[str] = Field(description="Beamlines allocated in this proposal")
    groups: Optional[list[str]] = Field(
        description="Beamline groups allocated in this proposal"
    )


class ProposalBase(BaseModel):
    proposalCode: str = Field(title="Proposal Code")
    proposalNumber: str = Field(title="Proposal Number")
    proposal: str
    title: str = Field(title="Proposal Title")
    state: Optional[ProposalState] = Field(title="Proposal State")

    metadata: ProposalMetaData = Field(alias="_metadata")


class Proposal(ProposalBase):
    proposalId: int

    class Config:
        orm_mode = True

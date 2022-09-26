from datetime import datetime
from typing import Union, Optional

from pydantic import BaseModel, Field

from .datacollections import DataCollection
from .robotactions import RobotAction


class EventBase(BaseModel):
    id: int
    type: str
    startTime: Optional[datetime] = Field(title="Start Time")
    endTime: Optional[datetime] = Field(title="End Time")
    count: int
    session: str
    proposal: str
    blSample: Optional[str] = Field(description="Sample Name")
    blSampleId: Optional[int] = Field(description="Sample Id")
    attachments: Optional[int] = Field(description="No. of attachments")

    Item: Union[DataCollection, RobotAction]


class Event(EventBase):
    class Config:
        orm_mode = True


class EventType(BaseModel):
    eventTypeName: str
    eventType: str

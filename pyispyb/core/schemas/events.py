# import datetime

from typing import Union, Optional
from datetime import datetime

from pydantic import BaseModel, Field
from ispyb import models

d = models.DataCollection
g = models.DataCollectionGroup
x = models.XFEFluorescenceSpectrum
r = models.RobotAction


class DataCollectionGroup(BaseModel):
    dataCollectionGroupId: int
    experimentType: str

    class Config:
        orm_mode = True


class DataCollectionMetaData(BaseModel):
    snapshots: dict[str, bool] = Field(description="Snapshot statuses with ids 1-4")


class DataCollection(BaseModel):
    runStatus: Optional[str]
    wavelength: Optional[float]
    exposureTime: Optional[float]
    numberOfImages: Optional[int]
    imageDirectory: Optional[str]
    fileTemplate: Optional[str]
    imageContainerSubPath: Optional[str]
    beamSizeAtSampleX: Optional[float]
    beamSizeAtSampleY: Optional[float]

    DataCollectionGroup: DataCollectionGroup

    metadata: DataCollectionMetaData = Field(alias="_metadata")

    class Config:
        orm_mode = True


class RobotAction(BaseModel):
    actionType: str
    status: Optional[str]
    message: Optional[str]

    class Config:
        orm_mode = True


class EventBase(BaseModel):
    id: int
    type: str
    startTime: datetime
    endTime: Optional[datetime]
    count: int
    session: str
    blSample: Optional[str] = Field(description="Sample name")
    blSampleId: Optional[int] = Field(description="Sample id")

    Item: Union[DataCollection, RobotAction]


class Event(EventBase):
    class Config:
        orm_mode = True
        # extra = 'forbid'

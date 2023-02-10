import datetime
from typing import Any, Optional

from pydantic import BaseModel, Field

from ispyb import models

from .dewars import DewarShipping

c = models.Container


class ContainerDewar(BaseModel):
    code: str = Field(title="Name")

    Shipping: DewarShipping

    class Config:
        orm_mode = True


class ContainerCreate(BaseModel):
    code: str = Field(title="Name")
    dewarId: int
    containerType: str

    sampleChangerLocation: Optional[str] = Field(
        description="Position in sample change"
    )
    beamlineLocation: Optional[str] = Field(
        description="Beamline if container is assigned"
    )


class Container(ContainerCreate):
    containerId: int

    Dewar: ContainerDewar

    class Config:
        orm_mode = True


class ContainerQueueMetaData(BaseModel):
    samples: Optional[int] = Field(description="Number of samples queued")


class ContainerQueue(BaseModel):
    containerQueueId: int
    createdTimeStamp: Optional[datetime.datetime]
    completedTimeStamp: Optional[datetime.datetime]

    Container: Container

    metadata: ContainerQueueMetaData = Field(alias="_metadata")

    class Config:
        orm_mode = True


class ContainerQueueUpdate(BaseModel):
    completed: Optional[bool]


class ContainerQueueDataCollection(BaseModel):
    dataCollectionId: int
    runStatus: Optional[str]


class ContainerQueueSampleMetaData(BaseModel):
    datacollections: list[ContainerQueueDataCollection] = Field(
        description="Related data collections"
    )
    dataCollectionGroupId: Optional[int] = Field(
        description="Related dataCollectionGroupId"
    )
    sessionId: Optional[int] = Field(description="Related sessionId")
    proposal: Optional[str] = Field(description="Related proposal")
    started: Optional[datetime.datetime] = Field(
        description="Time first datacollection started"
    )
    finished: Optional[datetime.datetime] = Field(
        description="Time last datacollection ended"
    )
    types: Optional[list[str]] = Field(description="Types of data collections")


class ContainerQueueBLSample(BaseModel):
    blSampleId: int
    name: str

    class Config:
        orm_mode = True


class ContainerQueueBLSubSample(BaseModel):
    type: str

    BLSample: ContainerQueueBLSample

    class Config:
        orm_mode = True


class ContainerQueueDiffractionPlan(BaseModel):
    diffractionPlanId: int
    recordTimeStamp: datetime.datetime
    scanParameters: Any  # Optional[dict[str, Any]]
    monoBandwidth: Optional[int]

    class Config:
        orm_mode = True


class ContainerQueueSample(BaseModel):
    containerQueueSampleId: int
    dataCollectionPlanId: int
    blSubSampleId: Optional[int]

    BLSample: Optional[ContainerQueueBLSample]
    BLSubSample: Optional[ContainerQueueBLSubSample]
    DiffractionPlan: Optional[ContainerQueueDiffractionPlan]

    metadata: ContainerQueueSampleMetaData = Field(alias="_metadata")

    class Config:
        orm_mode = True

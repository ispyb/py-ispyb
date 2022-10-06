# import datetime

from typing import Optional

from pydantic import BaseModel, Field
from ispyb import models

from .crystal import Crystal
from .shipping import Container

s = models.BLSample


class Position(BaseModel):
    posX: int
    posY: int

    class Config:
        orm_mode = True


class SampleMetaData(BaseModel):
    subsamples: int = Field(description="Number of sub samples")
    datacollections: int = Field(description="Number of data collections")
    types: Optional[list[str]] = Field(description="Types of data collections")
    queued: Optional[bool] = Field(
        description="Whether this sample is queued for data collection"
    )
    strategies: Optional[int] = Field(description="Number of successful strategies")
    autoIntegrations: Optional[int] = Field(
        description="Number of successful auto-integrations"
    )
    processings: Optional[int] = Field(description="Number of processings")


class SampleBase(BaseModel):
    name: str
    comments: Optional[str] = Field(title="Comments", nullable=True)
    location: Optional[int] = Field(
        title="Location", description="Location in container"
    )
    containerId: int

    metadata: Optional[SampleMetaData] = Field(alias="_metadata")


class SampleProtein(BaseModel):
    name: str
    acronym: str

    class Config:
        orm_mode = True


class SampleCrystal(Crystal):
    Protein: SampleProtein


class Sample(SampleBase):
    blSampleId: int

    Crystal: SampleCrystal
    Container: Container

    class Config:
        orm_mode = True


class SampleImageMetaData(BaseModel):
    url: str = Field(description="Url to sample image")


class SampleImage(BaseModel):
    blSampleImageId: int
    blSampleId: int
    micronsPerPixelX: float
    micronsPerPixelY: float
    offsetX: int
    offsetY: int

    metadata: SampleImageMetaData = Field(alias="_metadata")

    class Config:
        orm_mode = True


class SubSampleSample(BaseModel):
    name: str

    class Config:
        orm_mode = True


class SubSampleMetaData(BaseModel):
    datacollections: int = Field(description="Number of data collections")
    types: Optional[list[str]] = Field(description="Types of data collections")


class SubSampleBase(BaseModel):
    type: Optional[str] = Field(title="Subsample Type")
    comments: Optional[str] = Field(title="Comments", nullable=True)
    blSampleId: int

    metadata: SubSampleMetaData = Field(alias="_metadata")


class SubSample(SubSampleBase):
    blSubSampleId: int

    BLSample: SubSampleSample
    Position1: Optional[Position]
    Position2: Optional[Position]

    class Config:
        orm_mode = True

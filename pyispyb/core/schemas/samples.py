# import datetime

from typing import Optional

from pydantic import BaseModel, Field

from .crystal import Crystal


class Position(BaseModel):
    posX: int
    posY: int

    class Config:
        orm_mode = True


class SampleMetaData(BaseModel):
    subsamples: int = Field(description="Number of sub samples")
    datacollections: int = Field(description="Number of data collections")
    types: Optional[list[str]] = Field(
        description="Types of data collections", nullable=True
    )
    queued: Optional[bool] = Field(
        description="Whether this sample is queued for data collection"
    )
    strategies: Optional[int] = Field(description="Number of successful strategies")
    autoIntegrations: Optional[int] = Field(
        description="Number of successful auto-integrations"
    )
    integratedResolution: Optional[float] = Field(
        description="Highest integration resolution", nullable=True
    )
    proposal: Optional[str] = Field(description="The associated proposal")


class SampleBase(BaseModel):
    name: str
    comments: Optional[str] = Field(title="Comments", nullable=True)
    location: Optional[int] = Field(
        title="Location", description="Location in container"
    )
    containerId: Optional[int]

    metadata: Optional[SampleMetaData] = Field(alias="_metadata")


class SampleProtein(BaseModel):
    proposalId: str
    name: str
    acronym: str

    class Config:
        orm_mode = True


class SampleCrystal(Crystal):
    Protein: SampleProtein = Field(title="Protein")


class SampleContainer(BaseModel):
    code: str

    sampleChangerLocation: Optional[str] = Field(
        description="Position in sample change"
    )
    beamlineLocation: Optional[str] = Field(
        description="Beamline if container is assigned"
    )

    class Config:
        orm_mode = True


class Sample(SampleBase):
    blSampleId: int

    Crystal: SampleCrystal = Field(title="Crystal")
    Container: Optional[SampleContainer] = Field(title="Container")

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

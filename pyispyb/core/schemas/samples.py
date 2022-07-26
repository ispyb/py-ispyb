# import datetime

from typing import Optional

from pydantic import BaseModel, Field
from ispyb import models

from .crystal import Crystal

s = models.BLSample


class SampleMetaData(BaseModel):
    subsamples: int = Field(description="Number of sub samples")
    datacollections: int = Field(description="Number of data collections")


class SampleBase(BaseModel):
    name: str
    comments: Optional[str] = Field(title="Comments", nullable=True)

    metadata: SampleMetaData = Field(alias="_metadata")


class Sample(SampleBase):
    blSampleId: int

    Crystal: Crystal

    class Config:
        orm_mode = True

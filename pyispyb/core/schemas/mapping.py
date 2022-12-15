from typing import Optional
from pydantic import BaseModel, Field


class MapROI(BaseModel):
    xrfFluorescenceMappingROIId: int
    element: Optional[str]
    edge: Optional[str]
    scalar: Optional[str]
    startEnergy: float
    endEnergy: float

    class Config:
        orm_mode = True


class MapGridInfo(BaseModel):
    gridInfoId: int
    steps_x: int
    steps_y: int
    snaked: bool
    orientation: str

    class Config:
        orm_mode = True


class MapMetaData(BaseModel):
    url: str = Field(description="Url to map image")
    blSubSampleId: Optional[int]
    blSampleId: Optional[int]


class Map(BaseModel):
    xrfFluorescenceMappingId: int
    colourMap: Optional[str]
    opacity: Optional[float]
    points: Optional[int]
    dataFormat: str

    metadata: MapMetaData = Field(alias="_metadata")

    GridInfo: MapGridInfo
    XRFFluorescenceMappingROI: MapROI

    class Config:
        orm_mode = True


class MapHistogram(BaseModel):
    xrfFluorescenceMappingId: int
    hist: list[int]
    bins: list[float]
    width: list[float]


class MapPixelValue(BaseModel):
    xrfFluorescenceMappingId: int
    x: int
    y: int
    value: float

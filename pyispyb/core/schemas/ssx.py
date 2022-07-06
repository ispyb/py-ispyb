from typing import Literal, Optional
from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from pyispyb.core import models

from pydantic import BaseModel


class DataCollectionResponse(
    sqlalchemy_to_pydantic(models.DataCollection, exclude=["dataCollectionId"])
):
    DataCollectionGroup: sqlalchemy_to_pydantic(models.DataCollectionGroup)


class SSXDataCollectionResponse(
    sqlalchemy_to_pydantic(models.SSXDataCollection, exclude=["dataCollectionId"])
):
    DataCollection: DataCollectionResponse


class SSXBufferCreate(BaseModel):
    type: Optional[str]
    concentration: Optional[float]


class SSXSampleCreate(BaseModel):
    proteinId: int

    avgXtalSize: Optional[float]
    xtalConcentration: Optional[float]
    sampleSupport: Optional[str]
    jetMaterial: Optional[str]

    buffer: SSXBufferCreate


class SSXDataCollectionCreate(BaseModel):
    sessionId: int

    # Table DataCollection
    exposureTime: Optional[float]
    transmission: Optional[float]
    flux: Optional[float]
    xBeam: Optional[float]
    yBeam: Optional[float]
    wavelength: Optional[float]
    detectorDistance: Optional[float]
    beamSizeAtSampleX: Optional[float]
    beamSizeAtSampleY: Optional[float]
    averageTemperature: Optional[float]

    # Table DataCollectionGroup
    experimentType: Optional[Literal["SSXChip", "SSXInjector"]]

    # Table SSXDataCollection
    repetitionRate: Optional[float]
    energyBandwidth: Optional[float]
    monoStripe: Optional[str]

    sample: SSXSampleCreate

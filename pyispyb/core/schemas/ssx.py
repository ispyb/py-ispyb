from typing import Literal, Optional
from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from pyispyb.core import models

from pydantic import BaseModel


class DataCollectionResponse(
    sqlalchemy_to_pydantic(models.DataCollection, exclude=["dataCollectionId"])
):
    DataCollectionGroup: sqlalchemy_to_pydantic(models.DataCollectionGroup)


class MacromoleculeResponse(sqlalchemy_to_pydantic(models.Macromolecule)):
    pass


class BufferResponse(sqlalchemy_to_pydantic(models.Buffer)):
    pass


class ExperimentResponse(sqlalchemy_to_pydantic(models.Experiment)):
    pass


class SpecimenResponse(sqlalchemy_to_pydantic(models.Specimen)):
    Macromolecule: MacromoleculeResponse
    Buffer: BufferResponse
    Experiment: ExperimentResponse


class SSXSpecimenResponse(sqlalchemy_to_pydantic(models.SSXSpecimen)):
    Specimen: SpecimenResponse


class SSXDataCollectionResponse(
    sqlalchemy_to_pydantic(models.SSXDataCollection, exclude=["dataCollectionId"])
):
    DataCollection: DataCollectionResponse
    SSXSpecimen: SSXSpecimenResponse


class SSXSampleCreate(BaseModel):
    # Table SSXSpecimen
    avgXtalSize: Optional[float]
    ligandConcentration: Optional[float]
    sampleSupport: Optional[str]
    jetMaterial: Optional[str]

    # Table Specimen
    crystalConcentration: Optional[float]

    # Table Buffer
    bufferName: Optional[str]
    bufferComposition: Optional[str]

    # Table Macromolecule
    acronym: Optional[str]

    # Table Structure
    ligandName: Optional[str]


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

from typing import Literal, Optional
from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from pyispyb.core import models

from pydantic import BaseModel


class DataCollectionResponse(sqlalchemy_to_pydantic(models.DataCollection)):
    DataCollectionGroup: sqlalchemy_to_pydantic(models.DataCollectionGroup)
    Detector: Optional[sqlalchemy_to_pydantic(models.Detector)]


class MacromoleculeResponse(sqlalchemy_to_pydantic(models.Macromolecule)):
    pass


class BufferResponse(sqlalchemy_to_pydantic(models.Buffer)):
    pass


class StructureResponse(sqlalchemy_to_pydantic(models.Structure)):
    pass


class SpecimenResponse(sqlalchemy_to_pydantic(models.Specimen)):
    Macromolecule: MacromoleculeResponse
    Buffer: BufferResponse
    Structures: list[StructureResponse] = []


class SSXSpecimenResponse(sqlalchemy_to_pydantic(models.SSXSpecimen)):
    Specimen: SpecimenResponse


class SSXDataCollectionResponse(sqlalchemy_to_pydantic(models.SSXDataCollection)):
    DataCollection: DataCollectionResponse


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


class UntrustedRegionCreate(BaseModel):
    x1: Optional[int]
    x2: Optional[int]
    y1: Optional[int]
    y2: Optional[int]


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
    xtalSnapshotFullPath1: Optional[str]
    xtalSnapshotFullPath2: Optional[str]
    xtalSnapshotFullPath3: Optional[str]
    xtalSnapshotFullPath4: Optional[str]
    imagePrefix: Optional[str]
    numberOfPasses: Optional[str]
    numberOfImages: Optional[str]
    resolution: Optional[str]
    resolutionAtCorner: Optional[str]
    flux_end: Optional[str]
    detectorId: Optional[int]

    # Table DataCollectionGroup
    experimentType: Optional[Literal["SSXChip", "SSXInjector"]]

    # Table SSXDataCollection
    repetitionRate: Optional[float]
    energyBandwidth: Optional[float]
    monoStripe: Optional[str]

    sample: SSXSampleCreate

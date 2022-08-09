from datetime import datetime
from typing import Literal, Optional
from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from pyispyb.core import models

from pydantic import BaseModel


class DataCollectionResponse(sqlalchemy_to_pydantic(models.DataCollection)):
    DataCollectionGroup: sqlalchemy_to_pydantic(models.DataCollectionGroup)
    Detector: Optional[sqlalchemy_to_pydantic(models.Detector)]


class CrystalResponse(sqlalchemy_to_pydantic(models.Crystal)):
    Protein: sqlalchemy_to_pydantic(models.Protein)


class SSXSampleResponse(sqlalchemy_to_pydantic(models.BLSample)):
    Crystal: CrystalResponse
    sample_components: list[sqlalchemy_to_pydantic(models.SampleComponent)]


class SSXDataCollectionResponse(sqlalchemy_to_pydantic(models.SSXDataCollection)):
    DataCollection: DataCollectionResponse


class SSXProteinCreate(BaseModel):
    name: Optional[str]
    acronym: Optional[str]


class SSXSampleComponentCreate(BaseModel):
    name: Optional[str]
    componentType: Optional[Literal["Ligand", "Buffer", "JetMaterial"]]
    composition: Optional[str]
    concentration: Optional[float]


class SSXCrystalCreate(BaseModel):
    size_X: Optional[float]
    size_X: Optional[float]
    size_X: Optional[float]
    abundance: Optional[float]
    protein: SSXProteinCreate


class SSXSampleCreate(BaseModel):
    name: Optional[str]
    support: Optional[str]
    crystal: SSXCrystalCreate
    components: list[SSXSampleComponentCreate]


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
    numberOfPasses: Optional[int]
    numberOfImages: Optional[int]
    resolution: Optional[float]
    resolutionAtCorner: Optional[float]
    flux_end: Optional[float]
    detectorId: Optional[int]
    startTime: datetime
    endTime: Optional[datetime]

    # Table DataCollectionGroup
    experimentType: Optional[Literal["SSXChip", "SSXInjector"]]

    # Table SSXDataCollection
    repetitionRate: Optional[float]
    energyBandwidth: Optional[float]
    monoStripe: Optional[str]

    sample: SSXSampleCreate

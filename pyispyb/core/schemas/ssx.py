from datetime import datetime
from typing import Literal, Optional
from pydantic_sqlalchemy import sqlalchemy_to_pydantic

from pyispyb.core import models

from pydantic import BaseModel


class DataCollectionResponse(sqlalchemy_to_pydantic(models.DataCollection)):
    DataCollectionGroup: sqlalchemy_to_pydantic(models.DataCollectionGroup)
    Detector: Optional[sqlalchemy_to_pydantic(models.Detector)]


class ComponentResponse(sqlalchemy_to_pydantic(models.Component)):
    ComponentType: sqlalchemy_to_pydantic(models.ComponentType)


class CrystalCompositionResponse(sqlalchemy_to_pydantic(models.CrystalComposition)):
    Component: ComponentResponse


class CrystalResponse(sqlalchemy_to_pydantic(models.Crystal)):
    Protein: sqlalchemy_to_pydantic(models.Protein)
    crystal_compositions: list[CrystalCompositionResponse]


class SampleCompositionResponse(sqlalchemy_to_pydantic(models.SampleComposition)):
    Component: ComponentResponse


class SSXSampleResponse(sqlalchemy_to_pydantic(models.BLSample)):
    Crystal: CrystalResponse
    sample_compositions: list[SampleCompositionResponse]


class SSXDataCollectionResponse(sqlalchemy_to_pydantic(models.SSXDataCollection)):
    DataCollection: DataCollectionResponse


class DataCollectionGroupResponse(sqlalchemy_to_pydantic(models.DataCollectionGroup)):
    nbDataCollection: Optional[int]


class SSXHitsResponse(sqlalchemy_to_pydantic(models.SSXHits)):
    pass


class GraphResponse(sqlalchemy_to_pydantic(models.Graph)):
    pass


class GraphDataResponse(sqlalchemy_to_pydantic(models.GraphData)):
    pass


class SSXHitsCreate(BaseModel):
    nbHits: int
    nbIndexed: int
    laticeType: Optional[str]
    estimatedResolution: Optional[float]
    unit_cells: Optional[list[list[float]]]


class SSXSequenceEventResponse(sqlalchemy_to_pydantic(models.SequenceEvent)):
    SequenceEventType: sqlalchemy_to_pydantic(models.SequenceEventType)


class SSXSequenceResponse(sqlalchemy_to_pydantic(models.Sequence)):
    sequence_events: list[SSXSequenceEventResponse]


class SSXProteinCreate(BaseModel):
    name: Optional[str]
    acronym: Optional[str]


class SSXSampleComponentCreate(BaseModel):
    name: Optional[str]
    componentType: Literal["Ligand", "Buffer", "JetMaterial"]
    composition: Optional[str]
    abundance: Optional[float]


class SSXCrystalCreate(BaseModel):
    size_X: Optional[float]
    size_Y: Optional[float]
    size_Z: Optional[float]
    abundance: Optional[float]
    protein: SSXProteinCreate
    components: list[SSXSampleComponentCreate]


class SSXSampleCreate(BaseModel):
    name: Optional[str]
    support: Optional[str]
    crystal: SSXCrystalCreate
    components: list[SSXSampleComponentCreate]


class SSXSequenceEventCreate(BaseModel):
    type: Literal["XrayDetection", "XrayExposure", "LaserExcitation", "ReactionTrigger"]
    name: Optional[str]
    time: datetime
    duration: Optional[float]
    period: Optional[float]
    repetition: Optional[float]


class SSXSequenceCreate(BaseModel):
    name: Optional[str]
    events: list[SSXSequenceEventCreate]


class SSXDataCollectionCreate(BaseModel):
    sessionId: int
    dataCollectionGroupId: int

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

    # Table SSXDataCollection
    repetitionRate: Optional[float]
    energyBandwidth: Optional[float]
    monoStripe: Optional[str]

    sequences: list[SSXSequenceCreate]


class SSXDataCollectionGroupCreate(BaseModel):
    # Table DataCollectionGroup
    sessionId: int
    startTime: datetime
    endTime: Optional[datetime]
    experimentType: Optional[Literal["SSXChip", "SSXInjector"]]
    comments: Optional[str]

    sample: SSXSampleCreate

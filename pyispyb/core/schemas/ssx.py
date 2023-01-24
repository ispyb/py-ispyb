from datetime import datetime
from typing import Literal, Optional
from .eventchain import EventChainCreate

from pydantic import BaseModel


class SSXDataCollectionProcessingStatsBase(BaseModel):
    nbHits: int
    nbIndexed: int
    laticeType: str
    estimatedResolution: float


class SSXDataCollectionProcessingStats(SSXDataCollectionProcessingStatsBase):
    dataCollectionId: int


class SSXDataCollectionProcessingCells(BaseModel):
    unit_cells: list[list[float]]


class Histogram(BaseModel):
    x: list[float]
    y: list[int]
    median: float


class SSXDataCollectionProcessingCellsHistogram(BaseModel):
    a: Histogram | None
    b: Histogram | None
    c: Histogram | None
    alpha: Histogram | None
    beta: Histogram | None
    gamma: Histogram | None
    dataCollectionIds: list[int]


class SSXDataCollectionProcessingCreate(BaseModel):
    processingCommandLine: Optional[str]
    processingPrograms: Optional[str]
    processingMessage: Optional[str]
    processingStartTime: Optional[datetime]
    processingEndTime: Optional[datetime]
    processingEnvironment: Optional[str]
    results: list[str]


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


class SSXDataCollectionCreate(BaseModel):
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
    beamShape: Optional[str]
    polarisation: Optional[float]
    undulatorGap1: Optional[float]

    # Table SSXDataCollection
    repetitionRate: Optional[float]
    energyBandwidth: Optional[float]
    monoStripe: Optional[str]
    experimentName: Optional[str]
    jetSize: Optional[float]
    jetSpeed: Optional[float]
    laserEnergy: Optional[float]
    chipModel: Optional[str]
    chipPattern: Optional[str]

    event_chains: list[EventChainCreate]


class SSXDataCollectionGroupCreate(BaseModel):
    # Table DataCollectionGroup
    sessionId: int
    startTime: datetime
    endTime: Optional[datetime]
    experimentType: Optional[Literal["SSX-Chip", "SSX-Jet"]]
    comments: Optional[str]

    sample: Optional[SSXSampleCreate]
    sampleId: Optional[int]

from datetime import datetime
from typing import Literal, Optional
from .eventchain import EventChainCreate

# from pydantic_sqlalchemy import sqlalchemy_to_pydantic

# from ispyb import models

from pydantic import BaseModel


# class DataCollectionResponse(sqlalchemy_to_pydantic(models.DataCollection)):
#     DataCollectionGroup: sqlalchemy_to_pydantic(models.DataCollectionGroup)
#     Detector: Optional[sqlalchemy_to_pydantic(models.Detector)]

#     def dict(self, *args, **kwargs) -> Dict[str, Any]:
#         kwargs.pop("exclude_none")
#         return super().dict(*args, exclude_none=True, **kwargs)


# class ComponentResponse(sqlalchemy_to_pydantic(models.Component)):
#     ComponentType: sqlalchemy_to_pydantic(models.ComponentType)

#     def dict(self, *args, **kwargs) -> Dict[str, Any]:
#         kwargs.pop("exclude_none")
#         return super().dict(*args, exclude_none=True, **kwargs)


# class CrystalCompositionResponse(sqlalchemy_to_pydantic(models.CrystalComposition)):
#     Component: ComponentResponse

#     def dict(self, *args, **kwargs) -> Dict[str, Any]:
#         kwargs.pop("exclude_none")
#         return super().dict(*args, exclude_none=True, **kwargs)


# class CrystalResponse(sqlalchemy_to_pydantic(models.Crystal)):
#     Protein: sqlalchemy_to_pydantic(models.Protein)
#     crystal_compositions: list[CrystalCompositionResponse]

#     def dict(self, *args, **kwargs) -> Dict[str, Any]:
#         kwargs.pop("exclude_none")
#         return super().dict(*args, exclude_none=True, **kwargs)


# class SampleCompositionResponse(sqlalchemy_to_pydantic(models.SampleComposition)):
#     Component: ComponentResponse

#     def dict(self, *args, **kwargs) -> Dict[str, Any]:
#         kwargs.pop("exclude_none")
#         return super().dict(*args, exclude_none=True, **kwargs)


# class SSXSampleResponse(sqlalchemy_to_pydantic(models.BLSample)):
#     Crystal: CrystalResponse
#     sample_compositions: list[SampleCompositionResponse]

#     def dict(self, *args, **kwargs) -> Dict[str, Any]:
#         kwargs.pop("exclude_none")
#         return super().dict(*args, exclude_none=True, **kwargs)


# class SSXDataCollectionResponse(sqlalchemy_to_pydantic(models.SSXDataCollection)):
#     DataCollection: DataCollectionResponse

#     def dict(self, *args, **kwargs) -> Dict[str, Any]:
#         kwargs.pop("exclude_none")
#         return super().dict(*args, exclude_none=True, **kwargs)


# class DataCollectionGroupResponse(sqlalchemy_to_pydantic(models.DataCollectionGroup)):
#     nbDataCollection: Optional[int]
#     ExperimentType: sqlalchemy_to_pydantic(models.ExperimentType)

#     def dict(self, *args, **kwargs) -> Dict[str, Any]:
#         kwargs.pop("exclude_none")
#         return super().dict(*args, exclude_none=True, **kwargs)


class SSXDataCollectionProcessingBase(BaseModel):
    nbHits: int
    nbIndexed: int
    laticeType: str
    estimatedResolution: float
    unit_cells: list[list[float]]


class SSXDataCollectionProcessing(SSXDataCollectionProcessingBase):
    dataCollectionId: int


class SSXDataCollectionProcessingCreate(BaseModel):
    processingCommandLine: Optional[str]
    processingPrograms: Optional[str]
    processingMessage: Optional[str]
    processingStartTime: Optional[datetime]
    processingEndTime: Optional[datetime]
    processingEnvironment: Optional[str]
    resultPath: str


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
    experimentName: Optional[str]

    event_chains: list[EventChainCreate]


class SSXDataCollectionGroupCreate(BaseModel):
    # Table DataCollectionGroup
    sessionId: int
    startTime: datetime
    endTime: Optional[datetime]
    experimentType: Optional[Literal["SSX-Chip", "SSX-Jet"]]
    comments: Optional[str]

    sample: SSXSampleCreate

import enum
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class StatusEnum(enum.Enum):
    RUNNING = None
    FAILED = 0
    SUCCESS = 1
    DIDNTRUN = 3


class ProcessingStatus(BaseModel):
    status: Optional[StatusEnum]


class ProcessingProcessingStatus(ProcessingStatus):
    autoProcProgramId: int


class ScreeningProcesingStatus(ProcessingStatus):
    indexingSuccess: StatusEnum
    alignmentSuccess: StatusEnum


class ProcessingStatuses(BaseModel):
    screening: Optional[dict[str, list[ScreeningProcesingStatus]]]
    xrc: Optional[dict[str, list[ProcessingStatus]]]
    processing: Optional[dict[str, list[ProcessingProcessingStatus]]]
    autoIntegration: Optional[dict[str, list[ProcessingProcessingStatus]]]


class ProcessingStatusesList(BaseModel):
    statuses: dict[int, ProcessingStatuses]


class ScreeningStrategySubWedge(BaseModel):
    subWedgeNumber = int
    rotationAxis = str
    axisStart: float
    axisEnd: float
    exposureTime: float
    transmission: float
    oscillationRange: float
    completeness: float
    multiplicity: float
    RESOLUTION: float
    doseTotal: float
    numberOfImages: int
    comments: float

    class Config:
        orm_mode = True


class ScreeningStrategyWedge(BaseModel):
    wedgeNumber: int
    resolution: float
    completeness: float
    multiplicity: float
    doseTotal: float
    numberOfImages: int
    phi: float
    kappa: float
    chi: float
    comments: float
    wavelength: float

    ScreeningStrategySubWedge: Optional[ScreeningStrategySubWedge]

    class Config:
        orm_mode = True


class ScreeningStrategy(BaseModel):
    rankingResolution: float

    ScreeningStrategyWedge: Optional[ScreeningStrategyWedge]

    class Config:
        orm_mode = True


class ScreeningOutputLattice(BaseModel):
    unitCell_a: float
    unitCell_b: float
    unitCell_c: float
    unitCell_alpha: float
    unitCell_beta: float
    unitCell_gamma: float

    class Config:
        orm_mode = True


class ScreeningOutput(BaseModel):

    ScreeningStrategy: Optional[ScreeningStrategy]
    ScreeningOutputLattice: Optional[ScreeningOutputLattice]

    class Config:
        orm_mode = True


class Screening(BaseModel):
    programVersion: str
    comments: str
    shortComments: str

    ScreeningOutput: Optional[ScreeningOutput]

    class Config:
        orm_mode = True


class ProcessingJobParameter(BaseModel):
    parameterKey: str
    parameterValue: str

    class Config:
        orm_mode = True


class ProcessingJob(BaseModel):
    processingJobId: int
    displayName: Optional[str]
    comments: Optional[str]
    recordTimestamp: datetime
    recipe: Optional[str]
    automatic: bool

    ProcessingJobParameters: Optional[list[ProcessingJobParameter]]

    class Config:
        orm_mode = True


class AutoProcProgram(BaseModel):
    autoProcProgramId: int
    processingCommandLine: Optional[str]
    processingPrograms: Optional[str]
    processingStatus: Optional[StatusEnum]
    processingMessage: Optional[str]
    processingStartTime: Optional[datetime]
    processingEndTime: Optional[datetime]
    processingEnvironment: Optional[str]
    recordTimeStamp: datetime

    ProcessingJob: Optional[ProcessingJob]

    class Config:
        orm_mode = True


class AutoProc(BaseModel):
    spaceGroup: str
    refinedCell_a: float
    refinedCell_b: float
    refinedCell_c: float
    refinedCell_alpha: float
    refinedCell_beta: float
    refinedCell_gamma: float


class ScalingStatisticsType(str, enum.Enum):
    overall = "overall"
    innerShell = "innerShell"
    outerShell = "outerShell"


class AutoProcScalingStatistics(BaseModel):
    comments: float
    scalingStatisticsType: ScalingStatisticsType
    resolutionLimitLow: float
    resolutionLimitHigh: float
    rMerge: float
    rMeasAllIPlusIMinus: float
    rPimAllIPlusIMinus: float
    fractionalPartialBias: float
    nTotalObservations: int
    nTotalUniqueObservations: int
    meanIOverSigI: float
    completeness: float
    multiplicity: float
    anomalousCompleteness: float
    anomalousMultiplicity: float
    anomalous: bool
    ccHalf: float
    ccAnomalous: float
    resIOverSigI2: float


class AutoProcScaling(BaseModel):
    AutoProc: Optional[AutoProc]
    AutoProcScalingStatistics: Optional[AutoProcScalingStatistics]


class AutoProcScalingHasInt(BaseModel):
    AutoProcScaling: Optional[AutoProcScaling]


class AutoProcIntegrationDataCollection(BaseModel):
    xBeam: float
    yBeam: float


class AutoProcIntegration(BaseModel):
    refinedXBeam: float
    refinedYBeam: float

    AutoProcScalingHasInt: Optional[AutoProcScalingHasInt]
    DataCollection: Optional[AutoProcIntegrationDataCollection]


class AutoProcProgramIntegration(AutoProcProgram):
    AutoProcIntegration: Optional[AutoProcIntegration]


class AutoProcProgramMessageStatus(BaseModel):
    errors: int
    warnings: int
    info: int


class AutoProcProgramMessageStatuses(BaseModel):
    statuses: dict[int, AutoProcProgramMessageStatus]


class AutoProcProgramMessageSeverity(str, enum.Enum):
    ERROR = "ERROR"
    WARNING = "WARNING"
    INFO = "INFO"


class AutoProcProgramMessage(BaseModel):
    autoProcProgramMessageId: int
    autoProcProgramId: int
    description: str
    message: str
    severity: AutoProcProgramMessageSeverity
    recordTimeStamp: datetime

    class Config:
        orm_mode = True


class AutoProcProgramAttachment(BaseModel):
    autoProcProgramAttachmentId: int
    autoProcProgramId: int
    fileName: str
    fileType: str
    importanceRank: Optional[int]

    class Config:
        orm_mode = True

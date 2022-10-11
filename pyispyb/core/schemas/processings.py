import enum
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, validator


class StatusEnum(enum.Enum):
    RUNNING = None
    FAILED = 0
    SUCCESS = 1
    DIDNTRUN = 2


class ProcessingStatus(BaseModel):
    status: Optional[StatusEnum]

    @validator("status", pre=True)
    def check_status(cls, status):
        if status == "SUCCESS":
            return 1
        if status == "FAILED":
            return 0
        if status == "RUNNING":
            return None

        return status


class ProcessingProcessingStatus(ProcessingStatus):
    autoProcProgramId: int


class ScreeningProcesingStatus(ProcessingStatus):
    indexingSuccess: StatusEnum


class EMProcessingStatus(BaseModel):
    motionCorrection: int
    ctf: int


class ProcessingStatuses(BaseModel):
    screening: Optional[dict[str, list[ScreeningProcesingStatus]]]
    xrc: Optional[dict[str, list[ProcessingStatus]]]
    processing: Optional[dict[str, list[ProcessingProcessingStatus]]]
    autoIntegration: Optional[dict[str, list[ProcessingProcessingStatus]]]
    em: Optional[EMProcessingStatus]


class ProcessingStatusesList(BaseModel):
    statuses: dict[int, ProcessingStatuses]


class ScreeningStrategySubWedge(BaseModel):
    screeningStrategySubWedgeId: int
    subWedgeNumber: Optional[int]
    rotationAxis: Optional[str]
    axisStart: Optional[float]
    axisEnd: Optional[float]
    exposureTime: Optional[float]
    transmission: Optional[float]
    oscillationRange: Optional[float]
    completeness: Optional[float]
    multiplicity: Optional[float]
    RESOLUTION: Optional[float]
    doseTotal: Optional[float]
    numberOfImages: Optional[int]
    comments: Optional[str]

    class Config:
        orm_mode = True


class ScreeningStrategyWedge(BaseModel):
    screeningStrategyWedgeId: int
    wedgeNumber: Optional[int]
    resolution: Optional[float]
    completeness: Optional[float]
    multiplicity: Optional[float]
    doseTotal: Optional[float]
    numberOfImages: Optional[int]
    phi: Optional[float]
    kappa: Optional[float]
    chi: Optional[float]
    comments: Optional[str]
    wavelength: Optional[float]

    ScreeningStrategySubWedge: Optional[list[ScreeningStrategySubWedge]]

    class Config:
        orm_mode = True


class ScreeningStrategy(BaseModel):
    screeningStrategyId: int
    rankingResolution: Optional[float]

    ScreeningStrategyWedge: Optional[list[ScreeningStrategyWedge]]

    class Config:
        orm_mode = True


class ScreeningOutputLattice(BaseModel):
    unitCell_a: float
    unitCell_b: float
    unitCell_c: float
    unitCell_alpha: float
    unitCell_beta: float
    unitCell_gamma: float
    spaceGroup: Optional[str]
    pointGroup: Optional[str]

    class Config:
        orm_mode = True


class ScreeningOutput(BaseModel):
    screeningOutputId: int
    indexingSuccess: int
    strategySuccess: int

    ScreeningStrategy: Optional[list[ScreeningStrategy]]
    ScreeningOutputLattice: Optional[list[ScreeningOutputLattice]]

    class Config:
        orm_mode = True


class Screening(BaseModel):
    screeningId: int
    programVersion: str
    comments: Optional[str]
    shortComments: Optional[str]

    ScreeningOutput: Optional[list[ScreeningOutput]]

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


class AutoProcProgramMetadata(BaseModel):
    attachments: Optional[int] = Field(description="Number of attachments")
    autoProcProgramMessages: Optional[list[AutoProcProgramMessage]]
    imageSweepCount: Optional[int]


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

    metadata: AutoProcProgramMetadata = Field(alias="_metadata")

    @validator("processingStatus", pre=True)
    def check_status(cls, status):
        if status == "SUCCESS":
            return 1
        if status == "FAILED":
            return 0
        if status == "RUNNING":
            return None

        return status

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

    class Config:
        orm_mode = True


class ScalingStatisticsType(str, enum.Enum):
    overall = "overall"
    innerShell = "innerShell"
    outerShell = "outerShell"


class AutoProcScalingStatistics(BaseModel):
    comments: Optional[str]
    scalingStatisticsType: Optional[ScalingStatisticsType]
    resolutionLimitLow: Optional[float]
    resolutionLimitHigh: Optional[float]
    rMerge: Optional[float]
    rMeasAllIPlusIMinus: Optional[float]
    rPimAllIPlusIMinus: Optional[float]
    fractionalPartialBias: Optional[float]
    nTotalObservations: Optional[int]
    nTotalUniqueObservations: Optional[int]
    meanIOverSigI: Optional[float]
    completeness: Optional[float]
    multiplicity: Optional[float]
    anomalousCompleteness: Optional[float]
    anomalousMultiplicity: Optional[float]
    anomalous: Optional[bool]
    ccHalf: Optional[float]
    ccAnomalous: Optional[float]
    resIOverSigI2: Optional[float]

    class Config:
        orm_mode = True


class AutoProcScaling(BaseModel):
    AutoProc: Optional[AutoProc]
    AutoProcScalingStatistics: Optional[list[AutoProcScalingStatistics]]

    class Config:
        orm_mode = True


class AutoProcScalingHasInt(BaseModel):
    AutoProcScaling: Optional[AutoProcScaling]

    class Config:
        orm_mode = True


class AutoProcIntegrationDataCollection(BaseModel):
    xBeam: Optional[float]
    yBeam: Optional[float]

    class Config:
        orm_mode = True


class AutoProcIntegration(BaseModel):
    refinedXBeam: Optional[float]
    refinedYBeam: Optional[float]

    AutoProcScalingHasInt: Optional[list[AutoProcScalingHasInt]]
    DataCollection: Optional[AutoProcIntegrationDataCollection]

    class Config:
        orm_mode = True


class AutoProcProgramIntegration(AutoProcProgram):
    AutoProcIntegration: Optional[list[AutoProcIntegration]]


class AutoProcProgramMessageStatus(BaseModel):
    errors: int
    warnings: int
    info: int


class AutoProcProgramMessageStatuses(BaseModel):
    statuses: dict[int, AutoProcProgramMessageStatus]


class AutoProcProgramAttachmentMetaData(BaseModel):
    url: str = Field(description="Url to autoproc program attachment")


class AutoProcProgramAttachment(BaseModel):
    autoProcProgramAttachmentId: int
    autoProcProgramId: int
    fileName: str
    fileType: str
    importanceRank: Optional[int]

    metadata: AutoProcProgramAttachmentMetaData = Field(alias="_metadata")

    class Config:
        orm_mode = True

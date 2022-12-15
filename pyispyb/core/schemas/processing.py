from pydantic import BaseModel
from typing import Literal, Optional
from datetime import datetime


class AutoProcProgram(BaseModel):
    processingCommandLine: Optional[str]
    processingPrograms: Optional[str]
    processingStatus: Literal["RUNNING", "FAILED", "SUCCESS"]
    processingMessage: Optional[str]
    processingStartTime: Optional[datetime]
    processingEndTime: Optional[datetime]
    processingEnvironment: Optional[str]
    recordTimeStamp: Optional[datetime]


class AutoProcIntegrationParameters(BaseModel):
    refinedDetectorDistance: Optional[float]
    refinedXBeam: Optional[float]
    refinedYBeam: Optional[float]
    rotationAxisX: Optional[float]
    rotationAxisY: Optional[float]
    rotationAxisZ: Optional[float]
    beamVectorX: Optional[float]
    beamVectorY: Optional[float]
    beamVectorZ: Optional[float]
    cell_a: Optional[float]
    cell_b: Optional[float]
    cell_c: Optional[float]
    cell_alpha: Optional[float]
    cell_beta: Optional[float]
    cell_gamma: Optional[float]
    anomalous: Optional[bool]


class AutoProcIntegration(BaseModel):
    dataCollectionId: int
    AutoProcIntegrationId: Optional[int]
    startImageNumber: Optional[int]
    endImageNumber: Optional[int]
    recordTimeStamp: Optional[datetime]
    parameters: Optional[AutoProcIntegrationParameters]


class AutoProcScalingStatistics(BaseModel):
    scalingStatisticsType: Literal["overall", "innerShell", "outerShell"]
    comments: Optional[str]
    resolutionLimitLow: Optional[float]
    resolutionLimitHigh: Optional[float]
    rMerge: Optional[float]
    rMeasWithinIPlusIMinus: Optional[float]
    rMeasAllIPlusIMinus: Optional[float]
    rPimWithinIPlusIMinus: Optional[float]
    rPimAllIPlusIMinus: Optional[float]
    fractionalPartialBias: Optional[float]
    nTotalObservations: Optional[int]
    nTotalUniqueObservations: Optional[int]
    meanIOverSigI: Optional[float]
    completeness: Optional[float]
    multiplicity: Optional[float]
    anomalousCompleteness: Optional[float]
    anomalousMultiplicity: Optional[float]
    recordTimeStamp: Optional[datetime]
    anomalous: Optional[bool]
    ccHalf: Optional[float]
    ccAno: Optional[float]
    sigAno: Optional[str]
    isa: Optional[str]
    completenessSpherical: Optional[float]
    completenessEllipsoidal: Optional[float]
    anomalousCompletenessSpherical: Optional[float]
    anomalousCompletenessEllipsoidal: Optional[float]


class AutoProcScaling(BaseModel):
    integrationIds: list[int]
    recordTimeStamp: Optional[datetime]
    statistics: list[AutoProcScalingStatistics]
    resolutionEllipsoidValue1: Optional[float]
    resolutionEllipsoidValue2: Optional[float]
    resolutionEllipsoidValue3: Optional[float]
    resolutionEllipsoidAxis11: Optional[float]
    resolutionEllipsoidAxis12: Optional[float]
    resolutionEllipsoidAxis13: Optional[float]
    resolutionEllipsoidAxis21: Optional[float]
    resolutionEllipsoidAxis22: Optional[float]
    resolutionEllipsoidAxis23: Optional[float]
    resolutionEllipsoidAxis31: Optional[float]
    resolutionEllipsoidAxis32: Optional[float]
    resolutionEllipsoidAxis33: Optional[float]
    spaceGroup: Optional[str]
    refinedCell_a: Optional[float]
    refinedCell_b: Optional[float]
    refinedCell_c: Optional[float]
    refinedCell_alpha: Optional[float]
    refinedCell_beta: Optional[float]
    refinedCell_gamma: Optional[float]
    recordTimeStamp: Optional[datetime]


class AutoProcStartProgram(BaseModel):
    dataCollectionIds: list[int]
    program: AutoProcProgram


class AutoProcUpdateProgram(BaseModel):
    program: AutoProcProgram
    integrations: list[AutoProcIntegration]
    scalings: list[AutoProcScaling]

# import datetime

import enum
from typing import Optional

from pydantic import BaseModel, Field


class DataCollectionGroup(BaseModel):
    dataCollectionGroupId: int
    experimentType: str

    class Config:
        orm_mode = True


class GridInfo(BaseModel):
    gridInfoId: int

    xOffset: Optional[float]
    yOffset: Optional[float]
    dx_mm: Optional[float]
    dy_mm: Optional[float]
    steps_x: Optional[float]
    steps_y: Optional[float]
    meshAngle: Optional[float]
    orientation: Optional[str]
    pixelsPerMicronX: Optional[float]
    pixelsPerMicronY: Optional[float]
    snapshot_offsetXPixel: Optional[float]
    snapshot_offsetYPixel: Optional[float]
    snaked: Optional[bool]

    class Config:
        orm_mode = True


class DataCollectionMetaData(BaseModel):
    snapshots: dict[str, bool] = Field(description="Snapshot statuses with ids 1-4")


class RotationAxis(str, enum.Enum):
    omega = "omega"
    phi = "phi"


class DataCollectionBase(BaseModel):
    runStatus: Optional[str] = Field(
        title="Status", description="`Successful` on success"
    )

    imageDirectory: Optional[str] = Field(
        title="Directory", description="Directory where the data is saved"
    )
    fileTemplate: Optional[str] = Field(
        title="Data File Template", description="File template for data"
    )
    imageContainerSubPath: Optional[str] = Field(
        title="Image Sub Path", description="For hdf5 files, path to the images"
    )
    numberOfImages: Optional[int] = Field(title="Number of Images / Points")

    wavelength: Optional[float] = Field(title="Wavelength", unit="Å")
    exposureTime: Optional[float] = Field(title="Exposure Time", unit="s")
    flux: Optional[float] = Field(title="Flux", unit="ph/s")
    xBeam: Optional[float] = Field(title="Beam Position (Horizontal)", unit="pixels")
    yBeam: Optional[float] = Field(title="Beam Position (Vertical)", unit="pixels")
    beamSizeAtSampleX: Optional[float] = Field(
        title="Beam Size at Sample (Horizontal)", unit="mm"
    )
    beamSizeAtSampleY: Optional[float] = Field(
        title="Beam Size at Sample (Vertical)", unit="mm"
    )
    transmission: Optional[float] = Field(title="Beam Transmision", unit="%")
    resolution: Optional[float] = Field(
        title="Resolution", description="At edge of detector", unit="Å"
    )
    detectorDistance: Optional[float] = Field(title="Detector Distance", unit="mm")

    axisStart: Optional[float] = Field(title="Rotation Axis Start", unit="°")
    axisEnd: Optional[float] = Field(title="Rotation Axis End", unit="°")
    axisRange: Optional[float] = Field(title="Rotation Axis Oscillation", unit="°")
    rotationAxis: Optional[str] = Field(title="Rotation Axis Motor")
    overlap: Optional[float] = Field(title="Rotation Axis Overlap", unit="°")

    phiStart: Optional[float] = Field(title="Phi Start", unit="°")
    kappaStart: Optional[float] = Field(title="Kappa Start", unit="°")
    omegaStart: Optional[float] = Field(title="Omega Start", unit="°")
    chiStart: Optional[float] = Field(title="Chi Start", unit="°")


class DataCollection(DataCollectionBase):
    dataCollectionId: int

    DataCollectionGroup: DataCollectionGroup
    GridInfo: Optional[list[GridInfo]]

    metadata: DataCollectionMetaData = Field(alias="_metadata")

    class Config:
        orm_mode = True


class DataCollectionFileAttachmentMetaData(BaseModel):
    url: str = Field(description="Url to data collection file attachment")
    fileName: str = Field(description="File name")


class DataCollectionFileAttachment(BaseModel):
    dataCollectionFileAttachmentId: int
    dataCollectionId: int
    fileType: str

    metadata: DataCollectionFileAttachmentMetaData = Field(alias="_metadata")

    class Config:
        orm_mode = True


class PerImageAnalysis(BaseModel):
    dataCollectionId: Optional[int]
    imageNumber: Optional[list[int]] = Field(description="Scan point")
    totalIntegratedSignal: Optional[list[float]] = Field(description="Total signal")
    goodBraggCandidates: Optional[list[int]] = Field(description="Number of spots")
    method2Res: Optional[list[float]] = Field(description="Estimated resolution")

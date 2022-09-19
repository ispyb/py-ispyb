# import datetime

import enum
from datetime import datetime
from typing import Union, Optional

from pydantic import BaseModel, Field
from ispyb import models


class DataCollectionGroup(BaseModel):
    dataCollectionGroupId: int
    experimentType: str

    class Config:
        orm_mode = True


class DataCollectionMetaData(BaseModel):
    snapshots: dict[str, bool] = Field(description="Snapshot statuses with ids 1-4")


class RotationAxis(str, enum.Enum):
    omega = "omega"
    phi = "phi"


class DataCollection(BaseModel):
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
    rotationAxis: Optional[RotationAxis] = Field(title="Exposure Time")
    overlap: Optional[float] = Field(title="Rotation Axis Overlap", unit="°")

    phiStart: Optional[float] = Field(title="Phi Start", unit="°")
    kappaStart: Optional[float] = Field(title="Kappa Start", unit="°")
    omegaStart: Optional[float] = Field(title="Omega Start", unit="°")
    chiStart: Optional[float] = Field(title="Chi Start", unit="°")

    DataCollectionGroup: DataCollectionGroup

    metadata: DataCollectionMetaData = Field(alias="_metadata")

    class Config:
        orm_mode = True


class RobotAction(BaseModel):
    actionType: str
    status: Optional[str]
    message: Optional[str]

    class Config:
        orm_mode = True


class EventBase(BaseModel):
    id: int
    type: str
    startTime: Optional[datetime] = Field(title="Start Time")
    endTime: Optional[datetime] = Field(title="End Time")
    count: int
    session: str
    blSample: Optional[str] = Field(description="Sample Name")
    blSampleId: Optional[int] = Field(description="Sample Id")

    Item: Union[DataCollection, RobotAction]


class Event(EventBase):
    class Config:
        orm_mode = True

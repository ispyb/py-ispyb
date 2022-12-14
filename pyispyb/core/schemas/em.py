from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime


class Tomogram(BaseModel):
    tomogramId: int
    dataCollectionId: int
    autoProcProgramId: Optional[int]
    volumeFile: Optional[str] = Field(..., max_length=255)
    stackFile: Optional[str] = Field(..., max_length=255)
    sizeX: Optional[int]
    sizeY: Optional[int]
    sizeZ: Optional[int]
    pixelSpacing: Optional[float]
    residualErrorMean: Optional[float]
    residualErrorSD: Optional[float]
    xAxisCorrection: Optional[float]
    tiltAngleOffset: Optional[float]
    zShift: Optional[float]

    class Config:
        orm_mode = True


class MotionCorrection(BaseModel):
    motionCorrectionId: int
    dataCollectionId: int
    autoProcProgramId: Optional[int]
    imageNumber: Optional[int] = Field(
        ..., title="Movie number, sequential in time 1-n"
    )
    firstFrame: Optional[int] = Field(..., title="First frame of movie used")
    lastFrame: Optional[int] = Field(..., title="Last frame of movie used")
    dosePerFrame: Optional[float] = Field(..., title="Dose per frame", unit="e-/A^2")
    doseWeight: Optional[float] = Field(..., title="Dose weight")
    totalMotion: Optional[float] = Field(..., title="Total motion", unit="A")
    averageMotionPerFrame: Optional[float] = Field(
        ..., title="Average motion per frame", unit="A"
    )
    driftPlotFullPath: Optional[str] = Field(
        ..., max_length=255, title="Path to drift plot"
    )
    micrographFullPath: Optional[str] = Field(
        ..., max_length=255, title="Path to micrograph"
    )
    micrographSnapshotFullPath: Optional[str] = Field(
        ..., max_length=255, title="Path to micrograph"
    )
    patchesUsedX: Optional[int] = Field(..., title="Patches used in x")
    patchesUsedY: Optional[int] = Field(..., title="Patches used in y")
    fftFullPath: Optional[str] = Field(
        ...,
        max_length=255,
        title="Path to raw micrograph FFT",
    )
    fftCorrectedFullPath: Optional[str] = Field(
        ...,
        max_length=255,
        title="Path to drift corrected micrograph FFT",
    )
    comments: Optional[str] = Field(..., max_length=255)

    class Config:
        orm_mode = True


class CTF(BaseModel):
    ctfId: int
    boxSizeX: Optional[float] = Field(..., title="Box size in x", unit="pixels")
    boxSizeY: Optional[float] = Field(..., title="Box size in y", unit="pixels")
    minResolution: Optional[float] = Field(
        ..., title="Minimum resolution for CTF", unit="A"
    )
    maxResolution: Optional[float] = Field(..., unit="A")
    minDefocus: Optional[float] = Field(..., unit="A")
    maxDefocus: Optional[float] = Field(..., unit="A")
    defocusStepSize: Optional[float] = Field(..., unit="A")
    astigmatism: Optional[float] = Field(..., unit="A")
    astigmatismAngle: Optional[float] = Field(..., unit="deg?")
    estimatedResolution: Optional[float] = Field(..., unit="A")
    estimatedDefocus: Optional[float] = Field(..., unit="A")
    amplitudeContrast: Optional[float] = Field(..., unit="%?")
    ccValue: Optional[float] = Field(..., title="Correlation value")
    fftTheoreticalFullPath: Optional[str] = Field(
        ..., max_length=255, title="Full path to the jpg image of the simulated FFT"
    )
    comments: Optional[str] = Field(..., max_length=255)

    class Config:
        orm_mode = True


class Movie(BaseModel):
    movieId: int
    movieNumber: int
    movieFullPath: Optional[str] = Field(..., max_length=255)
    createdTimeStamp: datetime
    positionX: Optional[float]
    positionY: Optional[float]
    nominalDefocus: Optional[float] = Field(..., title="Nominal defocus", unit="A")
    angle: Optional[float] = Field(
        ..., unit="degrees relative to perpendicular to beam"
    )
    fluence: Optional[float] = Field(
        ...,
        title="accumulated electron fluence from start to end of acquisition of this movie",
    )
    numberOfFrames: Optional[int] = Field(
        ...,
        title="number of frames per movie",
    )

    class Config:
        orm_mode = True


class FullMovie(BaseModel):
    CTF: CTF
    Movie: Movie
    MotionCorrection: MotionCorrection

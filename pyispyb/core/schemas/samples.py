# import datetime

from typing import Optional

from pydantic import BaseModel, Field

from pyispyb.core.schemas.utils import make_optional


class Position(BaseModel):
    posX: int
    posY: int

    class Config:
        orm_mode = True


class SampleMetaData(BaseModel):
    subsamples: int = Field(description="Number of sub samples")
    datacollections: int = Field(description="Number of data collections")
    types: Optional[list[str]] = Field(
        description="Types of data collections", nullable=True
    )
    queued: Optional[bool] = Field(
        description="Whether this sample is queued for data collection"
    )
    strategies: Optional[int] = Field(description="Number of successful strategies")
    autoIntegrations: Optional[int] = Field(
        description="Number of successful auto-integrations"
    )
    integratedResolution: Optional[float] = Field(
        description="Highest integration resolution", nullable=True
    )
    proposal: Optional[str] = Field(description="The associated proposal")

    class Config:
        orm_mode = True


class ComponentTypeCreate(BaseModel):
    name: str = Field(title="Name")

    class Config:
        orm_mode = True


class ComponentType(ComponentTypeCreate):
    componentTypeId: int = Field(title="id")

    class Config:
        orm_mode = True


class ConcentrationType(BaseModel):
    concentrationTypeId: int = Field(title="id")
    name: str = Field(title="Name")
    symbol: str = Field(title="Symbol")

    class Config:
        orm_mode = True


class ComponentCreate(BaseModel):
    name: str = Field(title="Name")
    composition: Optional[str] = Field(title="Composition", nullable=True)
    ComponentType: ComponentType | ComponentTypeCreate

    class Config:
        orm_mode = True


class Component(ComponentCreate):
    componentId: int = Field(name="id")
    ComponentType: ComponentType

    class Config:
        orm_mode = True


class CompositionCreate(BaseModel):
    Component: Component | ComponentCreate
    abundance: Optional[float] = Field(title="Abundance", nullable=True)
    ratio: Optional[float] = Field(title="Ratio", nullable=True)
    ph: Optional[float] = Field(title="pH", nullable=True)
    ConcentrationType: Optional[ConcentrationType]

    class Config:
        orm_mode = True


class Composition(CompositionCreate):
    class Config:
        orm_mode = True


class SampleCrystalProteinCreate(BaseModel):
    proteinId: int

    class Config:
        orm_mode = True


class SampleCrystalProtein(SampleCrystalProteinCreate):
    proposalId: str
    name: str
    acronym: str

    class Config:
        orm_mode = True


class SampleCrystalCreate(BaseModel):
    Protein: SampleCrystalProteinCreate
    cell_a: Optional[int]
    cell_b: Optional[int]
    cell_c: Optional[int]
    cell_alpha: Optional[int]
    cell_beta: Optional[int]
    cell_gamma: Optional[int]
    size_X: Optional[int]
    size_Y: Optional[int]
    size_Z: Optional[int]
    crystal_compositions: Optional[list[CompositionCreate | None]]

    class Config:
        orm_mode = True


class SampleCrystal(SampleCrystalCreate):
    crystalId: int = Field(name="id")
    Protein: SampleCrystalProtein
    crystal_compositions: Optional[list[Composition]]


class SampleCrystalUpdate(make_optional(SampleCrystal)):
    crystalId: int = Field(name="id")
    Protein: SampleCrystalProteinCreate = Field(title="Protein")
    crystal_compositions: Optional[list[CompositionCreate | None]]


class SampleContainer(BaseModel):
    code: str

    sampleChangerLocation: Optional[str] = Field(
        title="Sample Changer Location", description="Position in sample change"
    )
    beamlineLocation: Optional[str] = Field(
        title="Beamline Location", description="Beamline if container is assigned"
    )

    class Config:
        orm_mode = True


class SampleCreate(BaseModel):
    name: str

    Crystal: SampleCrystalUpdate | SampleCrystalCreate
    sample_compositions: Optional[list[CompositionCreate | None]]

    comments: Optional[str] = Field(title="Comments", nullable=True)
    location: Optional[int] = Field(
        title="Location", description="Location in container"
    )
    containerId: Optional[int]
    loopType: Optional[str] = Field(title="Sample support", nullable=True)


class Sample(SampleCreate):
    blSampleId: int

    Crystal: SampleCrystal = Field(title="Crystal")
    sample_compositions: Optional[list[Composition]]

    Container: Optional[SampleContainer] = Field(title="Container")
    metadata: Optional[SampleMetaData] = Field(alias="_metadata")

    class Config:
        orm_mode = True


class SampleUpdate(
    make_optional(Sample, exclude={"Container": True, "metadata": True})
):
    blSampleId: int
    sample_compositions: Optional[list[CompositionCreate | None]]
    Crystal: SampleCrystalUpdate | SampleCrystalCreate

    class Config:
        orm_mode = True


class SampleImageMetaData(BaseModel):
    url: str = Field(description="Url to sample image")


class SampleImage(BaseModel):
    blSampleImageId: int
    blSampleId: int
    micronsPerPixelX: float
    micronsPerPixelY: float
    offsetX: int
    offsetY: int

    metadata: SampleImageMetaData = Field(alias="_metadata")

    class Config:
        orm_mode = True


class SubSampleSample(BaseModel):
    name: str

    class Config:
        orm_mode = True


class SubSampleMetaData(BaseModel):
    datacollections: int = Field(description="Number of data collections")
    types: Optional[list[str]] = Field(description="Types of data collections")


class SubSampleBase(BaseModel):
    type: Optional[str] = Field(title="Subsample Type")
    comments: Optional[str] = Field(title="Comments", nullable=True)
    blSampleId: int

    metadata: SubSampleMetaData = Field(alias="_metadata")


class SubSample(SubSampleBase):
    blSubSampleId: int

    BLSample: SubSampleSample
    Position1: Optional[Position]
    Position2: Optional[Position]

    class Config:
        orm_mode = True

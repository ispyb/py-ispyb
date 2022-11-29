from typing import Optional
from pydantic import BaseModel, Field

from ispyb import models

from .dewars import DewarShipping

c = models.Container


class ContainerDewar(BaseModel):
    code: str = Field(title="Name")

    Shipping: DewarShipping

    class Config:
        orm_mode = True


class ContainerCreate(BaseModel):
    code: str = Field(title="Name")
    dewarId: int
    containerType: str

    sampleChangerLocation: Optional[str] = Field(
        description="Position in sample change"
    )
    beamlineLocation: Optional[str] = Field(
        description="Beamline if container is assigned"
    )


class Container(ContainerCreate):
    containerId: int

    Dewar: ContainerDewar

    class Config:
        orm_mode = True

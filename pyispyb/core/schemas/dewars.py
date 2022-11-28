from typing import Optional
from pydantic import BaseModel, Field

from ispyb import models

d = models.Dewar


class DewarShipping(BaseModel):
    proposalId: int
    shippingName: str = Field(title="Name")

    class Config:
        orm_mode = True


class DewarCreate(BaseModel):
    shippingId: int
    code: str = Field(title="Name")
    dewarType: Optional[str]


class Dewar(DewarCreate):
    dewarId: int

    Shipping: DewarShipping

    class Config:
        orm_mode = True

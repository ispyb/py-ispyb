# import datetime
from pydantic import BaseModel, Field


class Shipping(BaseModel):
    shippingName: str = Field(title="Name")

    class Config:
        orm_mode = True


class Dewar(BaseModel):
    code: str = Field(title="Name")

    Shipping: Shipping

    class Config:
        orm_mode = True


class Container(BaseModel):
    code: str = Field(title="Name")

    Dewar: Dewar

    class Config:
        orm_mode = True

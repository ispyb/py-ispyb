# import datetime
from pydantic import BaseModel


class Shipping(BaseModel):
    shippingName: str

    class Config:
        orm_mode = True


class Dewar(BaseModel):
    code: str

    Shipping: Shipping

    class Config:
        orm_mode = True


class Container(BaseModel):
    code: str

    Dewar: Dewar

    class Config:
        orm_mode = True

from pydantic import BaseModel


class ImageHeader(BaseModel):
    pass


class ImageHistogram(BaseModel):
    values: list[int]
    bins: list[int]
    shape: tuple
    max: float

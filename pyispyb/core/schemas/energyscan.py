from pydantic import BaseModel


class EnergyScan(BaseModel):
    energyScanId: int

    class Config:
        orm_mode = True

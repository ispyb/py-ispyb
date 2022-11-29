from pydantic import BaseModel


class XFEFluorescenceSpectrum(BaseModel):
    xfeFluorescenceSpectrumId: int

    class Config:
        orm_mode = True

from typing import Optional

from pydantic import BaseModel, Field


class ComponentType(BaseModel):
    componentTypeId: int
    name: str

    class Config:
        orm_mode = True


class ConcentrationType(BaseModel):
    concentrationTypeId: int
    name: str
    symbol: str

    class Config:
        orm_mode = True


class ProteinMetaData(BaseModel):
    pdbs: Optional[int] = Field(description="Number of attached pdbs")


class ProteinBase(BaseModel):
    name: str
    acronym: str = Field(title="Acronym", description="A short name")
    proposalId: int
    sequence: Optional[str] = Field(
        title="Sequence/SMILES", description="Sequence or chemical composition"
    )
    density: Optional[float] = Field(title="Density", unit="g/L")
    molecularMass: Optional[float] = Field(title="Mass", unit="kDa")

    containmentLevel: Optional[str]
    hazardGroup: Optional[str]
    safetyLevel: Optional[str]

    ComponentType: Optional[ComponentType]
    ConcentrationType: Optional[ConcentrationType]


class Protein(ProteinBase):
    proteinId: int

    metadata: Optional[ProteinMetaData] = Field(alias="_metadata")

    class Config:
        orm_mode = True

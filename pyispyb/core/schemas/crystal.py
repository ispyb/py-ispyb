"""
Project: py-ispyb.

https://github.com/ispyb/py-ispyb

This file is part of py-ispyb software.

py-ispyb is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

py-ispyb is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with py-ispyb. If not, see <http://www.gnu.org/licenses/>.
"""


__license__ = "LGPLv3+"

from typing import Optional

from pydantic import BaseModel, Field
from ispyb import models

from .protein import Protein

c = models.Crystal


class CrystalBase(BaseModel):
    cell_a: Optional[float] = Field(title="Cell A", nullable=True)
    cell_b: Optional[float] = Field(title="Cell B", nullable=True)
    cell_c: Optional[float] = Field(title="Cell C", nullable=True)
    cell_alpha: Optional[float] = Field(title="Cell Alpha", nullable=True)
    cell_beta: Optional[float] = Field(title="Cell Beta", nullable=True)
    cell_gamma: Optional[float] = Field(title="Cell Gamma", nullable=True)
    Protein: Protein


class Crystal(CrystalBase):
    crystalId: int
    proteinId: int = Field(title="Protein")

    Protein: Protein

    class Config:
        orm_mode = True

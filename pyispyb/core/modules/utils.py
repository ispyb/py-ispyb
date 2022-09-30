import os

from pint import UnitRegistry
from sqlalchemy.sql.expression import cast
from sqlalchemy import (
    func,
    Integer,
)

ureg = UnitRegistry()


# Taken from https://gitlab.esrf.fr/ui/replicator/-/blob/master/replicator/impl/ispyb.py#L116
def decode_external_id(column):
    return cast(func.CONV(func.HEX(column), 16, 10), Integer)


def encode_external_id(column):
    return column.to_bytes(16, byteorder="big")


def to_energy(wavelength: float, round_value: bool = True) -> float:
    """Convert from wavelength in Angstroms to energy in eV"""
    energy = (
        ((ureg.planck_constant * ureg.c) / (wavelength * ureg.angstrom))
        .to(ureg.eV)
        .magnitude
    )
    return round(energy) if round_value else energy


def get_last_line(file: str) -> str:
    """Get the last line of the file
    https://stackoverflow.com/questions/46258499/how-to-read-the-last-line-of-a-file-in-python
    """
    with open(file, "rb") as f:
        try:
            f.seek(-2, os.SEEK_END)
            while f.read(1) != b"\n":
                f.seek(-2, os.SEEK_CUR)
        except OSError:
            f.seek(0)
        return f.readline().decode().strip()

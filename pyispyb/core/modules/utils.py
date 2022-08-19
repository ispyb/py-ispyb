from sqlalchemy.sql.expression import cast
from sqlalchemy import (
    func,
    Integer,
)


# Taken from https://gitlab.esrf.fr/ui/replicator/-/blob/master/replicator/impl/ispyb.py#L116
def decode_external_id(column):
    return cast(func.CONV(func.HEX(column), 16, 10), Integer)


def encode_external_id(column):
    return column.to_bytes(16, byteorder="big")

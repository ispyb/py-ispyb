from typing import Optional
from fastapi import Query


def session(
    session: Optional[str] = Query(
        None, description="Session name to filter by", regex=r"^\w+\d+-\d+$"
    )
) -> Optional[str]:
    return session


def data_collection_group_id(
    data_collection_group_id: Optional[int] = Query(
        None, description="Data collection group id to filter by"
    )
) -> Optional[int]:
    return data_collection_group_id


def bl_sample_id(
    bl_sample_id: Optional[int] = Query(None, description="Sample id to filter by")
) -> Optional[int]:
    return bl_sample_id


def protein_id(
    protein_id: Optional[int] = Query(None, description="Protein id to filter by")
) -> Optional[int]:
    return protein_id

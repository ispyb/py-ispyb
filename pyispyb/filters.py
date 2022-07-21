from typing import Optional
from fastapi import Query


def session(
    session: Optional[str] = Query(
        None, description="Session name to filter by", regex=r"^\w+\d+-\d+$"
    )
) -> Optional[str]:
    return session


def dataCollectionGroupId(
    dataCollectionGroupId: Optional[int] = Query(
        None, description="Data collection group id to filter by"
    )
) -> Optional[int]:
    return dataCollectionGroupId


def blSampleId(
    blSampleId: Optional[int] = Query(None, description="Sample id to filter by")
) -> Optional[int]:
    return blSampleId


def proteinId(
    proteinId: Optional[int] = Query(None, description="Protein id to filter by")
) -> Optional[int]:
    return proteinId


def search(
    search: str = Query(None, description="Search string to filter by")
) -> Optional[str]:
    return search


def userGroupId(
    userGroupId: Optional[int] = Query(None, description="UserGroup id to filter by")
) -> Optional[int]:
    return userGroupId

from typing import Optional
from fastapi import Query


def session(
    session: Optional[str] = Query(
        None, description="Session name to filter by", regex=r"^\w+\d+-\d+$"
    )
) -> Optional[str]:
    return session


def proposal(
    proposal: Optional[str] = Query(
        None, description="Proposal name to filter by", regex=r"^\w+\d+$"
    )
) -> Optional[str]:
    return proposal


def beamLineName(
    beamLineName: Optional[str] = Query(None, description="Beamline name to filter by")
) -> Optional[str]:
    return beamLineName


def dataCollectionGroupId(
    dataCollectionGroupId: Optional[int] = Query(
        None, description="Data collection group id to filter by"
    )
) -> Optional[int]:
    return dataCollectionGroupId


def dataCollectionId(
    dataCollectionId: Optional[int] = Query(
        None, description="Data collection id to filter by"
    )
) -> Optional[int]:
    return dataCollectionId


def blSampleId(
    blSampleId: Optional[int] = Query(None, description="Sample id to filter by")
) -> Optional[int]:
    return blSampleId


def blSubSampleId(
    blSubSampleId: Optional[int] = Query(None, description="Sub sample id to filter by")
) -> Optional[int]:
    return blSubSampleId


def proteinId(
    proteinId: Optional[int] = Query(None, description="Protein id to filter by")
) -> Optional[int]:
    return proteinId


def search(
    search: str = Query(None, description="Search string to filter by")
) -> Optional[str]:
    return search


def containerId(
    containerId: Optional[int] = Query(None, description="Container id to filter by")
) -> Optional[int]:
    return containerId


def month(
    month: Optional[str] = Query(None, description="Month filter by", regex=r"^\d\d?$")
) -> Optional[str]:
    return month


def year(
    year: Optional[str] = Query(None, description="Year filter by", regex=r"^\d\d\d\d$")
) -> Optional[str]:
    return year

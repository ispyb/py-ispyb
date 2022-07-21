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


def beamlineName(
    beamlineName: Optional[str] = Query(None, description="Beamline name to filter by")
) -> Optional[str]:
    return beamlineName


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


def proteinId(
    proteinId: Optional[int] = Query(None, description="Protein id to filter by")
) -> Optional[int]:
    return proteinId

def containerId(
    containerId: Optional[int] = Query(None, description="Container id to filter by")
) -> Optional[int]:
    return containerId

import logging
from typing import Optional

from fastapi import Depends, HTTPException, status
from ispyb import models

from ...dependencies import pagination, order_by_factory
from ...app.extensions.database.utils import Paged
from ...app.base import AuthenticatedAPIRouter
from ... import filters

from ..modules import containers as crud
from ..schemas import containers as schema
from ..schemas.utils import paginated, make_optional


logger = logging.getLogger(__name__)
router = AuthenticatedAPIRouter(prefix="/containers", tags=["Containers"])


@router.get("/queue", response_model=paginated(schema.ContainerQueue))
def get_queued_containers(
    proposal: str = Depends(filters.proposal),
    beamLineName: str = Depends(filters.beamLineName),
    page: dict[str, int] = Depends(pagination),
) -> Paged[models.ContainerQueue]:
    """Get a list of queued containers"""
    return crud.get_queued_containers(
        proposal=proposal, beamLineName=beamLineName, **page
    )


@router.patch("/queue/{containerQueueId}", response_model=schema.ContainerQueue)
def update_queued_container(
    containerQueueId: int,
    containerQueue: schema.ContainerQueueUpdate,
) -> models.ContainerQueue:
    """Update a queued container"""
    try:
        return crud.update_queued_container(containerQueueId, containerQueue)
    except IndexError:
        raise HTTPException(status_code=404, detail="Container queue not found")
    except Exception:
        logger.exception(
            f"Could not update container queue `{containerQueueId}` with payload `{containerQueue}`"
        )
        raise HTTPException(status_code=400, detail="Could not update container queue")


QUEUED_SAMPLE_ORDER_BY = order_by_factory(
    crud.QUEUED_SAMPLE_ORDER_BY_MAP, "QueuedSampleOrder"
)


@router.get("/queue/samples", response_model=paginated(schema.ContainerQueueSample))
def get_queued_subsamples(
    proposal: str = Depends(filters.proposal),
    blSampleId: int = Depends(filters.blSampleId),
    containerId: int = Depends(filters.containerId),
    beamLineName: str = Depends(filters.beamLineName),
    status: Optional[crud.QUEUED_SAMPLE_STATUS_ENUM] = None,
    sort_order: dict = Depends(QUEUED_SAMPLE_ORDER_BY),
    page: dict[str, int] = Depends(pagination),
) -> Paged[models.ContainerQueueSample]:
    """Get a list of queued samples and sub samples"""
    return crud.get_queued_samples(
        proposal=proposal,
        blSampleId=blSampleId,
        containerId=containerId,
        beamLineName=beamLineName,
        status=status,
        sort_order=sort_order,
        **page,
    )


@router.delete(
    "/queue/samples/{containerQueueSampleId}", status_code=status.HTTP_204_NO_CONTENT
)
def delete_queued_sample(containerQueueSampleId: int) -> None:
    """Delete a queued sample"""
    try:
        crud.delete_queued_sample(containerQueueSampleId=containerQueueSampleId)
    except IndexError:
        raise HTTPException(status_code=404, detail="Queued sample not found")
    except Exception as e:
        logger.exception(f"Could not delete queued sample `{containerQueueSampleId}`")
        raise HTTPException(
            status_code=400, detail=f"Could not delete queued sample: {str(e)}"
        )


@router.get("", response_model=paginated(schema.Container))
def get_containers(
    proposal: str = Depends(filters.proposal),
    page: dict[str, int] = Depends(pagination),
) -> Paged[models.Container]:
    """Get a list of containers"""
    return crud.get_containers(proposal=proposal, **page)


@router.get(
    "/{containerId}",
    response_model=schema.Container,
    responses={404: {"description": "No such container"}},
)
def get_container(containerId: int) -> models.Container:
    """Get a container"""
    container = crud.get_containers(
        containerId=containerId,
        skip=0,
        limit=1,
    )
    try:
        return container.first
    except IndexError:
        raise HTTPException(status_code=404, detail="Container not found")


@router.post(
    "",
    response_model=schema.Container,
    status_code=status.HTTP_201_CREATED,
)
def create_container(container: schema.ContainerCreate) -> models.Container:
    """Create a new container"""
    return crud.create_container(
        container=container,
    )


CONTAINER_UPDATE_EXCLUDED = {}


@router.patch(
    "/{containerId}",
    response_model=schema.Container,
    responses={
        404: {"description": "No such container"},
        400: {"description": "Could not update container"},
    },
)
def update_container(
    containerId: int,
    container: make_optional(
        schema.ContainerCreate,
        exclude=CONTAINER_UPDATE_EXCLUDED,
    ),
):
    """Update a Container"""
    try:
        return crud.update_container(containerId, container)
    except IndexError:
        raise HTTPException(status_code=404, detail="Container not found")
    except Exception:
        logger.exception(
            f"Could not update container `{containerId}` with payload `{container}`"
        )
        raise HTTPException(status_code=400, detail="Could not update container")

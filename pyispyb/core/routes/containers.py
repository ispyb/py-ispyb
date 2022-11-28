import logging

from fastapi import Depends, HTTPException, status
from ispyb import models

from ...dependencies import pagination
from ...app.extensions.database.utils import Paged
from ...app.base import AuthenticatedAPIRouter
from ... import filters

from ..modules import containers as crud
from ..schemas import containers as schema
from ..schemas.utils import paginated, make_optional


logger = logging.getLogger(__name__)
router = AuthenticatedAPIRouter(prefix="/containers", tags=["Containers"])


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

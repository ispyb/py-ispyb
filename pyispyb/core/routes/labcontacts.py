from fastapi import Depends, HTTPException, status, Request
from ispyb import models

from pyispyb.dependencies import pagination
from pyispyb.app.extensions.database.utils import Paged
from pyispyb.app.base import AuthenticatedAPIRouter
from pyispyb import filters

from ..modules import labcontacts as crud
from ..schemas import labcontacts as schema
from ..schemas.utils import paginated


router = AuthenticatedAPIRouter(prefix="/labcontacts", tags=["Lab Contacts"])


@router.get("", response_model=paginated(schema.LabContact))
def get_lab_contacts(
    request: Request,
    proposal: str = Depends(filters.proposal),
    page: dict[str, int] = Depends(pagination),
) -> Paged[models.LabContact]:
    """Get a list of lab contacts"""
    return crud.get_labcontacts(
        proposal=proposal, beamLineGroups=request.app.db_options.beamLineGroups, **page
    )


@router.get(
    "/{labContactId}",
    response_model=schema.LabContact,
    responses={404: {"description": "No such contact"}},
)
def get_lab_contact(request: Request, labContactId: int) -> models.LabContact:
    """Get a lab contact"""
    users = crud.get_labcontacts(
        labContactId=labContactId,
        beamLineGroups=request.app.db_options.beamLineGroups,
        skip=0,
        limit=1,
    )
    try:
        return users.first
    except IndexError:
        raise HTTPException(status_code=404, detail="Lab contact not found")


@router.post(
    "/",
    response_model=schema.LabContact,
    status_code=status.HTTP_201_CREATED,
)
def create_lab_contact(
    request: Request, labcontact: schema.LabContactCreate
) -> models.LabContact:
    """Create a new lab contact"""
    return crud.create_labcontact(
        labcontact=labcontact,
        beamLineGroups=request.app.db_options.beamLineGroups,
    )

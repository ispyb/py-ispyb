from fastapi import Depends, HTTPException, status

from pyispyb.dependencies import pagination
from pyispyb.core import models
from pyispyb.app.extensions.database.utils import Paged
from pyispyb.app.base import AuthenticatedAPIRouter

from ..modules import labcontacts as crud
from ..schemas import labcontacts as schema
from ..schemas.utils import paginated


router = AuthenticatedAPIRouter(prefix="/labcontacts", tags=["Lab Contacts"])


@router.get("/", response_model=paginated(schema.LabContact))
def get_lab_contacts(
    page: dict[str, int] = Depends(pagination)
) -> Paged[models.LabContact]:
    """Get a list of lab contacts"""
    return crud.get_labcontacts(**page)


@router.get(
    "/{lab_contact_id}",
    response_model=schema.LabContact,
    responses={404: {"description": "No such contact"}},
)
def get_lab_contact(
    lab_contact_id: int
) -> models.LabContact:
    """Get a list of lab contacts"""
    users = crud.get_labcontacts(lab_contact_id=lab_contact_id, skip=0, limit=1)
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
    labcontact: schema.LabContactCreate
) -> models.LabContact:
    """Create a new lab contact"""
    return crud.create_labcontact(labcontact=labcontact)

from fastapi import Depends, HTTPException, status
from ispyb import models

from pyispyb.dependencies import pagination
from pyispyb.app.extensions.database.utils import Paged
from pyispyb.app.base import AuthenticatedAPIRouter
from pyispyb import filters

from ..modules import labcontacts as crud
from ..schemas import labcontacts as schema
from ..schemas.utils import paginated, make_optional


router = AuthenticatedAPIRouter(prefix="/labcontacts", tags=["Lab Contacts"])


@router.get("", response_model=paginated(schema.LabContact))
def get_lab_contacts(
    proposal: str = Depends(filters.proposal),
    page: dict[str, int] = Depends(pagination),
) -> Paged[models.LabContact]:
    """Get a list of lab contacts"""
    return crud.get_labcontacts(proposal=proposal, **page)


@router.get(
    "/{labContactId}",
    response_model=schema.LabContact,
    responses={404: {"description": "No such contact"}},
)
def get_lab_contact(labContactId: int) -> models.LabContact:
    """Get a lab contact"""
    users = crud.get_labcontacts(
        labContactId=labContactId,
        skip=0,
        limit=1,
    )
    try:
        return users.first
    except IndexError:
        raise HTTPException(status_code=404, detail="Lab contact not found")


@router.post(
    "",
    response_model=schema.LabContact,
    status_code=status.HTTP_201_CREATED,
)
def create_lab_contact(labcontact: schema.LabContactCreate) -> models.LabContact:
    """Create a new lab contact"""
    return crud.create_labcontact(
        labcontact=labcontact,
    )


LABCONTACT_UPDATE_EXCLUDED = {
    "proposalId": True,
    "Person": {
        "givenName": True,
        "familyname": True,
        "Laboratory": {"laboratoryExtPk": True},
    },
}


@router.patch(
    "/{labContactId}",
    response_model=schema.LabContact,
    responses={
        404: {"description": "No such group"},
        400: {"description": "Could not update group"},
    },
)
def update_lab_contact(
    labContactId: int,
    labContact: make_optional(
        schema.LabContactCreate,
        exclude=LABCONTACT_UPDATE_EXCLUDED,
    ),
):
    """Update a Lab Contact"""
    try:
        return crud.update_labcontact(labContactId, labContact)
    except IndexError:
        raise HTTPException(status_code=404, detail="Lab contact not found")

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..database.session import get_session
from ..dependencies import pagination
from ..modules import labcontacts as crud
from ..schemas import labcontacts as schema
from ..schemas.utils import paginated
from ..database import models
from ..database.utils import Paged


_router = APIRouter(prefix="/labcontacts", tags=["Lab Contacts"])


@router.get("/", response_model=paginated(schema.LabContact))
def get_lab_contacts(
    db: Session = Depends(get_session), page: dict[str, int] = Depends(pagination)
) -> Paged[models.LabContact]:
    """Get a list of lab contacts"""
    return crud.get_labcontacts(db, **page)


@router.get(
    "/{labContactId}",
    response_model=schema.LabContact,
    responses={404: {"description": "No such contact"}},
)
def get_lab_contact(
    labContactId: int, db: Session = Depends(get_session)
) -> models.LabContact:
    """Get a list of lab contacts"""
    users = crud.get_labcontacts(db, labContactId=labContactId, skip=0, limit=1)
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
    labcontact: schema.LabContactCreate, db: Session = Depends(get_session)
) -> models.LabContact:
    """Create a new lab contact"""
    return crud.create_labcontact(db=db, labcontact=labcontact)

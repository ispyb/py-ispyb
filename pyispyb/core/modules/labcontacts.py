from typing import Optional
from sqlalchemy.orm import Session, joinedload

from ..database import models
from ..database.utils import Paged, page
from ..schemas import labcontacts as schema


def get_labcontacts(
    db: Session, skip: int, limit: int, labContactId: Optional[int] = None
) -> Paged[models.LabContact]:
    query = (
        db.query(models.LabContact)
        .options(joinedload(models.LabContact.Person))
        .options(joinedload(models.LabContact.Person, models.Person.Laboratory))  # type: ignore   
    )

    if labContactId:
        query = query.filter(models.LabContact.labContactId == labContactId)

    total = query.count()
    query = page(query, skip=skip, limit=limit)

    return Paged(total=total, results=query.all(), skip=skip, limit=limit)


def create_labcontact(
    db: Session, labcontact: schema.LabContactCreate
) -> models.LabContact:

    labcontact_dict = labcontact.dict()
    person_dict = labcontact_dict.pop("Person")
    laboratory_dict = person_dict.pop("Laboratory")

    laboratory = models.Laboratory(**laboratory_dict)
    db.add(laboratory)
    db.commit()

    person = models.Person(laboratoryId=laboratory.laboratoryId, **person_dict)
    db.add(person)
    db.commit()

    contact = models.LabContact(personId=person.personId, **labcontact_dict)
    db.add(contact)
    db.commit()

    new_labcontact = get_labcontacts(
        db, labContactId=int(contact.labContactId), skip=0, limit=1
    )
    return new_labcontact.first

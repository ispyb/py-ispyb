from typing import Optional

from sqlalchemy.orm import joinedload
from ispyb import models

from pyispyb.app.extensions.database.utils import Paged, page
from pyispyb.app.extensions.database.middleware import db
from ..schemas import labcontacts as schema


def get_labcontacts(
    skip: int,
    limit: int,
    labContactId: Optional[int] = None,
    proposalId: Optional[int] = None,
) -> Paged[models.LabContact]:
    query = (
        db.session.query(models.LabContact)
        .options(joinedload(models.LabContact.Person))
        .options(joinedload(models.LabContact.Person, models.Person.Laboratory))  # type: ignore
    )

    if labContactId:
        query = query.filter(models.LabContact.labContactId == labContactId)

    if proposalId:
        query = query.filter(models.LabContact.proposalId == proposalId)

    total = query.count()
    query = page(query, skip=skip, limit=limit)

    return Paged(total=total, results=query.all(), skip=skip, limit=limit)


def create_labcontact(labcontact: schema.LabContactCreate) -> models.LabContact:

    labcontact_dict = labcontact.dict()
    person_dict = labcontact_dict.pop("Person")
    laboratory_dict = person_dict.pop("Laboratory")

    laboratory = models.Laboratory(**laboratory_dict)
    db.session.add(laboratory)
    db.session.commit()

    person = models.Person(laboratoryId=laboratory.laboratoryId, **person_dict)
    db.session.add(person)
    db.session.commit()

    contact = models.LabContact(personId=person.personId, **labcontact_dict)
    db.session.add(contact)
    db.session.commit()

    new_labcontact = get_labcontacts(
        labContactId=int(contact.labContactId), skip=0, limit=1
    )
    return new_labcontact.first

from typing import Optional

from sqlalchemy.orm import joinedload
from ispyb import models

from ...app.extensions.database.definitions import with_authorization
from ...app.extensions.database.utils import Paged, page, update_model
from ...app.extensions.database.middleware import db
from ..schemas import labcontacts as schema
from .proposals import get_proposals


def get_labcontacts(
    skip: int,
    limit: int,
    labContactId: Optional[int] = None,
    proposal: str = None,
    proposalId: Optional[int] = None,
    withAuthorization: bool = True,
) -> Paged[models.LabContact]:
    query = (
        db.session.query(models.LabContact)
        .options(joinedload(models.LabContact.Person))
        .options(joinedload(models.LabContact.Person, models.Person.Laboratory))
        .join(
            models.Proposal, models.Proposal.proposalId == models.LabContact.proposalId
        )
        .group_by(models.LabContact.labContactId)
    )

    if labContactId:
        query = query.filter(models.LabContact.labContactId == labContactId)

    if proposal:
        query = query.filter(models.Proposal.proposal == proposal)

    if proposalId:
        query = query.filter(models.LabContact.proposalId == proposalId)

    if withAuthorization:
        query = with_authorization(query)

    total = query.count()
    query = page(query, skip=skip, limit=limit)

    return Paged(total=total, results=query.all(), skip=skip, limit=limit)


def create_labcontact(labcontact: schema.LabContactCreate) -> models.LabContact:
    labcontact_dict = labcontact.dict()
    person_dict = labcontact_dict.pop("Person")
    laboratory_dict = person_dict.pop("Laboratory")

    proposals = get_proposals(proposalId=labcontact.proposalId, skip=0, limit=1)
    proposals.first

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


def update_labcontact(
    labContactId: int, labContact: schema.LabContactCreate
) -> models.LabContact:
    labcontact_dict = labContact.dict(exclude_unset=True)
    labconcat = get_labcontacts(labContactId=labContactId, skip=0, limit=1).first

    update_model(labconcat, labcontact_dict)
    db.session.commit()

    return get_labcontacts(labContactId=labContactId, skip=0, limit=1).first

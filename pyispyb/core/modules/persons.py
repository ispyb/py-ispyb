from typing import Optional
from sqlalchemy.orm import contains_eager
from pyispyb.core import models
from pyispyb.app.extensions.database.utils import Paged, page
from pyispyb.app.extensions.database.middleware import db


def get_persons(
    skip: int,
    limit: int,
    personId: Optional[int] = None,
    externalId: Optional[int] = None,
    familyName: Optional[str] = None,
    givenName: Optional[str] = None,
    login: Optional[str] = None,
    emailAddress: Optional[str] = None,
    withLaboratory: Optional[bool] = False,
) -> Paged[models.Person]:
    if withLaboratory:
        query = (
            db.session.query(models.Person)
            .join(models.Person.Laboratory)
            .options(
                contains_eager(models.Person.Laboratory),
            )
        )
    else:
        query = db.session.query(models.Person)

    if personId:
        query = query.filter(models.Person.personId == personId)

    if externalId:
        externalId = externalId.to_bytes(16, byteorder="big")
        query = query.filter(models.Person.externalId == externalId)

    if familyName:
        query = query.filter(models.Person.familyName == familyName)

    if givenName:
        query = query.filter(models.Person.givenName == givenName)

    if login:
        query = query.filter(models.Person.login == login)

    if emailAddress:
        query = query.filter(models.Person.emailAddress == emailAddress)

    if withLaboratory:
        query = query.populate_existing()

    total = query.count()
    query = page(query, skip=skip, limit=limit)

    return Paged(total=total, results=query.all(), skip=skip, limit=limit)

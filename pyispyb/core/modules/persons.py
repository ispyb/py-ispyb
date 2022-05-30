from typing import Optional
from sqlalchemy.orm import joinedload
from pyispyb.core import models
from pyispyb.app.extensions.database.utils import Paged, page
from pyispyb.app.extensions.database.middleware import db


def get_persons(
    skip: int,
    limit: int,
    personId: Optional[int] = None,
    siteId: Optional[int] = None,
    familyName: Optional[str] = None,
    givenName: Optional[str] = None,
    login: Optional[str] = None,
    emailAddress: Optional[str] = None,
) -> Paged[models.Person]:
    query = db.session.query(models.Person).options(
        joinedload(models.Person.Laboratory)
    )

    if personId:
        query = query.filter(models.Person.personId == personId)

    if siteId:
        query = query.filter(models.Person.siteId == siteId)

    if familyName:
        query = query.filter(models.Person.familyName == familyName)

    if givenName:
        query = query.filter(models.Person.givenName == givenName)

    if login:
        query = query.filter(models.Person.login == login)

    if emailAddress:
        query = query.filter(models.Person.emailAddress == emailAddress)

    total = query.count()
    query = page(query, skip=skip, limit=limit)

    return Paged(total=total, results=query.all(), skip=skip, limit=limit)

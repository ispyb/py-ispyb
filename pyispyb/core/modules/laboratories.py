from typing import Optional
from pyispyb.core import models
from pyispyb.app.extensions.database.utils import Paged, page
from pyispyb.app.extensions.database.middleware import db
from pyispyb.core.schemas import laboratories as schema


def get_laboratories(
    skip: int,
    limit: int,
    laboratoryId: Optional[int] = None,
    name: Optional[str] = None,
    city: Optional[str] = None,
    country: Optional[str] = None,
    laboratoryExtPk: Optional[int] = None,
) -> Paged[models.Laboratory]:
    query = db.session.query(models.Laboratory)

    if laboratoryId:
        query = query.filter(models.Laboratory.laboratoryId == laboratoryId)

    if name:
        query = query.filter(models.Laboratory.name == name)

    if city:
        query = query.filter(models.Laboratory.city == city)

    if country:
        query = query.filter(models.Laboratory.country == country)

    if laboratoryExtPk:
        query = query.filter(models.Laboratory.laboratoryExtPk == laboratoryExtPk)

    total = query.count()
    query = page(query, skip=skip, limit=limit)

    return Paged(total=total, results=query.all(), skip=skip, limit=limit)


def create_laboratory(laboratory: schema.Laboratory) -> models.Laboratory:

    laboratory_dict = laboratory.dict()

    laboratory = models.Laboratory(**laboratory_dict)
    db.session.add(laboratory)
    db.session.commit()

    new_laboratory = get_laboratories(
        laboratoryId=int(laboratory.labContactId), skip=0, limit=1
    )
    return new_laboratory.first

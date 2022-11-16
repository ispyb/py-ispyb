from typing import Optional

from sqlalchemy import and_, func
from sqlalchemy.orm import contains_eager, aliased
from ispyb import models

from ...app.extensions.database.utils import Paged, page, with_metadata
from ...app.extensions.database.middleware import db
from ...core.modules.utils import encode_external_id
from ...app.extensions.database.definitions import with_authorization


def get_persons(
    skip: int,
    limit: int,
    personId: Optional[int] = None,
    proposal: Optional[str] = None,
    sessionId: Optional[int] = None,
    externalId: Optional[int] = None,
    familyName: Optional[str] = None,
    givenName: Optional[str] = None,
    login: Optional[str] = None,
    emailAddress: Optional[str] = None,
    withLaboratory: Optional[bool] = False,
    withAuthorization: bool = False,
) -> Paged[models.Person]:
    metadata = {}

    query = (
        db.session.query(models.Person)
        .outerjoin(models.LabContact)
        .outerjoin(
            models.Proposal, models.LabContact.proposalId == models.Proposal.proposalId
        )
        .group_by(models.Person.personId)
    )

    if personId:
        query = query.filter(models.Person.personId == personId)

    if externalId:
        externalId = encode_external_id(externalId)
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
        query = query.join(models.Person.Laboratory).options(
            contains_eager(models.Person.Laboratory),
        )
        query = query.populate_existing()

    if sessionId:

        metadata["sessions"] = func.count(models.BLSession.sessionId)
        metadata["lastSession"] = func.max(models.BLSession.startDate)
        metadata["remote"] = models.SessionHasPerson.remote
        metadata["role"] = models.SessionHasPerson.role

        shp2 = aliased(models.SessionHasPerson)
        bls2 = aliased(models.BLSession)
        query = (
            query.join(models.SessionHasPerson)
            .join(models.BLSession)
            .outerjoin(shp2, shp2.personId == models.Person.personId)
            .outerjoin(
                bls2,
                and_(
                    models.BLSession.sessionId == shp2.sessionId,
                    bls2.startDate < models.BLSession.startDate,
                ),
            )
            .add_columns(
                metadata["sessions"],
                metadata["lastSession"],
                metadata["remote"],
                metadata["role"],
            )
        )

    # if withAuthorization:
    #     query = with_authorization(query)

    total = query.count()
    query = page(query, skip=skip, limit=limit)
    # print(query)
    results = with_metadata(query.all(), list(metadata.keys()))

    return Paged(total=total, results=results, skip=skip, limit=limit)

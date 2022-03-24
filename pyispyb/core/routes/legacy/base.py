from fastapi import Depends, HTTPException
from sqlalchemy.orm import joinedload
from pyispyb.app.base import BaseRouter
from pyispyb.app.globals import g
from pyispyb.app.extensions.auth.bearer import verify_jwt
from pyispyb.app.extensions.database.middleware import db
from pyispyb.core import models


async def token(token: str):
    print("decoding token")
    decoded = verify_jwt(token)
    if not decoded:
        raise HTTPException(status_code=403, detail="Invalid token or expired token.")

    g.login = decoded["username"]
    person = (
        db.session.query(models.Person)
        .options(joinedload(models.Person.UserGroup))
        .options(joinedload(models.Person.UserGroup, models.UserGroup.Permission))
        .filter(models.Person.login == g.login)
        .first()
    )
    if not person:
        raise HTTPException(status_code=403, detail="User does not exist in database.")
    g.person = person

    permissions = []
    for group in person.UserGroup:
        for permission in group.Permission:
            permissions.append(permission.type)
    g.permissions = permissions

    print("permissions", permissions)

    print("set person", g.login, g.person)

    return token


class LegacyAPIRouter(BaseRouter):
    def __init__(self, *args, **kwargs):
        print("LegacyAPIRouter")
        super().__init__(*args, dependencies=[Depends(token)], **kwargs)


router = LegacyAPIRouter(prefix="/legacy", tags=["Legacy"])

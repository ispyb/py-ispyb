from fastapi import Request
from pydantic import BaseModel

from pyispyb.app.extensions.options.schema import BeamLineGroup

from ...app.extensions.database.definitions import get_current_person
from ...app.base import AuthenticatedAPIRouter
from ...app.globals import g

router = AuthenticatedAPIRouter(prefix="/user", tags=["Current User"])


class CurrentUser(BaseModel):
    givenName: str
    familyName: str
    Permissions: list[str]
    personId: int
    uiGroups: list[str]


@router.get(
    "/current",
    response_model=CurrentUser,
)
def current_user(request: Request) -> CurrentUser:
    person = get_current_person(g.login)

    beamLineGroups: list[BeamLineGroup] = request.app.db_options.beamLineGroups
    groups = []
    for beamLineGroup in beamLineGroups:
        if beamLineGroup.permission in g.permissions:
            groups.append(beamLineGroup.uiGroup)

    return {
        "personId": person.personId,
        "givenName": person.givenName,
        "familyName": person.familyName,
        "Permissions": g.permissions,
        "uiGroups": groups,
    }

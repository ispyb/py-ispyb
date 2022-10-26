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
    beamLineGroups: list[str]
    beamLines: list[str]


@router.get(
    "/current",
    response_model=CurrentUser,
)
def current_user() -> CurrentUser:
    from pyispyb.app.main import app

    person = get_current_person(g.login)
    beamLineGroups: list[BeamLineGroup] = app.db_options.beamLineGroups
    groups = []
    beamLines = []
    for beamLineGroup in beamLineGroups:
        if beamLineGroup.permission in g.permissions:
            groups.append(beamLineGroup.groupName)
            beamLines.extend(
                [beamLine.beamLineName for beamLine in beamLineGroup.beamLines]
            )

    return {
        "personId": person.personId,
        "givenName": person.givenName,
        "familyName": person.familyName,
        "Permissions": g.permissions,
        "beamLineGroups": groups,
        "beamLines": list(set(beamLines)),
    }

from typing import Optional
from pydantic import BaseModel, Field

from ...app.extensions.database.definitions import get_current_person, get_options
from ...app.extensions.auth.onetime import generate_onetime_token
from ...app.extensions.options.schema import BeamLineGroup
from ...app.base import AuthenticatedAPIRouter
from ...app.globals import g

router = AuthenticatedAPIRouter(prefix="/user", tags=["Current User"])


class CurrentUser(BaseModel):
    givenName: Optional[str]
    familyName: Optional[str]
    login: str
    Permissions: list[str]
    personId: int
    beamLineGroups: list[str]
    beamLines: list[str]


@router.get(
    "/current",
    response_model=CurrentUser,
)
def current_user() -> CurrentUser:
    person = get_current_person(g.login)
    db_options = get_options()
    beamLineGroups: list[BeamLineGroup] = db_options.beamLineGroups
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
        "login": person.login,
        "Permissions": g.permissions,
        "beamLineGroups": groups,
        "beamLines": list(set(beamLines)),
    }


class OneTimeToken(BaseModel):
    validity: str = Field(description="The url to sign")
    token: Optional[str]


@router.post(
    "/sign",
    response_model=OneTimeToken,
)
def sign_url(token_request: OneTimeToken) -> OneTimeToken:
    """Sign a url with a one time token"""
    token = generate_onetime_token(token_request.validity, g.personId)
    return OneTimeToken(token=token, validity=token_request.validity)

from pydantic import BaseModel

from ...app.extensions.database.definitions import get_current_person
from ...app.base import AuthenticatedAPIRouter
from ...app.globals import g

router = AuthenticatedAPIRouter(prefix="/user", tags=["Current User"])


class CurrentUser(BaseModel):
    givenName: str
    familyName: str
    Permissions: list[str]
    personId: int


@router.get(
    "/current",
    response_model=CurrentUser,
)
def current_user() -> CurrentUser:
    person = get_current_person(g.login)

    return {
        "personId": person.personId,
        "givenName": person.givenName,
        "familyName": person.familyName,
        "Permissions": g.permissions,
    }

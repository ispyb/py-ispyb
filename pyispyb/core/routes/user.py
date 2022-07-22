from pydantic import BaseModel

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
    return {
        "personId": g.person.personId,
        "givenName": g.person.givenName,
        "familyName": g.person.familyName,
        "login": g.login,
        "Permissions": g.permissions,
    }

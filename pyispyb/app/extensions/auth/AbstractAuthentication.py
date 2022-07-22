from abc import ABC
import enum
import logging
from typing import Any, Optional

from fastapi import HTTPException
from ispyb import models

from ...extensions.database.middleware import db
from ...extensions.database.definitions import get_current_person


logger = logging.getLogger(__name__)


class AuthType(str, enum.Enum):
    login = "login"
    token = "token"  # nosec


class AbstractAuthentication(ABC):
    """
    Abstract authentication class.

    Base class for all site specific authentication classes
    """

    authentication_type: AuthType = AuthType.login

    def configure(self, config: dict[str, Any]) -> None:
        """Configure auth plugin.

        Args:
            config (dict): plugin configuration from file
        """
        return

    def authenticate(
        self, login: Optional[str], password: Optional[str], token: Optional[str]
    ) -> Optional[models.Person]:
        if self.authentication_type == AuthType.token:
            logger.debug("Authenticating via token")
            login = self.authenticate_by_token(token)
        else:
            logger.debug("Authenticating via username")
            login = self.authenticate_by_login(login, password)

        if not login:
            return

        person = get_current_person(login)
        if not person:
            if False:  # request.app.db_options.create_person_on_missing:
                person = self.create_person()
                if not person:
                    logger.warning(
                        "Could not create person from login `{login}` in `{self.__class__.__name__}`"
                    )
                    return
                db.session.add(person)
                db.session.commit()
            else:
                raise HTTPException(
                    status_code=401, detail="User does not exist in database."
                )

        return person

    def authenticate_by_login(self, login: str, password: str) -> Optional[str]:
        """Child method if authenticating via login / password

        Returns the login if authentication succeeded

        Args:
            login (str): The login
            password (str): The password

        Returns:
            login (str): If authenticated, the login

        """
        pass

    def authenticate_by_token(self, token: str) -> Optional[str]:
        """Child method if authenticating via token

        Returns the login if authentication succeeded

        Args:
            token (str): The token

        Returns:
            login (str): If authenticated, the login

        """
        pass

    def create_person(self) -> models.Person:
        """Child method to optionally create a new Person model

        Returns:
            person (models.Person): The new person ready to be committed to the db
        """
        pass

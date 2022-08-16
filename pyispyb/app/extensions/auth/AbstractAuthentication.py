from abc import ABC
import enum
import logging
from typing import Any, Optional

from ispyb import models


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
    config_export = []

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
            person = self.authenticate_by_token(token)
        else:
            logger.debug("Authenticating via login")
            person = self.authenticate_by_login(login, password)

        return person

    def authenticate_by_login(
        self, login: str, password: str
    ) -> Optional[models.Person]:
        """Child method if authenticating via login / password

        Returns the login if authentication succeeded

        Args:
            login (str): The login
            password (str): The password

        Returns:
            person (models.Person): If authenticated, a prepopulated `Person`

        """
        pass

    def authenticate_by_token(self, token: str) -> Optional[models.Person]:
        """Child method if authenticating via token

        Returns the login if authentication succeeded

        Args:
            token (str): The token

        Returns:
            person (models.Person): If authenticated, a prepopulated `Person`

        """
        pass

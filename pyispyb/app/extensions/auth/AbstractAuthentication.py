from abc import ABC
import enum
import logging
from typing import Any, Optional

from ispyb import models


logger = logging.getLogger(__name__)


class AuthType(str, enum.Enum):
    login = "login"
    token = "token"


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
    ) -> Optional[str]:
        if self.authentication_type == AuthType.token:
            logger.error("Authenticating via token")
            return self.authenticate_by_token(token)
        else:
            logger.error("Authenticating via username")
            return self.authenticate_by_login(login, password)

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

    def get_info(self) -> models.Person:
        """Child method to optionally return login info"""
        pass

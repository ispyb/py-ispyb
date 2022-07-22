import logging
from typing import Any, Optional

from keycloak.exceptions import KeycloakAuthenticationError
from keycloak.keycloak_openid import KeycloakOpenID
from ispyb import models

from .AbstractAuthentication import AbstractAuthentication, AuthType


logger = logging.getLogger(__name__)


class KeycloakAuthentication(AbstractAuthentication):
    """Keycloak authentication class."""

    authentication_type = AuthType.token

    def configure(self, config: dict[str, Any]):
        """Configure auth plugin.

        Args:
            config (dict): plugin configuration from file
        """
        server_url = config["KEYCLOAK_SERVER_URL"]
        client_id = config["KEYCLOAK_CLIENT_ID"]
        realm_name = config["KEYCLOAK_REALM_NAME"]
        client_secret_key = config["KEYCLOAK_CLIENT_SECRET_KEY"]

        self.keycloak_openid = KeycloakOpenID(
            server_url=server_url,
            client_id=client_id,
            realm_name=realm_name,
            client_secret_key=client_secret_key,
            verify=True,
        )

        self._userinfo = None

    def authenticate_by_token(self, token: str) -> Optional[str]:
        try:
            self._userinfo = self.keycloak_openid.userinfo(token)
            return self._userinfo["preferred_username"]
        except KeycloakAuthenticationError:
            logger.exception("Could not log user in via keycloak token")

    def create_person(self) -> dict[str, Any]:
        return models.Person(
            givenName=self._userinfo["given_name"],
            familyName=self._userinfo["family_name"],
            login=self._userinfo["preferred_username"],
            emailAddress=self._userinfo["email"],
        )

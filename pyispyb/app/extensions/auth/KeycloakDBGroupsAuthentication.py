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
    config_export = ["KEYCLOAK_SERVER_URL", "KEYCLOAK_CLIENT_ID", "KEYCLOAK_REALM_NAME"]

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

    def authenticate_by_token(self, token: str) -> Optional[models.Person]:
        try:
            userinfo = self.keycloak_openid.userinfo(token)
            return models.Person(
                givenName=userinfo["given_name"],
                familyName=userinfo["family_name"],
                login=userinfo["preferred_username"],
                emailAddress=userinfo["email"],
            )
        except KeycloakAuthenticationError:
            logger.exception("Could not log user in via keycloak token")

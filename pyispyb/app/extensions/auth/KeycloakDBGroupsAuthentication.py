"""Project: py-ispyb.

https://github.com/ispyb/py-ispyb

This file is part of py-ispyb software.

py-ispyb is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

py-ispyb is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with py-ispyb. If not, see <http://www.gnu.org/licenses/>.
"""


__license__ = "LGPLv3+"


from typing import Any
from keycloak.exceptions import KeycloakAuthenticationError
from keycloak.keycloak_openid import KeycloakOpenID

from pyispyb.app.extensions.auth.AbstractDBGroupsAuthentication import AbstractDBGroupsAuthentication
from pyispyb.core import models
import logging


log = logging.getLogger(__name__)


class KeycloakDBGroupsAuthentication(AbstractDBGroupsAuthentication):
    """Keycloak authentication class."""

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
            verify=True)

    def get_person(self, username: str | None, password: str | None, token: str | None) -> models.Person | None:
        """Return db person associated to the user.

        Args:
            username : username if present in the request
            password : password if present in the request
            token : token if present in the request

        Returns: Person
        """
        if not token:
            return None
        try:
            userinfo = self.keycloak_openid.userinfo(token)
            return models.Person(
                login=userinfo["preferred_username"],
                familyName=userinfo["family_name"],
                givenName=userinfo["given_name"],
                emailAddress=userinfo["email"],
            )
        except KeycloakAuthenticationError as e:
            log.error(e)
            return None

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


from keycloak.exceptions import KeycloakAuthenticationError
from keycloak import KeycloakOpenID

from pyispyb.app.extensions.auth.AbstractAuthenticationDBRoles import AbstractAuthenticationDBRoles


class KeycloakAuthentication(AbstractAuthenticationDBRoles):
    """Keycloak authentication class."""

    def init_app(self, app):
        server_url = app.config["KEYCLOAK_SERVER_URL"]
        client_id = app.config["KEYCLOAK_CLIENT_ID"]
        realm_name = app.config["KEYCLOAK_REALM_NAME"]
        client_secret_key = app.config["KEYCLOAK_CLIENT_SECRET_KEY"]

        self.keycloak_openid = KeycloakOpenID(server_url=server_url,
                                              client_id=client_id,
                                              realm_name=realm_name,
                                              client_secret_key=client_secret_key,
                                              verify=True)

    def get_username(self, request):
        keycloak_token = request.headers.get("Keycloak-Token")
        if not keycloak_token:
            return None
        try:
            userinfo = self.keycloak_openid.userinfo(keycloak_token)
            print(userinfo)
            return userinfo["preferred_username"]
        except KeycloakAuthenticationError as e:
            print(e)
            return None

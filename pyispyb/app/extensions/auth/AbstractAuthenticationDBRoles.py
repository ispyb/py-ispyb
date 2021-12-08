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


import abc
from pyispyb.app.extensions.auth.AbstractAuthentication import AbstractAuthentication
from pyispyb.app.extensions.auth.models import Roles
from pyispyb.app.extensions import db
import json


class AbstractAuthenticationDBRoles(AbstractAuthentication):
    """Keycloak authentication class."""

    def init_app(self, app):
        pass

    def get_auth(self, request):
        username = self.get_username(request)
        if not username:
            return None, None
        roles = Roles.query.filter_by(username=username).first()
        if not roles:
            roles = Roles(username=username, roles="[]")
            db.session.add(roles)
            db.session.commit()
        return username, json.loads(roles.roles)

    @abc.abstractmethod
    def get_username(self, request):
        """Returns username associated to the user.

        Args:
            request: request object
        """

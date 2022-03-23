# Project: py-ispyb
# https://github.com/ispyb/py-ispyb

# This file is part of py-ispyb software.

# py-ispyb is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# py-ispyb is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License
# along with py-ispyb. If not, see <http://www.gnu.org/licenses/>.


import logging
import importlib
from .token import generate_token

from pyispyb.config import settings

__license__ = "LGPLv3+"


log = logging.getLogger(__name__)


class AuthProvider:
    """Allows to authentificate users."""

    def init_app(self, app):
        """Init extension."""

        module_name = settings.auth_module
        class_name = settings.auth_class
        config = {}
        cls = getattr(importlib.import_module(module_name), class_name)
        self._instance = cls()
        self._instance.configure(config)

    def get_auth(self, username, password, token):
        """
        Return username, groups, permissions associated to user.

        Basically this is the main authentification method where site_auth is site specific authentication class.

        Args:
            plugin (str): plugin to be used
            username (str): auth username
            password (str): auth password
            token (str): auth token

        Returns:
            username, groups, permissions
        """
        username, groups, permissions = self._instance.get_auth(
            username, password, token
        )
        if username is not None and groups is not None and permissions is not None:
            return username, groups, permissions
        return None, None, None

    def generate_token(self, username, groups, permissions):
        return generate_token(username, groups, permissions)


auth_provider = AuthProvider()

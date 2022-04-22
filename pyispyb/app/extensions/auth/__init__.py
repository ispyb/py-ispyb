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

from pyispyb.config import settings

__license__ = "LGPLv3+"


log = logging.getLogger(__name__)


class AuthProvider:
    """Allows to authentificate users."""

    def __init__(self):
        self.site_authentications = {}

    def init_app(self, app):
        """Init extension."""
        auth_list = settings.auth
        for auth_plugin in auth_list:
            for auth_name in auth_plugin:
                enabled = auth_plugin[auth_name]["ENABLED"]
                if enabled:
                    module_name: str = auth_plugin[auth_name]["AUTH_MODULE"]
                    class_name: str = auth_plugin[auth_name]["AUTH_CLASS"]
                    config = {}
                    if "CONFIG" in auth_plugin[auth_name]:
                        config = auth_plugin[auth_name]["CONFIG"]
                    cls = getattr(importlib.import_module(
                        module_name), class_name)
                    instance = cls()
                    instance.configure(config)
                    self.site_authentications[auth_name] = instance

    def get_auth(self, plugin, username, password, token):
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
        if plugin not in self.site_authentications:
            return None, None, None
        username, groups, permissions = self.site_authentications[plugin].get_auth(
            username, password, token)
        if username is not None and groups is not None and permissions is not None:
            return username, groups, permissions
        return None, None, None


auth_provider = AuthProvider()

"""
Project: py-ispyb
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

import logging
import ldap


from flask import current_app
from pyispyb.app.extensions.auth.AbstractAuth import AbstractAuth


__license__ = "LGPLv3+"


log = logging.getLogger(__name__)


class EMBLAuth(AbstractAuth):
    def __init__(self):
        AbstractAuth.__init__(self)

        self.ldap_conn = None

    def init_app(self, app):
        """
        Initializes ldap connection

        Args:
            app (flask app): current flask app
        """
        self.ldap_conn = ldap.initialize(app.config["LDAP_URI"])

    def get_roles(self, username, password):
        """
        Returns list of roles based on username and password.

        Args:
            username (str): user name
            password (str): password

        Returns:
            list: [list of roles as strings
        """
        roles = []
        search_filter = "(uid=%s)" % username
        attrs = ["*"]

        try:
            msg = "LDAP login: try to authenticate user %s as internal user" % username
            log.debug(msg)
            search_str = (
                "uid=" + username + "," + current_app.config["LDAP_BASE_INTERNAL"]
            )
            self.ldap_conn.simple_bind_s(search_str, password)
            result = self.ldap_conn.search_s(
                current_app.config["LDAP_BASE_INTERNAL"],
                ldap.SCOPE_ONELEVEL,
                search_filter,
                attrs,
            )
            if result:
                roles.append("manager")
                msg = (
                    "LDAP login: user %s authenticated as internal user (manager role)"
                    % username
                )
                log.debug(msg)
        except ldap.INVALID_CREDENTIALS as ex:
            msg = "LDAP login: unable to authenticate user %s (%s)" % (
                username,
                str(ex),
            )
            log.exception(msg)

        try:
            msg = "LDAP login: try to authenticate user %s as external user" % username
            log.debug(msg)
            search_str = (
                "uid=" + username + "," + current_app.config["LDAP_BASE_EXTERNAL"]
            )
            self.ldap_conn.simple_bind_s(search_str, password)
            result = self.ldap_conn.search_s(
                current_app.config["LDAP_BASE_EXTERNAL"],
                ldap.SCOPE_ONELEVEL,
                search_filter,
                attrs,
            )
            if result:
                roles.append("user")
                msg = (
                    "LDAP login: user %s authenticated as external user (user role)"
                    % username
                )
                log.debug(msg)
        except ldap.INVALID_CREDENTIALS as ex:
            msg = "LDAP login: unable to authenticate user %s (%s)" % (
                username,
                str(ex),
            )
            log.exception(msg)

        return roles

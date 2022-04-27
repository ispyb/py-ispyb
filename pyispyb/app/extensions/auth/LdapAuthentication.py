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
from typing import Any
import ldap


from pyispyb.app.extensions.auth.AbstractAuthentication import AbstractAuthentication


__license__ = "LGPLv3+"


log = logging.getLogger(__name__)


class LdapAuthentication(AbstractAuthentication):
    def __init__(self):
        AbstractAuthentication.__init__(self)

        self.ldap_conn = None
        self.ldap_base_internal = None
        self.ldap_base_groups = None

    def configure(self, config: dict[str, Any]):
        """Configure auth plugin.

        Args:
            config (dict): plugin configuration from file
        """
        self.ldap_conn = ldap.initialize(config["LDAP_URI"])
        self.ldap_base_internal = config["LDAP_BASE_INTERNAL"]
        self.ldap_base_groups = config["LDAP_BASE_GROUPS"]

    def get_user_and_groups(
        self, username: str | None, password: str | None, token: str | None
    ) -> tuple[str | None, list[str] | None]:
        """Return username and groups associated to the user.

        Args:
            username (string): auth username
            password (string): auth password
            token (string): auth token
        Returns:
            username, groups
        """
        user = None
        groups = None
        try:
            
            log.debug(f'LDAP login: try to authenticate user {username} as internal user')
            search_filter = "(uid=%s)" % username
            attrs = ["*"]
            search_str = f'uid={username}, {self.ldap_base_internal}'
            self.ldap_conn.simple_bind_s(search_str, password)
            result = self.ldap_conn.search_s(
                self.ldap_base_internal,
                ldap.SCOPE_ONELEVEL,
                search_filter,
                attrs,
            )
            user = username
        except ldap.INVALID_CREDENTIALS as ex:            
            log.exception(f'LDAP login: unable to authenticate user {username} ({str(ex)})')
            return None, None

        try:
            
            log.debug(f'LDAP login: Find {username} in  {self.ldap_base_internal}')
            
            search_filter = (
                f'(&(objectClass=groupOfUniqueNames)(uniqueMember=uid={username},{self.ldap_base_internal}))'
            )
            attrs = ["cn"]
            search_str = f'uid={username},{self.ldap_base_internal}'
            self.ldap_conn.simple_bind_s(search_str, password)
            result = self.ldap_conn.search_s(
                self.ldap_base_groups,
                ldap.SCOPE_SUBTREE,
                search_filter,
                attrs,
            )
            if result:
                groups = [
                    group_name.decode("utf-8")
                    for group in result
                    for group_name in group[1]["cn"]
                ]
                if not groups:
                    groups = ["User"]
        except ldap.INVALID_CREDENTIALS as ex:
            log.exception(f'LDAP login: unable to authenticate user {username} ({str(ex)})')
            return None, None

        if user is None or groups is None:
            return None, None
        return user, groups

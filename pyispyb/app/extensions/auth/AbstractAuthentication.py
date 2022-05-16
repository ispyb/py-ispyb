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
from typing import Any

from pyispyb.core import models
from pyispyb.app.extensions.database.middleware import db
from sqlalchemy.orm import joinedload


def get_groups_permissions(groups: list[str]) -> list[str]:
    """Get permission list from group list.

    Args:
        groups (string[]): list of groups

    Returns:
        string[]: list of permissions
    """
    permissions: list[str] = []
    for group_name in groups:
        db_group: models.UserGroup | None = (
            db.session.query(models.UserGroup)
            .options(joinedload(models.UserGroup.Permission))
            .filter_by(name=group_name)
            .first()
        )
        if db_group is not None:
            for permission in db_group.permissions:
                permissions.append(permission.type)
    return permissions


class AbstractAuthentication(object):
    """
    Abstract authentication class.

    Base class for all site specific authentication classes
    """

    __metaclass__ = abc.ABCMeta

    def configure(self, config: dict[str, Any]):
        """Configure auth plugin.

        Args:
            config (dict): plugin configuration from file
        """
        return

    def get_auth(
        self, username: str | None, password: str | None, token: str | None
    ) -> tuple[str | None, list[str] | None, list[str] | None]:
        """Return username, groups and permissions associated to the user.

        Args:
            username (string): auth username
            password (string): auth password
            token (string): auth token
        Returns:
            username, groups, permissions
        """
        username, groups = self.get_user_and_groups(username, password, token)
        if username is None or groups is None:
            return None, None, None
        return username, groups, get_groups_permissions(groups)

    @abc.abstractmethod
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

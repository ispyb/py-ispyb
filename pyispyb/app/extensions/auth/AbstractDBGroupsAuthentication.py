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

from sqlalchemy.orm import joinedload
from ispyb import models

from pyispyb.app.extensions.auth.AbstractAuthentication import AbstractAuthentication
from pyispyb.app.extensions.database.middleware import db


def get_person_groups(person: models.Person):
    """Get group list for person.

    Args:
        person (Person): person

    Returns:
        str[]: group list
    """
    groups: list[str] = []
    for group in person.UserGroup:
        groups.append(group.name)
    return groups


class AbstractDBGroupsAuthentication(AbstractAuthentication):
    """Keycloak authentication class."""

    def configure(self, config: dict[str, Any]):
        """Configure auth plugin.

        Args:
            config (dict): plugin configuration from file
        """
        pass

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
        person = self.get_person(username, password, token)
        if not person:
            return None, None
        db_person = (
            db.session.query(models.Person)
            .options(joinedload(models.Person.UserGroup))
            .filter(models.Person.login == person.login)
            .first()
        )
        if not db_person:
            db_person = person
            db.session.add(db_person)
            db.session.commit()
        return db_person.login, get_person_groups(db_person)

    @abc.abstractmethod
    def get_person(
        self, username: str | None, password: str | None, token: str | None
    ) -> models.Person | None:
        """Return db person associated to the user.

        Args:
            username : username if present in the request
            password : password if present in the request
            token : token if present in the request

        Returns: Person
        """

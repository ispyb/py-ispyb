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
from pyispyb.app.extensions import db

from pyispyb.core.models import Person


def get_person_groups(person):
    groups = []
    for group in person.UserGroup:
        groups.append(group.name)
    return groups


class AbstractDBGroupsAuthentication(AbstractAuthentication):
    """Keycloak authentication class."""

    def init_app(self, app):
        pass

    def get_user_and_groups(self, username, password, token):
        person = self.get_person(username, password, token)
        if not person:
            return None, None
        db_person = Person.query.filter_by(login=person.login).first()
        if not db_person:
            db_person = person
            db.session.add(db_person)
            db.session.commit()
        return db_person.login, get_person_groups(db_person)

    @abc.abstractmethod
    def get_person(self, username, password, token):
        """Returns username associated to the user.

        Args:
            username : username if present in the request
            password : password if present in the request
            token : token if present in the request

        Returns: Person
        """

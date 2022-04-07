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


from pyispyb.app.extensions.auth.AbstractAuthentication import AbstractAuthentication


class DummyAuthentication(AbstractAuthentication):
    """Dummy authentication class."""

    def get_auth(self, username: str | None, password: str | None, token: str | None) -> tuple[str | None, list[str] | None, list[str] | None]:
        """Return username, groups and permissions associated to the user.

        Args:
            username (string): auth username
            password (string): auth password
            token (string): auth token
        Returns:
            username, groups, permissions
        """
        if not username:
            return None, None, None

        permissions = []
        if password:
            permissions = password.split(",")

        return username, permissions, permissions

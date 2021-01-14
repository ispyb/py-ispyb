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


__license__ = "LGPLv3+"


from sqlalchemy.dialects.mysql.enumerated import ENUM
from sqlalchemy.dialects.mysql.types import LONGBLOB

from pyispyb.app.extensions.logging import Logging
logging = Logging()

from . import api
from .auth import auth_provider
from .user_office_link import user_office_link
from .flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
db.ENUM = ENUM
db.LONGBLOB = LONGBLOB


def init_app(app):
    """Initializes app extensions

    Args:
        app (flask app): Flask application
    """
    for extension in (api, auth_provider, logging, db, user_office_link):
        extension.init_app(app)

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


from copy import deepcopy

from .api import Api
from .namespace import Namespace
from .http_exceptions import abort


api_v1 = Api(
    version="1.0",
    title="ISPyB",
    description="ISPyB Flask rest server",
    doc="/doc",
    default="Main",
    default_label="Main",
)


def init_app(app, **kwargs):
    # pylint: disable=unused-argument
    """
    API extension initialization point.
    """
    # Prevent config variable modification with runtime changes
    api_v1.authorizations = deepcopy(app.config["AUTHORIZATIONS"])

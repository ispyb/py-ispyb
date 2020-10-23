"""
Project: py-ispyb.

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

from flask import request, current_app
from flask_restx._http import HTTPStatus

from flask_restx_patched import Resource

from app.extensions.api import api_v1, Namespace
from app.extensions.auth import token_required, authorization_required
from app.extensions.user_office_link import user_office_link


api = Namespace(
    "User office", description="User office related namespace", path="/user_office"
)
api_v1.add_namespace(api)


@api.route("/sync", endpoint="user_office")
@api.doc(security="apikey")
class UserOfficeSync(Resource):

    """Sync with user office"""

    #@token_required
    #@authorization_required
    def post(self):
        """Sync with user office"""

        api.logger.info("Sync with uer office")
        user_office_link.sync_with_user_office()
        return HTTPStatus.OK, {"message": "Done!"}
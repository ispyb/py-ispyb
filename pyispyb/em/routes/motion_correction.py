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

from pyispyb.flask_restx_patched import Resource

from pyispyb.app.extensions.api import api_v1, Namespace
from pyispyb.app.extensions.auth import token_required, role_required
from pyispyb.em.schemas import motion_correction as motion_correction_schemas
from pyispyb.em.modules import motion_correction


api = Namespace(
    "Motion correction", description="Motion correction namespace", path="/motion_correction"
)
api_v1.add_namespace(api)


@api.route("", endpoint="motion_correction")
@api.doc(security="apikey")
class MotionCorrections(Resource):
    """Allows to get all motion_corrections"""

    @token_required
    @role_required
    def get(self):
        """Returns motion_corrections based on query parameters"""

        api.logger.info("Get all motion_corrections")
        return "Test"
        #return motion_correction.get_motion_corrections(request)

    @api.expect(motion_correction_schemas.f_schema)
    @api.marshal_with(motion_correction_schemas.f_schema, code=201)
    # @api.errorhandler(FakeException)
    # TODO add custom exception handling
    @token_required
    @role_required
    def post(self):
        """Adds a new motion_correction"""

        api.logger.info("Inserts a new motion_correction")
        return "Test post"
        #return motion_correction.add_motion_correction(api.payload)

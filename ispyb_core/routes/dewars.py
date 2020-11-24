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

from flask import request
from flask_restx_patched import Resource, HTTPStatus

from app.extensions.api import api_v1, Namespace
from app.extensions.auth import token_required, authorization_required

from ispyb_core.schemas import dewar as dewar_schemas
from ispyb_core.modules import dewar


__license__ = "LGPLv3+"


api = Namespace("Dewars", description="Dewar related namespace", path="/dewars")
api_v1.add_namespace(api)


@api.route("", endpoint="dewars")
@api.doc(security="apikey")
class Dewars(Resource):
    """Dewars resource"""

    @token_required
    @authorization_required
    def get(self):
        """Returns all dewars items"""
        return dewar.get_dewars(request)

    @token_required
    @api.expect(dewar_schemas.f_schema)
    @api.marshal_with(dewar_schemas.f_schema, code=201)
    def post(self):
        """Adds a new sample item"""
        dewar.add_dewar(api.payload)


@api.route("/<int:dewar_id>", endpoint="dewar_by_id")
@api.param("dewar_id", "Dewar id (integer)")
@api.doc(security="apikey")
@api.response(code=HTTPStatus.NOT_FOUND, description="Dewar not found.")
class DewarById(Resource):
    """Allows to get/set/delete a dewar item"""

    @api.doc(description="dewar_id should be an integer ")
    @api.marshal_with(dewar_schemas.f_schema, skip_none=False, code=HTTPStatus.OK)
    @token_required
    @authorization_required
    def get(self, dewar_id):
        """Returns a sample by sampleId"""
        return dewar.get_dewar_by_id(dewar_id)

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

from ispyb_core.schemas import container as container_schemas
from ispyb_core.modules import container


__license__ = "LGPLv3+"


api = Namespace(
    "Containers", description="Container related namespace", path="/containers"
)
api_v1.add_namespace(api)


@api.route("", endpoint="containers")
@api.doc(security="apikey")
class Containers(Resource):
    """Containers resource"""

    @token_required
    @authorization_required
    def get(self):
        """Returns all container items"""
        return container.get_containers(request)

    @token_required
    @api.expect(container_schemas.f_schema)
    @api.marshal_with(container_schemas.f_schema, code=201)
    def post(self):
        """Adds a new sample item"""
        container.add_container(api.payload)


@api.route("/<int:container_id>", endpoint="container_by_id")
@api.param("container_id", "Container id (integer)")
@api.doc(security="apikey")
@api.response(code=HTTPStatus.NOT_FOUND, description="Container not found.")
class ContainerById(Resource):
    """Allows to get/set/delete a container item"""

    @api.doc(description="container_id should be an integer ")
    @api.marshal_with(container_schemas.f_schema, skip_none=False, code=HTTPStatus.OK)
    @token_required
    @authorization_required
    def get(self, container_id):
        """Returns a container by container_id"""
        return container.get_container_by_id(container_id)

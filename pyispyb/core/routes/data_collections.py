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


from flask import request

from pyispyb.flask_restx_patched import Resource, HTTPStatus


from pyispyb.app.extensions.api import api_v1, Namespace
from pyispyb.app.extensions.auth import token_required, authorization_required

from pyispyb.core.schemas import data_collection as data_collection_schemas
from pyispyb.core.modules import data_collection


__license__ = "LGPLv3+"


api = Namespace(
    "Data collections",
    description="Data collection related namespace",
    path="/data_collections",
)
api_v1.add_namespace(api)


@api.route("")
@api.doc(security="apikey")
class DataColletions(Resource):
    """Allows to get all data_collections"""

    # @api.marshal_list_with(data_collection_schemas.data_collection_f_schema, skip_none=False, code=HTTPStatus.OK)
    # TODO Define model with JSON Schema
    @token_required
    @authorization_required
    def get(self):
        """Returns list of data_collections"""
        return data_collection.get_data_collections(request)


@api.route("/<int:data_collection_id>")
@api.param("data_collection_id", "data_collection id (integer)")
@api.doc(security="apikey")
@api.response(code=HTTPStatus.NOT_FOUND, description="data collection not found.")
class DataCollectionById(Resource):
    """Allows to get/set/delete a data_collection"""

    @api.doc(description="data_collection_id should be an integer ")
    @api.marshal_with(
        data_collection_schemas.f_schema,
        skip_none=False,
        code=HTTPStatus.OK,
    )
    @token_required
    @authorization_required
    def get(self, data_collection_id):
        """Returns a data_collection by data_collectionId"""
        return data_collection.get_data_collection_by_id(data_collection_id)


@api.route("/groups")
@api.doc(security="apikey")
class DataCollectionGroups(Resource):
    """Allows to get all data collection groups and add a new one"""

    # @api.marshal_list_with(data_collection_schemas.data_collection_f_schema, skip_none=False, code=HTTPStatus.OK)
    # TODO Define model with JSON Schema
    @token_required
    @authorization_required
    def get(self):
        """Returns list of data_collection_groups"""
        return data_collection.get_data_collection_groups(request)


# DatacollectionsByShipment ?do we need this?

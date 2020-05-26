# encoding: utf-8
#
#  Project: py-ispyb
#  https://github.com/ispyb/py-ispyb
#
#  This file is part of py-ispyb software.
#
#  py-ispyb is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  py-ispyb is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with py-ispyb. If not, see <http://www.gnu.org/licenses/>.


__license__ = "LGPLv3+"


from flask_restx_patched import Resource
from app.extensions.api import api_v1, Namespace
from app.extensions.auth import token_required
from app.schemas import data_collection_group as data_collection_group_schemas
from app.modules import data_collection_group


api = Namespace(
    "Data collection group",
    description="Data collection group related namespace",
    path="/dc_gr",
)


@api.route("")
class DataCollectionGroupList(Resource):
    """Data collection group resource"""

    @api.doc(security="apikey")
    # @token_required
    def get(self):
        """Returns all data collection groups"""
        # app.logger.info("Return all data collection groups")
        return data_collection_group.get_all_data_collection_groups()

    @api.expect(data_collection_group_schemas.f_data_collection_group_schema)
    @api.marshal_with(
        data_collection_group_schemas.f_data_collection_group_schema, code=201
    )
    def post(self):
        """Adds a new data collection group"""
        data_collection_group.add_data_collection_group(**api.payload)

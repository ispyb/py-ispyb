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


from flask_restx import Namespace, Resource

from app.extensions.api import api_v1
from app.extensions.auth import token_required
from app.modules import data_collection


api = Namespace(
    "Data collections", description="Data collection related namespace", path="/data_collections"
)
api_v1.add_namespace(api)


@api.route("")
@api.doc(security="apikey")
class DataCollections(Resource):
    """Data collection resource"""

    @token_required
    def get(self):
        """Returns all data collections"""
        # app.logger.info("Return all data collections")
        return data_collection.get_all_data_collections()

    @token_required
    @api.expect(data_collection.schemas.f_data_collection_schema)
    @api.marshal_with(data_collection.schemas.f_data_collection_schema, code=201)
    def post(self):
        """Adds a new proposal"""
        # app.logger.info("Insert new data collection")
        data_collection.add_data_collection(**api.payload)

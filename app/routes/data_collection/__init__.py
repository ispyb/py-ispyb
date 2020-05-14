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
#  along with MXCuBE. If not, see <http://www.gnu.org/licenses/>.


__license__ = "LGPLv3+"


from flask_restx import Namespace, Resource

from app.extensions.api import api_v1
from app.extensions import db
from app.modules import data_collection


api = Namespace(
    "Data collections", description="Data collection related namespace", path="/dc"
)
api_v1.add_namespace(api)


@api.route("/list")
class DataCollectionList(Resource):
    """Data collection resource"""

    @api.doc(security="apikey")
    # @token_required
    def get(self):
        """Returns all data collections"""
        # app.logger.info("Return all data collections")
        return data_collection.get_all_data_collections()

    @api.expect(data_collection.schemas.f_data_collection_schema)
    @api.marshal_with(data_collection.schemas.f_data_collection_schema, code=201)
    def post(self):
        """Adds a new proposal"""
        # app.logger.info("Insert new data collection")
        data_collection.add_data_collection(**api.payload)

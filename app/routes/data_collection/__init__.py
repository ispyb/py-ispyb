"""
ISPyB flask server
"""

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

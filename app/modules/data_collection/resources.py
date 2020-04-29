"""
ISPyB flask server
"""

from flask_restx import Namespace, Resource

#from ispyb.auth import token_required
from app.models import DataCollection as DataCollectionModel
from app.modules.data_collect.schemas import f_data_collection_schema, ma_data_collection_schema

api = Namespace('Data collections', description='Data collection related namespace', path='/dc')

def get_all_data_collections():
    data_collections = DataCollectionModel.query.all()
    return ma_data_collection_schema.dump(data_collections, many=True)

#def get_data_collection_by_id():


@api.route("")
class DataCollectionList(Resource):
    """Data collection resource"""

    @api.doc(security="apikey")
    #@token_required
    def get(self):
        """Returns all data collections"""
        #app.logger.info("Return all data collections")
        return get_all_data_collections()

    @api.expect(f_data_collection_schema)
    @api.marshal_with(f_data_collection_schema, code=201)
    def post(self):
        """Adds a new proposal"""
        #app.logger.info("Insert new data collection")
        try:
            data_collection = DataCollectionModel(**api.payload)
            db.session.add(data_collection)
            db.session.commit()
        except Exception as ex:
            #app.logger.exception(str(ex))
            db.session.rollback()


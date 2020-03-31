from flask_restplus import Namespace, Resource
from ispyb import app, api, db
from ispyb.models import DataCollection as DataCollectionModel
from ispyb.schemas import f_data_collection_schema, ma_data_collection_schema
from ispyb.auth import token_required

ns = Namespace('Data collections', description='Data collection related namespace', path='dc')

@ns.route("/")
class DataCollectionList(Resource):
    """Data collection resource"""

    @ns.doc(security="apikey")
    #@token_required
    def get(self):
        """Returns all data collections"""
        app.logger.info("Return all data collections")
        data_collections = DataCollectionModel.query.all()
        return ma_data_collection_schema.dump(data_collections, many=True)

    @ns.expect(f_data_collection_schema)
    @ns.marshal_with(f_data_collection_schema, code=201)
    def post(self):
        """Adds a new proposal"""
        app.logger.info("Insert new data collection")
        try:
            data_collection = DataCollectionModel(**api.payload)
            db.session.add(data_collection)
            db.session.commit()
        except Exception as ex:
            app.logger.exception(str(ex))
            db.session.rollback()


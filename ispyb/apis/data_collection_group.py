from flask_restplus import Namespace, Resource

from ispyb import app, api, db
from ispyb.auth import token_required
from ispyb.models import DataCollectionGroup as DataCollectionGroupModel
from ispyb.schemas import f_data_collection_group_schema, ma_data_collection_group_schema

ns = Namespace('Data collection group', description='Data collection group related namespace', path='/dc_gr')

def get_all_data_collection_groups():
    data_collection_groups = DataCollectionGroupModel.query.all()
    return ma_data_collection_group_schema.dump(data_collection_groups, many=True)


@ns.route("")
class DataCollectionGroupList(Resource):
    """Data collection group resource"""

    @ns.doc(security="apikey")
    #@token_required
    def get(self):
        """Returns all data collection groups"""
        app.logger.info("Return all data collection groups")
        return get_all_data_collection_groups()

    @ns.expect(f_data_collection_group_schema)
    @ns.marshal_with(f_data_collection_group_schema, code=201)
    def post(self):
        """Adds a new data collection group"""
        app.logger.info("Insert new data collection group")
        try:
            data_collection_group = DataCollectionGroupModel(**api.payload)
            db.session.add(data_collection_group)
            db.session.commit()
        except Exception as ex:
            app.logger.exception(str(ex))
            db.session.rollback()

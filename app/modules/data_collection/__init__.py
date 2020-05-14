"""ISPyB flask server"""
import logging

from app.extensions import db
from app.models import DataCollection as DataCollectionModel
from app.modules import data_collection
from app.modules.data_collection.schemas import (
    f_data_collection_schema,
    ma_data_collection_schema,
)


log = logging.getLogger(__name__)


def get_all_data_collections():
    data_collections = DataCollectionModel.query.all()
    return ma_data_collection_schema.dump(data_collections, many=True)


def add_data_collection(data_collection_dict):
    try:
        data_collection = DataCollectionModel(data_collection_dict)
        db.session.add(data_collection)
        db.session.commit()
    except Exception as ex:
        print(ex)
        # app.logger.exception(str(ex))
        db.session.rollback()

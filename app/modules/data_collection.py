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


import logging

from app.extensions import db
from app.models import DataCollection as DataCollectionModel
from app.schemas.data_collection import (
    data_collection_f_schema,
    data_collection_ma_schema,
)


log = logging.getLogger(__name__)


def get_all_data_collections():
    data_collections = DataCollectionModel.query.all()
    return data_collection_ma_schema.dump(data_collections, many=True)


def add_data_collection(data_collection_dict):
    try:
        data_collection = DataCollectionModel(data_collection_dict)
        db.session.add(data_collection)
        db.session.commit()
    except Exception as ex:
        print(ex)
        # app.logger.exception(str(ex))
        db.session.rollback()

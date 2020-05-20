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


from app.extensions import db

from app.models import DataCollectionGroup as DataCollectionGroupModel
from app.modules.data_collection_group.schemas import (
    f_data_collection_group_schema,
    ma_data_collection_group_schema,
)


def get_all_data_collection_groups():
    data_collection_groups = DataCollectionGroupModel.query.all()
    return ma_data_collection_group_schema.dump(data_collection_groups, many=True)


def add_data_collection_group(data_collection_group_dict):
    try:
        data_collection_group = DataCollectionGroupModel(data_collection_group_dict)
        db.session.add(data_collection_group)
        db.session.commit()
    except Exception as ex:
        print(ex)
        # app.logger.exception(str(ex))
        db.session.rollback()

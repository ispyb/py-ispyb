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


from marshmallow import Schema, fields as ma_fields
from flask_restx import fields as f_fields
from marshmallow_jsonschema import JSONSchema

from app.extensions.api import api_v1 as api

data_set_dict_schema = {
    "dataSetId": f_fields.Integer(required=True, description=""),
    "name": f_fields.String(required=True, description=""),
    "dataAcquisitionId": f_fields.Integer(required=False, description=""),
    "mergedResults": f_fields.String(required=False, description=""),
}


class DataSetSchema(Schema):
    """Marshmallows schema class representing DataSet table"""

    dataSetId = ma_fields.Integer()
    name = ma_fields.String()
    dataAcquisitionId = ma_fields.Integer()
    mergedResults = ma_fields.String()


data_set_f_schema = api.model("DataSet", data_set_dict_schema)
data_set_ma_schema = DataSetSchema()
data_set_json_schema = JSONSchema().dump(data_set_ma_schema)

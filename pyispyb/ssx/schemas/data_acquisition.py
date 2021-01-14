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

from pyispyb.app.extensions.api import api_v1 as api

data_acquisition_dict_schema = {
    "dataAcquisitionId": f_fields.Integer(required=True, description=""),
    "loadedSampleId": f_fields.Integer(required=True, description=""),
    "dataCollectionId": f_fields.Integer(
        required=True, description="reference to DataCollection.dataCollectionId"
    ),
    "experimentalPlanId": f_fields.Integer(required=True, description=""),
    "shortList": f_fields.String(required=True, description="url to shorlist file"),
    "autoprocessingProgrammId": f_fields.Integer(
        required=False, description="reference to AutoProcProgram.autoProcProgramId"
    ),
}


class DataAcquisitionSchema(Schema):
    """Marshmallows schema class representing DataAcquisition table"""

    dataAcquisitionId = ma_fields.Integer()
    loadedSampleId = ma_fields.Integer()
    dataCollectionId = ma_fields.Integer()
    experimentalPlanId = ma_fields.Integer()
    shortList = ma_fields.String()
    autoprocessingProgrammId = ma_fields.Integer()


data_acquisition_f_schema = api.model("DataAcquisition", data_acquisition_dict_schema)
data_acquisition_ma_schema = DataAcquisitionSchema()
data_acquisition_json_schema = JSONSchema().dump(data_acquisition_ma_schema)

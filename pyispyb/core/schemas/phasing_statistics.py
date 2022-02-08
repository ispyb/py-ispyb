"""
Project: py-ispyb.

https://github.com/ispyb/py-ispyb

This file is part of py-ispyb software.

py-ispyb is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

py-ispyb is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with py-ispyb. If not, see <http://www.gnu.org/licenses/>.
"""


__license__ = "LGPLv3+"


from marshmallow import Schema, fields as ma_fields
from flask_restx import fields as f_fields
from marshmallow_jsonschema import JSONSchema

from pyispyb.app.extensions.api import api_v1 as api

dict_schema = {
    'phasingStatisticsId': f_fields.Integer(
        required=True,
        description='Primary key (auto-incremented)'),
    'phasingHasScalingId1': f_fields.Integer(
        required=False,
        description='the dataset in question'),
    'phasingHasScalingId2': f_fields.Integer(
        required=False,
        description='if this is MIT or MAD, which scaling are being compared, null otherwise'),
    'phasingStepId': f_fields.Integer(
        required=False,
        description=''),
    'numberOfBins': f_fields.Integer(
        required=False,
        description='the total number of bins'),
    'binNumber': f_fields.Integer(
        required=False,
        description='binNumber, 999 for overall'),
    'lowRes': f_fields.String(
        required=False,
        description='low resolution cutoff of this binfloat'),
    'highRes': f_fields.String(
        required=False,
        description='high resolution cutoff of this binfloat'),
    'metric': f_fields.String(
        required=False,
        description='metricenum(Rcullis,Average Fragment Length,Chain Count,Residues Count,CC,PhasingPower,FOM,<d"/sig>,Best CC,CC(1/2),Weak CC,CFOM,Pseudo_free_CC,CC of partial model,Start R-work,Start R-free,Final R-work,Final R-free)'),
    'statisticsValue': f_fields.String(
        required=False,
        description='the statistics value'),
    'nReflections': f_fields.Integer(
        required=False,
        description=''),
    'recordTimeStamp': f_fields.DateTime(
        required=False,
        description='Creation or last update date/time'),
}


class PhasingStatisticsSchema(Schema):
    """Marshmallows schema class representing PhasingStatistics table"""

    phasingStatisticsId = ma_fields.Integer()
    phasingHasScalingId1 = ma_fields.Integer()
    phasingHasScalingId2 = ma_fields.Integer()
    phasingStepId = ma_fields.Integer()
    numberOfBins = ma_fields.Integer()
    binNumber = ma_fields.Integer()
    lowRes = ma_fields.String()
    highRes = ma_fields.String()
    metric = ma_fields.String()
    statisticsValue = ma_fields.String()
    nReflections = ma_fields.Integer()
    recordTimeStamp = ma_fields.DateTime()


f_schema = api.model('PhasingStatistics', dict_schema)
ma_schema = PhasingStatisticsSchema()
json_schema = JSONSchema().dump(ma_schema)

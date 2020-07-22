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

timed_xray_detection_dict_schema = {
        'timedXrayDetectionId': f_fields.Integer(required=True, description=''),
        'name': f_fields.String(required=False, description=''),
        'timedSequenceId': f_fields.Integer(required=False, description=''),
        'numberOfInternalTriggers': f_fields.Integer(required=False, description=''),
        'internalTriggerPeriod': f_fields.Integer(required=False, description=''),
        'internalGateDuration': f_fields.Integer(required=False, description=''),
        }

class TimedXrayDetectionSchema(Schema):
    """Marshmallows schema class representing TimedXrayDetection table"""

    timedXrayDetectionId = ma_fields.Integer()
    name = ma_fields.String()
    timedSequenceId = ma_fields.Integer()
    numberOfInternalTriggers = ma_fields.Integer()
    internalTriggerPeriod = ma_fields.Integer()
    internalGateDuration = ma_fields.Integer()

timed_xray_detection_f_schema = api.model('TimedXrayDetection', timed_xray_detection_dict_schema)
timed_xray_detection_ma_schema = TimedXrayDetectionSchema()
timed_xray_detection_json_schema = JSONSchema().dump(timed_xray_detection_ma_schema)

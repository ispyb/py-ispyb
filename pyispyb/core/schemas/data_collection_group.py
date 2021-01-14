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
        'dataCollectionGroupId': f_fields.Integer(required=True, description='Primary key (auto-incremented)'),
        'sessionId': f_fields.Integer(required=True, description='references Session table'),
        'comments': f_fields.String(required=False, description='comments'),
        'blSampleId': f_fields.Integer(required=False, description='references BLSample table'),
        'experimentType': f_fields.String(required=False, description='Standard: Routine structure determination experiment. Time Resolved: Investigate the change of a system over time. Custom: Special or non-standard data collection.enum(SAD,SAD - Inverse Beam,OSC,Collect - Multiwedge,MAD,Helical,Multi-positional,Mesh,Burn,MAD - Inverse Beam,Characterization,Dehydration,tomo,experiment,EM,PDF,PDF+Bragg,Bragg,single particle,Serial Fixed,Serial Jet,Standard,Time Resolved,Diamond Anvil High Pressure,Custom)'),
        'startTime': f_fields.DateTime(required=False, description='Start time of the dataCollectionGroup'),
        'endTime': f_fields.DateTime(required=False, description='end time of the dataCollectionGroup'),
        'crystalClass': f_fields.String(required=False, description='Crystal Class for industrials users'),
        'detectorMode': f_fields.String(required=False, description='Detector mode'),
        'actualSampleBarcode': f_fields.String(required=False, description='Actual sample barcode'),
        'actualSampleSlotInContainer': f_fields.Integer(required=False, description='Actual sample slot number in container'),
        'actualContainerBarcode': f_fields.String(required=False, description='Actual container barcode'),
        'actualContainerSlotInSC': f_fields.Integer(required=False, description='Actual container slot number in sample changer'),
        'workflowId': f_fields.Integer(required=False, description=''),
        'xtalSnapshotFullPath': f_fields.String(required=False, description=''),
        'scanParameters': f_fields.String(required=False, description=''),
        }

class DataCollectionGroupSchema(Schema):
    """Marshmallows schema class representing DataCollectionGroup table"""

    dataCollectionGroupId = ma_fields.Integer()
    sessionId = ma_fields.Integer()
    comments = ma_fields.String()
    blSampleId = ma_fields.Integer()
    experimentType = ma_fields.String()
    startTime = ma_fields.DateTime()
    endTime = ma_fields.DateTime()
    crystalClass = ma_fields.String()
    detectorMode = ma_fields.String()
    actualSampleBarcode = ma_fields.String()
    actualSampleSlotInContainer = ma_fields.Integer()
    actualContainerBarcode = ma_fields.String()
    actualContainerSlotInSC = ma_fields.Integer()
    workflowId = ma_fields.Integer()
    xtalSnapshotFullPath = ma_fields.String()
    scanParameters = ma_fields.String()

f_schema = api.model('DataCollectionGroup', dict_schema)
ma_schema = DataCollectionGroupSchema()
json_schema = JSONSchema().dump(ma_schema)

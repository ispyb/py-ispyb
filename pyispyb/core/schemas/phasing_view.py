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
        'phasingStepId': f_fields.Integer(required=False, description=''),
        'previousPhasingStepId': f_fields.Integer(required=False, description=''),
        'phasingAnalysisId': f_fields.Integer(required=False, description=''),
        'autoProcIntegrationId': f_fields.Integer(required=True, description='Primary key (auto-incremented)'),
        'dataCollectionId': f_fields.Integer(required=True, description='DataCollection item'),
        'anomalous': f_fields.Integer(required=False, description='boolean type:0 noanoum - 1 anoum'),
        'spaceGroup': f_fields.String(required=False, description='Space group'),
        'autoProcId': f_fields.Integer(required=False, description='Primary key (auto-incremented)'),
        'phasingStepType': f_fields.String(required=False, description='enum(PREPARE,SUBSTRUCTUREDETERMINATION,PHASING,MODELBUILDING)'),
        'method': f_fields.String(required=False, description=''),
        'solventContent': f_fields.String(required=False, description=''),
        'enantiomorph': f_fields.String(required=False, description=''),
        'lowRes': f_fields.String(required=False, description=''),
        'highRes': f_fields.String(required=False, description=''),
        'autoProcScalingId': f_fields.Integer(required=False, description='Primary key (auto-incremented)'),
        'spaceGroupShortName': f_fields.String(required=False, description='short name without blank'),
        'processingPrograms': f_fields.String(required=False, description='Processing programs (comma separated)'),
        'processingStatus': f_fields.Integer(required=False, description='success (1) / fail (0)'),
        'phasingPrograms': f_fields.String(required=False, description='Phasing programs (comma separated)'),
        'phasingStatus': f_fields.Integer(required=False, description='success (1) / fail (0)'),
        'phasingStartTime': f_fields.DateTime(required=False, description='Processing start time'),
        'phasingEndTime': f_fields.DateTime(required=False, description='Processing end time'),
        'sessionId': f_fields.Integer(required=False, description='references Session table'),
        'proposalId': f_fields.Integer(required=False, description=''),
        'blSampleId': f_fields.Integer(required=False, description=''),
        'name': f_fields.String(required=False, description=''),
        'code': f_fields.String(required=False, description=''),
        'acronym': f_fields.String(required=False, description=''),
        'proteinId': f_fields.Integer(required=False, description=''),
        }

class DatacollectionSummaryPhasingViewSchema(Schema):
    """Marshmallows schema class representing v_datacollection_summary_phasing table"""

    phasingStepId = ma_fields.Integer()
    previousPhasingStepId = ma_fields.Integer()
    phasingAnalysisId = ma_fields.Integer()
    autoProcIntegrationId = ma_fields.Integer()
    dataCollectionId = ma_fields.Integer()
    anomalous = ma_fields.Integer()
    spaceGroup = ma_fields.String()
    autoProcId = ma_fields.Integer()
    phasingStepType = ma_fields.String()
    method = ma_fields.String()
    solventContent = ma_fields.String()
    enantiomorph = ma_fields.String()
    lowRes = ma_fields.String()
    highRes = ma_fields.String()
    autoProcScalingId = ma_fields.Integer()
    spaceGroupShortName = ma_fields.String()
    processingPrograms = ma_fields.String()
    processingStatus = ma_fields.Integer()
    phasingPrograms = ma_fields.String()
    phasingStatus = ma_fields.Integer()
    phasingStartTime = ma_fields.DateTime()
    phasingEndTime = ma_fields.DateTime()
    sessionId = ma_fields.Integer()
    proposalId = ma_fields.Integer()
    blSampleId = ma_fields.Integer()
    name = ma_fields.String()
    code = ma_fields.String()
    acronym = ma_fields.String()
    proteinId = ma_fields.Integer()

f_schema = api.model('v_datacollection_summary_phasing', dict_schema)
ma_schema = DatacollectionSummaryPhasingViewSchema()
json_schema = JSONSchema().dump(ma_schema)

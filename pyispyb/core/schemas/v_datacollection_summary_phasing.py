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
    'v_datacollection_summary_phasing_autoProcIntegrationId': f_fields.Integer(
        required=True,
        description='Primary key (auto-incremented)'),
    'v_datacollection_summary_phasing_dataCollectionId': f_fields.Integer(
        required=True,
        description='DataCollection item'),
    'v_datacollection_summary_phasing_cell_a': f_fields.Float(
        required=False,
        description='Unit cell'),
    'v_datacollection_summary_phasing_cell_b': f_fields.Float(
        required=False,
        description='Unit cell'),
    'v_datacollection_summary_phasing_cell_c': f_fields.Float(
        required=False,
        description='Unit cell'),
    'v_datacollection_summary_phasing_cell_alpha': f_fields.Float(
        required=False,
        description='Unit cell'),
    'v_datacollection_summary_phasing_cell_beta': f_fields.Float(
        required=False,
        description='Unit cell'),
    'v_datacollection_summary_phasing_cell_gamma': f_fields.Float(
        required=False,
        description='Unit cell'),
    'v_datacollection_summary_phasing_anomalous': f_fields.Integer(
        required=False,
        description='boolean type:0 noanoum - 1 anoum'),
    'v_datacollection_summary_phasing_autoproc_space_group': f_fields.String(
        required=False,
        description='Space group'),
    'v_datacollection_summary_phasing_autoproc_autoprocId': f_fields.Integer(
        required=False,
        description='Primary key (auto-incremented)'),
    'v_datacollection_summary_phasing_autoProcScalingId': f_fields.Integer(
        required=False,
        description='Primary key (auto-incremented)'),
    'v_datacollection_summary_phasing_processingPrograms': f_fields.String(
        required=False,
        description='Processing programs (comma separated)'),
    'v_datacollection_summary_phasing_autoProcProgramId': f_fields.Integer(
        required=False,
        description='Primary key (auto-incremented)'),
    'v_datacollection_summary_phasing_processingStatus': f_fields.String(
        required=False,
        description='success (1) / fail (0)enum(RUNNING,FAILED,SUCCESS,0,1)'),
    'v_datacollection_summary_session_sessionId': f_fields.Integer(
        required=False,
        description=''),
    'v_datacollection_summary_session_proposalId': f_fields.Integer(
        required=False,
        description=''),
}


class v_datacollection_summary_phasingSchema(Schema):
    """Marshmallows schema class representing v_datacollection_summary_phasing table"""

    v_datacollection_summary_phasing_autoProcIntegrationId = ma_fields.Integer()
    v_datacollection_summary_phasing_dataCollectionId = ma_fields.Integer()
    v_datacollection_summary_phasing_cell_a = ma_fields.Float()
    v_datacollection_summary_phasing_cell_b = ma_fields.Float()
    v_datacollection_summary_phasing_cell_c = ma_fields.Float()
    v_datacollection_summary_phasing_cell_alpha = ma_fields.Float()
    v_datacollection_summary_phasing_cell_beta = ma_fields.Float()
    v_datacollection_summary_phasing_cell_gamma = ma_fields.Float()
    v_datacollection_summary_phasing_anomalous = ma_fields.Integer()
    v_datacollection_summary_phasing_autoproc_space_group = ma_fields.String()
    v_datacollection_summary_phasing_autoproc_autoprocId = ma_fields.Integer()
    v_datacollection_summary_phasing_autoProcScalingId = ma_fields.Integer()
    v_datacollection_summary_phasing_processingPrograms = ma_fields.String()
    v_datacollection_summary_phasing_autoProcProgramId = ma_fields.Integer()
    v_datacollection_summary_phasing_processingStatus = ma_fields.String()
    v_datacollection_summary_session_sessionId = ma_fields.Integer()
    v_datacollection_summary_session_proposalId = ma_fields.Integer()


f_schema = api.model('v_datacollection_summary_phasing', dict_schema)
ma_schema = v_datacollection_summary_phasingSchema()
json_schema = JSONSchema().dump(ma_schema)

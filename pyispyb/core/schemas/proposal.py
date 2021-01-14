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
        'proposalId': f_fields.Integer(required=True, description=''),
        'personId': f_fields.Integer(required=True, description=''),
        'title': f_fields.String(required=False, description=''),
        'proposalCode': f_fields.String(required=False, description=''),
        'proposalNumber': f_fields.String(required=False, description=''),
        'bltimeStamp': f_fields.DateTime(required=True, description=''),
        'proposalType': f_fields.String(required=False, description='Proposal type: MX, BX'),
        'externalId': f_fields.Integer(required=False, description=''),
        'state': f_fields.String(required=False, description='enum(Open,Closed,Cancelled)'),
        }

class ProposalSchema(Schema):
    """Marshmallows schema class representing Proposal table"""

    proposalId = ma_fields.Integer()
    personId = ma_fields.Integer()
    title = ma_fields.String()
    proposalCode = ma_fields.String()
    proposalNumber = ma_fields.String()
    bltimeStamp = ma_fields.DateTime()
    proposalType = ma_fields.String()
    externalId = ma_fields.Integer()
    state = ma_fields.String()

f_schema = api.model('Proposal', dict_schema)
ma_schema = ProposalSchema()
json_schema = JSONSchema().dump(ma_schema)

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

from app.extensions.api import api_v1 as api

auto_proc_dict = {
        'autoProcId': f_fields.Integer(required=True, description='Primary key (auto-incremented)'),
        'autoProcProgramId': f_fields.Integer(required=False, description='Related program item'),
        'spaceGroup': f_fields.String(required=False, description='Space group'),
        'refinedCell_a': f_fields.Float(required=False, description='Refined cell'),
        'refinedCell_b': f_fields.Float(required=False, description='Refined cell'),
        'refinedCell_c': f_fields.Float(required=False, description='Refined cell'),
        'refinedCell_alpha': f_fields.Float(required=False, description='Refined cell'),
        'refinedCell_beta': f_fields.Float(required=False, description='Refined cell'),
        'refinedCell_gamma': f_fields.Float(required=False, description='Refined cell'),
        'recordTimeStamp': f_fields.DateTime(required=False, description='Creation or last update date/time'),
        }

class AutoProcSchema(Schema):
    """Marshmallows schema class representing AutoProc table"""

    autoProcId = ma_fields.Integer()
    autoProcProgramId = ma_fields.Integer()
    spaceGroup = ma_fields.String()
    refinedCell_a = ma_fields.Float()
    refinedCell_b = ma_fields.Float()
    refinedCell_c = ma_fields.Float()
    refinedCell_alpha = ma_fields.Float()
    refinedCell_beta = ma_fields.Float()
    refinedCell_gamma = ma_fields.Float()
    recordTimeStamp = ma_fields.DateTime()

f_auto_proc_schema = api.model('AutoProc', auto_proc_dict)
ma_auto_proc_schema = AutoProcSchema()


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

session_dict = {
        'sessionId': f_fields.Integer(required=True, description=''),
        'expSessionPk': f_fields.Integer(required=False, description='smis session Pk '),
        'beamLineSetupId': f_fields.Integer(required=False, description=''),
        'proposalId': f_fields.Integer(required=True, description=''),
        'beamCalendarId': f_fields.Integer(required=False, description=''),
        'projectCode': f_fields.String(required=False, description=''),
        'startDate': f_fields.DateTime(required=False, description=''),
        'endDate': f_fields.DateTime(required=False, description=''),
        'beamLineName': f_fields.String(required=False, description=''),
        'scheduled': f_fields.Integer(required=False, description=''),
        'nbShifts': f_fields.Integer(required=False, description=''),
        'comments': f_fields.String(required=False, description=''),
        'beamLineOperator': f_fields.String(required=False, description=''),
        'visit_number': f_fields.Integer(required=False, description=''),
        'bltimeStamp': f_fields.DateTime(required=True, description=''),
        'usedFlag': f_fields.Integer(required=False, description='indicates if session has Datacollections or XFE or EnergyScans attached'),
        'sessionTitle': f_fields.String(required=False, description='fx accounts only'),
        'structureDeterminations': f_fields.Float(required=False, description=''),
        'dewarTransport': f_fields.Float(required=False, description=''),
        'databackupFrance': f_fields.Float(required=False, description='data backup and express delivery France'),
        'databackupEurope': f_fields.Float(required=False, description='data backup and express delivery Europe'),
        'operatorSiteNumber': f_fields.String(required=False, description='matricule site'),
        'lastUpdate': f_fields.DateTime(required=True, description='last update timestamp: by default the end of the session, the last collect...'),
        'protectedData': f_fields.String(required=False, description='indicates if the data are protected or not'),
        'externalId': f_fields.Integer(required=False, description=''),
        'nbReimbDewars': f_fields.Integer(required=False, description=''),
        }

class SessionSchema(Schema):
    """Marshmallows schema class representing Session table"""

    sessionId = ma_fields.Integer()
    expSessionPk = ma_fields.Integer()
    beamLineSetupId = ma_fields.Integer()
    proposalId = ma_fields.Integer()
    beamCalendarId = ma_fields.Integer()
    projectCode = ma_fields.String()
    startDate = ma_fields.DateTime()
    endDate = ma_fields.DateTime()
    beamLineName = ma_fields.String()
    scheduled = ma_fields.Integer()
    nbShifts = ma_fields.Integer()
    comments = ma_fields.String()
    beamLineOperator = ma_fields.String()
    visit_number = ma_fields.Integer()
    bltimeStamp = ma_fields.DateTime()
    usedFlag = ma_fields.Integer()
    sessionTitle = ma_fields.String()
    structureDeterminations = ma_fields.Float()
    dewarTransport = ma_fields.Float()
    databackupFrance = ma_fields.Float()
    databackupEurope = ma_fields.Float()
    operatorSiteNumber = ma_fields.String()
    lastUpdate = ma_fields.DateTime()
    protectedData = ma_fields.String()
    externalId = ma_fields.Integer()
    nbReimbDewars = ma_fields.Integer()

f_session_schema = api.model('Session', session_dict)
ma_session_schema = SessionSchema()


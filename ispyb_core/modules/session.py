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


from ispyb_core.models import BLSession as SessionModel
from ispyb_core.schemas.session import session_f_schema, session_ma_schema


def get_all_sessions():
    session_list = SessionModel.query.all()
    return session_ma_schema.dump(session_list, many=True)


def get_proposal_sessions(proposal_id):
    session_list = SessionModel.query.filter_by(proposalId=proposal_id)
    return session_ma_schema.dump(session_list, many=True)

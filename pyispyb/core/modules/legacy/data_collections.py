# Project: py-ispyb.

# https://github.com/ispyb/py-ispyb

# This file is part of py-ispyb software.

# py-ispyb is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# py-ispyb is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License
# along with py-ispyb. If not, see <http://www.gnu.org/licenses/>.


__license__ = "LGPLv3+"

from pyispyb.app.utils import get_sql_query, queryresult_to_dict
from pyispyb.app.extensions.database.middleware import db


def get_data_collections_groups(session_id):
    """Get data collection groups for session.

    Args:
        session_id (str): session id

    Returns:
        dict: Data collection groups
    """
    sql = get_sql_query(
        "dataCollection/groups",
        append=" where DataCollectionGroup_sessionId = :sessionId group by v_datacollection_summary.DataCollectionGroup_dataCollectionGroupId order by DataCollection_startTime desc",
    )
    sql = sql.bindparams(sessionId=session_id)
    group_list = db.sesion.execute(sql)
    return queryresult_to_dict(group_list)


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
from pyispyb.app.extensions import db


def get_crystal_snapshots(proposal_id, datacollection_id):
    """Get crystal snaphots for datacollection.

    Args:
        proposal_id (str): proposal id
        datacollection_id (str): data collection id

    Returns:
        str: images path
    """
    sql = get_sql_query(
        "mx/crystal_snapshot")
    sql = sql.bindparams(dataCollectionId=datacollection_id,
                         proposalId=proposal_id)
    res = db.engine.execute(sql)
    res = queryresult_to_dict(res)
    if len(res) > 0:
        return res[0]
    return None

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


from pyispyb.app.extensions import db
from pyispyb.core import models, schemas


__license__ = "LGPLv3+"


def get_energy_scans(request):
    """
    Returns list of energy scans.

    Returns:
        [type]: [description]
    """
    query_dict = request.args.to_dict()

    return db.get_db_items(
        models.EnergyScan,
        schemas.energy_scan.dict_schema,
        schemas.energy_scan.ma_schema,
        query_dict,
    )

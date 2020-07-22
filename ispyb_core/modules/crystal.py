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


from ispyb_core.models import Crystal as CrystalModel
from ispyb_core.schemas.crystal import crystal_f_schema, crystal_ma_schema


def get_crystal_list():
    crystal_list = CrystalModel.query.all()
    return crystal_ma_schema.dump(crystal_list, many=True)

def get_crystal_by_id(crystal_id):
    """Returns crystal by its crystalId

    Args:
        crystal_id (int): corresponds to crystalId in db

    Returns:
        dict: info about crystal as dict
    """
    crystal_item = CrystalModel.query.filter_by(crystalId=crystal_id).first()
    return crystal_ma_schema.dump(crystal_item)[0]

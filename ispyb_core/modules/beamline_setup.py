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


from app.extensions import get_db_items, get_db_item_by_id, add_db_item

from ispyb_core.models import BeamLineSetup as BeamLineSetupModel
from ispyb_core.schemas.beamline_setup import (
    beamline_setup_dict_schema,
    beamline_setup_f_schema,
    beamline_setup_ma_schema,
)


def get_beamline_setups(query_params):
    """Returns beamline_setup items based on query parameters

    Args:
        query_params (dict): [description]

    Returns:
        [type]: [description]
    """
    return get_db_items(
        BeamLineSetupModel,
        beamline_setup_dict_schema,
        beamline_setup_ma_schema,
        query_params,
    )

def add_beamline_setup(beamline_setup_dict):
    """Adds data collection item

    Args:
        beamline_setup_dict ([type]): [description]

    Returns:
        [type]: [description]
    """
    return add_db_item(BeamLineSetupModel, beamline_setup_dict)


def get_beamline_setup_by_id(beamline_setup_id):
    """Returns beamline_setup by its beamline_setupId

    Args:
        beamline_setup_id (int): corresponds to beamlineSetupId in db

    Returns:
        dict: info about beamline_setup as dict
    """
    return get_db_item_by_id(BeamLineSetupModel, beamline_setup_ma_schema, {"beamLineSetupId": beamline_setup_id})

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


from flask import current_app

from ispyb_core.models import BeamLineSetup as BeamLineSetupModel
from ispyb_core.schemas.beamline_setup import (
    beamline_setup_f_schema,
    beamline_setup_ma_schema,
)


def get_beamline_setups(offset, limit):
    """Returns beamline_setups defined by pagination offset and limit

    Args:
        offset (int): pagination offset
        limit (int): if not passed then limit is defined as
        PAGINATION_ITEMS_LIMIT in config.py

    Returns:
        list: list of beamline_setups
    """

    if not offset:
        offset = 1
    if not limit:
        limit = current_app.config["PAGINATION_ITEMS_LIMIT"]

    total = BeamLineSetupModel.query.count()
    query = BeamLineSetupModel.query.limit(limit).offset(offset)
    beamline_setups = beamline_setup_ma_schema.dump(query, many=True)[0]

    return {"total": total, "rows": beamline_setups}


def get_beamline_setup_by_id(beamline_setup_id):
    """Returns beamline_setup by its beamline_setupId

    Args:
        beamline_setup_id (int): corresponds to beamlineSetupId in db

    Returns:
        dict: info about beamline_setup as dict
    """
    beamline_setup = BeamLineSetupModel.query.filter_by(
        beamLineSetupId=beamline_setup_id
    ).first()
    beamline_setup_json = beamline_setup_ma_schema.dump(beamline_setup)[0]

    return beamline_setup_json

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


from pyispyb.app.extensions import db

from pyispyb.core import models, schemas


def get_beamline_setups(request):
    """
    Returns beamline_setup items based on query parameters.

    Args:
        query_params (dict): [description]

    Returns:
        [type]: [description]
    """
    query_params = request.args.to_dict()

    return db.get_db_items(
        models.BeamLineSetup,
        schemas.beamline_setup.dict_schema,
        schemas.beamline_setup.ma_schema,
        query_params,
    )


def add_beamline_setup(data_dict):
    """
    Adds data collection item.

    Args:
        beamline_setup_dict ([type]): [description]

    Returns:
        [type]: [description]
    """
    return db.add_db_item(
        models.BeamLineSetup, schemas.beamline_setup.ma_schema, data_dict
    )


def get_beamline_setup_by_id(beamline_setup_id):
    """
    Returns beamline_setup by its beamline_setupId.

    Args:
        beamline_setup_id (int): corresponds to beamlineSetupId in db

    Returns:
        dict: info about beamline_setup as dict
    """
    data_dict = {"beamLineSetupId": beamline_setup_id}
    return db.get_db_item_by_params(
        models.BeamLineSetup, schemas.beamline_setup.ma_schema, data_dict
    )


def update_beamline_setup(beamline_setup_id, data_dict):
    """
    Updates beamline_setup.

    Args:
        beamline_setup_id ([type]): [description]
        beamline_setup_dict ([type]): [description]

    Returns:
        [type]: [description]
    """
    id_dict = {"beamLineSetupId": beamline_setup_id}
    return db.update_db_item(
        models.BeamLineSetup, schemas.beamline_setup.ma_schema, id_dict, data_dict
    )


def patch_beamline_setup(beamline_setup_id, data_dict):
    """
    Patch a beamline_setup

    Args:
        beamline_setup_id ([type]): [description]
        data_dict ([type]): [description]

    Returns:
        [type]: [description]
    """
    id_dict = {"beamLineSetupId": beamline_setup_id}
    return db.patch_db_item(
        models.BeamLineSetup, schemas.beamline_setup.ma_schema, id_dict, data_dict
    )


def delete_beamline_setup(beamline_setup_id):
    """Deletes beamline_setup item from db.

    Args:
        beamline_setup_id (int): beamline_setupId column in db

    Returns:
        bool: True if the beamline_setup exists and deleted successfully,
        otherwise return False
    """
    id_dict = {"beamLineSetupId": beamline_setup_id}
    return db.delete_db_item(models.BeamLineSetup, id_dict)

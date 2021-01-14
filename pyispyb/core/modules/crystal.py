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


def get_crystals(request):
    """
    Returns crystal entries.

    Returns:
        [type]: [description]
    """
    query_params = request.args.to_dict()
    
    return db.get_db_items(
        models.Crystal,
        schemas.crystal.dict_schema,
        schemas.crystal.ma_schema,
        query_params,
    )


def get_crystal_by_id(crystal_id):
    """
    Returns crystal by its crystalId.

    Args:
        crystal_id (int): corresponds to crystalId in db

    Returns:
        dict: info about crystal as dict
    """
    data_dict = {"crystalId": crystal_id}
    return db.get_db_item_by_params(
        models.Crystal, schemas.crystal.ma_schema, data_dict
    )


def add_crystal(data_dict):
    """
    Adds a crystal to db.

    Args:
        data_dict ([type]): [description]

    Returns:
        [type]: [description]
    """
    return db.add_db_item(models.Crystal, schemas.crystal.ma_schema, data_dict)


def update_crystal(crystal_id, data_dict):
    """
    Updates crystal.

    Args:
        crystal_id ([type]): [description]
        crystal_dict ([type]): [description]

    Returns:
        [type]: [description]
    """
    id_dict = {"crystalId": crystal_id}
    return db.update_db_item(
        models.Crystal, schemas.crystal.ma_schema, id_dict, data_dict
    )


def patch_crystal(crystal_id, data_dict):
    """
    Patch a crystal.

    Args:
        crystal_id ([type]): [description]
        data_dict ([type]): [description]

    Returns:
        [type]: [description]
    """
    id_dict = {"crystalId": crystal_id}
    return db.patch_db_item(
        models.Crystal, schemas.crystal.ma_schema, id_dict, data_dict
    )


def delete_crystal(crystal_id):
    """
    Deletes crystal item from db.

    Args:
        crystal_id (int): crystalId column in db

    Returns:
        bool: True if the crystal exists and deleted successfully,
        otherwise return False
    """
    id_dict = {"crystalId": crystal_id}
    return db.delete_db_item(models.Crystal, id_dict)

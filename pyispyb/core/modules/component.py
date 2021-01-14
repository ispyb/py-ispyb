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


def get_component_types(request):
    """
    Returns component_type entries.

    Returns:
        [type]: [description]
    """
    query_params = request.args.to_dict()

    return db.get_db_items(
        models.ComponentType,
        schemas.component_type.dict_schema,
        schemas.component_type.ma_schema,
        query_params,
    )


def get_component_type_by_id(component_type_id):
    """
    Returns component_type by its component_typeId.

    Args:
        component_type_id (int): corresponds to component_typeId in db

    Returns:
        dict: info about component_type as dict
    """
    data_dict = {"componentTypeId": component_type_id}
    return db.get_db_item_by_params(
        models.ComponentType, schemas.component_type.ma_schema, data_dict
    )


def add_component_type(data_dict):
    """
    Adds a component_type to db.

    Args:
        data_dict ([type]): [description]

    Returns:
        [type]: [description]
    """
    return db.add_db_item(
        models.ComponentType, schemas.component_type.ma_schema, data_dict
    )


def update_component_type(component_type_id, data_dict):
    """
    Updates component_type.

    Args:
        component_type_id ([type]): [description]
        data_dict ([type]): [description]

    Returns:
        [type]: [description]
    """
    id_dict = {"componentTypeId": component_type_id}
    return db.update_db_item(
        models.ComponentType, schemas.component_type.ma_schema, id_dict, data_dict
    )


def patch_component_type(component_type_id, data_dict):
    """
    Patch a component_type.

    Args:
        component_type_id ([type]): [description]
        data_dict ([type]): [description]

    Returns:
        [type]: [description]
    """
    id_dict = {"componentTypeId": component_type_id}
    return db.patch_db_item(
        models.ComponentType, schemas.component_type.ma_schema, id_dict, data_dict
    )


def delete_component_type(component_type_id):
    """
    Deletes component_type item from db.

    Args:
        component_type_id (int): componentTypeId column in db

    Returns:
        bool: True if the component_type exists and deleted successfully,
        otherwise return False
    """
    id_dict = {"componentTypeId": component_type_id}
    return db.delete_db_item(models.ComponentType, id_dict)

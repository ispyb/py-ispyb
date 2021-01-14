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


def get_containers(request):
    """
    Returns all containers.

    Returns:
        dict: list with dewars]
    """

    query_params = request.args.to_dict()

    return db.get_db_items(
        models.Container,
        schemas.dewar.dict_schema,
        schemas.dewar.ma_schema,
        query_params,
    )


def get_container_by_id(container_id):
    """
    Returns container by its container_id.

    Args:
        container_id (int): corresponds to containerId in db

    Returns:
        dict: info about container as dict
    """
    id_dict = {"containerId": container_id}
    return db.get_db_item_by_params(
        models.Container, schemas.container.ma_schema, id_dict
    )


def add_container(data_dict):
    """
    Adds a container to db.

    Args:
        data_dict ([type]): [description]

    Returns:
        [type]: [description]
    """
    return db.add_db_item(models.Container, schemas.container.ma_schema, data_dict)


def update_container(container_id, data_dict):
    """
    Updates container.

    Args:
        container_id ([type]): [description]
        container_dict ([type]): [description]

    Returns:
        [type]: [description]
    """
    id_dict = {"containerId": container_id}
    return db.update_db_item(
        models.Container, schemas.container.ma_schema, id_dict, data_dict
    )


def patch_container(container_id, data_dict):
    """
    Patch a container.

    Args:
        container_id ([type]): [description]
        data_dict ([type]): [description]

    Returns:
        [type]: [description]
    """
    id_dict = {"containerId": container_id}
    return db.patch_db_item(
        models.Container, schemas.container.ma_schema, id_dict, data_dict
    )


def delete_container(container_id):
    """
    Deletes container item from db.

    Args:
        container_id (int): containerId column in db

    Returns:
        bool: True if the container exists and deleted successfully,
        otherwise return False
    """
    id_dict = {"containerId": container_id}
    return db.delete_db_item(models.Container, id_dict)

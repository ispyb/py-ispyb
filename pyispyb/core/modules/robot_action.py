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


def get_robot_actions(request):
    """
    Returns robot_action items based on query parameters.

    Args:
        query_params (dict): [description]

    Returns:
        [type]: [description]
    """
    query_params = request.args.to_dict()

    return db.get_db_items(
        models.RobotAction,
        schemas.robot_action.dict_schema,
        schemas.robot_action.ma_schema,
        query_params,
    )


def add_robot_action(data_dict):
    """
    Adds data collection item.

    Args:
        robot_action_dict ([type]): [description]

    Returns:
        [type]: [description]
    """
    return db.add_db_item(models.RobotAction, schemas.robot_action.ma_schema, data_dict)


def get_robot_action_by_id(robot_action_id):
    """
    Returns robot_action by its robot_actionId.

    Args:
        robot_action_id (int): corresponds to beamlineSetupId in db

    Returns:
        dict: info about robot_action as dict
    """
    data_dict = {"robotActionId": robot_action_id}
    return db.get_db_item_by_params(
        models.RobotAction, schemas.robot_action.ma_schema, data_dict
    )


def update_robot_action(robot_action_id, data_dict):
    """
    Updates robot_action.

    Args:
        robot_action_id ([type]): [description]
        robot_action_dict ([type]): [description]

    Returns:
        [type]: [description]
    """
    id_dict = {"robotActionId": robot_action_id}
    return db.update_db_item(
        models.RobotAction, schemas.robot_action.ma_schema, id_dict, data_dict
    )


def patch_robot_action(robot_action_id, data_dict):
    """
    Patch a robot_action.

    Args:
        robot_action_id ([type]): [description]
        data_dict ([type]): [description]

    Returns:
        [type]: [description]
    """
    id_dict = {"robotActionId": robot_action_id}
    return db.patch_db_item(
        models.RobotAction, schemas.robot_action.ma_schema, id_dict, data_dict
    )


def delete_robot_action(robot_action_id):
    """
    Deletes robot_action item from db.

    Args:
        robot_action_id (int): robot_actionId column in db

    Returns:
        bool: True if the robot_action exists and deleted successfully,
        otherwise return False
    """
    id_dict = {"robotActionId": robot_action_id}
    return db.delete_db_item(models.RobotAction, id_dict)

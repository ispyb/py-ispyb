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
from pyispyb.app.extensions.auth import auth_provider
from pyispyb.app.utils import create_response_item

from pyispyb.em import models, schemas


def get_motion_corrections(request):
    """
    Returns motion_correction based on query parameters.

    Args:
        query_dict ([type]): [description]

    Returns:
        [type]: [description]
    """
    query_dict = request.args.to_dict()

    #is_admin, proposal_id_list = proposal.get_proposal_ids_by_username(request)

    run_query = True
    #if is_admin:
    #    run_query = True
    msg = "Unable to run query"

    if run_query:
        return db.get_db_items(
            models.MotionCorrection,
            schemas.motion_correction.dict_schema,
            schemas.motion_correction.ma_schema,
            query_dict,
        )
    else:
        return create_response_item(msg=msg)


def add_motion_correction(data_dict):
    """
    Adds new motion_correction.

    Args:
        motion_correction_dict ([type]): [description]

    Returns:
        [type]: [description]
    """
    return db.add_db_item(models.MotionCorrection, schemas.motion_correction.ma_schema, data_dict)


def get_motion_correction_by_id(motion_correction_id):
    """
    Returns motion_correction info by its motion_correctionId.

    Args:
        motion_correction_id (int): corresponds to motion_correctionId in db

    Returns:
        dict: info about motion_correction as dict
    """
    data_dict = {"motionCorrectionId": motion_correction_id}
    return db.get_db_item(
        models.MotionCorrection, schemas.motion_correction.ma_schema, data_dict
    )


def get_motion_correction_info_by_id(motion_correction_id):
    """
    Returns motion_correction info by its motion_correctionId.

    Args:
        motion_correction_id (int): corresponds to motion_correctionId in db

    Returns:
        dict: info about motion_correction as dict
    """
    motion_correction_json = get_motion_correction_by_id(motion_correction_id)
    return motion_correction_json


def update_motion_correction(motion_correction_id, data_dict):
    """
    Updates motion_correction.

    Args:
        motion_correction_id ([type]): [description]
        motion_correction_dict ([type]): [description]

    Returns:
        [type]: [description]
    """
    id_dict = {"motionCorrectionId": motion_correction_id}
    return db.update_db_item(
        models.MotionCorrection, schemas.motion_correction.ma_schema, id_dict, data_dict
    )


def patch_motion_correction(motion_correction_id, data_dict):
    """
    Patch a motion_correction.

    Args:
        motion_correction_id ([type]): [description]
        data_dict ([type]): [description]

    Returns:
        [type]: [description]
    """
    id_dict = {"motionCorrectionId": motion_correction_id}
    return db.patch_db_item(
        models.MotionCorrection, schemas.motion_correction.ma_schema, id_dict, data_dict
    )


def delete_motion_correction(motion_correction_id):
    """
    Deletes motion_correction item from db.

    Args:
        motion_correction_id (int): motion_correctionId column in db

    Returns:
        bool: True if the motion_correction exists and deleted successfully,
        otherwise return False
    """
    id_dict = {"motionCorrectionId": motion_correction_id}
    return db.delete_db_item(models.MotionCorrection, id_dict)
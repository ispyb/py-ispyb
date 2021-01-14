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


def get_detectors(request):
    """
    Returns detector items based on query parameters.

    Args:
        query_params (dict): [description]

    Returns:
        [type]: [description]
    """
    query_params = request.args.to_dict()

    return db.get_db_items(
        models.Detector,
        schemas.detector.dict_schema,
        schemas.detector.ma_schema,
        query_params,
    )


def add_detector(data_dict):
    """
    Adds data collection item.

    Args:
        detector_dict ([type]): [description]

    Returns:
        [type]: [description]
    """
    return db.add_db_item(models.Detector, schemas.detector.ma_schema, data_dict)


def get_detector_by_id(detector_id):
    """
    Returns detector by its detectorId.

    Args:
        detector_id (int): corresponds to detectorId in db

    Returns:
        dict: info about detector as dict
    """
    data_dict = {"detectorId": detector_id}
    return db.get_db_item_by_params(
        models.Detector, schemas.detector.ma_schema, data_dict
    )


def update_detector(detector_id, data_dict):
    """
    Updates detector.

    Args:
        detector_id ([type]): [description]
        detector_dict ([type]): [description]

    Returns:
        [type]: [description]
    """
    id_dict = {"detectorId": detector_id}
    return db.update_db_item(
        models.Detector, schemas.detector.ma_schema, id_dict, data_dict
    )


def patch_detector(detector_id, data_dict):
    """
    Patch a detector.

    Args:
        detector_id ([type]): [description]
        data_dict ([type]): [description]

    Returns:
        [type]: [description]
    """
    id_dict = {"detectorId": detector_id}
    return db.patch_db_item(
        models.Detector, schemas.detector.ma_schema, id_dict, data_dict
    )


def delete_detector(detector_id):
    """
    Deletes detector item from db.

    Args:
        detector_id (int): detectorId column in db

    Returns:
        bool: True if the detector exists and deleted successfully,
        otherwise return False
    """
    id_dict = {"detectorId": detector_id}
    return db.delete_db_item(models.Detector, id_dict)

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


def get_samples(request):
    """
    Returns sample entries.

    Returns:
        [type]: [description]
    """
    query_params = request.args.to_dict()

    return db.get_db_items(
        models.BLSample,
        schemas.sample.dict_schema,
        schemas.sample.ma_schema,
        query_params,
    )


def get_sample_by_id(sample_id):
    """
    Returns sample by its sampleId.

    Args:
        sample (int): corresponds to sampleId in db

    Returns:
        dict: info about sample as dict
    """
    data_dict = {"blSampleId": sample_id}
    return db.get_db_item_by_params(
        models.BLSample, schemas.sample.ma_schema, data_dict
    )


def add_sample(data_dict):
    """
    Adds a sample to db.

    Args:
        data_dict ([type]): [description]

    Returns:
        [type]: [description]
    """
    return db.add_db_item(models.BLSample, schemas.sample.ma_schema, data_dict)


def update_sample(sample_id, data_dict):
    """
    Updates sample.

    Args:
        sample_id ([type]): [description]
        sample_dict ([type]): [description]

    Returns:
        [type]: [description]
    """
    id_dict = {"blSampleId": sample_id}
    return db.update_db_item(
        models.BLSample, schemas.sample.ma_schema, id_dict, data_dict
    )


def patch_sample(sample_id, data_dict):
    """
    Patch a sample.

    Args:
        sample_id ([type]): [description]
        data_dict ([type]): [description]

    Returns:
        [type]: [description]
    """
    id_dict = {"blSampleId": sample_id}
    return db.patch_db_item(
        models.BLSample, schemas.sample.ma_schema, id_dict, data_dict
    )


def delete_sample(sample_id):
    """
    Deletes sample item from db.

    Args:
        sample_id (int): blSampleId column in db

    Returns:
        bool: True if the sample exists and deleted successfully,
        otherwise return False
    """
    id_dict = {"blSampleId": sample_id}
    return db.delete_db_item(models.BLSample, id_dict)

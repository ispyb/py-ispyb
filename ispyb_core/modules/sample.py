"""
Project: py-ispyb
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

from app.extensions import db
from ispyb_core import models, schemas


def get_samples():
    sample_list = models.BLSample.query.all()
    return schemas.sample.ma_schema.dump(sample_list, many=True)


def get_sample_by_id(sample_id):
    """Returns sample by its sampleId

    Args:
        sample_id (int): corresponds to sampleId in db

    Returns:
        dict: info about sample as dict
    """
    sample_item = models.BLSample.query.filter_by(blSampleId=sample_id).first()
    return schemas.sample.ma_schema.dump(sample_item)[0]


def add_sample(data_dict):
    """
    Adds a sample to db

    Args:
        data_dict ([type]): [description]

    Returns:
        [type]: [description]
    """
    return db.add_db_item(
        models.BLSample,
        schemas.sample.ma_schema,
        data_dict
        )

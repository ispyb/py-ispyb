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


def get_dewars(request):
    """Returns all dewars.

    Returns:
        dict: list with dewars]
    """

    query_params = request.args.to_dict()

    return db.get_db_items(
        models.Dewar,
        schemas.dewar.dict_schema,
        schemas.dewar.ma_schema,
        query_params,
    )


def get_dewar_by_id(dewar_id):
    """Returns dewar by its dewar_id

    Args:
        dewar_id (int): corresponds to dewarId in db

    Returns:
        dict: info about dewar as dict
    """
    id_dict = {"dewarId": dewar_id}
    return db.get_db_item_by_params(
        models.Dewar,
        schemas.dewar.ma_schema,
        id_dict
    )


def add_dewar(data_dict):
    """
    Adds a dewar to db

    Args:
        data_dict ([type]): [description]

    Returns:
        [type]: [description]
    """
    return db.add_db_item(models.Dewar, schemas.dewar.ma_schema, data_dict)

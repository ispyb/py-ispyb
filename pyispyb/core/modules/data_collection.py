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


def get_data_collections(request):
    """
    Returns data collection items based on query parameters.

    Args:
        query_params ([type]): [description]

    Returns:
        [type]: [description]
    """
    query_params = request.args.to_dict()

    return db.get_db_items(
        models.DataCollection,
        schemas.data_collection.dict_schema,
        schemas.data_collection.ma_schema,
        query_params,
    )


def add_data_collection(data_dict):
    """
    Adds data collection item.

    Args:
        data_collection_dict ([type]): [description]

    Returns:
        [type]: [description]
    """
    return db.add_db_item(
        models.DataCollection, schemas.data_collection.ma_schema, data_dict
    )


def get_data_collection_by_id(data_collection_id):
    """
    Returns data_collection by its id.

    Args:
        data_collection_id (int): corresponds to dataCollectionId in db

    Returns:
        dict: info about data_collection as dict
    """
    data_dict = {"dataCollectionId": data_collection_id}
    return db.get_db_item_by_params(
        models.DataCollection, schemas.data_collection.ma_schema, data_dict
    )


def get_data_collection_groups(request):
    """
    Returns data collection group items based on query parameters.

    Args:
        query_params ([type]): [description]

    Returns:
        [type]: [description]
    """

    query_params = request.args.to_dict()

    return db.get_db_items(
        models.DataCollectionGroup,
        schemas.data_collection_group.dict_schema,
        schemas.data_collection_group.ma_schema,
        query_params,
    )


def add_data_collection_group(data_dict):
    """
    Adds data collection item.

    Args:
        data_collection_dict ([type]): [description]

    Returns:
        [type]: [description]
    """
    return db.add_db_item(
        models.DataCollectionGroup, schemas.data_collection_group.ma_schema, data_dict
    )


def get_data_collection_group_by_id(data_collection_group_id):
    """
    Returns data collection group by its id.

    Args:
        data_collection_group_id (int): corresponds to dataCollectionGroupId

    Returns:
        dict: info about data collection group as dict
    """
    data_dict = {"dataCollectionGroupId": data_collection_group_id}

    return db.get_db_item_by_params(
        models.DataCollectionGroup, schemas.data_collection_group.ma_schema, data_dict
    )

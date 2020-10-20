# encoding: utf-8
#
#  Project: py-ispyb
#  https://github.com/ispyb/py-ispyb
#
#  This file is part of py-ispyb software.
#
#  py-ispyb is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  py-ispyb is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with py-ispyb. If not, see <http://www.gnu.org/licenses/>.


__license__ = "LGPLv3+"


import logging

from flask_restx._http import HTTPStatus


import ispyb_service_connector
from app.extensions import db, auth_provider

from ispyb_ssx import models, schemas


log = logging.getLogger(__name__)


def get_loaded_samples(request):
    """Returns loaded_samples by query parameters"""
    
    query_params = request.args.to_dict()
    
    return db.get_db_items(
        models.LoadedSample,
        schemas.loaded_sample_dict_schema,
        schemas.loaded_sample_ma_schema,
        query_params
    ), HTTPStatus.OK
    
def get_loaded_sample_by_id(loaded_sample_id):
    """Returns loaded_sample by its loaded_sampleId.

    Args:
        loaded_sample_id (int): corresponds to loaded_sampleId in db

    Returns:
        dict: info about loaded_sample as dict
    """
    id_dict = {"loaded_sampleId": loaded_sample_id}
    return db.get_db_item_by_params(
        models.LoadedSample,
        schemas.loaded_sample_ma_schema,
        id_dict
        )


def add_loaded_sample(data_dict):
    """Adds a new ssx loaded sample.

    Args:
        loaded_sample_dict ([type]): [description]

    Returns:
        [type]: [description]
    """
    return db.add_db_item(
        models.LoadedSample,
        loaded_sample_ma_schema,
        data_dict
        )

def get_all_crystal_slurry():
    """Returns all crystal slurry db items.

    Returns:
        [type]: [description]
    """
    crystal_slurry_list = models.CrystalSlurry.query.all()
    return crystal_slurry_ma_schema.dump(crystal_slurry_list, many=True)

def add_crystal_slurry(api):
    """Adds a new crystal slurry item.

    Args:
        crystal_slurry_dict ([type]): [description]

    Returns:
        [type]: [description]
    """

    data_dict = api.payload

    status_code, result = ispyb_service_connector.get_ispyb_resource("ispyb_core", "/samples/crystals/%d" % data_dict["crystalId"])
    if status_code == 200:
        crystal_id = data_dict.get("crystalId")
        if crystal_id is None:
            api.abort(HTTPStatus.NOT_ACCEPTABLE, "No crystalId in crystalSlurry dict")
        else:
            data_dict.pop("crystalId")
            return db.add_db_item(
                models.CrystalSlurry,
                crystal_slurry_ma_schema,
                data_dict
                )

def get_crystal_size_distributions():
        """Returns all crystal size distribution db items.

    Returns:
        [type]: [description]
    """
    crystal_slurry_list = models.CrystalSlurry.query.all()
    return crystal_slurry_ma_schema.dump(crystal_slurry_list, many=True)

    
def get_sample_delivery_devices(request):
    """Returns all sample delivery devices.

    Args:
        query_params ([type]): [description]

    Returns:
        [type]: [description]
    """
    query_params = request.args.to_dict()

    return db.get_db_items(
        models.SampleDeliveryDevice,
        sample_delivery_device_f_schema,
        sample_delivery_device_ma_schema,
        query_params
    ), HTTPStatus.OK

def add_sample_delivery_device(data_dict):
    """Adds a new sample delivery device.

    Args:
        sample_delivery_device ([type]): [description]

    Returns:
        [type]: [description]
    """
    return db.add_db_item(
        models.SampleDeliveryDevice,
        sample_delivery_device_ma_schema,
        data_dict)

def get_sample_stocks():
    """Returns all sample stock db items.

    Returns:
        [type]: [description]
    """
    sample_stock_list = models.SampleStock.query.all()
    return sample_delivery_device_ma_schema.dump(sample_stock_list, many=True)

def add_sample_stock(data_dict):
    """Adds a new crystal slurry item.

    Args:
        data_dict ([type]): [description]

    Returns:
        [type]: [description]
        
    """
    return db.add_db_item(
        models.SampleStock,
        schemas.sample_delivery_device.ma_schema,
        data_dict)
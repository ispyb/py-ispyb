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


import logging

from flask_restx import abort
from flask_restx._http import HTTPStatus

from pyispyb.app.extensions import db
from pyispyb.ssx import models, schemas
from pyispyb import connector as ispyb_service_connector

log = logging.getLogger(__name__)


__license__ = "LGPLv3+"


def get_loaded_samples(request):
    """Returns loaded_samples by query parameters"""

    query_dict = request.args.to_dict()

    return (
        db.get_db_items(
            models.LoadedSample,
            schemas.loaded_sample.dict_schema,
            schemas.loaded_sample.ma_schema,
            query_dict,
        ),
        HTTPStatus.OK,
    )


def get_loaded_sample_by_id(loaded_sample_id):
    """Returns loaded_sample by its loaded_sampleId.

    Args:
        loaded_sample_id (int): corresponds to loaded_sampleId in db

    Returns:
        dict: info about loaded_sample as dict
    """
    id_dict = {"loadedSampleId": loaded_sample_id}

    return db.get_db_item(
        models.LoadedSample, schemas.loaded_sample.ma_schema, id_dict
    )


def add_loaded_sample(data_dict):
    """Adds a new ssx loaded sample.

    Args:
        data_dict ([type]): [description]

    Returns:
        int, dict: HTTP status code and response dict
    """
    return db.add_db_item(
        models.LoadedSample, schemas.loaded_sample.ma_schema, data_dict
    )


def get_loaded_sample_info_by_id(loaded_sample_id):
    """
    Returns loaded_sample by its loaded_sampleId.

    Args:
        loaded_sample_id (int): corresponds to loaded_sampleId in db

    Returns:
        dict: info about loaded_sample as dict
    """
    loaded_sample_json = get_loaded_sample_by_id(loaded_sample_id)

    sample_stock_json = get_sample_stock_info_by_id(loaded_sample_json["sampleStockId"])
    loaded_sample_json["sample_stock"] = sample_stock_json

    sample_delivery_device = get_sample_delivery_device_by_id(
        loaded_sample_json["sampleDeliveryDeviceId"]
    )
    loaded_sample_json["sample_delivery_device"] = sample_delivery_device

    return loaded_sample_json


def get_all_crystal_slurry():
    """Returns all crystal slurry db items.

    Returns:
        [type]: [description]
    """
    crystal_slurry_list = models.CrystalSlurry.query.all()
    return schemas.crystal_slurry.ma_schema.dump(crystal_slurry_list, many=True)


def get_crystal_slurry_by_id(crystal_slurry_id):
    id_dict = {"crystalSlurryId": crystal_slurry_id}
    return db.get_db_item(
        models.CrystalSlurry, schemas.crystal_slurry.ma_schema, id_dict
    )


def add_crystal_slurry(data_dict):
    """Adds a new crystal slurry item.

    Args:
        crystal_slurry_dict ([type]): [description]

    Returns:
        [type]: [description]
    """
    status_code, result = ispyb_service_connector.get_ispyb_resource(
        "core", "/samples/crystals/%d" % data_dict["crystalId"]
    )
    if status_code == 200:
        crystal_id = data_dict.get("crystalId")
        if crystal_id is None:
            abort(HTTPStatus.NO_CONTENT, "No crystalId in crystalSlurry dict")
        else:
            data_dict.pop("crystalId")
            return db.add_db_item(
                models.CrystalSlurry, schemas.crystal_slurry.ma_schema, data_dict
            )
    else:
        result = (
            "Unable to add new crystal slurry Crystal with id %s do not exist"
            % data_dict["crystalId"]
        )
        abort(status_code, result)


def get_crystal_size_distributions():
    """Returns all crystal size distribution db items.

    Returns:
        [type]: [description]
    """
    crystal_size_distribution_list = models.CrystalSizeDistribution.query.all()
    return schemas.crystal_size_distribution.ma_schema.dump(
        crystal_size_distribution_list, many=True
    )


def add_crystal_size_distribution(data_dict):
    """Adds a new crystal size distribution.

    Args:
        data_dict ([type]): [description]

    Returns:
        int, dict: HTTP status code and response dict
    """
    return db.add_db_item(
        models.CrystalSizeDistribution,
        schemas.crystal_size_distribution.ma_schema,
        data_dict,
    )


def get_sample_delivery_devices(request):
    """Returns all sample delivery devices.

    Args:
        query_dict ([type]): [description]

    Returns:
        [type]: [description]
    """
    query_dict = request.args.to_dict()

    return (
        db.get_db_items(
            models.SampleDeliveryDevice,
            schemas.sample_delivery_device.f_schema,
            schemas.sample_delivery_device.ma_schema,
            query_dict,
        ),
        HTTPStatus.OK,
    )


def add_sample_delivery_device(data_dict):
    """Adds a new sample delivery device.

    Args:
        sample_delivery_device ([type]): [description]

    Returns:
        [type]: [description]
    """
    return db.add_db_item(
        models.SampleDeliveryDevice, schemas.sample_delivery_device.ma_schema, data_dict
    )


def get_sample_delivery_device_by_id(sample_delivery_device_id):
    id_dict = {"sampleDeliveryDeviceId": sample_delivery_device_id}
    return db.get_db_item(
        models.SampleDeliveryDevice, schemas.sample_delivery_device.ma_schema, id_dict
    )


def get_sample_stocks():
    """Returns all sample stock db items.

    Returns:
        [type]: [description]
    """
    sample_stock_list = models.SampleStock.query.all()
    return schemas.sample_stock.ma_schema.dump(sample_stock_list, many=True)


def add_sample_stock(data_dict):
    """Adds a new crystal slurry item.

    Args:
        data_dict ([type]): [description]

    Returns:
        [type]: [description]

    """
    return db.add_db_item(models.SampleStock, schemas.sample_stock.ma_schema, data_dict)


def get_sample_stock_by_id(sample_stock_id):
    id_dict = {"sampleStockId": sample_stock_id}
    return db.get_db_item(
        models.SampleStock, schemas.sample_stock.ma_schema, id_dict
    )


def get_sample_stock_info_by_id(sample_stock_id):
    sample_stock_json = get_sample_stock_by_id(sample_stock_id)

    crystal_slurry_json = get_crystal_slurry_by_id(sample_stock_json["crystalSlurryId"])

    sample_stock_json["crystal_slurry"] = crystal_slurry_json

    return sample_stock_json

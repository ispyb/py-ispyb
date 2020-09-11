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
from app.extensions import db, auth_provider, create_response

#from ispyb_core
from ispyb_ssx.models import LoadedSample as LoadedSampleModel
from ispyb_ssx.models import CrystalSlurry as CrystalSlurryModel
from ispyb_ssx.schemas.loaded_sample import (
    loaded_sample_dict_schema,
    loaded_sample_f_schema,
    loaded_sample_ma_schema,
)
from ispyb_ssx.schemas.crystal_slurry import (
    crystal_slurry_f_schema,
    crystal_slurry_ma_schema,
)


log = logging.getLogger(__name__)


def get_loaded_samples(request):
    """Returns loaded_samples by query parameters"""
    
    query_params = request.args.to_dict()
    user_info = auth_provider.get_user_info_by_auth_header(request.headers.get("Authorization"))
    run_query = True

    """
    if not user_info["is_admin"]:
        #If the user is not admin or manager then loaded_samples associated to the user login name are returned
        person_id = contacts.get_person_id_by_login(user_info["username"])
        run_query = person_id is not None
    else:
        print(query_params.get("login_name"))
        person_id = contacts.get_person_id_by_login(query_params.get("login_name"))

    if person_id:    
        query_params["personId"] = person_id
    """
    print(ispyb_service_connector.get_ispyb_resource("ispyb_core", "/schemas/available_names"))
    if run_query:
        return db.get_db_items(
            LoadedSampleModel, loaded_sample_dict_schema, loaded_sample_ma_schema, query_params
        ), HTTPStatus.OK
    else:
        msg = "No loaded_samples associated to the username %s" % user_info["username"]
        return create_response(info_msg=msg), HTTPStatus.OK
    
def get_loaded_sample_by_id(loaded_sample_id):
    """Returns loaded_sample by its loaded_sampleId

    Args:
        loaded_sample_id (int): corresponds to loaded_sampleId in db

    Returns:
        dict: info about loaded_sample as dict
    """
    id_dict = {"loaded_sampleId": loaded_sample_id}
    return db.get_db_item_by_params(loaded_sampleModel, loaded_sample_ma_schema, id_dict)


def add_loaded_sample(loaded_sample_dict):
    return db.add_db_item(loaded_sampleModel, loaded_sample_ma_schema, loaded_sample_dict)

def get_all_crystal_slurry():
    crystal_slurry_list = CrystalSlurryModel.query.all()
    return crystal_slurry_ma_schema.dump(crystal_slurry_list, many=True)

def add_crystal_slurry(crystal_slurry_dict):
    status_code, result = ispyb_service_connector.get_ispyb_resource("ispyb_core", "/sample/crystal/%d" % crystal_slurry_dict["crystalId"])
    if status_code == 200:
        crystal_id = crystal_slurry_dict.get("crystalId")
        if crystal_id is None:
            status_code = 404
            result = "No crystalId in crystalSlurry dict"
        else:
            try:
                crystal_slurry_item = CrystalSlurryModel(**crystal_slurry_dict)
                db.session.add(crystal_slurry_item)
                db.session.commit()
                status_code = 200
                result = crystal_slurry_item.crystalSlurryId
            except BaseException as ex:
                print(ex)
                db.session.rollback()
                status_code = 400
                result = "Unable to store item in db (%s)" % str(ex)
    
    return status_code, result["message"]
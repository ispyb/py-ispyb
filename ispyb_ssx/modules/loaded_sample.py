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

from ispyb_service_connector import get_ispyb_resource
from app.extensions import db


from ispyb_ssx.models import LoadedSample as LoadedSampleModel
from ispyb_ssx.models import CrystalSlurry as CrystalSlurryModel
from ispyb_ssx.schemas.loaded_sample import (
    loaded_sample_f_schema,
    loaded_sample_ma_schema,
)
from ispyb_ssx.schemas.crystal_slurry import (
    crystal_slurry_f_schema,
    crystal_slurry_ma_schema,
)


log = logging.getLogger(__name__)


def get_all_loaded_samples():
    loaded_samples = LoadedSampleModel.query.all()
    return loaded_sample_ma_schema.dump(loaded_samples, many=True)

def add_loaded_sample(loaded_sample_dict):
    print(loaded_sample_dict)
    return

def get_all_crystal_slurry():
    crystal_slurry_list = CrystalSlurryModel.query.all()
    return crystal_slurry_ma_schema.dump(crystal_slurry_list, many=True)

def add_crystal_slurry(crystal_slurry_dict):
    print(crystal_slurry_dict)
    crystal_id = crystal_slurry_dict.get("crystalId")
    print(crystal_id)
    if crystal_id is None:
        return 404, "No crystalId in crystalSlurry dict"
    else:
        status_code, result = get_ispyb_resource("ispyb_core", "/sample/crystal/%d" % crystal_id)
        if status_code == 200:
            try:
                crystal_slurry_item = CrystalSlurryModel(**crystal_slurry_dict)
                db.session.add(crystal_slurry_item)
                db.session.commit()
                return crystal_slurry_item.crystalSlurryId
            except BaseException as ex:
                print(ex)
                db.session.rollback()
                return 400, "Unable to store item in db (%s)" % str(ex)
        else:
            return status_code, result
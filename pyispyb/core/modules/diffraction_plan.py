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


def get_diffraction_plans(request):
    """
    Returns diffraction_plan entries.

    Returns:
        [type]: [description]
    """
    query_params = request.args.to_dict()

    return db.get_db_items(
        models.DiffractionPlan,
        schemas.diffraction_plan.dict_schema,
        schemas.diffraction_plan.ma_schema,
        query_params,
    )


def get_diffraction_plan_by_id(diffraction_plan_id):
    """
    Returns diffraction_plan by its diffraction_planId.

    Args:
        diffraction_plan_id (int): corresponds to diffraction_planId in db

    Returns:
        dict: info about diffraction_plan as dict
    """
    data_dict = {"diffractionPlanId": diffraction_plan_id}
    return db.get_db_item_by_params(
        models.DiffractionPlan, schemas.diffraction_plan.ma_schema, data_dict
    )


def add_diffraction_plan(data_dict):
    """
    Adds a diffraction_plan to db.

    Args:
        data_dict ([type]): [description]

    Returns:
        [type]: [description]
    """
    return db.add_db_item(
        models.DiffractionPlan, schemas.diffraction_plan.ma_schema, data_dict
    )


def update_diffraction_plan(diffraction_plan_id, data_dict):
    """
    Updates diffraction_plan.

    Args:
        diffraction_plan_id ([type]): [description]
        diffraction_plan_dict ([type]): [description]

    Returns:
        [type]: [description]
    """
    id_dict = {"diffractionPlanId": diffraction_plan_id}
    return db.update_db_item(
        models.DiffractionPlan, schemas.diffraction_plan.ma_schema, id_dict, data_dict
    )


def patch_diffraction_plan(diffraction_plan_id, data_dict):
    """
    Patch a diffraction_plan.

    Args:
        diffraction_plan_id ([type]): [description]
        data_dict ([type]): [description]

    Returns:
        [type]: [description]
    """
    id_dict = {"diffractionPlanId": diffraction_plan_id}
    return db.patch_db_item(
        models.DiffractionPlan, schemas.diffraction_plan.ma_schema, id_dict, data_dict
    )


def delete_diffraction_plan(diffraction_plan_id):
    """
    Deletes diffraction_plan item from db.

    Args:
        diffraction_plan_id (int): diffraction_planId column in db

    Returns:
        bool: True if the diffraction_plan exists and deleted successfully,
        otherwise return False
    """
    id_dict = {"diffractionPlanId": diffraction_plan_id}
    return db.delete_db_item(models.DiffractionPlan, id_dict)

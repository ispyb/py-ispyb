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


from flask_restx._http import HTTPStatus

from pyispyb.app.extensions import db, auth_provider
from pyispyb.app.utils import create_response_item

from pyispyb.core import models, schemas

# from pyispyb.core.schemas import phasing_view


def get_phasing_results(request):
    """Returns phasing_results_results by query parameters"""

    query_dict = request.args.to_dict()

    query_arg_list = ("dataCollectionId", "autoProcScalingId", "phasingStepId")

    # print(query_arg_list)
    # return db.get_db_items_by_view(
    #    models.t_v_datacollection_summary_phasing,
    #    phasing_view.dict_schema,
    #    phasing_view.ma_schema,
    #    query_dict,
    # )


def add_phasing_results(data_dict):
    """
    Adds a phasing_results.

    Args:
        phasing_results_dict ([type]): [description]

    Returns:
        [type]: [description]
    """
    return "Ok"
    # return db.add_db_item(models.phasing_results,
    # schemas.phasing_results.ma_schema, data_dict)

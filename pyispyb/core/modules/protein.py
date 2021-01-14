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
from pyispyb.app.utils import create_response_item

from pyispyb.core import models, schemas
from pyispyb.core.modules import proposal


def get_proteins(request):
    """
    Returns protein entries.

    Returns:
        [type]: [description]
    """
    query_params = request.args.to_dict()

    is_admin, proposal_id_list = proposal.get_proposal_ids_by_username(request)

    run_query = False
    if is_admin:
        run_query = True
    else:
        if not proposal_id_list:
            msg = "No sessions returned. User has no proposals."
        else:
            if "proposalId" in query_params.keys():
                if query_params["proposalId"] in proposal_id_list:
                    run_query = True
                else:
                    msg = "Proposal with id %s is not associated with user" % query_params["proposalId"]
            else:
                query_params["proposalId"] = proposal_id_list

    if run_query:
        return db.get_db_items(
            models.Protein,
            schemas.protein.dict_schema,
            schemas.protein.ma_schema,
            query_params,
        )
    else:
        return create_response_item(msg=msg)


def get_protein_by_id(protein_id):
    """
    Returns protein by its proteinId.

    Args:
        protein (int): corresponds to proteinId in db

    Returns:
        dict: info about protein as dict
    """
    data_dict = {"proteinId": protein_id}
    return db.get_db_item_by_params(
        models.Protein, schemas.protein.ma_schema, data_dict
    )


def add_protein(data_dict):
    """
    Adds a protein to db.

    Args:
        data_dict ([type]): [description]

    Returns:
        [type]: [description]
    """
    return db.add_db_item(models.Protein, schemas.protein.ma_schema, data_dict)


def update_protein(protein_id, data_dict):
    """
    Updates protein.

    Args:
        protein_id ([type]): [description]
        protein_dict ([type]): [description]

    Returns:
        [type]: [description]
    """
    id_dict = {"proteinId": protein_id}
    return db.update_db_item(
        models.Protein, schemas.protein.ma_schema, id_dict, data_dict
    )


def patch_protein(protein_id, data_dict):
    """
    Patch a protein.

    Args:
        protein_id ([type]): [description]
        data_dict ([type]): [description]

    Returns:
        [type]: [description]
    """
    id_dict = {"proteinId": protein_id}
    return db.patch_db_item(
        models.Protein, schemas.protein.ma_schema, id_dict, data_dict
    )


def delete_protein(protein_id):
    """
    Deletes protein item from db.

    Args:
        protein_id (int): proteinId column in db

    Returns:
        bool: True if the protein exists and deleted successfully,
        otherwise return False
    """
    id_dict = {"proteinId": protein_id}
    return db.delete_db_item(models.Protein, id_dict)

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


from pyispyb.app.extensions import db
from pyispyb.core import models, schemas


def get_auto_procs(request):
    """
    Returns auto_proc entries.

    Returns:
        [type]: [description]
    """
    query_params = request.args.to_dict()

    return db.get_db_items(
        models.AutoProc,
        schemas.auto_proc.dict_schema,
        schemas.auto_proc.ma_schema,
        query_params,
    )


def get_auto_proc_by_id(auto_proc_id):
    """
    Returns auto_proc by its id

    Args:
        auto_proc_id (int): corresponds to autoProcId in db

    Returns:
        dict: info about auto_proc as dict
    """
    data_dict = {"autoProcId": auto_proc_id}
    return db.get_db_item_by_params(
        models.AutoProc, schemas.auto_proc.ma_schema, data_dict
    )


def add_auto_proc(data_dict):
    """
    Adds a auto_proc to db.

    Args:
        data_dict ([type]): [description]

    Returns:
        [type]: [description]
    """
    return db.add_db_item(models.AutoProc, schemas.auto_proc.ma_schema, data_dict)


def get_auto_proc_status(request):
    """
    Returns auto_proc_status entries.

    Returns:
        [type]: [description]
    """
    query_params = request.args.to_dict()

    return db.get_db_items(
        models.AutoProcStatus,
        schemas.auto_proc_status.dict_schema,
        schemas.auto_proc_status.ma_schema,
        query_params,
    )


def get_auto_proc_status_by_id(auto_proc_status_id):
    """
    Returns auto_proc_status by its auto_proc_statusId.

    Args:
        auto_proc_status (int): corresponds to auto_proc_statusId in db

    Returns:
        dict: info about auto_proc_status as dict
    """
    data_dict = {"auto_proc_statusId": auto_proc_status_id}
    return db.get_db_item_by_params(
        models.AutoProcStatus, schemas.auto_proc_status.ma_schema, data_dict
    )


def add_auto_proc_status(data_dict):
    """
    Adds a auto_proc_status to db.

    Args:
        data_dict ([type]): [description]

    Returns:
        [type]: [description]
    """
    return db.add_db_item(
        models.AutoProcStatus, schemas.auto_proc_status.ma_schema, data_dict
    )


def get_auto_proc_programs(request):
    """
    Returns auto_proc_program entries.

    Returns:
        [type]: [description]
    """
    query_params = request.args.to_dict()

    return db.get_db_items(
        models.AutoProcProgram,
        schemas.auto_proc_program.dict_schema,
        schemas.auto_proc_program.ma_schema,
        query_params,
    )


def get_auto_proc_program_by_id(auto_proc_program_id):
    """
    Returns auto_proc_program by its auto_proc_programId.

    Args:
        auto_proc_program (int): corresponds to auto_proc_programId in db

    Returns:
        dict: info about auto_proc_program as dict
    """
    data_dict = {"autoProcProgramId": auto_proc_program_id}
    return db.get_db_item_by_params(
        models.AutoProcProgram, schemas.auto_proc_program.ma_schema, data_dict
    )


def add_auto_proc_program(data_dict):
    """
    Adds a auto_proc_program to db.

    Args:
        data_dict ([type]): [description]

    Returns:
        [type]: [description]
    """
    return db.add_db_item(
        models.AutoProcProgram, schemas.auto_proc_program.ma_schema, data_dict
    )


def get_auto_proc_program_attachments(request):
    """
    Returns auto_proc_program_attachment entries.

    Returns:
        [type]: [description]
    """
    query_params = request.args.to_dict()

    return db.get_db_items(
        models.AutoProcProgramAttachment,
        schemas.auto_proc_program_attachment.dict_schema,
        schemas.auto_proc_program_attachment.ma_schema,
        query_params,
    )


def get_auto_proc_program_attachment_by_id(auto_proc_program_attachment_id):
    """
    Returns auto_proc_program_attachment by its auto_proc_program_attachmentId.

    Args:
        auto_proc_program_attachment (int): corresponds to autoProcProgramAttachmentId

    Returns:
        dict: info about auto_proc_program_attachment as dict
    """
    data_dict = {"autoProcProgramAttachmentId": auto_proc_program_attachment_id}
    return db.get_db_item_by_params(
        models.AutoProcProgramAttachment,
        schemas.auto_proc_program_attachment.ma_schema,
        data_dict,
    )


def add_auto_proc_program_attachment(data_dict):
    """
    Adds a auto_proc_program_attachment to db.

    Args:
        data_dict ([type]): [description]

    Returns:
        [type]: [description]
    """
    return db.add_db_item(
        models.AutoProcProgramAttachment,
        schemas.auto_proc_program_attachment.ma_schema,
        data_dict,
    )


def get_auto_proc_program_messages(request):
    """
    Returns auto_proc_program_message entries.

    Returns:
        [type]: [description]
    """
    query_params = request.args.to_dict()

    return db.get_db_items(
        models.AutoProcProgramMessage,
        schemas.auto_proc_program_message.dict_schema,
        schemas.auto_proc_program_message.ma_schema,
        query_params,
    )


def get_auto_proc_program_message_by_id(auto_proc_program_message_id):
    """
    Returns auto_proc_program_message by its autoProcProgramMessageId.

    Args:
        auto_proc_program_message (int): corresponds to autoProcProgramMessageId

    Returns:
        dict: info about auto_proc_program_message as dict
    """
    data_dict = {"autoProcProgramMessageId": auto_proc_program_message_id}
    return db.get_db_item_by_params(
        models.AutoProcProgramMessage,
        schemas.auto_proc_program_message.ma_schema,
        data_dict,
    )


def add_auto_proc_program_message(data_dict):
    """
    Adds a auto_proc_program_message to db.

    Args:
        data_dict ([type]): [description]

    Returns:
        [type]: [description]
    """
    return db.add_db_item(
        models.AutoProcProgramMessage,
        schemas.auto_proc_program_message.ma_schema,
        data_dict,
    )

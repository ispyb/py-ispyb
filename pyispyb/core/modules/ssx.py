import json
import logging
import os
import traceback
from typing import Optional, Type, TypeVar

from ispyb import models
import pydantic
from pyispyb.app.extensions.database.definitions import with_authorization
from sqlalchemy.orm import joinedload

from pyispyb.app.extensions.database.middleware import db
from pyispyb.app.utils import model_from_json
from pyispyb.config import settings
from pyispyb.core.modules.events import get_events
from pyispyb.core.modules.session import get_session
from pyispyb.core.schemas import events, ssx as schema
from fastapi.concurrency import run_in_threadpool
import numpy as np


def find_or_create_event_type(name: str):
    type = (
        db.session.query(models.EventType).filter(models.EventType.name == name).first()
    )
    if type is None:
        type = models.EventType(name=name)
        db.session.add(type)
        db.session.flush()
    return type


def create_ssx_datacollection(
    ssx_datacollection_create: schema.SSXDataCollectionCreate,
) -> Optional[events.Event]:
    data_collection_dict = ssx_datacollection_create.dict()
    event_chains_list = data_collection_dict.pop("event_chains")

    try:
        # DATA COLLECTION

        data_collection = model_from_json(
            models.DataCollection,
            {**data_collection_dict},
        )
        db.session.add(data_collection)
        db.session.flush()

        ssx_data_collection = model_from_json(
            models.SSXDataCollection,
            {
                **data_collection_dict,
                "dataCollectionId": data_collection.dataCollectionId,
            },
        )
        db.session.add(ssx_data_collection)
        db.session.flush()

        # EVENT CHAINS

        for event_chain_dict in event_chains_list:
            events_list = event_chain_dict.pop("events")
            event_chain = model_from_json(
                models.EventChain,
                {
                    **event_chain_dict,
                    "dataCollectionId": data_collection.dataCollectionId,
                },
            )
            db.session.add(event_chain)
            db.session.flush()
            for event_dict in events_list:
                type = find_or_create_event_type(event_dict["type"])
                event = model_from_json(
                    models.Event,
                    {
                        **event_dict,
                        "eventChainId": event_chain.eventChainId,
                        "eventTypeId": type.eventTypeId,
                    },
                )
                db.session.add(event)
            db.session.flush()

        db.session.commit()
        return get_events(
            skip=0, limit=1, dataCollectionId=data_collection.dataCollectionId
        ).first

    except Exception as e:
        logging.error(traceback.format_exc())
        db.session.rollback()
        raise e


def find_or_create_component_type(name: str):
    type = (
        db.session.query(models.ComponentType)
        .filter(models.ComponentType.name == name)
        .first()
    )
    if type is None:
        type = models.ComponentType(name=name)
        db.session.add(type)
        db.session.flush()
    return type


def create_ssx_datacollectiongroup(
    ssx_datacollectiongroup_create: schema.SSXDataCollectionGroupCreate,
) -> Optional[int]:
    datacollectiongroup_dict = ssx_datacollectiongroup_create.dict()
    sample_dict = datacollectiongroup_dict.pop("sample")
    crystal_dict = sample_dict.pop("crystal")
    protein_dict = crystal_dict.pop("protein")
    crystal_components_list = crystal_dict.pop("components")
    sample_components_list = sample_dict.pop("components")

    try:

        ## SAMPLE

        protein = model_from_json(
            models.Protein,
            {
                **protein_dict,
                "proposalId": get_session(
                    datacollectiongroup_dict["sessionId"]
                ).proposalId,
            },
        )
        db.session.add(protein)
        db.session.flush()

        crystal = model_from_json(
            models.Crystal,
            {
                **crystal_dict,
                "proteinId": protein.proteinId,
            },
        )
        db.session.add(crystal)
        db.session.flush()

        sample = model_from_json(
            models.BLSample,
            {
                **sample_dict,
                "crystalId": crystal.crystalId,
            },
        )
        db.session.add(sample)
        db.session.flush()

        for component_dict in crystal_components_list:
            type = find_or_create_component_type(component_dict["componentType"])
            component = model_from_json(
                models.Component,
                {
                    **component_dict,
                    "componentTypeId": type.componentTypeId,
                },
            )
            db.session.add(component)
            db.session.flush()
            composition = model_from_json(
                models.CrystalComposition,
                {
                    **component_dict,
                    "componentId": component.componentId,
                    "crystalId": crystal.crystalId,
                },
            )
            db.session.add(composition)
            db.session.flush()

        for component_dict in sample_components_list:
            type = find_or_create_component_type(component_dict["componentType"])
            component = model_from_json(
                models.Component,
                {
                    **component_dict,
                    "componentTypeId": type.componentTypeId,
                },
            )
            db.session.add(component)
            db.session.flush()
            composition = model_from_json(
                models.SampleComposition,
                {
                    **component_dict,
                    "componentId": component.componentId,
                    "blSampleId": sample.blSampleId,
                },
            )
            db.session.add(composition)
            db.session.flush()

        # DATA COLLECTION GROUP

        data_collection_group = model_from_json(
            models.DataCollectionGroup,
            {
                **datacollectiongroup_dict,
                "blSampleId": sample.blSampleId,
            },
        )
        db.session.add(data_collection_group)
        db.session.flush()

        db.session.commit()
        return data_collection_group.dataCollectionGroupId

    except Exception as e:
        logging.error(traceback.format_exc())
        db.session.rollback()
        raise e


def create_ssx_datacollection_processing(
    dataCollectionId: int, data: schema.SSXDataCollectionProcessingCreate
) -> int:

    program = models.AutoProcProgram(
        dataCollectionId=dataCollectionId,
        processingCommandLine=data.processingCommandLine,
        processingPrograms=data.processingPrograms,
        processingStatus="SUCCESS",
        processingMessage=data.processingMessage,
        processingStartTime=data.processingStartTime,
        processingEndTime=data.processingEndTime,
        processingEnvironment=data.processingEnvironment,
    )
    db.session.add(program)
    db.session.flush()

    autoProcProgramId = program.autoProcProgramId

    for resultPath in data.results:
        [filePath, fileName] = os.path.split(resultPath)
        attachment = models.AutoProcProgramAttachment(
            filePath=filePath,
            fileName=fileName,
            fileType="Result",
            autoProcProgramId=autoProcProgramId,
        )
        db.session.add(attachment)
        db.session.flush()

    db.session.commit()
    return autoProcProgramId


def get_ssx_datacollection_processing_attachments_results(
    dataCollectionIds: list[int],
) -> list[models.AutoProcProgramAttachment]:
    query = (
        db.session.query(models.AutoProcProgramAttachment)
        .filter(models.AutoProcProgramAttachment.fileType == "Result")
        .options(joinedload(models.AutoProcProgramAttachment.AutoProcProgram))
        .options(
            joinedload(
                models.AutoProcProgramAttachment.AutoProcProgram,
                models.AutoProcProgram.DataCollection,
            )
        )
        .join(
            models.AutoProcProgram,
            models.AutoProcProgramAttachment.autoProcProgramId
            == models.AutoProcProgram.autoProcProgramId,
        )
        .join(
            models.DataCollection,
            models.AutoProcProgram.dataCollectionId
            == models.DataCollection.dataCollectionId,
        )
        .filter(models.DataCollection.dataCollectionId.in_(dataCollectionIds))
        .join(
            models.BLSession,
            models.DataCollection.sessionId == models.BLSession.sessionId,
        )
        .join(
            models.Proposal, models.BLSession.proposalId == models.Proposal.proposalId
        )
    )

    query = with_authorization(query, joinBLSession=False)

    return query.all()


T = TypeVar("T")


def parse_file_as_sync(type_: Type[T], path: str, validate: bool = True) -> T | None:
    try:
        with open(path, mode="r") as f:
            contents = f.read()
        if validate:
            parsed = pydantic.parse_raw_as(type_, contents)
        else:
            parsed = json.loads(contents)
        return parsed
    except pydantic.error_wrappers.ValidationError:
        return None
    except FileNotFoundError:
        return None


async def get_ssx_datacollection_processing_stats(
    dataCollectionIds: list[int],
) -> list[schema.SSXDataCollectionProcessingStats]:
    attachments: list[
        models.AutoProcProgramAttachment
    ] = get_ssx_datacollection_processing_attachments_results(dataCollectionIds)

    res: list[schema.SSXDataCollectionProcessingStats] = []

    for attachment in attachments:
        if attachment.fileName == "ssx_stats.json":
            path = os.path.join(attachment.filePath, attachment.fileName)
            if settings.path_map:
                path = os.path.join(settings.path_map, path)
            parsed = await run_in_threadpool(
                parse_file_as_sync, schema.SSXDataCollectionProcessingStatsBase, path
            )
            if parsed is not None:
                res.append(
                    {
                        "dataCollectionId": attachment.AutoProcProgram.DataCollection.dataCollectionId,
                        **parsed.dict(),
                    }
                )
    return res


async def get_ssx_datacollection_processing_cells(
    dataCollectionId: int,
) -> schema.SSXDataCollectionProcessingCells | None:

    attachments: list[
        models.AutoProcProgramAttachment
    ] = get_ssx_datacollection_processing_attachments_results([dataCollectionId])

    for attachment in attachments:
        if attachment.fileName == "ssx_cells.json":
            path = os.path.join(attachment.filePath, attachment.fileName)
            if settings.path_map:
                path = os.path.join(settings.path_map, path)
            parsed = await run_in_threadpool(
                parse_file_as_sync,
                schema.SSXDataCollectionProcessingCells,
                path,
                validate=False,
            )
            if parsed is not None:
                return parsed
    return None


async def get_ssx_datacollection_processing_cells_histogram(
    dataCollectionIds: list[int],
) -> schema.SSXDataCollectionProcessingCellsHistogram:
    cells = []
    for dataCollectionId in dataCollectionIds:
        cells_json = await get_ssx_datacollection_processing_cells(dataCollectionId)
        if cells_json is not None:
            cells = cells + cells_json["unit_cells"]
    if len(cells) == 0:
        return None
    bins = to_bins(cells)
    return {
        "a": bins[0],
        "b": bins[1],
        "c": bins[2],
        "alpha": bins[3],
        "beta": bins[4],
        "gamma": bins[5],
    }


def to_bins(data: list[list[float]], nb_bins: int = 50):
    unzipped = list(zip(*data))
    res = []
    for cell in unzipped:
        hist, bin_edges = np.histogram(filter_outliers(cell), nb_bins)
        median = np.median(cell)
        res = res + [{"y": list(hist), "x": list(bin_edges), "median": median}]
    return res


def filter_outliers(data: list[float]):
    # FROM https://gist.github.com/vishalkuo/f4aec300cf6252ed28d3
    a = np.array(data)
    upper_quartile = np.percentile(a, 75)
    lower_quartile = np.percentile(a, 25)
    IQR = (upper_quartile - lower_quartile) * 1.5
    quartileSet = (lower_quartile - IQR, upper_quartile + IQR)
    resultList = []
    for y in a.tolist():
        if y >= quartileSet[0] and y <= quartileSet[1]:
            resultList.append(y)
    return resultList

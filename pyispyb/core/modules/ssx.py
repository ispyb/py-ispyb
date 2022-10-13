import logging
import traceback
from typing import Optional

from ispyb import models
from pyispyb.app.extensions.database.definitions import with_authorization
from pyispyb.app.extensions.database.middleware import db
from pyispyb.app.utils import model_from_json
from pyispyb.core.modules.session import get_session
from pyispyb.core.schemas import ssx as schema
from sqlalchemy.orm import joinedload


def get_ssx_datacollection_event_chains(
    dataCollectionId: int,
) -> list[models.EventChain]:
    q = (
        db.session.query(models.EventChain)
        .filter(models.EventChain.dataCollectionId == dataCollectionId)
        .options(
            joinedload(
                models.EventChain.events,
                models.Event.EventType,
            )
        )
        .join(
            models.DataCollection,
            models.EventChain.dataCollectionId
            == models.DataCollection.dataCollectionId,
        )
        .join(
            models.BLSession,
            models.DataCollection.sessionId == models.BLSession.sessionId,
        )
    )
    res = with_authorization(
        q, [], proposalColumn=models.BLSession.proposalId, joinBLSession=False
    ).all()
    return res


def get_ssx_datacollection_sample(
    dataCollectionId: int,
) -> Optional[models.BLSample]:
    res = (
        db.session.query(models.BLSample)
        .join(
            models.DataCollectionGroup,
            models.DataCollectionGroup.blSampleId == models.BLSample.blSampleId,
        )
        .join(
            models.DataCollection,
            models.DataCollection.dataCollectionGroupId
            == models.DataCollectionGroup.dataCollectionGroupId,
        )
        .filter(models.DataCollection.dataCollectionId == dataCollectionId)
        .options(
            joinedload(
                models.BLSample.sample_compositions,
                models.SampleComposition.Component,
                models.Component.ComponentType,
            )
        )
        .options(
            joinedload(
                models.BLSample.Crystal,
                models.Crystal.Protein,
            )
        )
        .options(
            joinedload(
                models.BLSample.Crystal,
                models.Crystal.crystal_compositions,
                models.CrystalComposition.Component,
                models.Component.ComponentType,
            )
        )
        .first()
    )
    return res


def get_ssx_datacollectiongroup_sample(
    dataCollectionGroupId: int,
) -> Optional[models.BLSample]:
    res = (
        db.session.query(models.BLSample)
        .join(
            models.DataCollectionGroup,
            models.DataCollectionGroup.blSampleId == models.BLSample.blSampleId,
        )
        .filter(
            models.DataCollectionGroup.dataCollectionGroupId == dataCollectionGroupId
        )
        .options(
            joinedload(
                models.BLSample.sample_compositions,
                models.SampleComposition.Component,
                models.Component.ComponentType,
            )
        )
        .options(
            joinedload(
                models.BLSample.Crystal,
                models.Crystal.Protein,
            )
        )
        .options(
            joinedload(
                models.BLSample.Crystal,
                models.Crystal.crystal_compositions,
                models.CrystalComposition.Component,
                models.Component.ComponentType,
            )
        )
        .first()
    )
    return res


def _ssx_datacollection_query():
    return db.session.query(models.SSXDataCollection).options(
        joinedload(
            models.SSXDataCollection.DataCollection,
            models.DataCollection.DataCollectionGroup,
        ),
        joinedload(
            models.SSXDataCollection.DataCollection,
            models.DataCollection.Detector,
        ),
    )


def get_ssx_datacollection(
    dataCollectionId: int,
) -> Optional[models.SSXDataCollection]:
    dc = (
        _ssx_datacollection_query()
        .filter(models.SSXDataCollection.dataCollectionId == dataCollectionId)
        .first()
    )

    return dc


def get_ssx_datacollectiongroup(
    dataCollectionGroupId: int,
) -> Optional[models.DataCollectionGroup]:
    return (
        db.session.query(models.DataCollectionGroup)
        .filter(
            models.DataCollectionGroup.dataCollectionGroupId == dataCollectionGroupId
        )
        .first()
    )


def count_datacollections(dataCollectionGroupId: int) -> int:
    dc = (
        db.session.query(models.DataCollection)
        .join(
            models.DataCollectionGroup,
            models.DataCollectionGroup.dataCollectionGroupId
            == models.DataCollection.dataCollectionGroupId,
        )
        .filter(
            models.DataCollectionGroup.dataCollectionGroupId == dataCollectionGroupId
        )
        .count()
    )

    return dc


def get_ssx_datacollections(
    sessionId: int, dataCollectionGroupId: int
) -> list[models.SSXDataCollection]:
    dc = (
        _ssx_datacollection_query()
        .join(
            models.DataCollection,
            models.DataCollection.dataCollectionId
            == models.SSXDataCollection.dataCollectionId,
        )
        .join(
            models.DataCollectionGroup,
            models.DataCollectionGroup.dataCollectionGroupId
            == models.DataCollection.dataCollectionGroupId,
        )
        .filter(models.DataCollectionGroup.sessionId == sessionId)
        .filter(
            models.DataCollectionGroup.dataCollectionGroupId == dataCollectionGroupId
        )
        .all()
    )

    return dc


def get_ssx_datacollectiongroups(
    sessionId: int,
) -> list[models.DataCollectionGroup]:
    dc = (
        db.session.query(models.DataCollectionGroup)
        .filter(models.DataCollectionGroup.sessionId == sessionId)
        .options(joinedload(models.DataCollectionGroup.ExperimentType))
        .all()
    )

    return dc


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
) -> Optional[models.SSXDataCollection]:
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
        return get_ssx_datacollection(data_collection.dataCollectionId)

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


def find_or_create_experiment_type(name: str):
    type = (
        db.session.query(models.ExperimentType)
        .filter(models.ComponentType.name == name)
        .first()
    )
    if type is None:
        type = models.ExperimentType(name=name)
        db.session.add(type)
        db.session.flush()
    return type


def create_ssx_datacollectiongroup(
    ssx_datacollectiongroup_create: schema.SSXDataCollectionGroupCreate,
) -> Optional[models.SSXDataCollection]:
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

        type = find_or_create_experiment_type(
            datacollectiongroup_dict.pop("experimentType")
        )

        data_collection_group = model_from_json(
            models.DataCollectionGroup,
            {
                **datacollectiongroup_dict,
                "blSampleId": sample.blSampleId,
                "experimentTypeId": type.experimentTypeId,
            },
        )
        db.session.add(data_collection_group)
        db.session.flush()

        db.session.commit()
        return get_ssx_datacollectiongroup(data_collection_group.dataCollectionGroupId)

    except Exception as e:
        logging.error(traceback.format_exc())
        db.session.rollback()
        raise e


def get_ssx_datacollection_processing(
    dataCollectionId: int,
) -> Optional[models.SSXDataCollectionProcessing]:
    return (
        db.session.query(models.SSXDataCollectionProcessing)
        .filter(models.SSXDataCollectionProcessing.dataCollectionId == dataCollectionId)
        .first()
    )


def create_ssx_datacollection_processing(
    dataCollectionId: int,
    ssx_hits_create: schema.SSXDataCollectionProcessingCreate,
) -> Optional[models.SSXDataCollectionProcessing]:
    hits_dict = ssx_hits_create.dict()
    # unit_cells_array = hits_dict.pop("unit_cells")

    try:

        # AUTO PROC PROGRAM

        prog = models.AutoProcProgram(
            dataCollectionId=dataCollectionId,
            processingPrograms="ssxDataCollectionProcessing",
            processingStatus="SUCCESS",
        )
        db.session.add(prog)
        db.session.flush()

        ## SSX DC PROCESSING

        hits = model_from_json(
            models.SSXDataCollectionProcessing,
            {
                **hits_dict,
                "dataCollectionId": dataCollectionId,
                "autoProcProgramId": prog.autoProcProgramId,
            },
        )
        db.session.add(hits)
        db.session.flush()

        # UNIT CELLS

        # if hits_dict["nbIndexed"] >= 1000:

        #     names = ["a", "b", "c", "alpha", "beta", "gamma"]

        #     for i in range(0, 6):
        #         d = list(map(lambda a: a[i], unit_cells_array))

        #         hist, bins = np.histogram(d, bins=100)

        #         graph = models.Graph(name=names[i], dataCollectionId=dataCollectionId)
        #         db.session.add(graph)
        #         db.session.flush()

        #         for n in range(0, hist.size):
        #             y = hist[n]
        #             x = round((bins[n] + bins[n + 1]) / 2, 2)
        #             graphData = models.GraphData(
        #                 graphId=graph.graphId, x=float(x), y=float(y)
        #             )
        #             db.session.add(graphData)
        #             db.session.flush()

        db.session.commit()
        return get_ssx_datacollection_processing(dataCollectionId)

    except Exception as e:
        logging.error(traceback.format_exc())
        db.session.rollback()
        raise e

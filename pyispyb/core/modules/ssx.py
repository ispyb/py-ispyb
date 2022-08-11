import logging
import traceback
from typing import Optional
from pyispyb.app.utils import model_from_json


from pyispyb.core import models
from pyispyb.app.extensions.database.middleware import db

from sqlalchemy.orm import joinedload
from pyispyb.core.modules.session import get_session
from pyispyb.core.schemas import ssx as schema

def get_ssx_datacollection_sequences(dataCollectionId: int)-> list[models.Sequence]:
    res = (
        db.session.query(models.Sequence)
        .filter(models.Sequence.dataCollectionId == dataCollectionId)
        .options(joinedload(models.Sequence.sequence_events))
        .all()
    )
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
        .options(joinedload(models.BLSample.sample_components))
        .options(
            joinedload(
                models.BLSample.Crystal,
                models.Crystal.Protein,
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
        .filter(models.DataCollection.dataCollectionId == dataCollectionId)
        .first()
    )

    return dc


def get_ssx_datacollections(
    sessionId: int,
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
        .all()
    )

    return dc


def create_ssx_datacollection(
    ssx_data_collection_create: schema.SSXDataCollectionCreate,
) -> Optional[models.SSXDataCollection]:
    data_collection_dict = ssx_data_collection_create.dict()
    sample_dict = data_collection_dict.pop("sample")
    crystal_dict = sample_dict.pop("crystal")
    protein_dict = crystal_dict.pop("protein")
    components_list = sample_dict.pop("components")
    sequences_list = data_collection_dict.pop("sequences")

    try:

        ## SAMPLE

        protein = model_from_json(
            models.Protein,
            {
                **protein_dict,
                "proposalId": get_session(data_collection_dict["sessionId"]).proposalId,
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

        for component_dict in components_list:
            component = model_from_json(
                models.SampleComponent,
                {
                    **component_dict,
                    "blSampleId": sample.blSampleId,
                },
            )
            db.session.add(component)
            db.session.flush()

        # DATA COLLECTION

        data_collection_group = model_from_json(
            models.DataCollectionGroup,
            {
                **data_collection_dict,
                "blSampleId": sample.blSampleId,
            },
        )
        db.session.add(data_collection_group)
        db.session.flush()

        data_collection = model_from_json(
            models.DataCollection,
            {
                **data_collection_dict,
                "dataCollectionGroupId": data_collection_group.dataCollectionGroupId,
            },
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

        # SEQUENCES

        for sequence_dict in sequences_list:
            events_list = sequence_dict.pop("events")
            sequence = model_from_json(
                models.Sequence,
                {
                    **sequence_dict,
                    "dataCollectionId": data_collection.dataCollectionId,
                },
            )
            db.session.add(sequence)
            db.session.flush()
            for event_dict in events_list:
                event = model_from_json(
                    models.SequenceEvent,
                    {
                        **event_dict,
                        "sequenceId": sequence.sequenceId,
                    },
                )
                db.session.add(event)
            db.session.flush()

        db.session.commit()
        return get_ssx_datacollection(ssx_data_collection.ssxDataCollectionId)

    except Exception as e:
        logging.error(traceback.format_exc())
        db.session.rollback()
        raise e

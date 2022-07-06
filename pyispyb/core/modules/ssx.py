import logging
import traceback
from typing import Optional
from pyispyb.app.utils import model_from_json


from pyispyb.core import models
from pyispyb.app.extensions.database.middleware import db

from sqlalchemy.orm import joinedload
from pyispyb.core.schemas import ssx as schema


def get_ssx_datacollection(
    ssxDataCollectionId: int,
) -> Optional[models.SSXDataCollection]:
    dc = (
        db.session.query(models.SSXDataCollection)
        .options(joinedload(models.SSXDataCollection.DataCollection))
        .options(joinedload(models.DataCollection.DataCollectionGroup))
        .filter(models.SSXDataCollection.ssxDataCollectionId == ssxDataCollectionId)
        .first()
    )

    return dc


def get_ssx_datacollections(
    sessionId: int,
) -> list[models.SSXDataCollection]:
    dc = (
        db.session.query(models.SSXDataCollection)
        .options(joinedload(models.SSXDataCollection.DataCollection))
        .options(
            joinedload(
                models.SSXDataCollection.DataCollection,
                models.DataCollection.DataCollectionGroup,
            )
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
    buffer_dict = sample_dict.pop("buffer")

    try:

        data_collection_group = model_from_json(
            models.DataCollectionGroup, data_collection_dict
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

        ssx_buffer = model_from_json(models.SSXBuffer, buffer_dict)
        db.session.add(ssx_buffer)
        db.session.flush()

        ssx_sample = model_from_json(
            models.SSXSample, {**sample_dict, "ssxBufferId": ssx_buffer.ssxBufferId}
        )
        db.session.add(ssx_sample)
        db.session.flush()

        ssx_data_collection = model_from_json(
            models.SSXDataCollection,
            {
                **data_collection_dict,
                "dataCollectionId": data_collection.dataCollectionId,
                "ssxSampleId": ssx_sample.ssxSampleId,
            },
        )
        db.session.add(ssx_data_collection)
        db.session.flush()

        db.session.commit()

    except Exception:
        logging.error(traceback.format_exc())
        db.session.rollback()

    return get_ssx_datacollection(ssx_data_collection.ssxDataCollectionId)

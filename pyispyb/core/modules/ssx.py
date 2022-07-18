import logging
import traceback
from typing import Optional
from pyispyb.app.utils import model_from_json


from pyispyb.core import models
from pyispyb.app.extensions.database.middleware import db

from sqlalchemy.orm import joinedload
from pyispyb.core.schemas import ssx as schema


def get_ssx_datacollection_sample(
    ssxDataCollectionId: int,
) -> Optional[schema.SSXSpecimenResponse]:
    specimen = (
        db.session.query(models.SSXSpecimen)
        .join(
            models.SSXDataCollection,
            models.SSXDataCollection.ssxSpecimenId == models.SSXSpecimen.ssxSpecimenId,
        )
        .filter(models.SSXDataCollection.ssxDataCollectionId == ssxDataCollectionId)
        .options(
            joinedload(
                models.SSXSpecimen.Specimen,
                models.Specimen.Macromolecule,
            )
        )
        .options(
            joinedload(
                models.SSXSpecimen.Specimen,
                models.Specimen.Buffer,
            )
        )
        .first()
    )
    structures = (
        db.session.query(models.Structure)
        .filter(models.Structure.macromoleculeId == specimen.Specimen.macromoleculeId)
        .all()
    )
    res = specimen.__dict__
    res["Specimen"] = specimen.Specimen.__dict__
    res["Specimen"]["Structures"] = structures
    return res


def _ssx_datacollection_query():
    return db.session.query(models.SSXDataCollection).options(
        joinedload(
            models.SSXDataCollection.DataCollection,
            models.DataCollection.DataCollectionGroup,
        )
    )


def get_ssx_datacollection(
    ssxDataCollectionId: int,
) -> Optional[models.SSXDataCollection]:
    dc = (
        _ssx_datacollection_query()
        .filter(models.SSXDataCollection.ssxDataCollectionId == ssxDataCollectionId)
        .first()
    )

    return dc


def get_ssx_datacollections(
    sessionId: int,
) -> list[models.SSXDataCollection]:
    dc = (
        _ssx_datacollection_query()
        .filter(models.DataCollectionGroup.sessionId == sessionId)
        .all()
    )

    return dc


def create_ssx_datacollection(
    ssx_data_collection_create: schema.SSXDataCollectionCreate,
) -> Optional[models.SSXDataCollection]:
    data_collection_dict = ssx_data_collection_create.dict()
    sample_dict = data_collection_dict.pop("sample")

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

        experiment = model_from_json(
            models.Experiment,
            {
                **data_collection_dict,
                "proposalId": data_collection_group.BLSession.Proposal.proposalId,
            },
        )
        db.session.add(experiment)
        db.session.flush()

        buffer = model_from_json(
            models.Buffer,
            {
                "name": sample_dict["bufferName"],
                "composition": sample_dict["bufferComposition"],
            },
        )
        db.session.add(buffer)
        db.session.flush()

        macromolecule = model_from_json(models.Macromolecule, sample_dict)
        db.session.add(macromolecule)
        db.session.flush()

        ligand = model_from_json(
            models.Structure,
            {
                "macromoleculeId": macromolecule.macromoleculeId,
                "structureType": "Ligand",
                "name": sample_dict["ligandName"],
            },
        )
        db.session.add(ligand)
        db.session.flush()

        specimen = model_from_json(
            models.Specimen,
            {
                "macromoleculeId": macromolecule.macromoleculeId,
                "experimentId": experiment.experimentId,
                "bufferId": buffer.bufferId,
                "concentration": sample_dict["crystalConcentration"],
            },
        )
        db.session.add(specimen)
        db.session.flush()

        ssx_specimen = model_from_json(
            models.SSXSpecimen,
            {
                "specimenId": specimen.specimenId,
                **sample_dict,
            },
        )
        db.session.add(ssx_specimen)
        db.session.flush()

        ssx_data_collection = model_from_json(
            models.SSXDataCollection,
            {
                **data_collection_dict,
                "dataCollectionId": data_collection.dataCollectionId,
                "ssxSpecimenId": ssx_specimen.ssxSpecimenId,
            },
        )
        db.session.add(ssx_data_collection)
        db.session.flush()

        db.session.commit()
        return get_ssx_datacollection(ssx_data_collection.ssxDataCollectionId)

    except Exception as e:
        logging.error(traceback.format_exc())
        db.session.rollback()
        raise e

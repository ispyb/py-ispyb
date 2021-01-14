from tests.core import data

from pyispyb.core import schemas


def test_data_collection_model():
    data_collection = schemas.data_collection.DataCollectionSchema().dump(
        data.test_data_collection
    )

    assert data_collection.errors == {}


def test_proposal_model():
    proposal = schemas.proposal.ProposalSchema().dump(data.test_proposal)

    assert proposal.errors == {}


def test_session_model():
    pass
    # session = schemas.session.SessionSchema().dump(data.test_session)

    # assert session.errors == {}


def test_lab_contact_model():
    lab_contact = schemas.lab_contact.LabContactSchema().dump(data.test_lab_contact)

    assert lab_contact.errors == {}


def test_shipment_model():
    shipmenmt = schemas.shipping.ShippingSchema().dump(data.test_shippment)

    assert shipmenmt.errors == {}


def test_laboratory_model():
    laboratory = schemas.laboratory.LaboratorySchema().dump(data.test_laboratory)

    assert laboratory.errors == {}


def test_person_model():
    person = schemas.person.PersonSchema().dump(data.test_person)

    assert person.errors == {}

from fastapi.testclient import TestClient
from sqlalchemy.orm import sessionmaker
from pyispyb.app.extensions.database.middleware import Database
from pyispyb.app.main import app
from pyispyb.config import settings
from pyispyb.app.extensions.database.session import engine
from pyispyb.core.modules.proposals import get_proposals
from pyispyb.core.modules.persons import get_persons
from pyispyb.core.modules.laboratories import get_laboratories
from pyispyb.core.modules.proteins import get_proteins
from pyispyb.core.modules.sessions import get_sessions
from pyispyb.core.modules.labcontacts import get_labcontacts
from tests.core.api.data.userportalsync import (
    test_data_proposal_userportalsync,
)


TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = TestingSessionLocal()
db = Database()
db.set_session(session)


client = TestClient(app)


def test_call_sync_proposal():
    res = client.post(
        f"{settings.api_root}/auth/login",
        json={"username": "efgh", "password": "efgh", "plugin": "dummy"},
    )
    assert res.status_code == 201

    data = test_data_proposal_userportalsync
    headers = {"Authorization": f"Bearer {res.json()['token']}"}
    res2 = client.post(
        f"{settings.api_root}/userportalsync/sync_proposal", headers=headers, json=data
    )

    # No errors running the sync_proposal endpoint passing the test_data_proposal_userportalsync JSON data
    assert res2.status_code == 200


def test_proposal_persons_sync():
    # Only one proposal with proposalCode and proposalNumber should have been created in DB
    proposals = get_proposals(
        skip=0,
        limit=10,
        proposalCode=test_data_proposal_userportalsync["proposal"]["proposalCode"],
        proposalNumber=test_data_proposal_userportalsync["proposal"]["proposalNumber"],
        proposalHasPerson=True,
    )

    assert proposals.total == 1

    # Check the persons related to the proposal were created
    total_proposal_persons = 0
    for i, json_person in enumerate(
        test_data_proposal_userportalsync["proposal"]["persons"]
    ):
        # Lookup for the persons in DB according to the input JSON data
        persons = get_persons(
            skip=0,
            limit=10,
            login=json_person["login"],
            givenName=json_person["givenName"],
            familyName=json_person["familyName"],
        )
        if persons.total == 1:
            total_proposal_persons += 1
        if i == 0:
            # Save the personID from the first person in the  JSON list
            first_person_id = persons.results[i].personId

    assert total_proposal_persons == len(
        test_data_proposal_userportalsync["proposal"]["persons"]
    )

    # The first person related to the proposal (PI or leader)
    # should be the one having the relation with the Proposal table in DB (foreign constraint)
    assert first_person_id == proposals.results[0].personId

    # Check the number of persons within the ProposalHasPerson table
    assert len(test_data_proposal_userportalsync["proposal"]["persons"]) == len(
        proposals.results[0].proposal_has_people
    )


# We could check also if the right persons where added within the ProposalHasPerson table


def test_proposal_persons_laboratories_sync():
    # Get a list of unique laboratories from proposal persons
    unique_laboratories = []
    for i, person in enumerate(
        test_data_proposal_userportalsync["proposal"]["persons"]
    ):
        if person["laboratory"] not in unique_laboratories:
            # Make a list of unique laboratories
            unique_laboratories.append(person["laboratory"])

    labs_in_db = 0
    for laboratory in unique_laboratories:
        # Lookup for the laboratories in DB according to the input JSON data
        laboratories = get_laboratories(
            skip=0,
            limit=10,
            name=laboratory["name"],
            city=laboratory["city"],
            country=laboratory["country"],
        )
        if laboratories.total == 1:
            labs_in_db += 1

    # Check the amount of unique laboratories corresponds with the entries in the DB
    assert len(unique_laboratories) == labs_in_db


def test_session_persons_sync():
    # Iterate over the session
    sessions_in_db = 0
    for json_session in test_data_proposal_userportalsync["sessions"]:

        sessions = get_sessions(
            skip=0,
            limit=10,
            expSessionPk=json_session["expSessionPk"],
            sessionHasPerson=True,
        )

        if sessions.total == 1:
            sessions_in_db += 1
            # Check the number of persons within the Session_has_Person table
            assert len(sessions.results[0].session_has_people) == len(
                json_session["persons"]
            )

    # Check the amount of sessions corresponds with the entries in the DB
    assert len(test_data_proposal_userportalsync["sessions"]) == sessions_in_db


def test_lab_contacts_sync():
    # Get the proposal from the DB
    proposals = get_proposals(
        skip=0,
        limit=10,
        proposalCode=test_data_proposal_userportalsync["proposal"]["proposalCode"],
        proposalNumber=test_data_proposal_userportalsync["proposal"]["proposalNumber"],
        proposalHasPerson=False,
    )
    # Get the lab contacts for the proposal in DB
    labcontacts = get_labcontacts(
        skip=0,
        limit=10,
        proposalId=proposals.results[0].proposalId,
    )

    # Check the amount of LabContacts for the proposal corresponds with the entries in the DB
    assert (
        len(test_data_proposal_userportalsync["proposal"]["labcontacts"])
        == labcontacts.total
    )

    # Later we can add more automatic testings to see if the right persons were added, etc


def test_proteins_sync():
    # Get the proposal from the DB
    proposals = get_proposals(
        skip=0,
        limit=10,
        proposalCode=test_data_proposal_userportalsync["proposal"]["proposalCode"],
        proposalNumber=test_data_proposal_userportalsync["proposal"]["proposalNumber"],
    )

    proteins_in_db = 0
    for i, protein in enumerate(test_data_proposal_userportalsync["proteins"]):
        # Check all proteins in DB related to the proposalID
        proteins = get_proteins(
            skip=0,
            limit=10,
            name=protein["name"],
            proposalId=proposals.results[0].proposalId,
        )
        if proteins.total == 1:
            proteins_in_db += 1
    # Check the amount of proteins in JSON corresponds with the entries in the DB
    assert len(test_data_proposal_userportalsync["proteins"]) == proteins_in_db

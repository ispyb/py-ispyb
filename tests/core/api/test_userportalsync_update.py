from pyispyb.app.main import app
from pyispyb.config import settings
from tests.core.api.utils.permissions import mock_permissions
from pyispyb.core.modules.proposals import get_proposals
from pyispyb.core.modules.persons import get_persons
from pyispyb.core.modules.sessions import get_sessions
from tests.core.api.data.userportalsync_update import (
    test_data_proposal_userportalsync_update,
)


def test_call_sync_proposal_update(client):
    with mock_permissions(["uportal_sync"], app):
        res = client.post(
            f"{settings.api_root}/auth/login",
            json={"login": "efgh", "password": "efgh", "plugin": "dummy"},
        )
        assert res.status_code == 201

        data = test_data_proposal_userportalsync_update
        headers = {"Authorization": f"Bearer {res.json()['token']}"}
        res2 = client.post(
            f"{settings.api_root}/userportalsync/sync_proposal",
            headers=headers,
            json=data,
        )

        # No errors running the sync_proposal endpoint passing the test_data_proposal_userportalsync_update JSON data
        assert res2.status_code == 200


def test_proposal_title_update(with_db_session):
    # Get the proposal from the DB
    proposals = get_proposals(
        skip=0,
        limit=10,
        proposalCode=test_data_proposal_userportalsync_update["proposal"][
            "proposalCode"
        ],
        proposalNumber=test_data_proposal_userportalsync_update["proposal"][
            "proposalNumber"
        ],
    )
    # Check the proposal title was updated as expected
    assert (
        proposals.results[0].title
        == test_data_proposal_userportalsync_update["proposal"]["title"]
    )


def test_person_email_update(with_db_session):
    # Get the person from the DB
    persons = get_persons(
        skip=0,
        limit=10,
        login=test_data_proposal_userportalsync_update["proposal"]["persons"][0][
            "login"
        ],
    )
    # Check the person email was updated as expected
    assert (
        persons.results[0].emailAddress
        == test_data_proposal_userportalsync_update["proposal"]["persons"][0][
            "emailAddress"
        ]
    )


def test_person_laboratory_name_update(with_db_session):
    # Get the person from the DB
    persons = get_persons(
        skip=0,
        limit=10,
        login=test_data_proposal_userportalsync_update["proposal"]["persons"][1][
            "login"
        ],
        withLaboratory=True,
    )
    # Check the laboratory name was updated as expected
    assert (
        persons.results[0].Laboratory.name
        == test_data_proposal_userportalsync_update["proposal"]["persons"][1][
            "laboratory"
        ]["name"]
    )


def test_session_beamline_name_update(with_db_session):
    # Get the session from the DB
    sessions = get_sessions(
        skip=0,
        limit=10,
        externalId=test_data_proposal_userportalsync_update["sessions"][0][
            "externalId"
        ],
    )
    # Check the laboratory name was updated as expected
    assert (
        sessions.results[0].beamLineName
        == test_data_proposal_userportalsync_update["sessions"][0]["beamLineName"]
    )


# More testings can be added later

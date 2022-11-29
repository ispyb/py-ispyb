import pytest
from tests.conftest import AuthClient
from tests.core.api.utils.apitest import get_elem_name, run_test, ApiTestElem
from starlette.types import ASGIApp
from pyispyb.core.modules.proposals import get_proposals
from pyispyb.core.modules.persons import get_persons
from pyispyb.core.modules.sessions import get_sessions
from tests.core.api.data.userportalsync_update import (
    test_data_proposal_userportalsync_update,
    test_route_uportal_sync_update,
)


@pytest.mark.parametrize("test_elem", test_route_uportal_sync_update, ids=get_elem_name)
def test_call_sync_proposal_create(
    auth_client: AuthClient, test_elem: ApiTestElem, app: ASGIApp
):
    run_test(auth_client, test_elem, app)


def test_proposal_title_update(with_db_session):
    # Get the proposal from the DB
    proposals = get_proposals(
        withAuthorization=False,
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
        withAuthorization=False,
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

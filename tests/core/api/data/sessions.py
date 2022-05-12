from tests.core.api.utils.apitest import ApiTestElem, ApiTestExpected, ApiTestInput


test_data_session_list = [
    ApiTestElem(
        name="list own_sessions",
        input=ApiTestInput(
            permissions=[
                "own_sessions",
            ],
            username="pasteur",
            route="/sessions",
        ),
        expected=ApiTestExpected(
            code=200,
            res=[
                {
                    "sessionId": 70565,
                    "expSessionPk": 78889,
                    "beamLineSetupId": 1761425,
                    "proposalId": 9096,
                    "projectCode": None,
                    "BLSession_startDate": "2016-11-22T09:30:00",
                    "BLSession_endDate": "2016-11-23T17:00:00",
                    "beamLineName": "BL01",
                    "scheduled": 1,
                    "nbShifts": 1,
                    "comments": None,
                    "beamLineOperator": "DARWIN C",
                    "visit_number": None,
                    "bltimeStamp": "2022-05-10T07:59:32",
                    "usedFlag": None,
                    "sessionTitle": None,
                    "structureDeterminations": None,
                    "dewarTransport": None,
                    "databackupFrance": None,
                    "databackupEurope": None,
                    "operatorSiteNumber": "91481",
                    "BLSession_lastUpdate": "2016-11-23T17:00:00",
                    "BLSession_protectedData": None,
                    "Proposal_title": "TEST",
                    "Proposal_proposalCode": "MX",
                    "Proposal_ProposalNumber": "1",
                    "Proposal_ProposalType": "MX",
                    "Person_personId": 404290,
                    "Person_familyName": "PASTEUR",
                    "Person_givenName": "Louis",
                    "Person_emailAddress": "test@test.test",
                    "energyScanCount": 0,
                    "sampleCount": 0,
                    "imagesCount": None,
                    "testDataCollectionGroupCount": 0,
                    "dataCollectionGroupCount": 0,
                    "EMdataCollectionGroupCount": 0,
                    "xrfSpectrumCount": 0,
                    "hplcCount": 0,
                    "sampleChangerCount": 0,
                    "calibrationCount": 0,
                    "lastExperimentDataCollectionGroup": None,
                    "lastEndTimeDataCollectionGroup": None,
                },
                {
                    "sessionId": 70566,
                    "expSessionPk": 78888,
                    "beamLineSetupId": 1761426,
                    "proposalId": 9096,
                    "projectCode": None,
                    "BLSession_startDate": "2016-11-23T09:30:00",
                    "BLSession_endDate": "2016-11-23T17:00:00",
                    "beamLineName": "BL01",
                    "scheduled": 1,
                    "nbShifts": 1,
                    "comments": None,
                    "beamLineOperator": "PASTEUR L",
                    "visit_number": None,
                    "bltimeStamp": "2022-05-10T07:59:32",
                    "usedFlag": None,
                    "sessionTitle": None,
                    "structureDeterminations": None,
                    "dewarTransport": None,
                    "databackupFrance": None,
                    "databackupEurope": None,
                    "operatorSiteNumber": "17074",
                    "BLSession_lastUpdate": "2016-11-23T17:00:00",
                    "BLSession_protectedData": None,
                    "Proposal_title": "TEST",
                    "Proposal_proposalCode": "MX",
                    "Proposal_ProposalNumber": "1",
                    "Proposal_ProposalType": "MX",
                    "Person_personId": 404290,
                    "Person_familyName": "PASTEUR",
                    "Person_givenName": "Louis",
                    "Person_emailAddress": "test@test.test",
                    "energyScanCount": 0,
                    "sampleCount": 0,
                    "imagesCount": None,
                    "testDataCollectionGroupCount": 0,
                    "dataCollectionGroupCount": 0,
                    "EMdataCollectionGroupCount": 0,
                    "xrfSpectrumCount": 0,
                    "hplcCount": 0,
                    "sampleChangerCount": 0,
                    "calibrationCount": 0,
                    "lastExperimentDataCollectionGroup": None,
                    "lastEndTimeDataCollectionGroup": None,
                },
                {
                    "sessionId": 70567,
                    "expSessionPk": 56630,
                    "beamLineSetupId": 1761427,
                    "proposalId": 9096,
                    "projectCode": None,
                    "BLSession_startDate": "2016-07-22T09:30:00",
                    "BLSession_endDate": "2016-07-23T08:00:00",
                    "beamLineName": "BL02",
                    "scheduled": 1,
                    "nbShifts": 3,
                    "comments": None,
                    "beamLineOperator": "DARWIN C",
                    "visit_number": None,
                    "bltimeStamp": "2022-05-10T07:59:32",
                    "usedFlag": None,
                    "sessionTitle": None,
                    "structureDeterminations": None,
                    "dewarTransport": None,
                    "databackupFrance": None,
                    "databackupEurope": None,
                    "operatorSiteNumber": "91481",
                    "BLSession_lastUpdate": "2016-07-23T08:00:00",
                    "BLSession_protectedData": None,
                    "Proposal_title": "TEST",
                    "Proposal_proposalCode": "MX",
                    "Proposal_ProposalNumber": "1",
                    "Proposal_ProposalType": "MX",
                    "Person_personId": 404290,
                    "Person_familyName": "PASTEUR",
                    "Person_givenName": "Louis",
                    "Person_emailAddress": "test@test.test",
                    "energyScanCount": 0,
                    "sampleCount": 0,
                    "imagesCount": None,
                    "testDataCollectionGroupCount": 0,
                    "dataCollectionGroupCount": 0,
                    "EMdataCollectionGroupCount": 0,
                    "xrfSpectrumCount": 0,
                    "hplcCount": 0,
                    "sampleChangerCount": 0,
                    "calibrationCount": 0,
                    "lastExperimentDataCollectionGroup": None,
                    "lastEndTimeDataCollectionGroup": None,
                },
                {
                    "sessionId": 70568,
                    "expSessionPk": 79910,
                    "beamLineSetupId": 1761428,
                    "proposalId": 9096,
                    "projectCode": None,
                    "BLSession_startDate": "2017-05-12T09:30:00",
                    "BLSession_endDate": "2017-05-13T08:00:00",
                    "beamLineName": "BL01",
                    "scheduled": 1,
                    "nbShifts": 3,
                    "comments": None,
                    "beamLineOperator": "PASTEUR L",
                    "visit_number": None,
                    "bltimeStamp": "2022-05-10T07:59:32",
                    "usedFlag": None,
                    "sessionTitle": None,
                    "structureDeterminations": None,
                    "dewarTransport": None,
                    "databackupFrance": None,
                    "databackupEurope": None,
                    "operatorSiteNumber": "17074",
                    "BLSession_lastUpdate": "2017-05-13T08:00:00",
                    "BLSession_protectedData": None,
                    "Proposal_title": "TEST",
                    "Proposal_proposalCode": "MX",
                    "Proposal_ProposalNumber": "1",
                    "Proposal_ProposalType": "MX",
                    "Person_personId": 404290,
                    "Person_familyName": "PASTEUR",
                    "Person_givenName": "Louis",
                    "Person_emailAddress": "test@test.test",
                    "energyScanCount": 0,
                    "sampleCount": 0,
                    "imagesCount": None,
                    "testDataCollectionGroupCount": 0,
                    "dataCollectionGroupCount": 0,
                    "EMdataCollectionGroupCount": 0,
                    "xrfSpectrumCount": 0,
                    "hplcCount": 0,
                    "sampleChangerCount": 0,
                    "calibrationCount": 0,
                    "lastExperimentDataCollectionGroup": None,
                    "lastEndTimeDataCollectionGroup": None,
                },
            ],
        ),
    ),
    ApiTestElem(
        name="empty list own_sessions",
        input=ApiTestInput(
            permissions=[
                "own_sessions",
            ],
            username="i_dont_have_sessions",
            route="/sessions",
        ),
        expected=ApiTestExpected(code=200, res=[]),
    ),
]


test_data_session_dates_list = [
    ApiTestElem(
        name="list own_sessions",
        input=ApiTestInput(
            permissions=[
                "own_sessions",
            ],
            username="pasteur",
            route="/sessions/date/20170512/20170513",
        ),
        expected=ApiTestExpected(
            code=200,
            res=[
                {
                    "sessionId": 70568,
                    "expSessionPk": 79910,
                    "beamLineSetupId": 1761428,
                    "proposalId": 9096,
                    "projectCode": None,
                    "BLSession_startDate": "2017-05-12T09:30:00",
                    "BLSession_endDate": "2017-05-13T08:00:00",
                    "beamLineName": "BL01",
                    "scheduled": 1,
                    "nbShifts": 3,
                    "comments": None,
                    "beamLineOperator": "PASTEUR L",
                    "visit_number": None,
                    "bltimeStamp": "2022-05-10T07:59:32",
                    "usedFlag": None,
                    "sessionTitle": None,
                    "structureDeterminations": None,
                    "dewarTransport": None,
                    "databackupFrance": None,
                    "databackupEurope": None,
                    "operatorSiteNumber": "17074",
                    "BLSession_lastUpdate": "2017-05-13T08:00:00",
                    "BLSession_protectedData": None,
                    "Proposal_title": "TEST",
                    "Proposal_proposalCode": "MX",
                    "Proposal_ProposalNumber": "1",
                    "Proposal_ProposalType": "MX",
                    "Person_personId": 404290,
                    "Person_familyName": "PASTEUR",
                    "Person_givenName": "Louis",
                    "Person_emailAddress": "test@test.test",
                    "energyScanCount": 0,
                    "sampleCount": 0,
                    "imagesCount": None,
                    "testDataCollectionGroupCount": 0,
                    "dataCollectionGroupCount": 0,
                    "EMdataCollectionGroupCount": 0,
                    "xrfSpectrumCount": 0,
                    "hplcCount": 0,
                    "sampleChangerCount": 0,
                    "calibrationCount": 0,
                    "lastExperimentDataCollectionGroup": None,
                    "lastEndTimeDataCollectionGroup": None,
                },
            ],
        ),
    ),
    ApiTestElem(
        name="empty list own_sessions",
        input=ApiTestInput(
            permissions=[
                "own_sessions",
            ],
            username="pasteur",
            route="/sessions/date/20000101/20000102",
        ),
        expected=ApiTestExpected(code=200, res=[]),
    ),
    ApiTestElem(
        name="list all_sessions",
        input=ApiTestInput(
            permissions=[
                "all_sessions",
            ],
            username="johndoe",
            route="/sessions/date/20170512/20170513",
        ),
        expected=ApiTestExpected(
            code=200,
            res=[
                {
                    "sessionId": 70568,
                    "expSessionPk": 79910,
                    "beamLineSetupId": 1761428,
                    "proposalId": 9096,
                    "projectCode": None,
                    "BLSession_startDate": "2017-05-12T09:30:00",
                    "BLSession_endDate": "2017-05-13T08:00:00",
                    "beamLineName": "BL01",
                    "scheduled": 1,
                    "nbShifts": 3,
                    "comments": None,
                    "beamLineOperator": "PASTEUR L",
                    "visit_number": None,
                    "bltimeStamp": "2022-05-10T07:59:32",
                    "usedFlag": None,
                    "sessionTitle": None,
                    "structureDeterminations": None,
                    "dewarTransport": None,
                    "databackupFrance": None,
                    "databackupEurope": None,
                    "operatorSiteNumber": "17074",
                    "BLSession_lastUpdate": "2017-05-13T08:00:00",
                    "BLSession_protectedData": None,
                    "Proposal_title": "TEST",
                    "Proposal_proposalCode": "MX",
                    "Proposal_ProposalNumber": "1",
                    "Proposal_ProposalType": "MX",
                    "Person_personId": 404290,
                    "Person_familyName": "PASTEUR",
                    "Person_givenName": "Louis",
                    "Person_emailAddress": "test@test.test",
                    "energyScanCount": 0,
                    "sampleCount": 0,
                    "imagesCount": None,
                    "testDataCollectionGroupCount": 0,
                    "dataCollectionGroupCount": 0,
                    "EMdataCollectionGroupCount": 0,
                    "xrfSpectrumCount": 0,
                    "hplcCount": 0,
                    "sampleChangerCount": 0,
                    "calibrationCount": 0,
                    "lastExperimentDataCollectionGroup": None,
                    "lastEndTimeDataCollectionGroup": None,
                },
            ],
        ),
    ),
]


test_data_session_proposal_list = [
    ApiTestElem(
        name="list own_sessions name",
        input=ApiTestInput(
            permissions=[
                "own_sessions",
            ],
            username="pasteur",
            route="/sessions/proposal/MX1",
        ),
        expected=ApiTestExpected(
            code=200,
            res=[
                {
                    "sessionId": 70565,
                    "expSessionPk": 78889,
                    "beamLineSetupId": 1761425,
                    "proposalId": 9096,
                    "projectCode": None,
                    "BLSession_startDate": "2016-11-22T09:30:00",
                    "BLSession_endDate": "2016-11-23T17:00:00",
                    "beamLineName": "BL01",
                    "scheduled": 1,
                    "nbShifts": 1,
                    "comments": None,
                    "beamLineOperator": "DARWIN C",
                    "visit_number": None,
                    "bltimeStamp": "2022-05-10T07:59:32",
                    "usedFlag": None,
                    "sessionTitle": None,
                    "structureDeterminations": None,
                    "dewarTransport": None,
                    "databackupFrance": None,
                    "databackupEurope": None,
                    "operatorSiteNumber": "91481",
                    "BLSession_lastUpdate": "2016-11-23T17:00:00",
                    "BLSession_protectedData": None,
                    "Proposal_title": "TEST",
                    "Proposal_proposalCode": "MX",
                    "Proposal_ProposalNumber": "1",
                    "Proposal_ProposalType": "MX",
                    "Person_personId": 404290,
                    "Person_familyName": "PASTEUR",
                    "Person_givenName": "Louis",
                    "Person_emailAddress": "test@test.test",
                    "energyScanCount": 0,
                    "sampleCount": 0,
                    "imagesCount": None,
                    "testDataCollectionGroupCount": 0,
                    "dataCollectionGroupCount": 0,
                    "EMdataCollectionGroupCount": 0,
                    "xrfSpectrumCount": 0,
                    "hplcCount": 0,
                    "sampleChangerCount": 0,
                    "calibrationCount": 0,
                    "lastExperimentDataCollectionGroup": None,
                    "lastEndTimeDataCollectionGroup": None,
                },
                {
                    "sessionId": 70566,
                    "expSessionPk": 78888,
                    "beamLineSetupId": 1761426,
                    "proposalId": 9096,
                    "projectCode": None,
                    "BLSession_startDate": "2016-11-23T09:30:00",
                    "BLSession_endDate": "2016-11-23T17:00:00",
                    "beamLineName": "BL01",
                    "scheduled": 1,
                    "nbShifts": 1,
                    "comments": None,
                    "beamLineOperator": "PASTEUR L",
                    "visit_number": None,
                    "bltimeStamp": "2022-05-10T07:59:32",
                    "usedFlag": None,
                    "sessionTitle": None,
                    "structureDeterminations": None,
                    "dewarTransport": None,
                    "databackupFrance": None,
                    "databackupEurope": None,
                    "operatorSiteNumber": "17074",
                    "BLSession_lastUpdate": "2016-11-23T17:00:00",
                    "BLSession_protectedData": None,
                    "Proposal_title": "TEST",
                    "Proposal_proposalCode": "MX",
                    "Proposal_ProposalNumber": "1",
                    "Proposal_ProposalType": "MX",
                    "Person_personId": 404290,
                    "Person_familyName": "PASTEUR",
                    "Person_givenName": "Louis",
                    "Person_emailAddress": "test@test.test",
                    "energyScanCount": 0,
                    "sampleCount": 0,
                    "imagesCount": None,
                    "testDataCollectionGroupCount": 0,
                    "dataCollectionGroupCount": 0,
                    "EMdataCollectionGroupCount": 0,
                    "xrfSpectrumCount": 0,
                    "hplcCount": 0,
                    "sampleChangerCount": 0,
                    "calibrationCount": 0,
                    "lastExperimentDataCollectionGroup": None,
                    "lastEndTimeDataCollectionGroup": None,
                },
                {
                    "sessionId": 70567,
                    "expSessionPk": 56630,
                    "beamLineSetupId": 1761427,
                    "proposalId": 9096,
                    "projectCode": None,
                    "BLSession_startDate": "2016-07-22T09:30:00",
                    "BLSession_endDate": "2016-07-23T08:00:00",
                    "beamLineName": "BL02",
                    "scheduled": 1,
                    "nbShifts": 3,
                    "comments": None,
                    "beamLineOperator": "DARWIN C",
                    "visit_number": None,
                    "bltimeStamp": "2022-05-10T07:59:32",
                    "usedFlag": None,
                    "sessionTitle": None,
                    "structureDeterminations": None,
                    "dewarTransport": None,
                    "databackupFrance": None,
                    "databackupEurope": None,
                    "operatorSiteNumber": "91481",
                    "BLSession_lastUpdate": "2016-07-23T08:00:00",
                    "BLSession_protectedData": None,
                    "Proposal_title": "TEST",
                    "Proposal_proposalCode": "MX",
                    "Proposal_ProposalNumber": "1",
                    "Proposal_ProposalType": "MX",
                    "Person_personId": 404290,
                    "Person_familyName": "PASTEUR",
                    "Person_givenName": "Louis",
                    "Person_emailAddress": "test@test.test",
                    "energyScanCount": 0,
                    "sampleCount": 0,
                    "imagesCount": None,
                    "testDataCollectionGroupCount": 0,
                    "dataCollectionGroupCount": 0,
                    "EMdataCollectionGroupCount": 0,
                    "xrfSpectrumCount": 0,
                    "hplcCount": 0,
                    "sampleChangerCount": 0,
                    "calibrationCount": 0,
                    "lastExperimentDataCollectionGroup": None,
                    "lastEndTimeDataCollectionGroup": None,
                },
                {
                    "sessionId": 70568,
                    "expSessionPk": 79910,
                    "beamLineSetupId": 1761428,
                    "proposalId": 9096,
                    "projectCode": None,
                    "BLSession_startDate": "2017-05-12T09:30:00",
                    "BLSession_endDate": "2017-05-13T08:00:00",
                    "beamLineName": "BL01",
                    "scheduled": 1,
                    "nbShifts": 3,
                    "comments": None,
                    "beamLineOperator": "PASTEUR L",
                    "visit_number": None,
                    "bltimeStamp": "2022-05-10T07:59:32",
                    "usedFlag": None,
                    "sessionTitle": None,
                    "structureDeterminations": None,
                    "dewarTransport": None,
                    "databackupFrance": None,
                    "databackupEurope": None,
                    "operatorSiteNumber": "17074",
                    "BLSession_lastUpdate": "2017-05-13T08:00:00",
                    "BLSession_protectedData": None,
                    "Proposal_title": "TEST",
                    "Proposal_proposalCode": "MX",
                    "Proposal_ProposalNumber": "1",
                    "Proposal_ProposalType": "MX",
                    "Person_personId": 404290,
                    "Person_familyName": "PASTEUR",
                    "Person_givenName": "Louis",
                    "Person_emailAddress": "test@test.test",
                    "energyScanCount": 0,
                    "sampleCount": 0,
                    "imagesCount": None,
                    "testDataCollectionGroupCount": 0,
                    "dataCollectionGroupCount": 0,
                    "EMdataCollectionGroupCount": 0,
                    "xrfSpectrumCount": 0,
                    "hplcCount": 0,
                    "sampleChangerCount": 0,
                    "calibrationCount": 0,
                    "lastExperimentDataCollectionGroup": None,
                    "lastEndTimeDataCollectionGroup": None,
                },
            ],
        ),
    ),
    ApiTestElem(
        name="list own_sessions id",
        input=ApiTestInput(
            permissions=[
                "own_sessions",
            ],
            username="pasteur",
            route="/sessions/proposal/9096",
        ),
        expected=ApiTestExpected(
            code=200,
            res=[
                {
                    "sessionId": 70565,
                    "expSessionPk": 78889,
                    "beamLineSetupId": 1761425,
                    "proposalId": 9096,
                    "projectCode": None,
                    "BLSession_startDate": "2016-11-22T09:30:00",
                    "BLSession_endDate": "2016-11-23T17:00:00",
                    "beamLineName": "BL01",
                    "scheduled": 1,
                    "nbShifts": 1,
                    "comments": None,
                    "beamLineOperator": "DARWIN C",
                    "visit_number": None,
                    "bltimeStamp": "2022-05-10T07:59:32",
                    "usedFlag": None,
                    "sessionTitle": None,
                    "structureDeterminations": None,
                    "dewarTransport": None,
                    "databackupFrance": None,
                    "databackupEurope": None,
                    "operatorSiteNumber": "91481",
                    "BLSession_lastUpdate": "2016-11-23T17:00:00",
                    "BLSession_protectedData": None,
                    "Proposal_title": "TEST",
                    "Proposal_proposalCode": "MX",
                    "Proposal_ProposalNumber": "1",
                    "Proposal_ProposalType": "MX",
                    "Person_personId": 404290,
                    "Person_familyName": "PASTEUR",
                    "Person_givenName": "Louis",
                    "Person_emailAddress": "test@test.test",
                    "energyScanCount": 0,
                    "sampleCount": 0,
                    "imagesCount": None,
                    "testDataCollectionGroupCount": 0,
                    "dataCollectionGroupCount": 0,
                    "EMdataCollectionGroupCount": 0,
                    "xrfSpectrumCount": 0,
                    "hplcCount": 0,
                    "sampleChangerCount": 0,
                    "calibrationCount": 0,
                    "lastExperimentDataCollectionGroup": None,
                    "lastEndTimeDataCollectionGroup": None,
                },
                {
                    "sessionId": 70566,
                    "expSessionPk": 78888,
                    "beamLineSetupId": 1761426,
                    "proposalId": 9096,
                    "projectCode": None,
                    "BLSession_startDate": "2016-11-23T09:30:00",
                    "BLSession_endDate": "2016-11-23T17:00:00",
                    "beamLineName": "BL01",
                    "scheduled": 1,
                    "nbShifts": 1,
                    "comments": None,
                    "beamLineOperator": "PASTEUR L",
                    "visit_number": None,
                    "bltimeStamp": "2022-05-10T07:59:32",
                    "usedFlag": None,
                    "sessionTitle": None,
                    "structureDeterminations": None,
                    "dewarTransport": None,
                    "databackupFrance": None,
                    "databackupEurope": None,
                    "operatorSiteNumber": "17074",
                    "BLSession_lastUpdate": "2016-11-23T17:00:00",
                    "BLSession_protectedData": None,
                    "Proposal_title": "TEST",
                    "Proposal_proposalCode": "MX",
                    "Proposal_ProposalNumber": "1",
                    "Proposal_ProposalType": "MX",
                    "Person_personId": 404290,
                    "Person_familyName": "PASTEUR",
                    "Person_givenName": "Louis",
                    "Person_emailAddress": "test@test.test",
                    "energyScanCount": 0,
                    "sampleCount": 0,
                    "imagesCount": None,
                    "testDataCollectionGroupCount": 0,
                    "dataCollectionGroupCount": 0,
                    "EMdataCollectionGroupCount": 0,
                    "xrfSpectrumCount": 0,
                    "hplcCount": 0,
                    "sampleChangerCount": 0,
                    "calibrationCount": 0,
                    "lastExperimentDataCollectionGroup": None,
                    "lastEndTimeDataCollectionGroup": None,
                },
                {
                    "sessionId": 70567,
                    "expSessionPk": 56630,
                    "beamLineSetupId": 1761427,
                    "proposalId": 9096,
                    "projectCode": None,
                    "BLSession_startDate": "2016-07-22T09:30:00",
                    "BLSession_endDate": "2016-07-23T08:00:00",
                    "beamLineName": "BL02",
                    "scheduled": 1,
                    "nbShifts": 3,
                    "comments": None,
                    "beamLineOperator": "DARWIN C",
                    "visit_number": None,
                    "bltimeStamp": "2022-05-10T07:59:32",
                    "usedFlag": None,
                    "sessionTitle": None,
                    "structureDeterminations": None,
                    "dewarTransport": None,
                    "databackupFrance": None,
                    "databackupEurope": None,
                    "operatorSiteNumber": "91481",
                    "BLSession_lastUpdate": "2016-07-23T08:00:00",
                    "BLSession_protectedData": None,
                    "Proposal_title": "TEST",
                    "Proposal_proposalCode": "MX",
                    "Proposal_ProposalNumber": "1",
                    "Proposal_ProposalType": "MX",
                    "Person_personId": 404290,
                    "Person_familyName": "PASTEUR",
                    "Person_givenName": "Louis",
                    "Person_emailAddress": "test@test.test",
                    "energyScanCount": 0,
                    "sampleCount": 0,
                    "imagesCount": None,
                    "testDataCollectionGroupCount": 0,
                    "dataCollectionGroupCount": 0,
                    "EMdataCollectionGroupCount": 0,
                    "xrfSpectrumCount": 0,
                    "hplcCount": 0,
                    "sampleChangerCount": 0,
                    "calibrationCount": 0,
                    "lastExperimentDataCollectionGroup": None,
                    "lastEndTimeDataCollectionGroup": None,
                },
                {
                    "sessionId": 70568,
                    "expSessionPk": 79910,
                    "beamLineSetupId": 1761428,
                    "proposalId": 9096,
                    "projectCode": None,
                    "BLSession_startDate": "2017-05-12T09:30:00",
                    "BLSession_endDate": "2017-05-13T08:00:00",
                    "beamLineName": "BL01",
                    "scheduled": 1,
                    "nbShifts": 3,
                    "comments": None,
                    "beamLineOperator": "PASTEUR L",
                    "visit_number": None,
                    "bltimeStamp": "2022-05-10T07:59:32",
                    "usedFlag": None,
                    "sessionTitle": None,
                    "structureDeterminations": None,
                    "dewarTransport": None,
                    "databackupFrance": None,
                    "databackupEurope": None,
                    "operatorSiteNumber": "17074",
                    "BLSession_lastUpdate": "2017-05-13T08:00:00",
                    "BLSession_protectedData": None,
                    "Proposal_title": "TEST",
                    "Proposal_proposalCode": "MX",
                    "Proposal_ProposalNumber": "1",
                    "Proposal_ProposalType": "MX",
                    "Person_personId": 404290,
                    "Person_familyName": "PASTEUR",
                    "Person_givenName": "Louis",
                    "Person_emailAddress": "test@test.test",
                    "energyScanCount": 0,
                    "sampleCount": 0,
                    "imagesCount": None,
                    "testDataCollectionGroupCount": 0,
                    "dataCollectionGroupCount": 0,
                    "EMdataCollectionGroupCount": 0,
                    "xrfSpectrumCount": 0,
                    "hplcCount": 0,
                    "sampleChangerCount": 0,
                    "calibrationCount": 0,
                    "lastExperimentDataCollectionGroup": None,
                    "lastEndTimeDataCollectionGroup": None,
                },
            ],
        ),
    ),
    ApiTestElem(
        name="list own_sessions empty",
        input=ApiTestInput(
            permissions=[
                "own_sessions",
            ],
            username="johndoe",
            route="/sessions/proposal/MX1",
        ),
        expected=ApiTestExpected(code=200, res=[]),
    ),
    ApiTestElem(
        name="no rights",
        input=ApiTestInput(
            permissions=[
                "none",
            ],
            username="pasteur",
            route="/sessions/proposal/MX1",
        ),
        expected=ApiTestExpected(
            code=401,
            res={
                "detail": "User pasteur (permissions assigned: ['none']) has no appropriate permission (any: ['own_sessions', 'all_sessions'])  to execute method."
            },
        ),
    ),
    ApiTestElem(
        name="list proposal does not exist",
        input=ApiTestInput(
            permissions=[
                "own_sessions",
            ],
            username="pasteur",
            route="/sessions/proposal/UNKN",
        ),
        expected=ApiTestExpected(code=200, res=[]),
    ),
]

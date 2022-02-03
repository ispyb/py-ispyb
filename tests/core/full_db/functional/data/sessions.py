test_data_session_list = [
    {
        "name": "list own_sessions",
        "input": {
            "permissions": [
                "own_sessions",
            ],
            "username":"konstanti1108",
            "route":"/sessions"
        },
        "expected":{
            "code": 200,
            "res": [{'sessionId': 61547, 'expSessionPk': 84291, 'beamLineSetupId': 1515410, 'proposalId': 8319, 'projectCode': None, 'BLSession_startDate': '2018-04-23T09:30:00', 'BLSession_endDate': '2018-04-27T08:00:00', 'beamLineName': 'CM01', 'scheduled': 1, 'nbShifts': 9, 'comments': None, 'beamLineOperator': 'HONS  M', 'visit_number': None, 'bltimeStamp': '2018-02-28T10:27:11', 'usedFlag': 1, 'sessionTitle': None, 'structureDeterminations': None, 'dewarTransport': None, 'databackupFrance': None, 'databackupEurope': None, 'operatorSiteNumber': '318226', 'BLSession_lastUpdate': '2018-04-27T06:00:00', 'BLSession_protectedData': None, 'Proposal_title': 'Cryo-EM structural studies of a potential bioscavenger and detoxification biocatalysts - human butyrylcholinesterase in its native tetrameri', 'Proposal_proposalCode': 'MX', 'Proposal_ProposalNumber': '2007', 'Proposal_ProposalType': 'MX', 'Person_personId': 391402, 'Person_familyName': 'BOYKO', 'Person_givenName': 'Konstantin', 'Person_emailAddress': 'kmb@inbi.ras.ru', 'energyScanCount': 0, 'sampleCount': 1, 'imagesCount': 152.0, 'testDataCollectionGroupCount': 0, 'dataCollectionGroupCount': 5, 'EMdataCollectionGroupCount': 5, 'xrfSpectrumCount': 0, 'hplcCount': 0, 'sampleChangerCount': 0, 'calibrationCount': 0, 'lastExperimentDataCollectionGroup': 'EM', 'lastEndTimeDataCollectionGroup': None}, {'sessionId': 67132, 'expSessionPk': 89472, 'beamLineSetupId': 1758042, 'proposalId': 9007, 'projectCode': None, 'BLSession_startDate': '2019-11-15T09:30:00', 'BLSession_endDate': '2019-11-18T08:00:00', 'beamLineName': 'CM01', 'scheduled': 1, 'nbShifts': 9, 'comments': None, 'beamLineOperator': 'HONS  M', 'visit_number': None, 'bltimeStamp': '2019-10-09T02:10:21', 'usedFlag': None, 'sessionTitle': None, 'structureDeterminations': None, 'dewarTransport': None, 'databackupFrance': None, 'databackupEurope': None, 'operatorSiteNumber': '318226', 'BLSession_lastUpdate': '2019-11-18T07:00:00', 'BLSession_protectedData': None, 'Proposal_title': 'Structural studies of the helicase/primase complex from Herpes simplex virus', 'Proposal_proposalCode': 'MX', 'Proposal_ProposalNumber': '2230', 'Proposal_ProposalType': 'MX', 'Person_personId': 391402, 'Person_familyName': 'BOYKO', 'Person_givenName': 'Konstantin', 'Person_emailAddress': 'kmb@inbi.ras.ru', 'energyScanCount': 0, 'sampleCount': 0, 'imagesCount': None, 'testDataCollectionGroupCount': 0, 'dataCollectionGroupCount': 0, 'EMdataCollectionGroupCount': 0, 'xrfSpectrumCount': 0, 'hplcCount': 0, 'sampleChangerCount': 0, 'calibrationCount': 0, 'lastExperimentDataCollectionGroup': None, 'lastEndTimeDataCollectionGroup': None}]
        }
    },
    {
        "name": "empty list own_sessions",
        "input": {
                "permissions": [
                    "own_sessions",
                ],
            "username":"gaonach",
            "route":"/sessions"
        },
        "expected":{
            "code": 200,
            "res": []
        }
    }
]

test_data_session_dates_list = [
    {
        "name": "list own_sessions",
        "input": {
            "permissions": [
                "own_sessions",
            ],
            "username":"konstanti1108",
            "route":"/sessions/date/20180101/20181231"
        },
        "expected":{
            "code": 200,
            "res": [{'sessionId': 61547, 'expSessionPk': 84291, 'beamLineSetupId': 1515410, 'proposalId': 8319, 'projectCode': None, 'BLSession_startDate': '2018-04-23T09:30:00', 'BLSession_endDate': '2018-04-27T08:00:00', 'beamLineName': 'CM01', 'scheduled': 1, 'nbShifts': 9, 'comments': None, 'beamLineOperator': 'HONS  M', 'visit_number': None, 'bltimeStamp': '2018-02-28T10:27:11', 'usedFlag': 1, 'sessionTitle': None, 'structureDeterminations': None, 'dewarTransport': None, 'databackupFrance': None, 'databackupEurope': None, 'operatorSiteNumber': '318226', 'BLSession_lastUpdate': '2018-04-27T06:00:00', 'BLSession_protectedData': None, 'Proposal_title': 'Cryo-EM structural studies of a potential bioscavenger and detoxification biocatalysts - human butyrylcholinesterase in its native tetrameri', 'Proposal_proposalCode': 'MX', 'Proposal_ProposalNumber': '2007', 'Proposal_ProposalType': 'MX', 'Person_personId': 391402, 'Person_familyName': 'BOYKO', 'Person_givenName': 'Konstantin', 'Person_emailAddress': 'kmb@inbi.ras.ru', 'energyScanCount': 0, 'sampleCount': 1, 'imagesCount': 152.0, 'testDataCollectionGroupCount': 0, 'dataCollectionGroupCount': 5, 'EMdataCollectionGroupCount': 5, 'xrfSpectrumCount': 0, 'hplcCount': 0, 'sampleChangerCount': 0, 'calibrationCount': 0, 'lastExperimentDataCollectionGroup': 'EM', 'lastEndTimeDataCollectionGroup': None}]
        }
    },
    {
        "name": "empty list own_sessions",
        "input": {
                "permissions": [
                    "own_sessions",
                ],
            "username":"konstanti1108",
            "route":"/sessions/date/20180101/20180109"
        },
        "expected":{
            "code": 200,
            "res": []
        }
    },
    {
        "name": "list all_sessions",
        "input": {
                "permissions": [
                    "all_sessions",
                ],
            "username":"konstanti1108",
            "route":"/sessions/date/20180101/20180109"
        },
        "expected":{
            "code": 200,
            "res": [{'sessionId': 60984, 'expSessionPk': None, 'beamLineSetupId': None, 'proposalId': 1170, 'projectCode': None, 'BLSession_startDate': '2018-01-08T23:00:00', 'BLSession_endDate': '2018-01-10T06:59:59', 'beamLineName': 'ID30A-2', 'scheduled': 0, 'nbShifts': 3, 'comments': 'Session created by the BCM', 'beamLineOperator': None, 'visit_number': None, 'bltimeStamp': '2018-01-09T13:41:48', 'usedFlag': None, 'sessionTitle': None, 'structureDeterminations': None, 'dewarTransport': None, 'databackupFrance': None, 'databackupEurope': None, 'operatorSiteNumber': None, 'BLSession_lastUpdate': '2018-01-10T05:59:59', 'BLSession_protectedData': "not a MX-style directory '20180108' (missing RAW_DATA)", 'Proposal_title': 'TEST', 'Proposal_proposalCode': 'MX', 'Proposal_ProposalNumber': '415', 'Proposal_ProposalType': 'MX', 'Person_personId': 403748, 'Person_familyName': 'MALBET MONACO', 'Person_givenName': 'Stephanie', 'Person_emailAddress': 'monaco@esrf.fr', 'energyScanCount': 0, 'sampleCount': 0, 'imagesCount': None, 'testDataCollectionGroupCount': 0, 'dataCollectionGroupCount': 0, 'EMdataCollectionGroupCount': 0, 'xrfSpectrumCount': 0, 'hplcCount': 0, 'sampleChangerCount': 0, 'calibrationCount': 0, 'lastExperimentDataCollectionGroup': None, 'lastEndTimeDataCollectionGroup': None}, {'sessionId': 60954, 'expSessionPk': None, 'beamLineSetupId': None, 'proposalId': 7, 'projectCode': None, 'BLSession_startDate': '2018-01-09T00:00:00', 'BLSession_endDate': '2018-01-10T07:59:59', 'beamLineName': 'ID29', 'scheduled': 0, 'nbShifts': 3, 'comments': 'Session created by the BCM', 'beamLineOperator': None, 'visit_number': None, 'bltimeStamp': '2018-01-09T08:22:42', 'usedFlag': None, 'sessionTitle': None, 'structureDeterminations': None, 'dewarTransport': None, 'databackupFrance': None, 'databackupEurope': None, 'operatorSiteNumber': None, 'BLSession_lastUpdate': '2018-01-10T06:59:59', 'BLSession_protectedData': None, 'Proposal_title': 'operator on ID29eh1', 'Proposal_proposalCode': 'OPID', 'Proposal_ProposalNumber': '291', 'Proposal_ProposalType': 'MX', 'Person_personId': 7, 'Person_familyName': 'operator on ID29', 'Person_givenName': None, 'Person_emailAddress': None, 'energyScanCount': 0, 'sampleCount': 0, 'imagesCount': None, 'testDataCollectionGroupCount': 0, 'dataCollectionGroupCount': 0, 'EMdataCollectionGroupCount': 0, 'xrfSpectrumCount': 0, 'hplcCount': 0, 'sampleChangerCount': 0, 'calibrationCount': 0, 'lastExperimentDataCollectionGroup': None, 'lastEndTimeDataCollectionGroup': None}]
        }
    }
]

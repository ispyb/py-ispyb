test_data_proposal_userportalsync = {
    "proposal": {
        "title": "Proposal title",
        "proposalCode": "I",
        "proposalNumber": "234444",
        "proposalType": "MX",
        "persons": [
            {
                "givenName": "Amity",
                "familyName": "Weaver",
                "title": "Dr.",
                "siteId": 157,
                "login": "aewaver",
                "emailAddress": "test@test.test",
                "laboratory": {
                    "name": "DESY",
                    "city": "HAMBURG",
                    "country": "DE",
                    "address": "Notkestr. 85\n22706",
                    "laboratoryExtPk": 1,
                },
            },
            {
                "givenName": "Kirk",
                "familyName": "Chambers",
                "siteId": 158,
                "login": "kchambers",
                "emailAddress": "test@test.test",
                "laboratory": {
                    "name": "Lab0",
                    "city": "GRENOBLE",
                    "country": "FR",
                    "address": "71 avenue des Martyrs\nCS 40220\n38043\n",
                },
            },
            {
                "givenName": "Sherri",
                "familyName": "Quinlan",
                "siteId": 159,
                "login": "squinlan",
                "emailAddress": "test@test.test",
                "laboratory": {
                    "name": "ALBA",
                    "city": "BARCELONA",
                    "country": "ES",
                    "address": "Carrer de la Llum 2-26.\n 08290\n Cerdanyola del Valles",
                    "laboratoryExtPk": 2,
                },
            },
        ],
    },
    "sessions": [
        {
            "expSessionPk": 23458,
            "startDate": "2022-05-20T14:09:20.340Z",
            "endDate": "2022-05-21T14:09:20.340Z",
            "beamLineName": "P11",
            "scheduled": 1,
            "nbShifts": 2,
            "comments": "Testing a session import",
            "beamLineOperator": "Kaye Wiley",
            "visit_number": 0,
            "usedFlag": 0,
            "sessionTitle": "Session 1 user portal sync",
            "structureDeterminations": 0,
            "dewarTransport": 0,
            "databackupFrance": 0,
            "databackupEurope": 0,
            "operatorSiteNumber": "234",
            "nbReimbDewars": 0,
            "persons": [
                {
                    "givenName": "Saim",
                    "familyName": "Gross",
                    "siteId": 160,
                    "login": "sgross",
                    "emailAddress": "test@test.test",
                    "laboratory": {
                        "name": "DESY",
                        "city": "HAMBURG",
                        "country": "DE",
                        "address": "Notkestr. 85\n22706",
                        "laboratoryExtPk": 1,
                    },
                    "session_options": {"role": "Local Contact", "remote": 0},
                },
                {
                    "givenName": "Jaspal",
                    "familyName": "Bernal",
                    "siteId": 161,
                    "login": "jbernal",
                    "title": "Dr.",
                    "phoneNumber": "+123456789",
                    "emailAddress": "test@test.test",
                    "laboratory": {
                        "name": "DESY",
                        "city": "HAMBURG",
                        "country": "DE",
                        "address": "Notkestr. 85\n22706",
                        "laboratoryExtPk": 1,
                    },
                    "session_options": {"role": "Principal Investigator", "remote": 1},
                },
            ],
        },
        {
            "expSessionPk": 23459,
            "startDate": "2022-06-20T16:09:20.340Z",
            "endDate": "2022-06-21T16:09:20.340Z",
            "beamLineName": "P11",
            "scheduled": 1,
            "nbShifts": 2,
            "comments": "Testing a second session import",
            "beamLineOperator": "Kaye Wiley",
            "visit_number": 0,
            "usedFlag": 0,
            "sessionTitle": "Session 2 user portal sync",
            "structureDeterminations": 0,
            "dewarTransport": 0,
            "databackupFrance": 0,
            "databackupEurope": 0,
            "operatorSiteNumber": "235",
            "nbReimbDewars": 0,
            "persons": [
                {
                    "givenName": "Saim",
                    "familyName": "Gross",
                    "siteId": 160,
                    "login": "sgross",
                    "emailAddress": "test@test.test",
                    "laboratory": {
                        "name": "DESY",
                        "city": "HAMBURG",
                        "country": "DE",
                        "address": "Notkestr. 85\n22706",
                        "laboratoryExtPk": 1,
                    },
                    "session_options": {"role": "Local Contact", "remote": 0},
                },
                {
                    "givenName": "Jaspal",
                    "familyName": "Bernal",
                    "siteId": 161,
                    "login": "jbernal",
                    "title": "Dr.",
                    "phoneNumber": "+123456789",
                    "emailAddress": "test@test.test",
                    "laboratory": {
                        "name": "DESY",
                        "city": "HAMBURG",
                        "country": "DE",
                        "address": "Notkestr. 85\n22706",
                        "laboratoryExtPk": 1,
                    },
                    "session_options": {"role": "Principal Investigator", "remote": 1},
                },
            ],
        },
    ],
    "proteins": [
        {
            "name": "Peralosyde Ratrei",
            "acronym": "P4R2",
            "hazardGroup": 1,
            "containmentLevel": 1,
            "person": {
                "givenName": "Amity",
                "familyName": "Weaver",
                "siteId": 157,
                "login": "aweaver",
                "emailAddress": "test@test.test",
                "laboratory": {
                    "name": "DESY",
                    "city": "HAMBURG",
                    "country": "DE",
                    "address": "Notkestr. 85\n22706",
                    "laboratoryExtPk": 1,
                },
            },
        }
    ],
}

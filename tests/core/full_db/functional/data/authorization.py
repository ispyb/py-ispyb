test_data_session = [
    {
        "name": "all_sessions permission OK",
        "input": {
            "permissions": [
                "all_sessions",
            ],
            "username":"admin",
            "route":"/em/session/4583/stats"
        },
        "expected":{
            "code": 200
        }
    },
    {
        "name": "no all_sessions permission DENIED",
        "input": {
            "permissions": [
                "none"
            ],
            "username":"admin",
            "route":"/em/session/4583/stats"
        },
        "expected":{
            "code": 401
        }
    },
    {
        "name": "own_sessions permission OK (proposal.personId)",
        "input": {
            "permissions": [
                "own_sessions",
            ],
            "username":"DI MARCO",
            "route":"/em/session/4583/stats"
        },
        "expected":{
            "code": 200
        }
    },
    {
        "name": "no own_sessions permission DENIED (proposal.personId)",
        "input": {
            "permissions": [
                "none"
            ],
            "username":"DI MARCO",
            "route":"/em/session/4583/stats"
        },
        "expected":{
            "code": 401
        }
    },
    {
        "name": "own_sessions permission OK (Session_has_Person.personId)",
        "input": {
            "permissions": [
                "own_sessions",
            ],
            "username":"SERRE",
            "route":"/em/session/8569/stats"
        },
        "expected":{
            "code": 200
        }
    },
    {
        "name": "no own_sessions permission DENIED (Session_has_Person.personId)",
        "input": {
            "permissions": [
                "none",
            ],
            "username":"SHEPARD",
            "route":"/em/session/4583/stats"
        },
        "expected":{
            "code": 401
        }
    },
    {
        "name": "own_sessions permission DENIED",
        "input": {
            "permissions": [
                "own_sessions",
            ],
            "username":"user",
            "route":"/em/session/4583/stats"
        },
        "expected":{
            "code": 401
        }
    },
]

test_data_proposal = [
    {
        "name": "all_proposals permission OK",
        "input": {
            "permissions": [
                "all_proposals",
            ],
            "username":"admin",
            "route":"/proposals/899"
        },
        "expected":{
            "code": 200
        }
    },
    {
        "name": "no all_proposals permission DENIED",
        "input": {
            "permissions": [
                "none"
            ],
            "username":"admin",
            "route":"/proposals/899"
        },
        "expected":{
            "code": 401
        }
    },
    {
        "name": "own_proposals permission OK (proposal.personId)",
        "input": {
            "permissions": [
                "own_proposals",
            ],
            "username":"DI MARCO",
            "route":"/proposals/899"
        },
        "expected":{
            "code": 200
        }
    },
    {
        "name": "no own_proposals permission DENIED (proposal.personId)",
        "input": {
            "permissions": [
                "none"
            ],
            "username":"DI MARCO",
            "route":"/proposals/899"
        },
        "expected":{
            "code": 401
        }
    },
    {
        "name": "own_proposals permission OK (proposal_has_Person.personId)",
        "input": {
            "permissions": [
                "own_proposals",
            ],
            "username":"leonard",
            "route":"/proposals/1170"
        },
        "expected":{
            "code": 200
        }
    },
    {
        "name": "no own_proposals permission DENIED (proposal_has_Person.personId)",
        "input": {
            "permissions": [
                "none",
            ],
            "username":"leonard",
            "route":"/proposals/1170"
        },
        "expected":{
            "code": 401
        }
    },
    {
        "name": "own_proposals permission DENIED",
        "input": {
            "permissions": [
                "own_proposals",
            ],
            "username":"user",
            "route":"/proposals/1170"
        },
        "expected":{
            "code": 401
        }
    },
]

from tests.core.api.utils.apitest import ApiTestElem, ApiTestExpected, ApiTestInput


test_data_ssx_stats = [
    ApiTestElem(
        name="list stats empty",
        input=ApiTestInput(
            permissions=[],
            route="/ssx/datacollection/processing/stats?dataCollectionIds=1,2",
        ),
        expected=ApiTestExpected(code=200, res=[]),
    ),
    ApiTestElem(
        name="list stats wrong ids",
        input=ApiTestInput(
            permissions=[],
            route="/ssx/datacollection/processing/stats?dataCollectionIds=1d2",
        ),
        expected=ApiTestExpected(code=422),
    ),
]

test_data_ssx_cells = [
    ApiTestElem(
        name="cells empty",
        input=ApiTestInput(
            permissions=[],
            route="/ssx/datacollection/processing/cells?dataCollectionId=1",
        ),
        expected=ApiTestExpected(code=404),
    ),
    ApiTestElem(
        name="list stats wrong ids",
        input=ApiTestInput(
            permissions=[],
            route="/ssx/datacollection/processing/cells?dataCollectionId=1d2",
        ),
        expected=ApiTestExpected(code=422),
    ),
]


test_data_ssx_histogram = [
    ApiTestElem(
        name="histogram empty",
        input=ApiTestInput(
            permissions=[],
            route="/ssx/datacollection/processing/cells/histogram?dataCollectionIds=1,2",
        ),
        expected=ApiTestExpected(
            code=200,
            res={
                "a": None,
                "b": None,
                "c": None,
                "alpha": None,
                "beta": None,
                "gamma": None,
                "dataCollectionIds": [1, 2],
            },
        ),
    ),
    ApiTestElem(
        name="histogram wrong ids",
        input=ApiTestInput(
            permissions=[],
            route="/ssx/datacollection/processing/cells/histogram?dataCollectionIds=1d2",
        ),
        expected=ApiTestExpected(code=422),
    ),
]


test_data_ssx_create = [
    ApiTestElem(
        name="create dc no permission",
        input=ApiTestInput(
            permissions=[],
            route="/webservices/ssx/datacollection",
            method="post",
            payload={"dummy": 0},
        ),
        expected=ApiTestExpected(
            code=403,
        ),
    ),
    ApiTestElem(
        name="create dc",
        input=ApiTestInput(
            permissions=["ssx_sync"],
            route="/webservices/ssx/datacollection",
            method="post",
            payload={
                "dataCollectionGroupId": 1,
                "detectorId": 4,
                "exposureTime": 0,
                "transmission": 0,
                "flux": 0,
                "xBeam": 0,
                "yBeam": 0,
                "wavelength": 0,
                "detectorDistance": 0,
                "beamSizeAtSampleX": 0,
                "beamSizeAtSampleY": 0,
                "averageTemperature": 0,
                "xtalSnapshotFullPath1": "string",
                "xtalSnapshotFullPath2": "string",
                "xtalSnapshotFullPath3": "string",
                "xtalSnapshotFullPath4": "string",
                "imagePrefix": "string",
                "numberOfPasses": 0,
                "numberOfImages": 0,
                "resolution": 0,
                "resolutionAtCorner": 0,
                "flux_end": 0,
                "startTime": "2023-01-25T09:16:42.053Z",
                "endTime": "2023-01-25T09:16:42.053Z",
                "beamShape": "string",
                "polarisation": 0,
                "undulatorGap1": 0,
                "repetitionRate": 0,
                "energyBandwidth": 0,
                "monoStripe": "string",
                "experimentName": "string",
                "jetSize": 0,
                "jetSpeed": 0,
                "laserEnergy": 0,
                "chipModel": "string",
                "chipPattern": "string",
                "event_chains": [
                    {
                        "name": "string",
                        "events": [
                            {
                                "type": "XrayDetection",
                                "name": "string",
                                "offset": 0,
                                "duration": 0,
                                "period": 0,
                                "repetition": 0,
                            }
                        ],
                    }
                ],
            },
        ),
        expected=ApiTestExpected(
            code=200,
        ),
    ),
    ApiTestElem(
        name="create dc unknown group",
        input=ApiTestInput(
            permissions=["ssx_sync"],
            route="/webservices/ssx/datacollection",
            method="post",
            payload={
                "dataCollectionGroupId": 99999999,
                "detectorId": 4,
                "exposureTime": 0,
                "transmission": 0,
                "flux": 0,
                "xBeam": 0,
                "yBeam": 0,
                "wavelength": 0,
                "detectorDistance": 0,
                "beamSizeAtSampleX": 0,
                "beamSizeAtSampleY": 0,
                "averageTemperature": 0,
                "xtalSnapshotFullPath1": "string",
                "xtalSnapshotFullPath2": "string",
                "xtalSnapshotFullPath3": "string",
                "xtalSnapshotFullPath4": "string",
                "imagePrefix": "string",
                "numberOfPasses": 0,
                "numberOfImages": 0,
                "resolution": 0,
                "resolutionAtCorner": 0,
                "flux_end": 0,
                "startTime": "2023-01-25T09:16:42.053Z",
                "endTime": "2023-01-25T09:16:42.053Z",
                "beamShape": "string",
                "polarisation": 0,
                "undulatorGap1": 0,
                "repetitionRate": 0,
                "energyBandwidth": 0,
                "monoStripe": "string",
                "experimentName": "string",
                "jetSize": 0,
                "jetSpeed": 0,
                "laserEnergy": 0,
                "chipModel": "string",
                "chipPattern": "string",
                "event_chains": [
                    {
                        "name": "string",
                        "events": [
                            {
                                "type": "XrayDetection",
                                "name": "string",
                                "offset": 0,
                                "duration": 0,
                                "period": 0,
                                "repetition": 0,
                            }
                        ],
                    }
                ],
            },
        ),
        expected=ApiTestExpected(
            code=422,
        ),
    ),
    ApiTestElem(
        name="create dc unknown detector",
        input=ApiTestInput(
            permissions=["ssx_sync"],
            route="/webservices/ssx/datacollection",
            method="post",
            payload={
                "dataCollectionGroupId": 1,
                "detectorId": 99999999,
                "exposureTime": 0,
                "transmission": 0,
                "flux": 0,
                "xBeam": 0,
                "yBeam": 0,
                "wavelength": 0,
                "detectorDistance": 0,
                "beamSizeAtSampleX": 0,
                "beamSizeAtSampleY": 0,
                "averageTemperature": 0,
                "xtalSnapshotFullPath1": "string",
                "xtalSnapshotFullPath2": "string",
                "xtalSnapshotFullPath3": "string",
                "xtalSnapshotFullPath4": "string",
                "imagePrefix": "string",
                "numberOfPasses": 0,
                "numberOfImages": 0,
                "resolution": 0,
                "resolutionAtCorner": 0,
                "flux_end": 0,
                "startTime": "2023-01-25T09:16:42.053Z",
                "endTime": "2023-01-25T09:16:42.053Z",
                "beamShape": "string",
                "polarisation": 0,
                "undulatorGap1": 0,
                "repetitionRate": 0,
                "energyBandwidth": 0,
                "monoStripe": "string",
                "experimentName": "string",
                "jetSize": 0,
                "jetSpeed": 0,
                "laserEnergy": 0,
                "chipModel": "string",
                "chipPattern": "string",
                "event_chains": [
                    {
                        "name": "string",
                        "events": [
                            {
                                "type": "XrayDetection",
                                "name": "string",
                                "offset": 0,
                                "duration": 0,
                                "period": 0,
                                "repetition": 0,
                            }
                        ],
                    }
                ],
            },
        ),
        expected=ApiTestExpected(
            code=422,
        ),
    ),
    ApiTestElem(
        name="create dcg no rights",
        input=ApiTestInput(
            permissions=[],
            route="/webservices/ssx/datacollectiongroup",
            method="post",
            payload={"dummy": 0},
        ),
        expected=ApiTestExpected(
            code=403,
        ),
    ),
    ApiTestElem(
        name="create dcg",
        input=ApiTestInput(
            permissions=["ssx_sync"],
            route="/webservices/ssx/datacollectiongroup",
            method="post",
            payload={
                "sessionId": 1,
                "startTime": "2023-01-25T09:21:50.646Z",
                "endTime": "2023-01-25T09:21:50.646Z",
                "experimentType": "SSX-Chip",
                "comments": "string",
                "sample": {
                    "name": "string",
                    "support": "string",
                    "crystal": {
                        "size_X": 0,
                        "size_Y": 0,
                        "size_Z": 0,
                        "abundance": 0,
                        "protein": {"name": "string", "acronym": "string"},
                        "components": [
                            {
                                "name": "string",
                                "componentType": "Ligand",
                                "composition": "string",
                                "abundance": 0,
                            }
                        ],
                    },
                    "components": [
                        {
                            "name": "string",
                            "componentType": "Ligand",
                            "composition": "string",
                            "abundance": 0,
                        }
                    ],
                },
            },
        ),
        expected=ApiTestExpected(
            code=200,
        ),
    ),
    ApiTestElem(
        name="create dcg wrong session",
        input=ApiTestInput(
            permissions=["ssx_sync"],
            route="/webservices/ssx/datacollectiongroup",
            method="post",
            payload={
                "sessionId": 9999999,
                "startTime": "2023-01-25T09:21:50.646Z",
                "endTime": "2023-01-25T09:21:50.646Z",
                "experimentType": "SSX-Chip",
                "comments": "string",
                "sample": {
                    "name": "string",
                    "support": "string",
                    "crystal": {
                        "size_X": 0,
                        "size_Y": 0,
                        "size_Z": 0,
                        "abundance": 0,
                        "protein": {"name": "string", "acronym": "string"},
                        "components": [
                            {
                                "name": "string",
                                "componentType": "Ligand",
                                "composition": "string",
                                "abundance": 0,
                            }
                        ],
                    },
                    "components": [
                        {
                            "name": "string",
                            "componentType": "Ligand",
                            "composition": "string",
                            "abundance": 0,
                        }
                    ],
                },
            },
        ),
        expected=ApiTestExpected(
            code=422,
        ),
    ),
    ApiTestElem(
        name="create dcg wrong sample",
        input=ApiTestInput(
            permissions=["ssx_sync"],
            route="/webservices/ssx/datacollectiongroup",
            method="post",
            payload={
                "sessionId": 1,
                "startTime": "2023-01-25T09:21:50.646Z",
                "endTime": "2023-01-25T09:21:50.646Z",
                "experimentType": "SSX-Chip",
                "comments": "string",
                "sampleId": 99999,
            },
        ),
        expected=ApiTestExpected(
            code=422,
        ),
    ),
]

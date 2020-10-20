from datetime import datetime

test_proposal = {
    "proposalCode": "MX",
    "title": "Test proposal",
    "proposalType": "MX",
    "personId": 1,
    "proposalNumber": "111",
    "bltimeStamp": "2015-12-21 16:20:43",
    "state": "Open",
}

test_session = {
    "bltimeStamp": "2015-12-21 16:20:44",
    "proposalId": 37027,
    "beamLineName": "i03",
    "visit_number": 2,
    "archived": 0,
    "beamLineSetupId": 1,
    "endDate": "2016-03-11 17:00:00",
    "startDate": "2016-03-11 09:00:00",
}


test_data_collection = {
    "binning": 1,
    "FOCALSPOTSIZEATSAMPLEY": 20,
    "detectorDistance": 193.087,
    "xtalSnapshotFullPath3": "/path/to_snapshot3",
    "printableForReport": 1,
    "dataCollectionGroupId": 988855,
    "slitGapHorizontal": 0.099937,
    "axisStart": 45,
    "xtalSnapshotFullPath1": "/path/to_snapshot1",
    "imageDirectory": "/dls/i03/data/2016/cm14451-1/20160114/tlys_jan_4/",
    "BLSAMPLEID": 374695,
    "xBeam": 215.62,
    "SESSIONID": 55167,
    "comments": "(-402,345,142) EDNAStrategy4: subWedge:1Aperture: Medium",
    "fileTemplate": "tlys_jan_4_1_####.cbf",
    "imageSuffix": "cbf",
    "flux": 833107367454.3083,
    "overlap": 0,
    "wavelength": 1.28255,
    "axisEnd": 0.1,
    "slitGapVertical": 0.059918,
    "beamSizeAtSampleX": 0.05,
    "omegaStart": 45,
    "endTime": "2016-01-14 12:41:54",
    "dataCollectionNumber": 1,
    "imagePrefix": "tlys_jan_4",
    "xtalSnapshotFullPath4": "/path/to_snapshot4",
    "yBeam": 208.978,
    "synchrotronMode": "User",
    "numberOfPasses": 1,
    "resolution": 1.6,
    "undulatorGap1": 5.685,
    "xtalSnapshotFullPath2": "/path/to_snapshot2",
    "FOCALSPOTSIZEATSAMPLEX": 80,
    "runStatus": "DataCollection Successful",
    "dataCollectionId": 993677,
    "axisRange": 0.1,
    "POSITIONID": 595236,
    "numberOfImages": 3600,
    "beamSizeAtSampleY": 0.02,
    "transmission": 40.1936,
    "startImageNumber": 1,
    "rotationAxis": "Omega",
    "exposureTime": 0.02,
    "startTime": "2016-01-14 12:40:34",
}

test_local_contact = {
  "personId": 1,
  "cardName": "Card",
  "proposalId": 37027,
  "defaultCourrierCompany": "DHL",
  "courierAccount": "01",
  "billingReference": "02",
  "dewarAvgCustomsValue": 0,
  "dewarAvgTransportValue": 0
}

test_shippment = {
  "proposalId": 37027,
  "shippingName": "Test shipment",
  "deliveryAgent_agentName": "DHL",
  "deliveryAgent_agentCode": "Code",
  "deliveryAgent_flightCode": "Code",
  "shippingStatus": "Open",
  "laboratoryId": 1,
  "isStorageShipping": 0,
  "comments": "Comment",
  "sendingLabContactId": 1,
  "returnLabContactId": 1,
  "returnCourier": "DHL",
  "deliveryAgent_label": "Label",
  "physicalLocation": "Store"
}

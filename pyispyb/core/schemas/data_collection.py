"""
Project: py-ispyb.

https://github.com/ispyb/py-ispyb

This file is part of py-ispyb software.

py-ispyb is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

py-ispyb is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with py-ispyb. If not, see <http://www.gnu.org/licenses/>.
"""


__license__ = "LGPLv3+"



from marshmallow import Schema, fields as ma_fields
from flask_restx import fields as f_fields
from marshmallow_jsonschema import JSONSchema

from pyispyb.app.extensions.api import api_v1 as api

dict_schema = {
        'dataCollectionId': f_fields.Integer(required=True, description='Primary key (auto-incremented)'),
        'BLSAMPLEID': f_fields.Integer(required=False, description=''),
        'SESSIONID': f_fields.Integer(required=False, description=''),
        'experimenttype': f_fields.String(required=False, description=''),
        'dataCollectionNumber': f_fields.Integer(required=False, description=''),
        'startTime': f_fields.DateTime(required=False, description='Start time of the dataCollection'),
        'endTime': f_fields.DateTime(required=False, description='end time of the dataCollection'),
        'runStatus': f_fields.String(required=False, description=''),
        'axisStart': f_fields.Float(required=False, description=''),
        'axisEnd': f_fields.Float(required=False, description=''),
        'axisRange': f_fields.Float(required=False, description=''),
        'overlap': f_fields.Float(required=False, description=''),
        'numberOfImages': f_fields.Integer(required=False, description=''),
        'startImageNumber': f_fields.Integer(required=False, description=''),
        'numberOfPasses': f_fields.Integer(required=False, description=''),
        'exposureTime': f_fields.Float(required=False, description=''),
        'imageDirectory': f_fields.String(required=False, description='The directory where files reside - should end with a slash'),
        'imagePrefix': f_fields.String(required=False, description=''),
        'imageSuffix': f_fields.String(required=False, description=''),
        'imageContainerSubPath': f_fields.String(required=False, description='Internal path of a HDF5 file pointing to the data for this data collection'),
        'fileTemplate': f_fields.String(required=False, description=''),
        'wavelength': f_fields.Float(required=False, description=''),
        'resolution': f_fields.Float(required=False, description=''),
        'detectorDistance': f_fields.Float(required=False, description=''),
        'xBeam': f_fields.Float(required=False, description=''),
        'yBeam': f_fields.Float(required=False, description=''),
        'comments': f_fields.String(required=False, description=''),
        'printableForReport': f_fields.Integer(required=False, description=''),
        'CRYSTALCLASS': f_fields.String(required=False, description=''),
        'slitGapVertical': f_fields.Float(required=False, description=''),
        'slitGapHorizontal': f_fields.Float(required=False, description=''),
        'transmission': f_fields.Float(required=False, description=''),
        'synchrotronMode': f_fields.String(required=False, description=''),
        'xtalSnapshotFullPath1': f_fields.String(required=False, description=''),
        'xtalSnapshotFullPath2': f_fields.String(required=False, description=''),
        'xtalSnapshotFullPath3': f_fields.String(required=False, description=''),
        'xtalSnapshotFullPath4': f_fields.String(required=False, description=''),
        'rotationAxis': f_fields.String(required=False, description='enum(Omega,Kappa,Phi)'),
        'phiStart': f_fields.Float(required=False, description=''),
        'kappaStart': f_fields.Float(required=False, description=''),
        'omegaStart': f_fields.Float(required=False, description=''),
        'chiStart': f_fields.Float(required=False, description=''),
        'resolutionAtCorner': f_fields.Float(required=False, description=''),
        'detector2Theta': f_fields.Float(required=False, description=''),
        'DETECTORMODE': f_fields.String(required=False, description=''),
        'undulatorGap1': f_fields.Float(required=False, description=''),
        'undulatorGap2': f_fields.Float(required=False, description=''),
        'undulatorGap3': f_fields.Float(required=False, description=''),
        'beamSizeAtSampleX': f_fields.Float(required=False, description=''),
        'beamSizeAtSampleY': f_fields.Float(required=False, description=''),
        'centeringMethod': f_fields.String(required=False, description=''),
        'averageTemperature': f_fields.Float(required=False, description=''),
        'ACTUALSAMPLEBARCODE': f_fields.String(required=False, description=''),
        'ACTUALSAMPLESLOTINCONTAINER': f_fields.Integer(required=False, description=''),
        'ACTUALCONTAINERBARCODE': f_fields.String(required=False, description=''),
        'ACTUALCONTAINERSLOTINSC': f_fields.Integer(required=False, description=''),
        'actualCenteringPosition': f_fields.String(required=False, description=''),
        'beamShape': f_fields.String(required=False, description=''),
        'dataCollectionGroupId': f_fields.Integer(required=True, description='references DataCollectionGroup table'),
        'POSITIONID': f_fields.Integer(required=False, description=''),
        'detectorId': f_fields.Integer(required=False, description='references Detector table'),
        'FOCALSPOTSIZEATSAMPLEX': f_fields.Float(required=False, description=''),
        'POLARISATION': f_fields.Float(required=False, description=''),
        'FOCALSPOTSIZEATSAMPLEY': f_fields.Float(required=False, description=''),
        'APERTUREID': f_fields.Integer(required=False, description=''),
        'screeningOrigId': f_fields.Integer(required=False, description=''),
        'startPositionId': f_fields.Integer(required=False, description=''),
        'endPositionId': f_fields.Integer(required=False, description=''),
        'flux': f_fields.String(required=False, description=''),
        'strategySubWedgeOrigId': f_fields.Integer(required=False, description='references ScreeningStrategySubWedge table'),
        'blSubSampleId': f_fields.Integer(required=False, description=''),
        'flux_end': f_fields.String(required=False, description='flux measured after the collect'),
        'bestWilsonPlotPath': f_fields.String(required=False, description=''),
        'processedDataFile': f_fields.String(required=False, description=''),
        'datFullPath': f_fields.String(required=False, description=''),
        'magnification': f_fields.Float(required=False, description='Calibrated magnification, Units: dimensionless'),
        'totalAbsorbedDose': f_fields.Float(required=False, description='Unit: e-/A^2 for EM'),
        'binning': f_fields.Integer(required=False, description='1 or 2. Number of pixels to process as 1. (Use mean value.)'),
        'particleDiameter': f_fields.Float(required=False, description='Unit: nm'),
        'boxSize_CTF': f_fields.Float(required=False, description='Unit: pixels'),
        'minResolution': f_fields.Float(required=False, description='Unit: A'),
        'minDefocus': f_fields.Float(required=False, description='Unit: A'),
        'maxDefocus': f_fields.Float(required=False, description='Unit: A'),
        'defocusStepSize': f_fields.Float(required=False, description='Unit: A'),
        'amountAstigmatism': f_fields.Float(required=False, description='Unit: A'),
        'extractSize': f_fields.Float(required=False, description='Unit: pixels'),
        'bgRadius': f_fields.Float(required=False, description='Unit: nm'),
        'voltage': f_fields.Float(required=False, description='Unit: kV'),
        'objAperture': f_fields.Float(required=False, description='Unit: um'),
        'c1aperture': f_fields.Float(required=False, description='Unit: um'),
        'c2aperture': f_fields.Float(required=False, description='Unit: um'),
        'c3aperture': f_fields.Float(required=False, description='Unit: um'),
        'c1lens': f_fields.Float(required=False, description='Unit: %'),
        'c2lens': f_fields.Float(required=False, description='Unit: %'),
        'c3lens': f_fields.Float(required=False, description='Unit: %'),
        'totalExposedDose': f_fields.Float(required=False, description='Units: e-/A^2'),
        'nominalMagnification': f_fields.Float(required=False, description='Nominal magnification: Units: dimensionless'),
        'nominalDefocus': f_fields.Float(required=False, description='Nominal defocus, Units: A'),
        'imageSizeX': f_fields.Integer(required=False, description='Image size in x, incase crop has been used, Units: pixels'),
        'imageSizeY': f_fields.Integer(required=False, description='Image size in y, Units: pixels'),
        'pixelSizeOnImage': f_fields.Float(required=False, description='Pixel size on image, calculated from magnification, duplicate? Units: um?'),
        'phasePlate': f_fields.Integer(required=False, description='Whether the phase plate was used'),
        }

class DataCollectionSchema(Schema):
    """Marshmallows schema class representing DataCollection table"""

    dataCollectionId = ma_fields.Integer()
    BLSAMPLEID = ma_fields.Integer()
    SESSIONID = ma_fields.Integer()
    experimenttype = ma_fields.String()
    dataCollectionNumber = ma_fields.Integer()
    startTime = ma_fields.DateTime()
    endTime = ma_fields.DateTime()
    runStatus = ma_fields.String()
    axisStart = ma_fields.Float()
    axisEnd = ma_fields.Float()
    axisRange = ma_fields.Float()
    overlap = ma_fields.Float()
    numberOfImages = ma_fields.Integer()
    startImageNumber = ma_fields.Integer()
    numberOfPasses = ma_fields.Integer()
    exposureTime = ma_fields.Float()
    imageDirectory = ma_fields.String()
    imagePrefix = ma_fields.String()
    imageSuffix = ma_fields.String()
    imageContainerSubPath = ma_fields.String()
    fileTemplate = ma_fields.String()
    wavelength = ma_fields.Float()
    resolution = ma_fields.Float()
    detectorDistance = ma_fields.Float()
    xBeam = ma_fields.Float()
    yBeam = ma_fields.Float()
    comments = ma_fields.String()
    printableForReport = ma_fields.Integer()
    CRYSTALCLASS = ma_fields.String()
    slitGapVertical = ma_fields.Float()
    slitGapHorizontal = ma_fields.Float()
    transmission = ma_fields.Float()
    synchrotronMode = ma_fields.String()
    xtalSnapshotFullPath1 = ma_fields.String()
    xtalSnapshotFullPath2 = ma_fields.String()
    xtalSnapshotFullPath3 = ma_fields.String()
    xtalSnapshotFullPath4 = ma_fields.String()
    rotationAxis = ma_fields.String()
    phiStart = ma_fields.Float()
    kappaStart = ma_fields.Float()
    omegaStart = ma_fields.Float()
    chiStart = ma_fields.Float()
    resolutionAtCorner = ma_fields.Float()
    detector2Theta = ma_fields.Float()
    DETECTORMODE = ma_fields.String()
    undulatorGap1 = ma_fields.Float()
    undulatorGap2 = ma_fields.Float()
    undulatorGap3 = ma_fields.Float()
    beamSizeAtSampleX = ma_fields.Float()
    beamSizeAtSampleY = ma_fields.Float()
    centeringMethod = ma_fields.String()
    averageTemperature = ma_fields.Float()
    ACTUALSAMPLEBARCODE = ma_fields.String()
    ACTUALSAMPLESLOTINCONTAINER = ma_fields.Integer()
    ACTUALCONTAINERBARCODE = ma_fields.String()
    ACTUALCONTAINERSLOTINSC = ma_fields.Integer()
    actualCenteringPosition = ma_fields.String()
    beamShape = ma_fields.String()
    dataCollectionGroupId = ma_fields.Integer()
    POSITIONID = ma_fields.Integer()
    detectorId = ma_fields.Integer()
    FOCALSPOTSIZEATSAMPLEX = ma_fields.Float()
    POLARISATION = ma_fields.Float()
    FOCALSPOTSIZEATSAMPLEY = ma_fields.Float()
    APERTUREID = ma_fields.Integer()
    screeningOrigId = ma_fields.Integer()
    startPositionId = ma_fields.Integer()
    endPositionId = ma_fields.Integer()
    flux = ma_fields.String()
    strategySubWedgeOrigId = ma_fields.Integer()
    blSubSampleId = ma_fields.Integer()
    flux_end = ma_fields.String()
    bestWilsonPlotPath = ma_fields.String()
    processedDataFile = ma_fields.String()
    datFullPath = ma_fields.String()
    magnification = ma_fields.Float()
    totalAbsorbedDose = ma_fields.Float()
    binning = ma_fields.Integer()
    particleDiameter = ma_fields.Float()
    boxSize_CTF = ma_fields.Float()
    minResolution = ma_fields.Float()
    minDefocus = ma_fields.Float()
    maxDefocus = ma_fields.Float()
    defocusStepSize = ma_fields.Float()
    amountAstigmatism = ma_fields.Float()
    extractSize = ma_fields.Float()
    bgRadius = ma_fields.Float()
    voltage = ma_fields.Float()
    objAperture = ma_fields.Float()
    c1aperture = ma_fields.Float()
    c2aperture = ma_fields.Float()
    c3aperture = ma_fields.Float()
    c1lens = ma_fields.Float()
    c2lens = ma_fields.Float()
    c3lens = ma_fields.Float()
    totalExposedDose = ma_fields.Float()
    nominalMagnification = ma_fields.Float()
    nominalDefocus = ma_fields.Float()
    imageSizeX = ma_fields.Integer()
    imageSizeY = ma_fields.Integer()
    pixelSizeOnImage = ma_fields.Float()
    phasePlate = ma_fields.Integer()

f_schema = api.model('DataCollection', dict_schema)
ma_schema = DataCollectionSchema()
json_schema = JSONSchema().dump(ma_schema)

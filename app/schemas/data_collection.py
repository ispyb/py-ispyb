# encoding: utf-8
# 
#  Project: py-ispyb
#  https://github.com/ispyb/py-ispyb
#
#  This file is part of py-ispyb software.
#
#  py-ispyb is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  py-ispyb is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with py-ispyb. If not, see <http://www.gnu.org/licenses/>.


__license__ = "LGPLv3+"



from marshmallow import Schema, fields as ma_fields
from flask_restx import fields as f_fields

from app.extensions.api import api_v1 as api

data_collection_dict = {
        'dataCollectionId': f_fields.Integer(required=True, description='Primary key (auto-incremented)'),
        'dataCollectionGroupId': f_fields.Integer(required=True, description='references DataCollectionGroup table'),
        'strategySubWedgeOrigId': f_fields.Integer(required=False, description='references ScreeningStrategySubWedge table'),
        'detectorId': f_fields.Integer(required=False, description='references Detector table'),
        'blSubSampleId': f_fields.Integer(required=False, description=''),
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
        'imageDirectory': f_fields.String(required=False, description=''),
        'imagePrefix': f_fields.String(required=False, description=''),
        'imageSuffix': f_fields.String(required=False, description=''),
        'fileTemplate': f_fields.String(required=False, description=''),
        'wavelength': f_fields.Float(required=False, description=''),
        'resolution': f_fields.Float(required=False, description=''),
        'detectorDistance': f_fields.Float(required=False, description=''),
        'xBeam': f_fields.Float(required=False, description=''),
        'yBeam': f_fields.Float(required=False, description=''),
        'xBeamPix': f_fields.Float(required=False, description='Beam size in pixels'),
        'yBeamPix': f_fields.Float(required=False, description='Beam size in pixels'),
        'comments': f_fields.String(required=False, description=''),
        'printableForReport': f_fields.Integer(required=False, description=''),
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
        'resolutionAtCorner': f_fields.Float(required=False, description=''),
        'detector2Theta': f_fields.Float(required=False, description=''),
        'undulatorGap1': f_fields.Float(required=False, description=''),
        'undulatorGap2': f_fields.Float(required=False, description=''),
        'undulatorGap3': f_fields.Float(required=False, description=''),
        'beamSizeAtSampleX': f_fields.Float(required=False, description=''),
        'beamSizeAtSampleY': f_fields.Float(required=False, description=''),
        'centeringMethod': f_fields.String(required=False, description=''),
        'averageTemperature': f_fields.Float(required=False, description=''),
        'actualCenteringPosition': f_fields.String(required=False, description=''),
        'beamShape': f_fields.String(required=False, description=''),
        'flux': f_fields.String(required=False, description=''),
        'flux_end': f_fields.String(required=False, description='flux measured after the collect'),
        'totalAbsorbedDose': f_fields.String(required=False, description='expected dose delivered to the crystal, EDNA'),
        'bestWilsonPlotPath': f_fields.String(required=False, description=''),
        'imageQualityIndicatorsPlotPath': f_fields.String(required=False, description=''),
        'imageQualityIndicatorsCSVPath': f_fields.String(required=False, description=''),
        'blSampleId': f_fields.Integer(required=False, description=''),
        'sessionId': f_fields.Integer(required=False, description=''),
        'experimentType': f_fields.String(required=False, description=''),
        'crystalClass': f_fields.String(required=False, description=''),
        'chiStart': f_fields.Float(required=False, description=''),
        'detectorMode': f_fields.String(required=False, description=''),
        'actualSampleBarcode': f_fields.String(required=False, description=''),
        'actualSampleSlotInContainer': f_fields.Integer(required=False, description=''),
        'actualContainerBarcode': f_fields.String(required=False, description=''),
        'actualContainerSlotInSC': f_fields.Integer(required=False, description=''),
        'positionId': f_fields.Integer(required=False, description=''),
        'focalSpotSizeAtSampleX': f_fields.Float(required=False, description=''),
        'polarisation': f_fields.Float(required=False, description=''),
        'focalSpotSizeAtSampleY': f_fields.Float(required=False, description=''),
        'apertureId': f_fields.Integer(required=False, description=''),
        'screeningOrigId': f_fields.Integer(required=False, description=''),
        'processedDataFile': f_fields.String(required=False, description=''),
        'datFullPath': f_fields.String(required=False, description=''),
        'magnification': f_fields.Integer(required=False, description='Unit: X'),
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
        'nominalmagnification': f_fields.Float(required=False, description=''),
        'nominalDefocus': f_fields.Float(required=False, description=''),
        'imageSizeX': f_fields.Integer(required=False, description=''),
        'imageSizeY': f_fields.Integer(required=False, description=''),
        'pixelSizeOnImage': f_fields.Float(required=False, description=''),
        'phasePlate': f_fields.Integer(required=False, description=''),
        'totalExposedDose': f_fields.Float(required=False, description='Units: e-/A^2'),
        }

class DataCollectionSchema(Schema):
    """Marshmallows schema class representing DataCollection table"""

    dataCollectionId = ma_fields.Integer()
    dataCollectionGroupId = ma_fields.Integer()
    strategySubWedgeOrigId = ma_fields.Integer()
    detectorId = ma_fields.Integer()
    blSubSampleId = ma_fields.Integer()
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
    fileTemplate = ma_fields.String()
    wavelength = ma_fields.Float()
    resolution = ma_fields.Float()
    detectorDistance = ma_fields.Float()
    xBeam = ma_fields.Float()
    yBeam = ma_fields.Float()
    xBeamPix = ma_fields.Float()
    yBeamPix = ma_fields.Float()
    comments = ma_fields.String()
    printableForReport = ma_fields.Integer()
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
    resolutionAtCorner = ma_fields.Float()
    detector2Theta = ma_fields.Float()
    undulatorGap1 = ma_fields.Float()
    undulatorGap2 = ma_fields.Float()
    undulatorGap3 = ma_fields.Float()
    beamSizeAtSampleX = ma_fields.Float()
    beamSizeAtSampleY = ma_fields.Float()
    centeringMethod = ma_fields.String()
    averageTemperature = ma_fields.Float()
    actualCenteringPosition = ma_fields.String()
    beamShape = ma_fields.String()
    flux = ma_fields.String()
    flux_end = ma_fields.String()
    totalAbsorbedDose = ma_fields.String()
    bestWilsonPlotPath = ma_fields.String()
    imageQualityIndicatorsPlotPath = ma_fields.String()
    imageQualityIndicatorsCSVPath = ma_fields.String()
    blSampleId = ma_fields.Integer()
    sessionId = ma_fields.Integer()
    experimentType = ma_fields.String()
    crystalClass = ma_fields.String()
    chiStart = ma_fields.Float()
    detectorMode = ma_fields.String()
    actualSampleBarcode = ma_fields.String()
    actualSampleSlotInContainer = ma_fields.Integer()
    actualContainerBarcode = ma_fields.String()
    actualContainerSlotInSC = ma_fields.Integer()
    positionId = ma_fields.Integer()
    focalSpotSizeAtSampleX = ma_fields.Float()
    polarisation = ma_fields.Float()
    focalSpotSizeAtSampleY = ma_fields.Float()
    apertureId = ma_fields.Integer()
    screeningOrigId = ma_fields.Integer()
    processedDataFile = ma_fields.String()
    datFullPath = ma_fields.String()
    magnification = ma_fields.Integer()
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
    nominalmagnification = ma_fields.Float()
    nominalDefocus = ma_fields.Float()
    imageSizeX = ma_fields.Integer()
    imageSizeY = ma_fields.Integer()
    pixelSizeOnImage = ma_fields.Float()
    phasePlate = ma_fields.Integer()
    totalExposedDose = ma_fields.Float()

f_data_collection_schema = api.model('DataCollection', data_collection_dict)
ma_data_collection_schema = DataCollectionSchema()


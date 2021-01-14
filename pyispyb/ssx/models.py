# coding: utf-8
from sqlalchemy import Column, Float, ForeignKey, Integer, JSON, String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql.enumerated import ENUM
from flask_sqlalchemy import SQLAlchemy


from pyispyb.app.extensions import db



class CrystalSizeDistribution(db.Model):
    __tablename__ = 'CrystalSizeDistribution'

    crystalSizeDistributionId = db.Column(db.Integer, primary_key=True, unique=True)
    crystalHabit = db.Column(db.String(255))
    characteristicDimensions = db.Column(db.String(255))
    minDimension = db.Column(db.String(255), info='comma separated floats')
    maxDimension = db.Column(db.String(255), info='comma separated floats')



class CrystalSlurry(db.Model):
    __tablename__ = 'CrystalSlurry'

    crystalSlurryId = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(255))
    crystalSizeDistributionId = db.Column(db.ForeignKey('CrystalSizeDistribution.crystalSizeDistributionId'), index=True)
    crystalDensity = db.Column(db.Float, info='1/mm3')
    bufferId = db.Column(db.Float, info='reference to Buffer.bufferId')

    CrystalSizeDistribution = db.relationship('CrystalSizeDistribution', primaryjoin='CrystalSlurry.crystalSizeDistributionId == CrystalSizeDistribution.crystalSizeDistributionId')



class CrystalSlurryHasCrystal(db.Model):
    __tablename__ = 'CrystalSlurry_has_Crystal'

    CrystalSlurryHasCrystalId = db.Column(db.Integer, primary_key=True, unique=True)
    crystalSlurryId = db.Column(db.ForeignKey('CrystalSlurry.crystalSlurryId'), nullable=False, index=True)
    crystalId = db.Column(db.Integer, nullable=False)

    CrystalSlurry = db.relationship('CrystalSlurry', primaryjoin='CrystalSlurryHasCrystal.crystalSlurryId == CrystalSlurry.crystalSlurryId')



class DataSet(db.Model):
    __tablename__ = 'DataSet'

    dataSetId = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(255), nullable=False)
    mergedResultsFilename = db.Column(db.String(255))



class EventTrain(db.Model):
    __tablename__ = 'EventTrain'

    eventTrainId = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(255))
    timeOn = db.Column(db.Float, info='sec')
    duration = db.Column(db.Float, info='sec')
    period = db.Column(db.Float)
    numberOfRepetitions = db.Column(db.Float)
    nameInEventLog = db.Column(db.String(255))
    triggerDevice = db.Column(db.String(255))



class ExperimentalPlan(db.Model):
    __tablename__ = 'ExperimentalPlan'

    experimentalPlanId = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(255))
    numberOfRepetitions = db.Column(db.Integer, info='for micro-fluidic, jet, tape but not for chip')
    period = db.Column(db.Float, info='seconds but unknown/self adjusting for chip')
    masterTriggerId = db.Column(db.ForeignKey('MasterTrigger.masterTriggerId'), index=True)
    repeatedSequenceId = db.Column(db.ForeignKey('RepeatedSequence.repeatedSequenceId'), nullable=False, index=True)

    MasterTrigger = db.relationship('MasterTrigger', primaryjoin='ExperimentalPlan.masterTriggerId == MasterTrigger.masterTriggerId')
    RepeatedSequence = db.relationship('RepeatedSequence', primaryjoin='ExperimentalPlan.repeatedSequenceId == RepeatedSequence.repeatedSequenceId')



class LoadedSample(db.Model):
    __tablename__ = 'LoadedSample'

    loadedSampleId = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(255), info='to be used as part of the image and processing file names')
    sampleStockId = db.Column(db.ForeignKey('SampleStock.sampleStockId'), index=True)
    sampleDeliveryDeviceId = db.Column(db.ForeignKey('SampleDeliveryDevice.sampleDeliveryDeviceId'), index=True)
    loadingPattern = db.Column(db.Integer)
    descriptionJson = db.Column(db.JSON)

    SampleDeliveryDevice = db.relationship('SampleDeliveryDevice', primaryjoin='LoadedSample.sampleDeliveryDeviceId == SampleDeliveryDevice.sampleDeliveryDeviceId')
    SampleStock = db.relationship('SampleStock', primaryjoin='LoadedSample.sampleStockId == SampleStock.sampleStockId')



class MasterTrigger(db.Model):
    __tablename__ = 'MasterTrigger'

    masterTriggerId = db.Column(db.Integer, primary_key=True, unique=True)
    nameInEventLog = db.Column(db.String(255))
    triggerDevice = db.Column(db.Integer)
    descriptionJson = db.Column(db.JSON)



class Micrograph(db.Model):
    __tablename__ = 'Micrograph'

    micrographId = db.Column(db.Integer, primary_key=True, unique=True)
    crystalSlurryId = db.Column(db.ForeignKey('CrystalSlurry.crystalSlurryId'), nullable=False, index=True)
    url = db.Column(db.String(255))
    objectSidePixelSize = db.Column(db.String(255), info='comma separated two floats')
    descriptionJson = db.Column(db.JSON)

    CrystalSlurry = db.relationship('CrystalSlurry', primaryjoin='Micrograph.crystalSlurryId == CrystalSlurry.crystalSlurryId')



class RepeatedSequence(db.Model):
    __tablename__ = 'RepeatedSequence'

    repeatedSequenceId = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(255))



class SampleDeliveryDevice(db.Model):
    __tablename__ = 'SampleDeliveryDevice'

    sampleDeliveryDeviceId = db.Column(db.Integer, primary_key=True, unique=True)
    type = db.Column(db.ENUM('photoChip', 'microFluidics', 'viscoousJet', 'tapeDevice'))
    descriptionJson = db.Column(db.JSON)



class SampleStock(db.Model):
    __tablename__ = 'SampleStock'

    sampleStockId = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(255), nullable=False)
    crystalSlurryId = db.Column(db.ForeignKey('CrystalSlurry.crystalSlurryId'), nullable=False, index=True)
    concentrationFactor = db.Column(db.Float, nullable=False)
    crystalDensity = db.Column(db.Float, nullable=False)
    additiveId = db.Column(db.Integer, info='reference to Additive.additiveId')
    note = db.Column(db.String(255))

    CrystalSlurry = db.relationship('CrystalSlurry', primaryjoin='SampleStock.crystalSlurryId == CrystalSlurry.crystalSlurryId')



class SsxDataAcquisition(db.Model):
    __tablename__ = 'SsxDataAcquisition'

    ssxDataAcquisitionId = db.Column(db.Integer, primary_key=True, unique=True)
    loadedSampleId = db.Column(db.ForeignKey('LoadedSample.loadedSampleId'), nullable=False, index=True)
    dataCollectionId = db.Column(db.Integer, nullable=False, info='reference to DataCollection.dataCollectionId')
    experimentalPlanId = db.Column(db.ForeignKey('ExperimentalPlan.experimentalPlanId'), nullable=False, index=True)
    eventLogFilename = db.Column(db.String(255), nullable=False, info='url to shorlist file')
    dataSetId = db.Column(db.ForeignKey('DataSet.dataSetId'), nullable=False, index=True)
    autoprocessingProgrammId = db.Column(db.Integer, info='reference to AutoProcProgram.autoProcProgramId')

    DataSet = db.relationship('DataSet', primaryjoin='SsxDataAcquisition.dataSetId == DataSet.dataSetId')
    ExperimentalPlan = db.relationship('ExperimentalPlan', primaryjoin='SsxDataAcquisition.experimentalPlanId == ExperimentalPlan.experimentalPlanId')
    LoadedSample = db.relationship('LoadedSample', primaryjoin='SsxDataAcquisition.loadedSampleId == LoadedSample.loadedSampleId')



class TimedExcitation(db.Model):
    __tablename__ = 'TimedExcitation'

    timedExcitationId = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(255))
    repeatedSequenceId = db.Column(db.ForeignKey('RepeatedSequence.repeatedSequenceId'), index=True)
    eventTrainId = db.Column(db.ForeignKey('EventTrain.eventTrainId'), index=True)
    ssxExcitation = db.Column(db.String(255))

    EventTrain = db.relationship('EventTrain', primaryjoin='TimedExcitation.eventTrainId == EventTrain.eventTrainId')
    RepeatedSequence = db.relationship('RepeatedSequence', primaryjoin='TimedExcitation.repeatedSequenceId == RepeatedSequence.repeatedSequenceId')



class TimedXrayDetection(db.Model):
    __tablename__ = 'TimedXrayDetection'

    timedXrayDetectionId = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(255))
    repeatedSequenceId = db.Column(db.ForeignKey('RepeatedSequence.repeatedSequenceId'), index=True)
    eventTrainId = db.Column(db.ForeignKey('EventTrain.eventTrainId'), index=True)
    numberOfInternalTriggers = db.Column(db.Integer)
    internalTriggerPeriod = db.Column(db.Integer)
    internalGateDuration = db.Column(db.Integer)

    EventTrain = db.relationship('EventTrain', primaryjoin='TimedXrayDetection.eventTrainId == EventTrain.eventTrainId')
    RepeatedSequence = db.relationship('RepeatedSequence', primaryjoin='TimedXrayDetection.repeatedSequenceId == RepeatedSequence.repeatedSequenceId')



class TimedXrayExposure(db.Model):
    __tablename__ = 'TimedXrayExposure'

    timedXrayExposureId = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(255))
    repeatedSequenceId = db.Column(db.ForeignKey('RepeatedSequence.repeatedSequenceId'), index=True)
    eventTrainId = db.Column(db.ForeignKey('EventTrain.eventTrainId'), index=True)
    timedBunches = db.Column(db.String(255))
    shutter = db.Column(db.String(255))

    EventTrain = db.relationship('EventTrain', primaryjoin='TimedXrayExposure.eventTrainId == EventTrain.eventTrainId')
    RepeatedSequence = db.relationship('RepeatedSequence', primaryjoin='TimedXrayExposure.repeatedSequenceId == RepeatedSequence.repeatedSequenceId')

CREATE TABLE `CrystalSlurry` (
  `crystalSlurryId` int UNIQUE PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255),
  `crystalSizeDistributionId` int,
  `crystalDensity` float COMMENT '1/mm3',
  `bufferId` float COMMENT 'reference to Buffer.bufferId'
);

CREATE TABLE `CrystalSlurry_has_Crystal` (
  `CrystalSlurryHasCrystalId` int UNIQUE PRIMARY KEY AUTO_INCREMENT,
  `crystalSlurryId` int NOT NULL,
  `crystalId` int NOT NULL
);

CREATE TABLE `SampleStock` (
  `sampleStockId` int UNIQUE PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `crystalSlurryId` int NOT NULL,
  `concentrationFactor` float NOT NULL,
  `crystalDensity` float NOT NULL,
  `additiveId` int COMMENT 'reference to Additive.additiveId',
  `note` varchar(255)
);

CREATE TABLE `CrystalSizeDistribution` (
  `crystalSizeDistributionId` int UNIQUE PRIMARY KEY AUTO_INCREMENT,
  `crystalHabit` varchar(255),
  `characteristicDimensions` varchar(255),
  `minDimension` varchar(255) COMMENT 'comma separated floats',
  `maxDimension` varchar(255) COMMENT 'comma separated floats'
);

CREATE TABLE `Micrograph` (
  `micrographId` int UNIQUE PRIMARY KEY AUTO_INCREMENT,
  `crystalSlurryId` int NOT NULL,
  `url` varchar(255),
  `objectSidePixelSize` varchar(255) COMMENT 'comma separated two floats',
  `descriptionJson` varchar(255)
);

CREATE TABLE `LoadedSample` (
  `loadedSampleId` int UNIQUE PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255) COMMENT 'to be used as part of the image and processing file names',
  `sampleStockId` int,
  `sampleDeliveryDeviceId` int,
  `loadingPattern` int,
  `descriptionJson` varchar(255)
);

CREATE TABLE `SsxDataAcquisition` (
  `ssxDataAcquisitionId` int UNIQUE PRIMARY KEY AUTO_INCREMENT,
  `loadedSampleId` int NOT NULL,
  `dataCollectionId` int NOT NULL COMMENT 'reference to DataCollection.dataCollectionId',
  `experimentalPlanId` int NOT NULL,
  `eventLogFilename` varchar(255) NOT NULL COMMENT 'url to shorlist file',
  `dataSetId` int NOT NULL,
  `autoprocessingProgrammId` int COMMENT 'reference to AutoProcProgram.autoProcProgramId'
);

CREATE TABLE `DataSet` (
  `dataSetId` int UNIQUE PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `mergedResultsFilename` varchar(255)
);

CREATE TABLE `ExperimentalPlan` (
  `experimentalPlanId` int UNIQUE PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255),
  `numberOfRepetitions` int COMMENT 'for micro-fluidic, jet, tape but not for chip',
  `period` float COMMENT 'seconds but unknown/self adjusting for chip',
  `masterTriggerId` int,
  `repeatedSequenceId` int NOT NULL
);

CREATE TABLE `SampleDeliveryDevice` (
  `sampleDeliveryDeviceId` int UNIQUE PRIMARY KEY AUTO_INCREMENT,
  `type` ENUM ('photoChip', 'microFluidics', 'viscoousJet', 'tapeDevice'),
  `descriptionJson` varchar(255)
);

CREATE TABLE `MasterTrigger` (
  `masterTriggerId` int UNIQUE PRIMARY KEY AUTO_INCREMENT,
  `nameInEventLog` varchar(255),
  `triggerDevice` int,
  `descriptionJson` varchar(255)
);

CREATE TABLE `RepeatedSequence` (
  `repeatedSequenceId` int UNIQUE PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255)
);

CREATE TABLE `EventTrain` (
  `eventTrainId` int UNIQUE PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255),
  `timeOn` float COMMENT 'sec',
  `duration` float COMMENT 'sec',
  `period` float,
  `numberOfRepetitions` float,
  `nameInEventLog` varchar(255),
  `triggerDevice` varchar(255)
);

CREATE TABLE `TimedExcitation` (
  `timedExcitationId` int UNIQUE PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255),
  `repeatedSequenceId` int,
  `eventTrainId` int,
  `ssxExcitation` varchar(255)
);

CREATE TABLE `TimedXrayExposure` (
  `timedXrayExposureId` int UNIQUE PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255),
  `repeatedSequenceId` int,
  `eventTrainId` int,
  `timedBunches` varchar(255),
  `shutter` varchar(255)
);

CREATE TABLE `TimedXrayDetection` (
  `timedXrayDetectionId` int UNIQUE PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255),
  `repeatedSequenceId` int,
  `eventTrainId` int,
  `numberOfInternalTriggers` int,
  `internalTriggerPeriod` int,
  `internalGateDuration` int
);

ALTER TABLE `CrystalSlurry` ADD FOREIGN KEY (`crystalSizeDistributionId`) REFERENCES `CrystalSizeDistribution` (`crystalSizeDistributionId`);

ALTER TABLE `CrystalSlurry_has_Crystal` ADD FOREIGN KEY (`crystalSlurryId`) REFERENCES `CrystalSlurry` (`crystalSlurryId`);

ALTER TABLE `SampleStock` ADD FOREIGN KEY (`crystalSlurryId`) REFERENCES `CrystalSlurry` (`crystalSlurryId`);

ALTER TABLE `Micrograph` ADD FOREIGN KEY (`crystalSlurryId`) REFERENCES `CrystalSlurry` (`crystalSlurryId`);

ALTER TABLE `LoadedSample` ADD FOREIGN KEY (`sampleStockId`) REFERENCES `SampleStock` (`sampleStockId`);

ALTER TABLE `LoadedSample` ADD FOREIGN KEY (`sampleDeliveryDeviceId`) REFERENCES `SampleDeliveryDevice` (`sampleDeliveryDeviceId`);

ALTER TABLE `SsxDataAcquisition` ADD FOREIGN KEY (`loadedSampleId`) REFERENCES `LoadedSample` (`loadedSampleId`);

ALTER TABLE `SsxDataAcquisition` ADD FOREIGN KEY (`experimentalPlanId`) REFERENCES `ExperimentalPlan` (`experimentalPlanId`);

ALTER TABLE `SsxDataAcquisition` ADD FOREIGN KEY (`dataSetId`) REFERENCES `DataSet` (`dataSetId`);

ALTER TABLE `ExperimentalPlan` ADD FOREIGN KEY (`masterTriggerId`) REFERENCES `MasterTrigger` (`masterTriggerId`);

ALTER TABLE `ExperimentalPlan` ADD FOREIGN KEY (`repeatedSequenceId`) REFERENCES `RepeatedSequence` (`repeatedSequenceId`);

ALTER TABLE `TimedExcitation` ADD FOREIGN KEY (`repeatedSequenceId`) REFERENCES `RepeatedSequence` (`repeatedSequenceId`);

ALTER TABLE `TimedExcitation` ADD FOREIGN KEY (`eventTrainId`) REFERENCES `EventTrain` (`eventTrainId`);

ALTER TABLE `TimedXrayExposure` ADD FOREIGN KEY (`repeatedSequenceId`) REFERENCES `RepeatedSequence` (`repeatedSequenceId`);

ALTER TABLE `TimedXrayExposure` ADD FOREIGN KEY (`eventTrainId`) REFERENCES `EventTrain` (`eventTrainId`);

ALTER TABLE `TimedXrayDetection` ADD FOREIGN KEY (`repeatedSequenceId`) REFERENCES `RepeatedSequence` (`repeatedSequenceId`);

ALTER TABLE `TimedXrayDetection` ADD FOREIGN KEY (`eventTrainId`) REFERENCES `EventTrain` (`eventTrainId`);

ALTER TABLE `CrystalSlurry` COMMENT = "Describes sample as delivered to the beamline";

ALTER TABLE `SampleStock` COMMENT = "Describes sample prepared for loading on delivery device";

ALTER TABLE `CrystalSizeDistribution` COMMENT = "describes crystal mixture in suspension";

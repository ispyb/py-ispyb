CREATE TABLE `CrystalSlurry` (
  `crystalSlurryId` int UNIQUE PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255),
  `crystalId` int NOT NULL COMMENT 'refers to BLSample.Crystal',
  `crystalSizeDistributionId` int,
  `crystalDensity` float COMMENT '1/mm3',
  `bufferId` float COMMENT 'reference to Buffer.bufferId',
  `micrographId` int NOT NULL
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
  `characteristicDimensions` float,
  `minDimension` varchar(255) COMMENT 'comma separated floats',
  `maxDimension` float COMMENT 'comma separated floats'
);

CREATE TABLE `Micrograph` (
  `micrographId` int UNIQUE PRIMARY KEY AUTO_INCREMENT,
  `url` varchar(255),
  `objectSidePixelSize` varchar(255) COMMENT 'comma separated two floats',
  `description` varchar(255)
);

CREATE TABLE `LoadedSample` (
  `loadedSampleId` int UNIQUE PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255) COMMENT 'Used for image and processing file names',
  `sampleStockId` int,
  `sampleDeliveryDevice` int,
  `loadingPattern` int,
  `description` text
);

CREATE TABLE `SsxDataAcquisition` (
  `ssxDataAcquisitionId` int UNIQUE PRIMARY KEY AUTO_INCREMENT,
  `loadedSampleId` int NOT NULL,
  `dataCollectionId` int NOT NULL COMMENT 'reference to DataCollection.dataCollectionId',
  `experimentalPlanId` int NOT NULL,
  `shortList` varchar(255) NOT NULL COMMENT 'url to shorlist file',
  `autoprocessingProgrammId` int COMMENT 'reference to AutoProcProgram.autoProcProgramId'
);

CREATE TABLE `DataSet` (
  `dataSetId` int UNIQUE PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `ssxDataAcquisitionId` int,
  `mergedResults` varchar(255)
);

CREATE TABLE `ExperimentalPlan` (
  `experimentalPlanId` int UNIQUE PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255),
  `numberOfRepetitions` int COMMENT 'for micro-fluidic, jet, tape but not for chip',
  `period` float COMMENT 'seconds but unknown/self adjusting for chip',
  `masterTriggerId` int,
  `repeatedSequenceId` int NOT NULL
);

CREATE TABLE `MasterTrigger` (
  `masterTriggerId` int UNIQUE PRIMARY KEY AUTO_INCREMENT,
  `nameInShortlist` varchar(255),
  `triggerDevice` int,
  `description` varchar(255)
);

CREATE TABLE `RepeatedSequence` (
  `repeatedSequenceId` int UNIQUE PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255)
);

CREATE TABLE `RepeatedSequenceHasAction` (
  `repeatedSequenceHasActionId` int UNIQUE PRIMARY KEY AUTO_INCREMENT,
  `repeatedSequenceId` int,
  `timedExcitationId` int,
  `timedXrayExposureId` int,
  `timedXrayDetectionId` int
);

CREATE TABLE `TimedSequence` (
  `timedSequenceId` int UNIQUE PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255),
  `timeOn` float COMMENT 'sec',
  `timeOff` float COMMENT 'sec',
  `nameInShortlist` varchar(255),
  `triggerDevice` varchar(255)
);

CREATE TABLE `TimedExcitation` (
  `timedExcitationId` int UNIQUE PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255),
  `timedSequenceId` int,
  `ssxExcitation` varchar(255)
);

CREATE TABLE `TimedXrayExposure` (
  `timedXrayExposureId` int UNIQUE PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255),
  `timedSequenceId` int,
  `timedBunches` varchar(255),
  `shutter` varchar(255)
);

CREATE TABLE `TimedXrayDetection` (
  `timedXrayDetectionId` int UNIQUE PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255),
  `timedSequenceId` int,
  `numberOfInternalTriggers` int,
  `internalTriggerPeriod` int,
  `internalGateDuration` int
);

ALTER TABLE `CrystalSlurry` ADD FOREIGN KEY (`crystalSizeDistributionId`) REFERENCES `CrystalSizeDistribution` (`crystalSizeDistributionId`);

ALTER TABLE `CrystalSlurry` ADD FOREIGN KEY (`micrographId`) REFERENCES `Micrograph` (`micrographId`);

ALTER TABLE `SampleStock` ADD FOREIGN KEY (`crystalSlurryId`) REFERENCES `CrystalSlurry` (`crystalSlurryId`);

ALTER TABLE `LoadedSample` ADD FOREIGN KEY (`sampleStockId`) REFERENCES `SampleStock` (`sampleStockId`);

ALTER TABLE `SsxDataAcquisition` ADD FOREIGN KEY (`loadedSampleId`) REFERENCES `LoadedSample` (`loadedSampleId`);

ALTER TABLE `SsxDataAcquisition` ADD FOREIGN KEY (`experimentalPlanId`) REFERENCES `ExperimentalPlan` (`experimentalPlanId`);

ALTER TABLE `DataSet` ADD FOREIGN KEY (`ssxDataAcquisitionId`) REFERENCES `SsxDataAcquisition` (`ssxDataAcquisitionId`);

ALTER TABLE `ExperimentalPlan` ADD FOREIGN KEY (`masterTriggerId`) REFERENCES `MasterTrigger` (`masterTriggerId`);

ALTER TABLE `ExperimentalPlan` ADD FOREIGN KEY (`repeatedSequenceId`) REFERENCES `RepeatedSequence` (`repeatedSequenceId`);

ALTER TABLE `RepeatedSequenceHasAction` ADD FOREIGN KEY (`repeatedSequenceId`) REFERENCES `RepeatedSequence` (`repeatedSequenceId`);

ALTER TABLE `RepeatedSequenceHasAction` ADD FOREIGN KEY (`timedExcitationId`) REFERENCES `TimedExcitation` (`timedExcitationId`);

ALTER TABLE `RepeatedSequenceHasAction` ADD FOREIGN KEY (`timedXrayExposureId`) REFERENCES `TimedXrayExposure` (`timedXrayExposureId`);

ALTER TABLE `RepeatedSequenceHasAction` ADD FOREIGN KEY (`timedXrayDetectionId`) REFERENCES `TimedXrayDetection` (`timedXrayDetectionId`);

ALTER TABLE `TimedExcitation` ADD FOREIGN KEY (`timedSequenceId`) REFERENCES `TimedSequence` (`timedSequenceId`);

ALTER TABLE `TimedXrayExposure` ADD FOREIGN KEY (`timedSequenceId`) REFERENCES `TimedSequence` (`timedSequenceId`);

ALTER TABLE `TimedXrayDetection` ADD FOREIGN KEY (`timedSequenceId`) REFERENCES `TimedSequence` (`timedSequenceId`);

ALTER TABLE `CrystalSlurry` COMMENT = "Describes sample as delivered to the beamline";

ALTER TABLE `SampleStock` COMMENT = "Describes sample prepared for loading on delivery device";

ALTER TABLE `CrystalSizeDistribution` COMMENT = "describes crystal mixture in suspension";

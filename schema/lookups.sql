-- MariaDB dump 10.17  Distrib 10.4.11-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: ispyb_build
-- ------------------------------------------------------
-- Server version	10.4.11-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Dumping data for table `AdminVar`
--

/*!40000 ALTER TABLE `AdminVar` DISABLE KEYS */;
INSERT INTO `AdminVar` (`varId`, `name`, `value`) VALUES (4,'schemaVersion','1.10.4');
/*!40000 ALTER TABLE `AdminVar` ENABLE KEYS */;

--
-- Dumping data for table `SchemaStatus`
--

/*!40000 ALTER TABLE `SchemaStatus` DISABLE KEYS */;
INSERT INTO `SchemaStatus` (`schemaStatusId`, `scriptName`, `schemaStatus`, `recordTimeStamp`) VALUES (6,'20180213_BLSample_subLocation.sql','DONE','2018-02-13 13:27:19'),(12,'20180213_DataCollectionFileAttachment_fileType.sql','DONE','2018-02-13 15:12:54'),(16,'20180303_v_run_to_table.sql','DONE','2018-07-25 15:11:18'),(19,'20180328_ImageQualityIndicators_alter_table.sql','DONE','2018-07-25 15:11:18'),(22,'20180410_BeamLineSetup_alter.sql','DONE','2018-07-25 15:11:18'),(25,'20180413_BeamLineSetup_and_Detector_alter.sql','DONE','2018-07-25 15:11:18'),(28,'20180501_DataCollectionGroup_experimentType_enum.sql','DONE','2018-07-25 15:11:18'),(31,'20180531_ScreeningOutput_alignmentSuccess.sql','DONE','2018-07-25 15:11:18'),(34,'20180629_DataCollection_imageContainerSubPath.sql','DONE','2018-07-25 15:11:18'),(35,'20180913_BeamCalendar.sql','DONE','2018-09-19 09:52:45'),(36,'2018_09_19_DataCollection_imageDirectory_comment.sql','DONE','2018-09-19 12:38:01'),(37,'2018_09_27_increase_schema_version.sql','DONE','2018-09-27 13:17:15'),(38,'2018_11_01_XrayCenteringResult.sql','DONE','2018-11-01 13:36:53'),(39,'2018_11_01_AutoProcProgram_dataCollectionId.sql','DONE','2018-11-01 15:10:38'),(40,'2018_11_01_AutoProcProgramMessage.sql','DONE','2018-11-01 15:28:17'),(44,'2018_11_01_DiffractionPlan_centeringMethod.sql','DONE','2018-11-01 22:51:36'),(45,'2018_11_02_DataCollectionGroup_experimentType_enum.sql','DONE','2018-11-02 11:54:15'),(47,'2018_11_05_spelling_of_centring.sql','DONE','2018-11-05 15:31:38'),(48,'2018_11_09_AutoProcProgram_update_processing_program.sql','DONE','2018-11-09 16:38:34'),(49,'2018_11_14_AutoProcProgramMessage_autoinc.sql','DONE','2018-11-14 10:15:27'),(50,'2018_11_22_AutoProcProgram_processingStatus_update.sql','DONE','2018-11-22 16:11:15'),(51,'2018_12_04_EnergyScan_and_XFEFluorescenceSpectrum_add_axisPosition.sql','DONE','2018-12-04 14:13:23'),(52,'2018_12_20_DataCollectionGroup_scanParameters.sql','DONE','2018-12-20 17:30:04'),(53,'2019_01_14_Proposal_state.sql','DONE','2019-01-14 12:13:31'),(54,'2019_01_14_ProcessingJobParameter_parameterValue.sql','DONE','2019-01-14 14:00:02'),(57,'2019_01_15_Detector_localName.sql','DONE','2019-01-15 23:01:15'),(58,'2019_02_04_BLSession_unique_index.sql','DONE','2019-02-04 13:52:19'),(59,'2019_03_29_BLSession_archived.sql','DONE','2019-04-03 14:43:08'),(60,'2019_04_03_UserGroup_and_Permission.sql','DONE','2019-04-03 14:51:04'),(61,'2019_04_07_AdminVar_bump_version.sql','DONE','2019-04-07 11:35:06'),(62,'2019_04_08_AdminVar_bump_version.sql','DONE','2019-04-08 15:38:01'),(63,'2019_04_23_AdminVar_bump_version.sql','DONE','2019-04-23 11:13:27'),(64,'2019_04_23_drop_v_run_view.sql','DONE','2019-04-23 11:13:35'),(67,'2019_04_23_v_run_additional_runs.sql','DONE','2019-04-23 12:39:47'),(68,'2019_05_28_AdminVar_bump_version.sql','DONE','2019-05-28 13:29:27'),(72,'2019_07_17_BLSample_crystalId_default.sql','DONE','2019-07-17 15:21:59'),(73,'2019_08_15_Sleeve.sql','DONE','2019-08-15 08:34:34'),(74,'2019_08_15_AdminVar_bump_version.sql','DONE','2019-08-15 08:57:37'),(75,'2019_08_28_AdminVar_bump_version.sql','DONE','2019-08-28 13:30:13'),(76,'2019_08_30_AdminVar_bump_version.sql','DONE','2019-08-30 11:58:16'),(77,'2019_10_06_BLSampleImage_fk3.sql','DONE','2019-10-06 16:55:44'),(78,'2019_10_08_DiffractionPlan_experimentKind.sql','DONE','2019-10-08 12:47:10'),(79,'2019_11_07_AutoProcProgramAttachment_importanceRank.sql','DONE','2019-11-07 16:35:25'),(80,'2019_11_07_AdminVar_bump_version.sql','DONE','2019-11-07 16:45:44'),(81,'2019_11_08_AdminVar_bump_version.sql','DONE','2019-11-08 16:09:52'),(82,'2019_11_26_v_run_idx1.sql','DONE','2019-11-26 15:00:21'),(83,'2019_12_02_AdminVar_bump_version.sql','DONE','2019-12-02 11:29:05'),(84,'2019_12_02_AdminVar_bump_version_v2.sql','DONE','2019-12-02 18:14:11'),(85,'2020_01_03_BLSampleImage_tables.sql','DONE','2020-01-03 16:05:45'),(86,'2020_01_06_AdminVar_bump_version.sql','DONE','2020-01-06 11:45:02'),(87,'2020_01_07_AdminVar_bump_version.sql','DONE','2020-01-07 09:45:25'),(88,'2020_01_07_AdminVar_bump_version_v2.sql','DONE','2020-01-07 10:24:54'),(89,'2020_01_07_AdminVar_bump_version_v3.sql','DONE','2020-01-07 11:16:09'),(90,'2020_01_20_AdminVar_bump_version.sql','DONE','2020-01-20 13:40:52'),(91,'2020_01_20_AdminVar_bump_version_v2.sql','DONE','2020-01-20 16:27:37');
/*!40000 ALTER TABLE `SchemaStatus` ENABLE KEYS */;

--
-- Dumping data for table `ComponentType`
--

/*!40000 ALTER TABLE `ComponentType` DISABLE KEYS */;
INSERT INTO `ComponentType` (`componentTypeId`, `name`) VALUES (1,'Protein'),(2,'DNA'),(3,'Small Molecule'),(4,'RNA');
/*!40000 ALTER TABLE `ComponentType` ENABLE KEYS */;

--
-- Dumping data for table `ComponentSubType`
--

/*!40000 ALTER TABLE `ComponentSubType` DISABLE KEYS */;
INSERT INTO `ComponentSubType` (`componentSubTypeId`, `name`, `hasPh`) VALUES (1,'Buffer',1),(2,'Precipitant',0),(3,'Salt',0);
/*!40000 ALTER TABLE `ComponentSubType` ENABLE KEYS */;

--
-- Dumping data for table `ConcentrationType`
--

/*!40000 ALTER TABLE `ConcentrationType` DISABLE KEYS */;
INSERT INTO `ConcentrationType` (`concentrationTypeId`, `name`, `symbol`) VALUES (1,'Molar','M'),(2,'Percentage Weight / Volume','%(w/v)'),(3,'Percentage Volume / Volume','%(v/v)'),(4,'Milligrams / Millilitre','mg/ml'),(5,'Grams','g');
/*!40000 ALTER TABLE `ConcentrationType` ENABLE KEYS */;

--
-- Dumping data for table `InspectionType`
--

/*!40000 ALTER TABLE `InspectionType` DISABLE KEYS */;
INSERT INTO `InspectionType` (`inspectionTypeId`, `name`) VALUES (1,'Visible'),(2,'UV');
/*!40000 ALTER TABLE `InspectionType` ENABLE KEYS */;

--
-- Dumping data for table `PlateType`
--

/*!40000 ALTER TABLE `PlateType` DISABLE KEYS */;
/*!40000 ALTER TABLE `PlateType` ENABLE KEYS */;

--
-- Dumping data for table `SessionType`
--

/*!40000 ALTER TABLE `SessionType` DISABLE KEYS */;
/*!40000 ALTER TABLE `SessionType` ENABLE KEYS */;

--
-- Dumping data for table `WorkflowType`
--

/*!40000 ALTER TABLE `WorkflowType` DISABLE KEYS */;
/*!40000 ALTER TABLE `WorkflowType` ENABLE KEYS */;

--
-- Dumping data for table `Schedule`
--

/*!40000 ALTER TABLE `Schedule` DISABLE KEYS */;
INSERT INTO `Schedule` (`scheduleId`, `name`) VALUES (1,'Daily - 1 week'),(2,'Schedule 2'),(11,'Fibonacci'),(15,'3 Hour Interval');
/*!40000 ALTER TABLE `Schedule` ENABLE KEYS */;

--
-- Dumping data for table `Imager`
--

/*!40000 ALTER TABLE `Imager` DISABLE KEYS */;
INSERT INTO `Imager` (`imagerId`, `name`, `temperature`, `serial`, `capacity`) VALUES (2,'Imager1 20c',20,'Z125434',1000),(7,'VMXi sim',20,'RI1000-0000',750);
/*!40000 ALTER TABLE `Imager` ENABLE KEYS */;

--
-- Dumping data for table `Detector`
--

/*!40000 ALTER TABLE `Detector` DISABLE KEYS */;
INSERT INTO `Detector` (`detectorId`, `detectorType`, `detectorManufacturer`, `detectorModel`, `detectorPixelSizeHorizontal`, `detectorPixelSizeVertical`, `DETECTORMAXRESOLUTION`, `DETECTORMINRESOLUTION`, `detectorSerialNumber`, `detectorDistanceMin`, `detectorDistanceMax`, `trustedPixelValueRangeLower`, `trustedPixelValueRangeUpper`, `sensorThickness`, `overload`, `XGeoCorr`, `YGeoCorr`, `detectorMode`, `density`, `composition`, `numberOfPixelsX`, `numberOfPixelsY`, `detectorRollMin`, `detectorRollMax`, `localName`) VALUES (4,'Photon counting','In-house','Excalibur',NULL,NULL,NULL,NULL,'1109-434',100,300,NULL,NULL,NULL,NULL,NULL,NULL,NULL,55,'CrO3Br5Sr10',NULL,NULL,NULL,NULL,NULL),(8,'Diamond XPDF detector',NULL,NULL,NULL,NULL,NULL,NULL,'1109-761',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,10.4,'C+Br+He',NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `Detector` ENABLE KEYS */;

--
-- Dumping data for table `DewarLocationList`
--

/*!40000 ALTER TABLE `DewarLocationList` DISABLE KEYS */;
/*!40000 ALTER TABLE `DewarLocationList` ENABLE KEYS */;

--
-- Dumping data for table `BeamLineSetup`
--

/*!40000 ALTER TABLE `BeamLineSetup` DISABLE KEYS */;
INSERT INTO `BeamLineSetup` (`beamLineSetupId`, `detectorId`, `synchrotronMode`, `undulatorType1`, `undulatorType2`, `undulatorType3`, `focalSpotSizeAtSample`, `focusingOptic`, `beamDivergenceHorizontal`, `beamDivergenceVertical`, `polarisation`, `monochromatorType`, `setupDate`, `synchrotronName`, `maxExpTimePerDataCollection`, `maxExposureTimePerImage`, `minExposureTimePerImage`, `goniostatMaxOscillationSpeed`, `goniostatMaxOscillationWidth`, `goniostatMinOscillationWidth`, `maxTransmission`, `minTransmission`, `recordTimeStamp`, `CS`, `beamlineName`, `beamSizeXMin`, `beamSizeXMax`, `beamSizeYMin`, `beamSizeYMax`, `energyMin`, `energyMax`, `omegaMin`, `omegaMax`, `kappaMin`, `kappaMax`, `phiMin`, `phiMax`, `active`, `numberOfImagesMax`, `numberOfImagesMin`, `boxSizeXMin`, `boxSizeXMax`, `boxSizeYMin`, `boxSizeYMax`, `monoBandwidthMin`, `monoBandwidthMax`) VALUES (1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2007-04-26 00:00:00','Diamond Light Source',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-19 22:56:25',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `BeamLineSetup` ENABLE KEYS */;

--
-- Dumping data for table `BF_component`
--

/*!40000 ALTER TABLE `BF_component` DISABLE KEYS */;
/*!40000 ALTER TABLE `BF_component` ENABLE KEYS */;

--
-- Dumping data for table `BF_subcomponent`
--

/*!40000 ALTER TABLE `BF_subcomponent` DISABLE KEYS */;
/*!40000 ALTER TABLE `BF_subcomponent` ENABLE KEYS */;

--
-- Dumping data for table `BF_system`
--

/*!40000 ALTER TABLE `BF_system` DISABLE KEYS */;
/*!40000 ALTER TABLE `BF_system` ENABLE KEYS */;

--
-- Dumping data for table `Permission`
--

/*!40000 ALTER TABLE `Permission` DISABLE KEYS */;
INSERT INTO `Permission` (`permissionId`, `type`, `description`) VALUES (1,'mx_admin','MX Administrator'),(2,'manage_groups','Manage User Groups'),(4,'manage_perms','Manage User Group Permissions'),(5,'global_stats','View Global Statistics'),(6,'fault_view','View Fault Reports'),(7,'saxs_admin','SAXS Administrator'),(8,'em_admin','EM Administrator'),(9,'gen_admin','Powder Admin'),(10,'tomo_admin','Tomo Admin'),(11,'super_admin','Site Admin'),(12,'fault_global','Globally edit all faults'),(13,'schedules','Manage Imaging Schedules'),(15,'schedule_comps','Manage Imaging Schedule Components'),(16,'imaging_dash','Imaging Dashboard'),(17,'vmxi_queue','VMXi Data Collection Queue'),(18,'sm_admin','Small Molecule Admin'),(20,'pow_admin','Power Admin'),(23,'all_dewars','View All Dewars'),(26,'all_prop_stats','View All Proposal Stats'),(29,'all_breakdown','View Aggregated Visit Breakdown Stats'),(32,'disp_cont','VMXi Dispose Container'),(37,'view_manifest','View Shipping Manifest'),(43,'schedule_comp','typo fill in'),(49,'xpdf_admin','XPDF Admin'),(55,'edit_presets','Edit Beamline DC Presets'),(58,'manage_params','Edit Beamline Parameter Limits'),(64,'manage_detector','Manage Beamline Detector Limits'),(69,'auto_dash','AutoCollect Dashboard'),(77,'fault_admin','Edit Fault Categories'),(80,'fault_add','Add New Fault Reports');
/*!40000 ALTER TABLE `Permission` ENABLE KEYS */;

--
-- Dumping data for table `BLSampleImageAutoScoreSchema`
--

/*!40000 ALTER TABLE `BLSampleImageAutoScoreSchema` DISABLE KEYS */;
INSERT INTO `BLSampleImageAutoScoreSchema` (`blSampleImageAutoScoreSchemaId`, `schemaName`, `enabled`) VALUES (1,'MARCO',1);
/*!40000 ALTER TABLE `BLSampleImageAutoScoreSchema` ENABLE KEYS */;

--
-- Dumping data for table `BLSampleImageAutoScoreClass`
--

/*!40000 ALTER TABLE `BLSampleImageAutoScoreClass` DISABLE KEYS */;
INSERT INTO `BLSampleImageAutoScoreClass` (`blSampleImageAutoScoreClassId`, `blSampleImageAutoScoreSchemaId`, `scoreClass`) VALUES (1,1,'clear'),(2,1,'crystal'),(3,1,'precipitant'),(4,1,'other');
/*!40000 ALTER TABLE `BLSampleImageAutoScoreClass` ENABLE KEYS */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-01-20 16:27:53

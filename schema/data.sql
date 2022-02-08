-- MariaDB dump 10.17  Distrib 10.4.8-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: ispyb_build
-- ------------------------------------------------------
-- Server version	10.4.8-MariaDB

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
-- Dumping data for table `AbInitioModel`
--

/*!40000 ALTER TABLE `AbInitioModel` DISABLE KEYS */;
/*!40000 ALTER TABLE `AbInitioModel` ENABLE KEYS */;

--
-- Dumping data for table `Additive`
--

/*!40000 ALTER TABLE `Additive` DISABLE KEYS */;
/*!40000 ALTER TABLE `Additive` ENABLE KEYS */;

--
-- Dumping data for table `AdminActivity`
--

/*!40000 ALTER TABLE `AdminActivity` DISABLE KEYS */;
/*!40000 ALTER TABLE `AdminActivity` ENABLE KEYS */;

--
-- Dumping data for table `Aperture`
--

/*!40000 ALTER TABLE `Aperture` DISABLE KEYS */;
/*!40000 ALTER TABLE `Aperture` ENABLE KEYS */;

--
-- Dumping data for table `Assembly`
--

/*!40000 ALTER TABLE `Assembly` DISABLE KEYS */;
/*!40000 ALTER TABLE `Assembly` ENABLE KEYS */;

--
-- Dumping data for table `AssemblyHasMacromolecule`
--

/*!40000 ALTER TABLE `AssemblyHasMacromolecule` DISABLE KEYS */;
/*!40000 ALTER TABLE `AssemblyHasMacromolecule` ENABLE KEYS */;

--
-- Dumping data for table `AssemblyRegion`
--

/*!40000 ALTER TABLE `AssemblyRegion` DISABLE KEYS */;
/*!40000 ALTER TABLE `AssemblyRegion` ENABLE KEYS */;

--
-- Dumping data for table `AutoProc`
--

/*!40000 ALTER TABLE `AutoProc` DISABLE KEYS */;
INSERT INTO `AutoProc` (`autoProcId`, `autoProcProgramId`, `spaceGroup`, `refinedCell_a`, `refinedCell_b`, `refinedCell_c`, `refinedCell_alpha`, `refinedCell_beta`, `refinedCell_gamma`, `recordTimeStamp`) VALUES (596406,56425592,'P 6 2 2',92.5546,92.5546,129.784,90,90,120,'2016-01-14 12:46:22'),(596411,56425944,'P 63 2 2',92.53,92.53,129.75,90,90,120,'2016-01-14 13:09:51'),(596418,56425952,'P 61 2 2',92.6461,92.6461,129.879,90,90,120,'2016-01-14 13:24:22'),(596419,56425963,'P 63 2 2',92.511,92.511,129.722,90,90,120,'2016-01-14 13:34:34'),(596420,56426286,'P 61 2 2',92.693,92.693,129.839,90,90,120,'2016-01-14 14:01:57'),(596421,56426287,'P 63 2 2',92.64,92.64,129.77,90,90,120,'2016-01-14 14:13:57'),(603708,56983954,'I 2 3',78.1548,78.1548,78.1548,90,90,90,'2016-01-22 11:34:03'),(603731,56985584,'I 2 3',78.15,78.15,78.15,90,90,90,'2016-01-22 11:52:36'),(603732,56985589,'I 2 3',78.157,78.157,78.157,90,90,90,'2016-01-22 11:53:38'),(603735,56985592,'I 2 3',78.15,78.15,78.15,90,90,90,'2016-01-22 11:54:01'),(603744,56986673,'I 2 3',78.1381,78.1381,78.1381,90,90,90,'2016-01-22 12:01:59');
/*!40000 ALTER TABLE `AutoProc` ENABLE KEYS */;

--
-- Dumping data for table `AutoProcIntegration`
--

/*!40000 ALTER TABLE `AutoProcIntegration` DISABLE KEYS */;
INSERT INTO `AutoProcIntegration` (`autoProcIntegrationId`, `dataCollectionId`, `autoProcProgramId`, `startImageNumber`, `endImageNumber`, `refinedDetectorDistance`, `refinedXBeam`, `refinedYBeam`, `rotationAxisX`, `rotationAxisY`, `rotationAxisZ`, `beamVectorX`, `beamVectorY`, `beamVectorZ`, `cell_a`, `cell_b`, `cell_c`, `cell_alpha`, `cell_beta`, `cell_gamma`, `recordTimeStamp`, `anomalous`) VALUES (592508,993677,56425592,NULL,NULL,NULL,209.131,215.722,NULL,NULL,NULL,NULL,NULL,NULL,92.5546,92.5546,129.784,90,90,120,'2016-01-14 12:46:22',0),(592513,993677,56425944,1,3600,193.939,209.052,215.618,NULL,NULL,NULL,NULL,NULL,NULL,92.532,92.532,129.747,90,90,120,'2016-01-14 13:09:51',0),(592520,993677,56425952,1,3600,194.077,209.062,215.62,NULL,NULL,NULL,NULL,NULL,NULL,92.6461,92.6461,129.879,90,90,120,'2016-01-14 13:24:22',0),(592521,993677,56425963,1,3600,193.893,209.135,215.719,NULL,NULL,NULL,NULL,NULL,NULL,92.5114,92.5114,129.722,90,90,120,'2016-01-14 13:34:35',0),(592522,993677,56426286,1,3600,194.077,209.062,215.62,NULL,NULL,NULL,NULL,NULL,NULL,92.6461,92.6461,129.879,90,90,120,'2016-01-14 14:01:57',0),(592523,993677,56426286,1,1800,194.147,209.069,215.622,NULL,NULL,NULL,NULL,NULL,NULL,92.7867,92.7867,129.759,90,90,120,'2016-01-14 14:01:57',0),(592524,993677,56426287,1,3600,193.939,209.052,215.618,NULL,NULL,NULL,NULL,NULL,NULL,92.531,92.531,129.745,90,90,120,'2016-01-14 14:13:57',0),(592525,993677,56426287,1,1800,194.388,209.058,215.61,NULL,NULL,NULL,NULL,NULL,NULL,92.847,92.847,129.817,90,90,120,'2016-01-14 14:13:57',0),(600339,1002287,56983954,NULL,NULL,NULL,209.264,215.741,NULL,NULL,NULL,NULL,NULL,NULL,78.1548,78.1548,78.1548,90,90,90,'2016-01-22 11:34:03',0),(600362,1002287,56985584,1,7200,175.977,209.186,215.643,NULL,NULL,NULL,NULL,NULL,NULL,78.153,78.153,78.153,90,90,90,'2016-01-22 11:52:36',0),(600363,1002287,56985589,1,7200,176.262,209.264,215.741,NULL,NULL,NULL,NULL,NULL,NULL,78.1569,78.1569,78.1569,90,90,90,'2016-01-22 11:53:38',0),(600366,1002287,56985592,1,7200,176.239,209.177,215.651,NULL,NULL,NULL,NULL,NULL,NULL,78.153,78.153,78.153,90,90,90,'2016-01-22 11:54:01',0),(600376,1002287,56986673,1,7200,176.219,209.178,215.653,NULL,NULL,NULL,NULL,NULL,NULL,78.1381,78.1381,78.1381,90,90,90,'2016-01-22 12:01:59',0);
/*!40000 ALTER TABLE `AutoProcIntegration` ENABLE KEYS */;

--
-- Dumping data for table `AutoProcProgram`
--

/*!40000 ALTER TABLE `AutoProcProgram` DISABLE KEYS */;
INSERT INTO `AutoProcProgram` (`autoProcProgramId`, `processingCommandLine`, `processingPrograms`, `processingStatus`, `processingMessage`, `processingStartTime`, `processingEndTime`, `processingEnvironment`, `recordTimeStamp`, `processingJobId`, `dataCollectionId`) VALUES (56425592,'/dls_sw/apps/fast_dp/2395/src/fast_dp.py -a S -j 0 -J 18 /dls/i03/data/2016/cm14451-1/20160114/tlys_jan_4/tlys_jan_4_1_0001.cbf','fast_dp',1,NULL,NULL,NULL,NULL,'2016-01-14 12:46:22',NULL,NULL),(56425944,'xia2 min_images=3 -3dii -xparallel -1 -atom s -blend -project cm14451v1 -crystal xtlysjan41 -ispyb_xml_out ispyb.xml image=/dls/i03/data/2016/cm14451-1/20160114/tlys_jan_4/tlys_jan_4_1_0001.cbf','xia2 3dii',1,NULL,NULL,NULL,NULL,'2016-01-14 13:09:51',NULL,NULL),(56425952,'xia2 min_images=3 -dials -xparallel -1 -atom s -blend -project cm14451v1 -crystal xtlysjan41 -ispyb_xml_out ispyb.xml image=/dls/i03/data/2016/cm14451-1/20160114/tlys_jan_4/tlys_jan_4_1_0001.cbf','xia2 dials',1,NULL,NULL,NULL,NULL,'2016-01-14 13:24:22',NULL,NULL),(56425963,'/dls_sw/apps/GPhL/autoPROC/20151214/autoPROC/bin/linux64/process -xml -Id xtlysjan41,/dls/i03/data/2016/cm14451-1/20160114/tlys_jan_4/,tlys_jan_4_1_####.cbf,1,3600 autoPROC_XdsKeyword_MAXIMUM_NUMBER_OF_PROCESSORS=12 autoPROC_XdsKeyword_MAXIMUM_NUMBER_OF_J','autoPROC 1.0.4 (see: http://www.globalphasing.com/autoproc/)',1,NULL,NULL,NULL,NULL,'2016-01-14 13:34:34',NULL,NULL),(56426286,'xia2 min_images=3 -dials -atom s -blend -ispyb_xml_out ispyb.xml image=/dls/i03/data/2016/cm14451-1/20160114/tlys_jan_4/linediffraction_1_0001.cbf image=/dls/i03/data/2016/cm14451-1/20160114/tlys_jan_4/tlys_jan_4_1_0001.cbf','xia2 dials',1,NULL,NULL,NULL,NULL,'2016-01-14 14:01:57',NULL,NULL),(56426287,'xia2 min_images=3 -3dii -atom s -blend -ispyb_xml_out ispyb.xml image=/dls/i03/data/2016/cm14451-1/20160114/tlys_jan_4/linediffraction_1_0001.cbf image=/dls/i03/data/2016/cm14451-1/20160114/tlys_jan_4/tlys_jan_4_1_0001.cbf','xia2 3dii',1,NULL,NULL,NULL,NULL,'2016-01-14 14:13:57',NULL,NULL),(56983954,'/dls_sw/apps/fast_dp/2395/src/fast_dp.py -a S -j 0 -J 18 /dls/i03/data/2016/cm14451-1/20160122/gw/ins2/001/ins2_2_0001.cbf','fast_dp',1,NULL,NULL,NULL,NULL,'2016-01-22 11:34:03',NULL,NULL),(56985584,'xia2 min_images=3 -3d -xparallel -1 -atom s -blend -project cm14451v1 -crystal xins22 -ispyb_xml_out ispyb.xml image=/dls/i03/data/2016/cm14451-1/20160122/gw/ins2/001/ins2_2_0001.cbf','xia2 3d',1,NULL,NULL,NULL,NULL,'2016-01-22 11:52:36',NULL,NULL),(56985589,'/dls_sw/apps/GPhL/autoPROC/20151214/autoPROC/bin/linux64/process -xml -Id xins22,/dls/i03/data/2016/cm14451-1/20160122/gw/ins2/001/,ins2_2_####.cbf,1,7200 autoPROC_XdsKeyword_MAXIMUM_NUMBER_OF_PROCESSORS=12 autoPROC_XdsKeyword_MAXIMUM_NUMBER_OF_JOBS=4 Sto','autoPROC 1.0.4 (see: http://www.globalphasing.com/autoproc/)',1,NULL,NULL,NULL,NULL,'2016-01-22 11:53:38',NULL,NULL),(56985592,'xia2 min_images=3 -3dii -xparallel -1 -atom s -blend -project cm14451v1 -crystal xins22 -ispyb_xml_out ispyb.xml image=/dls/i03/data/2016/cm14451-1/20160122/gw/ins2/001/ins2_2_0001.cbf','xia2 3dii',1,NULL,NULL,NULL,NULL,'2016-01-22 11:54:01',NULL,NULL),(56986673,'xia2 min_images=3 -dials -xparallel -1 -atom s -blend -project cm14451v1 -crystal xins22 -ispyb_xml_out ispyb.xml image=/dls/i03/data/2016/cm14451-1/20160122/gw/ins2/001/ins2_2_0001.cbf','xia2 dials',1,NULL,NULL,NULL,NULL,'2016-01-22 12:01:59',5,NULL);
/*!40000 ALTER TABLE `AutoProcProgram` ENABLE KEYS */;

--
-- Dumping data for table `AutoProcProgramAttachment`
--

/*!40000 ALTER TABLE `AutoProcProgramAttachment` DISABLE KEYS */;
INSERT INTO `AutoProcProgramAttachment` (`autoProcProgramAttachmentId`, `autoProcProgramId`, `fileType`, `fileName`, `filePath`, `recordTimeStamp`, `importanceRank`) VALUES (1023947,56425592,'Log','fast_dp.log','/dls/i03/data/2016/cm14451-1/processed/20160114/tlys_jan_4/tlys_jan_4_1_/fast_dp','2016-01-14 12:46:22',NULL),(1023955,56425944,'Result','cm14451v1_xtlysjan41_free.mtz','/dls/i03/data/2016/cm14451-1/processed/20160114/tlys_jan_4/tlys_jan_4_1_/xia2/3dii-run/DataFiles','2016-01-14 13:09:51',NULL),(1023956,56425944,'Log','xia2.html','/dls/i03/data/2016/cm14451-1/processed/20160114/tlys_jan_4/tlys_jan_4_1_/xia2/3dii-run','2016-01-14 13:09:51',NULL),(1023969,56425952,'Result','cm14451v1_xtlysjan41_free.mtz','/dls/i03/data/2016/cm14451-1/processed/20160114/tlys_jan_4/tlys_jan_4_1_/xia2/dials-run/DataFiles','2016-01-14 13:24:22',NULL),(1023970,56425952,'Log','xia2.html','/dls/i03/data/2016/cm14451-1/processed/20160114/tlys_jan_4/tlys_jan_4_1_/xia2/dials-run','2016-01-14 13:24:22',NULL),(1023971,56425963,'Log','autoPROC.log','/dls/i03/data/2016/cm14451-1/processed/20160114/tlys_jan_4/tlys_jan_4_1_/autoPROC/ap-run','2016-01-14 13:34:34',NULL),(1023972,56425963,'Result','truncate-unique.mtz','/dls/i03/data/2016/cm14451-1/processed/20160114/tlys_jan_4/tlys_jan_4_1_/autoPROC/ap-run','2016-01-14 13:34:34',NULL),(1023973,56426286,'Result','AUTOMATIC_DEFAULT_free.mtz','/dls/i03/data/2016/cm14451-1/processed/20160114/tlys_jan_4/linediffraction_1_/multi-xia2/dials/DataFiles','2016-01-14 14:01:57',NULL),(1023974,56426286,'Log','xia2.html','/dls/i03/data/2016/cm14451-1/processed/20160114/tlys_jan_4/linediffraction_1_/multi-xia2/dials','2016-01-14 14:01:57',NULL),(1023975,56426287,'Result','AUTOMATIC_DEFAULT_free.mtz','/dls/i03/data/2016/cm14451-1/processed/20160114/tlys_jan_4/linediffraction_1_/multi-xia2/3dii/DataFiles','2016-01-14 14:13:57',NULL),(1023976,56426287,'Log','xia2.html','/dls/i03/data/2016/cm14451-1/processed/20160114/tlys_jan_4/linediffraction_1_/multi-xia2/3dii','2016-01-14 14:13:57',NULL),(1037121,56983954,'Log','fast_dp.log','/dls/i03/data/2016/cm14451-1/processed/20160122/gw/ins2/001/ins2_2_/fast_dp','2016-01-22 11:34:03',NULL),(1037160,56985584,'Result','cm14451v1_xins22_free.mtz','/dls/i03/data/2016/cm14451-1/processed/20160122/gw/ins2/001/ins2_2_/xia2/3d-run/DataFiles','2016-01-22 11:52:36',NULL),(1037161,56985584,'Log','xia2.html','/dls/i03/data/2016/cm14451-1/processed/20160122/gw/ins2/001/ins2_2_/xia2/3d-run','2016-01-22 11:52:36',NULL),(1037162,56985589,'Log','autoPROC.log','/dls/i03/data/2016/cm14451-1/processed/20160122/gw/ins2/001/ins2_2_/autoPROC/ap-run','2016-01-22 11:53:38',NULL),(1037163,56985589,'Result','truncate-unique.mtz','/dls/i03/data/2016/cm14451-1/processed/20160122/gw/ins2/001/ins2_2_/autoPROC/ap-run','2016-01-22 11:53:38',NULL),(1037168,56985592,'Result','cm14451v1_xins22_free.mtz','/dls/i03/data/2016/cm14451-1/processed/20160122/gw/ins2/001/ins2_2_/xia2/3dii-run/DataFiles','2016-01-22 11:54:01',NULL),(1037169,56985592,'Log','xia2.html','/dls/i03/data/2016/cm14451-1/processed/20160122/gw/ins2/001/ins2_2_/xia2/3dii-run','2016-01-22 11:54:01',NULL),(1037183,56986673,'Result','cm14451v1_xins22_free.mtz','/dls/i03/data/2016/cm14451-1/processed/20160122/gw/ins2/001/ins2_2_/xia2/dials-run/DataFiles','2016-01-22 12:01:59',NULL),(1037184,56986673,'Log','xia2.html','/dls/i03/data/2016/cm14451-1/processed/20160122/gw/ins2/001/ins2_2_/xia2/dials-run','2016-01-22 12:01:59',NULL);
/*!40000 ALTER TABLE `AutoProcProgramAttachment` ENABLE KEYS */;

--
-- Dumping data for table `AutoProcProgramMessage`
--

/*!40000 ALTER TABLE `AutoProcProgramMessage` DISABLE KEYS */;
/*!40000 ALTER TABLE `AutoProcProgramMessage` ENABLE KEYS */;

--
-- Dumping data for table `AutoProcScaling`
--

/*!40000 ALTER TABLE `AutoProcScaling` DISABLE KEYS */;
INSERT INTO `AutoProcScaling` (`autoProcScalingId`, `autoProcId`, `recordTimeStamp`) VALUES (596133,596406,'2016-01-14 12:46:22'),(596138,596411,'2016-01-14 13:09:51'),(596145,596418,'2016-01-14 13:24:22'),(596146,596419,'2016-01-14 13:34:35'),(596147,596420,'2016-01-14 14:01:57'),(596148,596421,'2016-01-14 14:13:57'),(603434,603708,'2016-01-22 11:34:03'),(603457,603731,'2016-01-22 11:52:36'),(603458,603732,'2016-01-22 11:53:38'),(603461,603735,'2016-01-22 11:54:01'),(603470,603744,'2016-01-22 12:01:59');
/*!40000 ALTER TABLE `AutoProcScaling` ENABLE KEYS */;

--
-- Dumping data for table `AutoProcScalingStatistics`
--

/*!40000 ALTER TABLE `AutoProcScalingStatistics` DISABLE KEYS */;
INSERT INTO `AutoProcScalingStatistics` (`autoProcScalingStatisticsId`, `autoProcScalingId`, `scalingStatisticsType`, `comments`, `resolutionLimitLow`, `resolutionLimitHigh`, `rMerge`, `rMeasWithinIPlusIMinus`, `rMeasAllIPlusIMinus`, `rPimWithinIPlusIMinus`, `rPimAllIPlusIMinus`, `fractionalPartialBias`, `nTotalObservations`, `nTotalUniqueObservations`, `meanIOverSigI`, `completeness`, `multiplicity`, `anomalousCompleteness`, `anomalousMultiplicity`, `recordTimeStamp`, `anomalous`, `ccHalf`, `ccAnomalous`) VALUES (1770617,596133,'outerShell',NULL,1.65,1.61,0.766,NULL,0.789,NULL,NULL,NULL,105090,3089,5.5,97.8,34,96.8,17.8,'2016-01-14 12:46:22',0,91.7,15.8),(1770618,596133,'innerShell',NULL,29.5,7.18,0.061,NULL,0.063,NULL,NULL,NULL,17093,593,61.7,98.6,28.8,100,19.5,'2016-01-14 12:46:22',0,99.9,73.4),(1770619,596133,'overall',NULL,29.5,1.61,0.106,NULL,0.109,NULL,NULL,NULL,1588225,43478,30.2,99.8,36.5,99.8,19.4,'2016-01-14 12:46:22',0,99.9,60.5),(1770632,596138,'outerShell',NULL,1.49,1.45,1.326,NULL,1.419,0.506,0.365,NULL,61482,4245,2,99.8,14.5,99.5,7.4,'2016-01-14 13:09:51',0,0.584,-0.059),(1770633,596138,'innerShell',NULL,68.18,6.48,0.064,NULL,0.07,0.015,0.012,NULL,23609,800,58.6,99.8,29.5,100,19.7,'2016-01-14 13:09:51',0,0.998,0.732),(1770634,596138,'overall',NULL,68.18,1.45,0.116,NULL,0.123,0.028,0.021,NULL,1942930,58601,22.9,99.9,33.2,99.9,17.4,'2016-01-14 13:09:51',0,0.999,0.592),(1770653,596145,'outerShell',NULL,1.46,1.42,3.758,NULL,4.107,1.67,1.216,NULL,42977,4422,2.2,97.9,9.7,96.3,5,'2016-01-14 13:24:22',0,0.497,-0.012),(1770654,596145,'innerShell',NULL,129.88,6.35,0.09,NULL,0.095,0.02,0.017,NULL,28041,858,32,100,32.7,100,21.3,'2016-01-14 13:24:22',0,0.996,0.556),(1770655,596145,'overall',NULL,129.88,1.42,0.177,NULL,0.184,0.045,0.033,NULL,1942399,62483,16.4,99.8,31.1,99.7,16.2,'2016-01-14 13:24:22',0,0.999,0.343),(1770656,596146,'outerShell',NULL,1.476,1.451,1.268,1.314,1.312,0.459,0.33,NULL,42945,2859,2.4,99.2,15,98.9,7.8,'2016-01-14 13:34:35',0,0.633,-0.059),(1770657,596146,'innerShell',NULL,129.722,3.938,0.08,0.078,0.081,0.017,0.014,NULL,103297,3251,50.7,100,31.8,99.7,19.1,'2016-01-14 13:34:35',0,0.993,-0.169),(1770658,596146,'overall',NULL,129.722,1.451,0.138,0.141,0.141,0.032,0.024,NULL,1953227,58523,22.5,100,33.4,100,17.8,'2016-01-14 13:34:35',0,0.996,0.035),(1770659,596147,'outerShell',NULL,1.47,1.43,3.442,NULL,3.711,1.471,1.058,NULL,46996,4388,1.6,99,10.7,97.8,5.5,'2016-01-14 14:01:57',0,0.627,-0.004),(1770660,596147,'innerShell',NULL,129.84,6.4,0.124,NULL,0.129,0.023,0.019,NULL,41147,842,27,100,48.9,100,31.8,'2016-01-14 14:01:57',0,0.996,0.532),(1770661,596147,'overall',NULL,129.84,1.43,0.707,NULL,0.719,0.156,0.114,NULL,2865527,61286,14.1,99.9,46.8,99.8,24.3,'2016-01-14 14:01:57',0,0.998,0.175),(1770662,596148,'outerShell',NULL,1.47,1.43,1.278,NULL,1.362,0.447,0.326,NULL,66780,4414,1.7,99.2,15.1,97,7.8,'2016-01-14 14:13:57',0,0.564,-0.056),(1770663,596148,'innerShell',NULL,80.23,6.4,0.106,NULL,0.112,0.02,0.017,NULL,36380,837,58.7,100,43.5,100,28.9,'2016-01-14 14:13:57',0,0.987,0.717),(1770664,596148,'overall',NULL,80.23,1.43,0.166,NULL,0.172,0.032,0.024,NULL,2926200,61215,22.9,99.9,47.8,99.8,25,'2016-01-14 14:13:57',0,0.997,0.589),(1792520,603434,'outerShell',NULL,1.57,1.53,0.765,NULL,0.775,NULL,NULL,NULL,64789,889,7.4,97.6,72.9,97.3,37,'2016-01-22 11:34:03',0,97.7,-4.8),(1792521,603434,'innerShell',NULL,27.63,6.84,0.043,NULL,0.044,NULL,NULL,NULL,10404,156,144.1,98.6,66.7,99,39.5,'2016-01-22 11:34:03',0,100,74.1),(1792522,603434,'overall',NULL,27.63,1.53,0.073,NULL,0.074,NULL,NULL,NULL,946151,12186,50.8,99.8,77.6,99.8,40,'2016-01-22 11:34:03',0,100,41.3),(1792589,603457,'outerShell',NULL,1.38,1.34,3.435,NULL,3.586,0.744,0.543,NULL,57789,1347,1.2,100,42.9,100,21.2,'2016-01-22 11:52:36',0,0.622,-0.017),(1792590,603457,'innerShell',NULL,31.9,6,0.044,NULL,0.046,0.007,0.006,NULL,15766,225,131.3,99.6,70.1,100,40.5,'2016-01-22 11:52:36',0,1,0.665),(1792591,603457,'overall',NULL,31.9,1.34,0.08,NULL,0.082,0.013,0.009,NULL,1309987,17989,34.2,100,72.8,100,37.2,'2016-01-22 11:52:36',0,1,0.484),(1792592,603458,'outerShell',NULL,1.4,1.376,2.142,2.136,2.156,0.345,0.249,NULL,60591,813,2.4,100,74.5,100,38.1,'2016-01-22 11:53:38',0,0.908,0.059),(1792593,603458,'innerShell',NULL,39.079,3.735,0.045,0.044,0.045,0.007,0.005,NULL,64542,887,114,99.9,72.8,99.9,40.2,'2016-01-22 11:53:38',0,1,0.267),(1792594,603458,'overall',NULL,39.079,1.376,0.083,0.084,0.083,0.013,0.009,NULL,1275766,16626,35,100,76.7,100,39.9,'2016-01-22 11:53:38',0,1,0.217),(1792601,603461,'outerShell',NULL,1.38,1.34,3.444,NULL,3.597,0.746,0.545,NULL,57746,1347,1.2,100,42.9,100,21.2,'2016-01-22 11:54:01',0,0.647,0.002),(1792602,603461,'innerShell',NULL,31.9,6,0.044,NULL,0.046,0.007,0.006,NULL,15773,225,131.2,99.6,70.1,100,40.5,'2016-01-22 11:54:01',0,1,0.654),(1792603,603461,'overall',NULL,31.9,1.34,0.08,NULL,0.082,0.013,0.009,NULL,1314502,17989,34.2,100,73.1,100,37.3,'2016-01-22 11:54:01',0,1,0.469),(1792628,603470,'outerShell',NULL,1.36,1.33,3.124,NULL,3.246,0.711,0.515,NULL,53402,1370,1.3,100,39,100,19.2,'2016-01-22 12:01:59',0,0.703,0.017),(1792629,603470,'innerShell',NULL,39.07,5.95,0.051,NULL,0.053,0.008,0.006,NULL,16799,235,117.7,99.7,71.5,100,41.9,'2016-01-22 12:01:59',0,1,0.654),(1792630,603470,'overall',NULL,39.07,1.33,0.08,NULL,0.082,0.013,0.009,NULL,1305126,18395,30.9,100,71,100,36.1,'2016-01-22 12:01:59',0,1,0.482);
/*!40000 ALTER TABLE `AutoProcScalingStatistics` ENABLE KEYS */;

--
-- Dumping data for table `AutoProcScaling_has_Int`
--

/*!40000 ALTER TABLE `AutoProcScaling_has_Int` DISABLE KEYS */;
INSERT INTO `AutoProcScaling_has_Int` (`autoProcScaling_has_IntId`, `autoProcScalingId`, `autoProcIntegrationId`, `recordTimeStamp`) VALUES (592507,596133,592508,'2016-01-14 12:46:22'),(592512,596138,592513,'2016-01-14 13:09:51'),(592519,596145,592520,'2016-01-14 13:24:22'),(592520,596146,592521,'2016-01-14 13:34:35'),(592521,596147,592522,'2016-01-14 14:01:57'),(592522,596147,592523,'2016-01-14 14:01:57'),(592523,596148,592524,'2016-01-14 14:13:57'),(592524,596148,592525,'2016-01-14 14:13:57'),(600338,603434,600339,'2016-01-22 11:34:03'),(600361,603457,600362,'2016-01-22 11:52:36'),(600362,603458,600363,'2016-01-22 11:53:38'),(600365,603461,600366,'2016-01-22 11:54:01'),(600375,603470,600376,'2016-01-22 12:01:59');
/*!40000 ALTER TABLE `AutoProcScaling_has_Int` ENABLE KEYS */;

--
-- Dumping data for table `AutoProcStatus`
--

/*!40000 ALTER TABLE `AutoProcStatus` DISABLE KEYS */;
/*!40000 ALTER TABLE `AutoProcStatus` ENABLE KEYS */;

--
-- Dumping data for table `BF_component_beamline`
--

/*!40000 ALTER TABLE `BF_component_beamline` DISABLE KEYS */;
/*!40000 ALTER TABLE `BF_component_beamline` ENABLE KEYS */;

--
-- Dumping data for table `BF_fault`
--

/*!40000 ALTER TABLE `BF_fault` DISABLE KEYS */;
/*!40000 ALTER TABLE `BF_fault` ENABLE KEYS */;

--
-- Dumping data for table `BF_subcomponent_beamline`
--

/*!40000 ALTER TABLE `BF_subcomponent_beamline` DISABLE KEYS */;
/*!40000 ALTER TABLE `BF_subcomponent_beamline` ENABLE KEYS */;

--
-- Dumping data for table `BF_system_beamline`
--

/*!40000 ALTER TABLE `BF_system_beamline` DISABLE KEYS */;
/*!40000 ALTER TABLE `BF_system_beamline` ENABLE KEYS */;

--
-- Dumping data for table `BLSample`
--

/*!40000 ALTER TABLE `BLSample` DISABLE KEYS */;
INSERT INTO `BLSample` (`blSampleId`, `diffractionPlanId`, `crystalId`, `containerId`, `name`, `code`, `location`, `holderLength`, `loopLength`, `loopType`, `wireWidth`, `comments`, `completionStage`, `structureStage`, `publicationStage`, `publicationComments`, `blSampleStatus`, `isInSampleChanger`, `lastKnownCenteringPosition`, `POSITIONID`, `recordTimeStamp`, `SMILES`, `blSubSampleId`, `lastImageURL`, `screenComponentGroupId`, `volume`, `dimension1`, `dimension2`, `dimension3`, `shape`, `packingFraction`, `preparationTemeprature`, `preparationHumidity`, `blottingTime`, `blottingForce`, `blottingDrainTime`, `support`, `subLocation`) VALUES (11550,NULL,3918,1326,'Sample-001','SAM-011550','1',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-17 16:16:11',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(11553,NULL,3921,1326,'Sample-002','SAM-011553','2',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-17 16:21:43',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(11556,NULL,3924,1326,'Sample-003','SAM-011556','3',NULL,NULL,NULL,NULL,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-17 16:27:25',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(11559,NULL,3927,1329,'Sample-004','SAM-011559','1',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-17 16:27:25',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(11562,NULL,3930,1329,'Sample-005','SAM-011562','2',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-17 16:27:25',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(11565,NULL,3933,1329,'Sample-006','SAM-011565','3',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-17 16:27:25',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(11568,NULL,3936,1332,'Sample-007','SAM-011568','1',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-17 16:27:25',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(11571,NULL,3939,1332,'Sample-008','SAM-011571','2',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-17 16:27:25',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(11574,NULL,3942,1332,'Sample-009','SAM-011574','3',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-17 16:27:25',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(11577,NULL,3942,1335,'Sample-010','SAM-011577','1',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-17 16:27:25',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(11580,NULL,3942,1335,'Sample-011','SAM-011580','2',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-17 16:27:25',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(11583,NULL,3951,1335,'Sample-012','SAM-011583','3',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-17 16:27:25',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(11586,NULL,3954,NULL,'Sample-013','SAM-011586',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-17 16:27:25',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(11589,NULL,3957,NULL,'Sample-014','SAM-011589',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-17 16:27:25',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(11592,NULL,3960,NULL,'Sample-015','SAM-011592',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-17 16:27:25',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(374695,NULL,310037,33049,'tlys_jan_4','HA00AU3712','4',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-19 22:57:04',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(398810,197784,333301,34864,'thau8','HA00AK8934','8',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-19 22:57:05',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(398816,197784,310037,34874,'thau88','HH00AU3788','1',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-09-30 14:21:28',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(398819,197784,310037,34877,'thau99','HH00AU3799','1',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-10-05 10:15:47',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(398824,NULL,333308,34883,'XPDF-1','XPDF-0001',NULL,NULL,NULL,NULL,NULL,'Test sample for XPDF',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-10-26 14:47:58',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(398827,NULL,333308,34883,'XPDF-2','XPDF-0002',NULL,NULL,NULL,NULL,NULL,'Test sample for XPDF',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-10-26 14:51:23',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `BLSample` ENABLE KEYS */;

--
-- Dumping data for table `BLSampleGroup`
--

/*!40000 ALTER TABLE `BLSampleGroup` DISABLE KEYS */;
INSERT INTO `BLSampleGroup` (`blSampleGroupId`) VALUES (5);
/*!40000 ALTER TABLE `BLSampleGroup` ENABLE KEYS */;

--
-- Dumping data for table `BLSampleGroup_has_BLSample`
--

/*!40000 ALTER TABLE `BLSampleGroup_has_BLSample` DISABLE KEYS */;
INSERT INTO `BLSampleGroup_has_BLSample` (`blSampleGroupId`, `blSampleId`, `groupOrder`, `type`) VALUES (5,398824,1,'background'),(5,398827,2,'sample');
/*!40000 ALTER TABLE `BLSampleGroup_has_BLSample` ENABLE KEYS */;

--
-- Dumping data for table `BLSampleImage`
--

/*!40000 ALTER TABLE `BLSampleImage` DISABLE KEYS */;
INSERT INTO `BLSampleImage` (`blSampleImageId`, `blSampleId`, `micronsPerPixelX`, `micronsPerPixelY`, `imageFullPath`, `blSampleImageScoreId`, `comments`, `blTimeStamp`, `containerInspectionId`, `modifiedTimeStamp`) VALUES (2,398819,NULL,NULL,'/dls/i03/data/2016/cm1234-5/something.jpg',NULL,NULL,'2016-10-05 11:23:33',NULL,NULL),(5,398816,1.1,1.2,'/dls/i03/data/2016/cm1234-5/something-else.jpg',NULL,NULL,'2016-10-10 14:31:06',4,NULL);
/*!40000 ALTER TABLE `BLSampleImage` ENABLE KEYS */;

--
-- Dumping data for table `BLSampleImageAnalysis`
--

/*!40000 ALTER TABLE `BLSampleImageAnalysis` DISABLE KEYS */;
INSERT INTO `BLSampleImageAnalysis` (`blSampleImageAnalysisId`, `blSampleImageId`, `oavSnapshotBefore`, `oavSnapshotAfter`, `deltaX`, `deltaY`, `goodnessOfFit`, `scaleFactor`, `resultCode`, `matchStartTimeStamp`, `matchEndTimeStamp`) VALUES (4,5,'/dls/i02-2/data/2016/cm14559-5/.ispyb/something.jpg',NULL,10,11,0.94,0.5,'OK','2016-12-09 12:32:24','2016-12-09 12:32:25');
/*!40000 ALTER TABLE `BLSampleImageAnalysis` ENABLE KEYS */;

--
-- Dumping data for table `BLSampleImageMeasurement`
--

/*!40000 ALTER TABLE `BLSampleImageMeasurement` DISABLE KEYS */;
/*!40000 ALTER TABLE `BLSampleImageMeasurement` ENABLE KEYS */;

--
-- Dumping data for table `BLSampleImageScore`
--

/*!40000 ALTER TABLE `BLSampleImageScore` DISABLE KEYS */;
INSERT INTO `BLSampleImageScore` (`blSampleImageScoreId`, `name`, `score`, `colour`) VALUES (1,'Clear',0,'#cccccc'),(2,'Contaminated',1,'#fffd96'),(3,'Light Precipitate',2,'#fdfd96'),(4,'Phase Separation',4,'#fdfd96'),(5,'Spherulites',5,'#ffb347'),(6,'Microcrystals',6,'#ffb347'),(7,'1D Crystals',7,'#87ceeb'),(8,'2D Crystals',8,'#77dd77'),(9,'3D Crystals',9,'#77dd77'),(10,'Heavy Precipitate',3,'#ff6961');
/*!40000 ALTER TABLE `BLSampleImageScore` ENABLE KEYS */;

--
-- Dumping data for table `BLSampleType_has_Component`
--

/*!40000 ALTER TABLE `BLSampleType_has_Component` DISABLE KEYS */;
/*!40000 ALTER TABLE `BLSampleType_has_Component` ENABLE KEYS */;

--
-- Dumping data for table `BLSample_has_DataCollectionPlan`
--

/*!40000 ALTER TABLE `BLSample_has_DataCollectionPlan` DISABLE KEYS */;
INSERT INTO `BLSample_has_DataCollectionPlan` (`blSampleId`, `dataCollectionPlanId`, `planOrder`) VALUES (398824,197792,NULL),(398827,197792,NULL);
/*!40000 ALTER TABLE `BLSample_has_DataCollectionPlan` ENABLE KEYS */;

--
-- Dumping data for table `BLSample_has_EnergyScan`
--

/*!40000 ALTER TABLE `BLSample_has_EnergyScan` DISABLE KEYS */;
/*!40000 ALTER TABLE `BLSample_has_EnergyScan` ENABLE KEYS */;

--
-- Dumping data for table `BLSession`
--

/*!40000 ALTER TABLE `BLSession` DISABLE KEYS */;
INSERT INTO `BLSession` (`sessionId`, `beamLineSetupId`, `proposalId`, `beamCalendarId`, `projectCode`, `startDate`, `endDate`, `beamLineName`, `scheduled`, `nbShifts`, `comments`, `beamLineOperator`, `bltimeStamp`, `visit_number`, `usedFlag`, `sessionTitle`, `structureDeterminations`, `dewarTransport`, `databackupFrance`, `databackupEurope`, `expSessionPk`, `operatorSiteNumber`, `lastUpdate`, `protectedData`, `externalId`, `archived`) VALUES (55167,1,37027,NULL,NULL,'2016-01-01 09:00:00','2016-01-01 17:00:00','i03',NULL,NULL,'ghfg',NULL,'2015-12-21 15:20:43',1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'0000-00-00 00:00:00',NULL,NULL,0),(55168,1,37027,NULL,NULL,'2016-03-11 09:00:00','2016-03-11 17:00:00','i03',NULL,NULL,'jhgjh',NULL,'2015-12-21 15:20:44',2,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'0000-00-00 00:00:00',NULL,NULL,0),(339525,NULL,141666,NULL,NULL,NULL,NULL,'i03',NULL,NULL,NULL,NULL,'2016-03-16 16:08:29',1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'0000-00-00 00:00:00',NULL,NULL,0),(339528,NULL,141666,NULL,NULL,NULL,NULL,'i03',NULL,NULL,NULL,NULL,'2016-03-17 15:07:42',2,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'0000-00-00 00:00:00',NULL,NULL,0),(339531,NULL,141666,NULL,NULL,NULL,NULL,'i03',NULL,NULL,NULL,NULL,'2016-03-17 15:08:09',3,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'0000-00-00 00:00:00',NULL,NULL,0),(339535,NULL,37027,NULL,NULL,'2018-03-27 09:00:00','2018-07-27 09:00:00','i02-2',NULL,NULL,NULL,NULL,'2018-04-05 15:48:37',99,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'0000-00-00 00:00:00',NULL,NULL,0);
/*!40000 ALTER TABLE `BLSession` ENABLE KEYS */;

--
-- Dumping data for table `BLSession_has_SCPosition`
--

/*!40000 ALTER TABLE `BLSession_has_SCPosition` DISABLE KEYS */;
/*!40000 ALTER TABLE `BLSession_has_SCPosition` ENABLE KEYS */;

--
-- Dumping data for table `BLSubSample`
--

/*!40000 ALTER TABLE `BLSubSample` DISABLE KEYS */;
INSERT INTO `BLSubSample` (`blSubSampleId`, `blSampleId`, `diffractionPlanId`, `blSampleImageId`, `positionId`, `position2Id`, `motorPositionId`, `blSubSampleUUID`, `imgFileName`, `imgFilePath`, `comments`, `recordTimeStamp`) VALUES (2,398816,197784,NULL,2,5,NULL,NULL,NULL,NULL,NULL,'2016-09-30 14:25:19'),(5,398819,197784,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-10-05 10:16:44');
/*!40000 ALTER TABLE `BLSubSample` ENABLE KEYS */;

--
-- Dumping data for table `BeamApertures`
--

/*!40000 ALTER TABLE `BeamApertures` DISABLE KEYS */;
/*!40000 ALTER TABLE `BeamApertures` ENABLE KEYS */;

--
-- Dumping data for table `BeamCalendar`
--

/*!40000 ALTER TABLE `BeamCalendar` DISABLE KEYS */;
/*!40000 ALTER TABLE `BeamCalendar` ENABLE KEYS */;

--
-- Dumping data for table `BeamCentres`
--

/*!40000 ALTER TABLE `BeamCentres` DISABLE KEYS */;
/*!40000 ALTER TABLE `BeamCentres` ENABLE KEYS */;

--
-- Dumping data for table `BeamlineAction`
--

/*!40000 ALTER TABLE `BeamlineAction` DISABLE KEYS */;
/*!40000 ALTER TABLE `BeamlineAction` ENABLE KEYS */;

--
-- Dumping data for table `BeamlineStats`
--

/*!40000 ALTER TABLE `BeamlineStats` DISABLE KEYS */;
/*!40000 ALTER TABLE `BeamlineStats` ENABLE KEYS */;

--
-- Dumping data for table `Buffer`
--

/*!40000 ALTER TABLE `Buffer` DISABLE KEYS */;
/*!40000 ALTER TABLE `Buffer` ENABLE KEYS */;

--
-- Dumping data for table `BufferHasAdditive`
--

/*!40000 ALTER TABLE `BufferHasAdditive` DISABLE KEYS */;
/*!40000 ALTER TABLE `BufferHasAdditive` ENABLE KEYS */;

--
-- Dumping data for table `CTF`
--

/*!40000 ALTER TABLE `CTF` DISABLE KEYS */;
/*!40000 ALTER TABLE `CTF` ENABLE KEYS */;

--
-- Dumping data for table `CalendarHash`
--

/*!40000 ALTER TABLE `CalendarHash` DISABLE KEYS */;
/*!40000 ALTER TABLE `CalendarHash` ENABLE KEYS */;

--
-- Dumping data for table `ComponentLattice`
--

/*!40000 ALTER TABLE `ComponentLattice` DISABLE KEYS */;
INSERT INTO `ComponentLattice` (`componentLatticeId`, `componentId`, `spaceGroup`, `cell_a`, `cell_b`, `cell_c`, `cell_alpha`, `cell_beta`, `cell_gamma`) VALUES (1,123497,'P21',10.1,11.1,12.1,90.1,90.2,90.3);
/*!40000 ALTER TABLE `ComponentLattice` ENABLE KEYS */;

--
-- Dumping data for table `Component_has_SubType`
--

/*!40000 ALTER TABLE `Component_has_SubType` DISABLE KEYS */;
/*!40000 ALTER TABLE `Component_has_SubType` ENABLE KEYS */;

--
-- Dumping data for table `Container`
--

/*!40000 ALTER TABLE `Container` DISABLE KEYS */;
INSERT INTO `Container` (`containerId`, `dewarId`, `code`, `containerType`, `capacity`, `sampleChangerLocation`, `containerStatus`, `bltimeStamp`, `beamlineLocation`, `screenId`, `scheduleId`, `barcode`, `imagerId`, `sessionId`, `ownerId`, `requestedImagerId`, `requestedReturn`, `comments`, `experimentType`, `storageTemperature`, `containerRegistryId`) VALUES (1326,573,'Container-1-cm0001-1','Puck-16',16,'3','processing',NULL,'i03',NULL,NULL,'container-cm0001-1-0000001',NULL,NULL,NULL,NULL,0,NULL,NULL,NULL,4),(1329,573,'Container-2-cm0001-1','Puck-16',16,'4','processing',NULL,'i03',NULL,NULL,'container-cm0001-1-0000002',NULL,NULL,NULL,NULL,0,NULL,NULL,NULL,NULL),(1332,576,'Container-3-cm0001-1','Puck-16',16,'5','processing',NULL,'i03',NULL,NULL,'container-cm0001-1-0000003',NULL,NULL,NULL,NULL,0,NULL,NULL,NULL,NULL),(1335,579,'Container-4-cm0001-2','Puck-16',16,'6','processing',NULL,'i03',NULL,NULL,'container-cm0001-2-0001335',NULL,NULL,NULL,NULL,0,NULL,NULL,NULL,NULL),(1338,582,'Container-5-cm0001-3','Puck-16',16,'7','processing',NULL,'i03',NULL,NULL,'container-cm0001-3-0001338',NULL,NULL,NULL,NULL,0,NULL,NULL,NULL,NULL),(1341,573,'Manual',NULL,NULL,'9',NULL,NULL,'i03',NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,NULL,NULL,NULL,NULL),(33049,8287,'cm14451-1_i03r-002','Puck',16,NULL,'at DLS',NULL,'i03',NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,NULL,NULL,NULL,NULL),(34864,8572,'I03R-001','Puck',16,'29','processing','2016-02-24 12:13:05','i03',NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,NULL,NULL,NULL,NULL),(34874,8572,'test_plate2','CrystalQuickX',192,'3','in_storage','2016-02-12 09:20:44','i03',NULL,2,'test_plate2',2,NULL,NULL,2,0,NULL,NULL,NULL,NULL),(34877,8572,'test_plate3','CrystalQuickX',192,'3','in_storage','2016-10-04 10:50:05','i03',NULL,2,'test_plate3',2,NULL,NULL,2,0,NULL,NULL,NULL,NULL),(34879,8572,'test_plate4','CrystalQuickX',192,'4','processing',NULL,'i02-2',NULL,2,'test_plate4',2,NULL,NULL,2,0,NULL,NULL,NULL,NULL),(34883,NULL,'XPDF-container-1','XPDF container',NULL,NULL,'processing',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,NULL,NULL,NULL,NULL),(34888,8578,'TestSim01','CrystalQuickX',192,'1','in_storage',NULL,'i02-2',NULL,2,'VMXiSim-001',7,339535,1,7,0,NULL,NULL,NULL,5);
/*!40000 ALTER TABLE `Container` ENABLE KEYS */;

--
-- Dumping data for table `ContainerHistory`
--

/*!40000 ALTER TABLE `ContainerHistory` DISABLE KEYS */;
INSERT INTO `ContainerHistory` (`containerHistoryId`, `containerId`, `location`, `blTimeStamp`, `status`, `beamlineName`) VALUES (6,34874,'3','2016-09-30 12:56:21','in_localstorage','i03'),(7,34874,'3','2017-10-19 13:35:34','in_storage','i02-2');
/*!40000 ALTER TABLE `ContainerHistory` ENABLE KEYS */;

--
-- Dumping data for table `ContainerInspection`
--

/*!40000 ALTER TABLE `ContainerInspection` DISABLE KEYS */;
INSERT INTO `ContainerInspection` (`containerInspectionId`, `containerId`, `inspectionTypeId`, `imagerId`, `temperature`, `blTimeStamp`, `scheduleComponentid`, `state`, `priority`, `manual`, `scheduledTimeStamp`, `completedTimeStamp`) VALUES (4,34874,1,NULL,NULL,'2018-08-07 15:20:00',NULL,'Completed',99,NULL,'2018-08-07 12:08:00','2018-08-07 15:36:00');
/*!40000 ALTER TABLE `ContainerInspection` ENABLE KEYS */;

--
-- Dumping data for table `ContainerQueue`
--

/*!40000 ALTER TABLE `ContainerQueue` DISABLE KEYS */;
INSERT INTO `ContainerQueue` (`containerQueueId`, `containerId`, `personId`, `createdTimeStamp`, `completedTimeStamp`) VALUES (2,34874,NULL,'2016-09-30 12:56:21',NULL),(8,34877,NULL,'2016-10-05 09:09:59',NULL);
/*!40000 ALTER TABLE `ContainerQueue` ENABLE KEYS */;

--
-- Dumping data for table `ContainerQueueSample`
--

/*!40000 ALTER TABLE `ContainerQueueSample` DISABLE KEYS */;
INSERT INTO `ContainerQueueSample` (`containerQueueSampleId`, `containerQueueId`, `blSubSampleId`) VALUES (2,2,2);
/*!40000 ALTER TABLE `ContainerQueueSample` ENABLE KEYS */;

--
-- Dumping data for table `ContainerRegistry`
--

/*!40000 ALTER TABLE `ContainerRegistry` DISABLE KEYS */;
INSERT INTO `ContainerRegistry` (`containerRegistryId`, `barcode`, `comments`, `recordTimestamp`) VALUES (4,'DLS-0001',NULL,'2017-09-21 10:01:07'),(5,'VMXiSim-001',NULL,'2019-03-22 11:48:43');
/*!40000 ALTER TABLE `ContainerRegistry` ENABLE KEYS */;

--
-- Dumping data for table `ContainerRegistry_has_Proposal`
--

/*!40000 ALTER TABLE `ContainerRegistry_has_Proposal` DISABLE KEYS */;
/*!40000 ALTER TABLE `ContainerRegistry_has_Proposal` ENABLE KEYS */;

--
-- Dumping data for table `ContainerReport`
--

/*!40000 ALTER TABLE `ContainerReport` DISABLE KEYS */;
/*!40000 ALTER TABLE `ContainerReport` ENABLE KEYS */;

--
-- Dumping data for table `CourierTermsAccepted`
--

/*!40000 ALTER TABLE `CourierTermsAccepted` DISABLE KEYS */;
/*!40000 ALTER TABLE `CourierTermsAccepted` ENABLE KEYS */;

--
-- Dumping data for table `Crystal`
--

/*!40000 ALTER TABLE `Crystal` DISABLE KEYS */;
INSERT INTO `Crystal` (`crystalId`, `diffractionPlanId`, `proteinId`, `crystalUUID`, `name`, `spaceGroup`, `morphology`, `color`, `size_X`, `size_Y`, `size_Z`, `cell_a`, `cell_b`, `cell_c`, `cell_alpha`, `cell_beta`, `cell_gamma`, `comments`, `pdbFileName`, `pdbFilePath`, `recordTimeStamp`, `abundance`, `theoreticalDensity`) VALUES (3918,NULL,4380,NULL,'Crystal 01',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-17 16:11:19',NULL,NULL),(3921,NULL,4383,NULL,'Crystal 02',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-17 16:11:19',NULL,NULL),(3924,NULL,4386,NULL,'Crystal 03',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-17 16:11:19',NULL,NULL),(3927,NULL,4389,NULL,'Crystal 04',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-17 16:11:19',NULL,NULL),(3930,NULL,4392,NULL,'Crystal 05',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-17 16:11:19',NULL,NULL),(3933,NULL,4395,NULL,'Crystal 06',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-17 16:11:19',NULL,NULL),(3936,NULL,4398,NULL,'Crystal 07',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-17 16:11:19',NULL,NULL),(3939,NULL,4401,NULL,'Crystal 08',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-17 16:11:19',NULL,NULL),(3942,NULL,4404,NULL,'Crystal 09',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-17 16:11:19',NULL,NULL),(3945,NULL,4407,NULL,'Crystal 10',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-17 16:11:19',NULL,NULL),(3948,NULL,4407,NULL,'Crystal 11',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-17 16:11:19',NULL,NULL),(3951,NULL,4410,NULL,'Crystal 12',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-17 16:11:19',NULL,NULL),(3954,NULL,4410,NULL,'Crystal 13',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-17 16:11:19',NULL,NULL),(3957,NULL,4413,NULL,'Crystal 14',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-17 16:11:19',NULL,NULL),(3960,NULL,4413,NULL,'Crystal 15',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-17 16:11:19',NULL,NULL),(310037,NULL,121393,NULL,'crystal-4-cm14451-1',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-19 22:58:00',NULL,NULL),(333301,NULL,123491,NULL,NULL,'P41212',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-19 22:58:00',NULL,NULL),(333308,NULL,123497,NULL,'SampleType01','P12121',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'sample type comments ...',NULL,NULL,'2017-03-23 22:06:42',NULL,NULL);
/*!40000 ALTER TABLE `Crystal` ENABLE KEYS */;

--
-- Dumping data for table `Crystal_has_UUID`
--

/*!40000 ALTER TABLE `Crystal_has_UUID` DISABLE KEYS */;
/*!40000 ALTER TABLE `Crystal_has_UUID` ENABLE KEYS */;

--
-- Dumping data for table `DataAcquisition`
--

/*!40000 ALTER TABLE `DataAcquisition` DISABLE KEYS */;
/*!40000 ALTER TABLE `DataAcquisition` ENABLE KEYS */;

--
-- Dumping data for table `DataCollection`
--

/*!40000 ALTER TABLE `DataCollection` DISABLE KEYS */;
INSERT INTO `DataCollection` (`dataCollectionId`, `BLSAMPLEID`, `SESSIONID`, `experimenttype`, `dataCollectionNumber`, `startTime`, `endTime`, `runStatus`, `axisStart`, `axisEnd`, `axisRange`, `overlap`, `numberOfImages`, `startImageNumber`, `numberOfPasses`, `exposureTime`, `imageDirectory`, `imagePrefix`, `imageSuffix`, `imageContainerSubPath`, `fileTemplate`, `wavelength`, `resolution`, `detectorDistance`, `xBeam`, `yBeam`, `comments`, `printableForReport`, `CRYSTALCLASS`, `slitGapVertical`, `slitGapHorizontal`, `transmission`, `synchrotronMode`, `xtalSnapshotFullPath1`, `xtalSnapshotFullPath2`, `xtalSnapshotFullPath3`, `xtalSnapshotFullPath4`, `rotationAxis`, `phiStart`, `kappaStart`, `omegaStart`, `chiStart`, `resolutionAtCorner`, `detector2Theta`, `DETECTORMODE`, `undulatorGap1`, `undulatorGap2`, `undulatorGap3`, `beamSizeAtSampleX`, `beamSizeAtSampleY`, `centeringMethod`, `averageTemperature`, `ACTUALSAMPLEBARCODE`, `ACTUALSAMPLESLOTINCONTAINER`, `ACTUALCONTAINERBARCODE`, `ACTUALCONTAINERSLOTINSC`, `actualCenteringPosition`, `beamShape`, `dataCollectionGroupId`, `POSITIONID`, `detectorId`, `FOCALSPOTSIZEATSAMPLEX`, `POLARISATION`, `FOCALSPOTSIZEATSAMPLEY`, `APERTUREID`, `screeningOrigId`, `startPositionId`, `endPositionId`, `flux`, `strategySubWedgeOrigId`, `blSubSampleId`, `flux_end`, `bestWilsonPlotPath`, `processedDataFile`, `datFullPath`, `magnification`, `totalAbsorbedDose`, `binning`, `particleDiameter`, `boxSize_CTF`, `minResolution`, `minDefocus`, `maxDefocus`, `defocusStepSize`, `amountAstigmatism`, `extractSize`, `bgRadius`, `voltage`, `objAperture`, `c1aperture`, `c2aperture`, `c3aperture`, `c1lens`, `c2lens`, `c3lens`, `totalExposedDose`, `nominalMagnification`, `nominalDefocus`, `imageSizeX`, `imageSizeY`, `pixelSizeOnImage`, `phasePlate`) VALUES (993677,374695,55167,NULL,1,'2016-01-14 12:40:34','2016-01-14 12:41:54','DataCollection Successful',45,0.1,0.1,0,3600,1,1,0.02,'/dls/i03/data/2016/cm14451-1/20160114/tlys_jan_4/','tlys_jan_4','cbf',NULL,'tlys_jan_4_1_####.cbf',1.28255,1.6,193.087,215.62,208.978,'(-402,345,142) EDNAStrategy4: subWedge:1Aperture: Medium',1,NULL,0.059918,0.099937,40.1936,'User','/dls/i03/data/2016/cm14451-1/jpegs/20160114/tlys_jan_4/tlys_jan_4_1_1_315.0.png','/dls/i03/data/2016/cm14451-1/jpegs/20160114/tlys_jan_4/tlys_jan_4_1_1_225.0.png','/dls/i03/data/2016/cm14451-1/jpegs/20160114/tlys_jan_4/tlys_jan_4_1_1_135.0.png','/dls/i03/data/2016/cm14451-1/jpegs/20160114/tlys_jan_4/tlys_jan_4_1_1_45.0.png','Omega',NULL,NULL,45,NULL,NULL,NULL,NULL,5.685,NULL,NULL,0.05,0.02,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,988855,595236,NULL,80,NULL,20,6,NULL,NULL,NULL,833107367454.3083,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(1002287,NULL,55167,NULL,2,'2016-01-22 11:25:18','2016-01-22 11:28:23','DataCollection Successful',0,0.1,0.1,0,7200,1,1,0.025,'/dls/i03/data/2016/cm14451-1/20160122/gw/ins2/001/','ins2','cbf',NULL,'ins2_2_####.cbf',1.2,1.41777,175,215.618,209.102,'(-307,322,-184) Aperture: Large',1,NULL,0.059918,0.099937,0.999423,'User','/dls/i03/data/2016/cm14451-1/jpegs/20160122/gw/ins2/001/ins2_2_1_270.0.png','/dls/i03/data/2016/cm14451-1/jpegs/20160122/gw/ins2/001/ins2_2_1_180.0.png','/dls/i03/data/2016/cm14451-1/jpegs/20160122/gw/ins2/001/ins2_2_1_90.0.png','/dls/i03/data/2016/cm14451-1/jpegs/20160122/gw/ins2/001/ins2_2_1_0.0.png','Omega',NULL,NULL,0,NULL,NULL,NULL,NULL,6.1213,NULL,NULL,0.08,0.02,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,996311,602072,NULL,80,NULL,20,3752,NULL,NULL,NULL,0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(1052494,NULL,55168,NULL,1,'2016-04-13 12:18:12','2016-04-13 12:18:50','DataCollection Successful',0,0.4,0.4,-89.6,2,1,1,0.01,'/dls/i03/data/2016/cm14451-2/20160413/test_xtal/','xtal1','cbf',NULL,'xtal1_1_####.cbf',0.976254,1.24362,200,214.33,208.71,'(-703,-47,-74) Aperture: Large',1,NULL,0.059918,0.099937,100,'User','/dls/i03/data/2016/cm14451-2/jpegs/20160413/test_xtal/xtal1_1_1_90.0.png','/dls/i03/data/2016/cm14451-2/jpegs/20160413/test_xtal/xtal1_1_1_0.0.png',NULL,NULL,'Omega',NULL,NULL,0,NULL,NULL,NULL,NULL,5.30095,NULL,NULL,0.08,0.02,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,1040398,647536,NULL,80,NULL,20,3752,NULL,NULL,NULL,1959830505829.428,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(1052503,NULL,55168,NULL,3,'2016-04-13 12:21:26','2016-04-13 12:21:54','DataCollection Successful',93,0.3,0.3,-44.7,3,1,1,0.01,'/dls/i03/data/2016/cm14451-2/20160413/test_xtal/','xtal1','cbf',NULL,'xtal1_3_####.cbf',0.976253,1.5,266.693,214.372,208.299,'(-703,-47,-74) Aperture: Large',1,NULL,0.059918,0.099937,100,'User','/dls/i03/data/2016/cm14451-2/jpegs/20160413/test_xtal/xtal1_3_1_183.0.png','/dls/i03/data/2016/cm14451-2/jpegs/20160413/test_xtal/xtal1_3_1_93.0.png',NULL,NULL,'Omega',NULL,NULL,93,NULL,NULL,NULL,NULL,5.30095,NULL,NULL,0.08,0.02,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,1040407,647545,NULL,80,NULL,20,3752,NULL,NULL,NULL,1972385107622.2878,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(1066786,398810,55168,NULL,2,'2016-04-18 11:04:44','2016-04-18 11:04:57','DataCollection Successful',0,0.5,0.5,-44.5,3,1,1,0.1,'/dls/i03/data/2016/cm14451-2/gw/20160418/thau/edna_test/','thau','cbf',NULL,'thau_2_####.cbf',0.976253,1.5,266.693,214.372,208.299,'(-345,-241,-185) Aperture: Large',1,NULL,0.059918,0.099937,5.00016,'User','/dls/i03/data/2016/cm14451-2/jpegs/gw/20160418/thau/edna_test/thau_2_1_90.0.png','/dls/i03/data/2016/cm14451-2/jpegs/gw/20160418/thau/edna_test/thau_2_1_0.0.png',NULL,NULL,'Omega',NULL,NULL,0,NULL,NULL,NULL,NULL,5.301,NULL,NULL,0.08,0.02,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,1054243,661459,NULL,80,NULL,20,3752,NULL,NULL,NULL,57087013071.909134,NULL,2,NULL,NULL,NULL,NULL,NULL,NULL,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `DataCollection` ENABLE KEYS */;

--
-- Dumping data for table `DataCollectionComment`
--

/*!40000 ALTER TABLE `DataCollectionComment` DISABLE KEYS */;
/*!40000 ALTER TABLE `DataCollectionComment` ENABLE KEYS */;

--
-- Dumping data for table `DataCollectionFileAttachment`
--

/*!40000 ALTER TABLE `DataCollectionFileAttachment` DISABLE KEYS */;
/*!40000 ALTER TABLE `DataCollectionFileAttachment` ENABLE KEYS */;

--
-- Dumping data for table `DataCollectionGroup`
--

/*!40000 ALTER TABLE `DataCollectionGroup` DISABLE KEYS */;
INSERT INTO `DataCollectionGroup` (`dataCollectionGroupId`, `sessionId`, `comments`, `blSampleId`, `experimentType`, `startTime`, `endTime`, `crystalClass`, `detectorMode`, `actualSampleBarcode`, `actualSampleSlotInContainer`, `actualContainerBarcode`, `actualContainerSlotInSC`, `workflowId`, `xtalSnapshotFullPath`, `scanParameters`) VALUES (988855,55167,NULL,374695,'SAD',NULL,NULL,NULL,'Ext. Trigger','HA00AU3712',NULL,NULL,NULL,NULL,NULL,NULL),(996311,55167,NULL,NULL,'SAD',NULL,NULL,NULL,'Ext. Trigger',NULL,NULL,NULL,NULL,NULL,NULL,NULL),(1040398,55168,NULL,NULL,'SAD',NULL,NULL,NULL,'Ext. Trigger',NULL,NULL,NULL,NULL,NULL,NULL,NULL),(1040407,55168,NULL,NULL,'SAD',NULL,NULL,NULL,'Ext. Trigger',NULL,NULL,NULL,NULL,NULL,NULL,NULL),(1054243,55168,NULL,398810,'SAD',NULL,NULL,NULL,'Ext. Trigger','CA00AG9993',NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `DataCollectionGroup` ENABLE KEYS */;

--
-- Dumping data for table `DataCollectionPlan_has_Detector`
--

/*!40000 ALTER TABLE `DataCollectionPlan_has_Detector` DISABLE KEYS */;
INSERT INTO `DataCollectionPlan_has_Detector` (`dataCollectionPlanHasDetectorId`, `dataCollectionPlanId`, `detectorId`, `exposureTime`, `distance`, `roll`) VALUES (4,197792,8,5.4,136.86,45);
/*!40000 ALTER TABLE `DataCollectionPlan_has_Detector` ENABLE KEYS */;

--
-- Dumping data for table `DataReductionStatus`
--

/*!40000 ALTER TABLE `DataReductionStatus` DISABLE KEYS */;
/*!40000 ALTER TABLE `DataReductionStatus` ENABLE KEYS */;

--
-- Dumping data for table `Dewar`
--

/*!40000 ALTER TABLE `Dewar` DISABLE KEYS */;
INSERT INTO `Dewar` (`dewarId`, `shippingId`, `code`, `comments`, `storageLocation`, `dewarStatus`, `bltimeStamp`, `isStorageDewar`, `barCode`, `firstExperimentId`, `customsValue`, `transportValue`, `trackingNumberToSynchrotron`, `trackingNumberFromSynchrotron`, `type`, `FACILITYCODE`, `weight`, `deliveryAgent_barcode`) VALUES (573,474,'Dewar-1-cm0001-1',NULL,NULL,'processing',NULL,0,'dewar-cm0001-1-0000001',NULL,NULL,NULL,NULL,NULL,'Dewar',NULL,NULL,NULL),(576,474,'Dewar-2-cm0001-1',NULL,NULL,'at DLS',NULL,0,'dewar-cm0001-1-0000002',NULL,NULL,NULL,NULL,NULL,'Dewar',NULL,NULL,NULL),(579,477,'Dewar-3-cm0001-2',NULL,NULL,'processing',NULL,0,'dewar-cm0001-2-0000477',NULL,NULL,NULL,NULL,NULL,'Dewar',NULL,NULL,NULL),(582,480,'Dewar-4-cm0001-3',NULL,NULL,'processing',NULL,0,'dewar-cm0001-3-0000480',NULL,NULL,NULL,NULL,NULL,'Dewar',NULL,NULL,NULL),(8287,6988,'Default Dewar:cm14451-1',NULL,NULL,'processing',NULL,0,NULL,NULL,NULL,NULL,NULL,NULL,'Dewar',NULL,NULL,NULL),(8572,7227,'cm14451-2_Dewar1',NULL,NULL,'processing','2016-02-10 13:03:07',0,NULL,NULL,NULL,NULL,NULL,NULL,'Dewar',NULL,NULL,NULL),(8578,7231,'Dewar_1',NULL,NULL,'opened',NULL,0,'cm14451-12345',NULL,NULL,NULL,NULL,NULL,'Dewar',NULL,NULL,NULL);
/*!40000 ALTER TABLE `Dewar` ENABLE KEYS */;

--
-- Dumping data for table `DewarLocation`
--

/*!40000 ALTER TABLE `DewarLocation` DISABLE KEYS */;
/*!40000 ALTER TABLE `DewarLocation` ENABLE KEYS */;

--
-- Dumping data for table `DewarRegistry`
--

/*!40000 ALTER TABLE `DewarRegistry` DISABLE KEYS */;
/*!40000 ALTER TABLE `DewarRegistry` ENABLE KEYS */;

--
-- Dumping data for table `DewarReport`
--

/*!40000 ALTER TABLE `DewarReport` DISABLE KEYS */;
/*!40000 ALTER TABLE `DewarReport` ENABLE KEYS */;

--
-- Dumping data for table `DewarTransportHistory`
--

/*!40000 ALTER TABLE `DewarTransportHistory` DISABLE KEYS */;
/*!40000 ALTER TABLE `DewarTransportHistory` ENABLE KEYS */;

--
-- Dumping data for table `DiffractionPlan`
--

/*!40000 ALTER TABLE `DiffractionPlan` DISABLE KEYS */;
INSERT INTO `DiffractionPlan` (`diffractionPlanId`, `name`, `experimentKind`, `observedResolution`, `minimalResolution`, `exposureTime`, `oscillationRange`, `maximalResolution`, `screeningResolution`, `radiationSensitivity`, `anomalousScatterer`, `preferredBeamSizeX`, `preferredBeamSizeY`, `preferredBeamDiameter`, `comments`, `DIFFRACTIONPLANUUID`, `aimedCompleteness`, `aimedIOverSigmaAtHighestRes`, `aimedMultiplicity`, `aimedResolution`, `anomalousData`, `complexity`, `estimateRadiationDamage`, `forcedSpaceGroup`, `requiredCompleteness`, `requiredMultiplicity`, `requiredResolution`, `strategyOption`, `kappaStrategyOption`, `numberOfPositions`, `minDimAccrossSpindleAxis`, `maxDimAccrossSpindleAxis`, `radiationSensitivityBeta`, `radiationSensitivityGamma`, `minOscWidth`, `recordTimeStamp`, `monochromator`, `energy`, `transmission`, `boxSizeX`, `boxSizeY`, `kappaStart`, `axisStart`, `axisRange`, `numberOfImages`, `presetForProposalId`, `beamLineName`, `detectorId`, `distance`, `orientation`, `monoBandwidth`, `centringMethod`) VALUES (197784,NULL,'OSC',NULL,NULL,0.2,NULL,NULL,NULL,NULL,NULL,10.5,10.5,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,NULL,0,NULL,NULL,NULL,1.1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-03-20 23:50:27',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(197788,NULL,NULL,NULL,NULL,10,NULL,NULL,NULL,NULL,NULL,160,100,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,NULL,0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2016-10-26 15:28:12',NULL,150,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,4,162.5,45,330.6,NULL),(197792,'XPDF-1',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,NULL,0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'2017-03-22 10:56:32',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `DiffractionPlan` ENABLE KEYS */;

--
-- Dumping data for table `EMMicroscope`
--

/*!40000 ALTER TABLE `EMMicroscope` DISABLE KEYS */;
/*!40000 ALTER TABLE `EMMicroscope` ENABLE KEYS */;

--
-- Dumping data for table `EnergyScan`
--

/*!40000 ALTER TABLE `EnergyScan` DISABLE KEYS */;
INSERT INTO `EnergyScan` (`energyScanId`, `sessionId`, `blSampleId`, `fluorescenceDetector`, `scanFileFullPath`, `jpegChoochFileFullPath`, `element`, `startEnergy`, `endEnergy`, `transmissionFactor`, `exposureTime`, `axisPosition`, `synchrotronCurrent`, `temperature`, `peakEnergy`, `peakFPrime`, `peakFDoublePrime`, `inflectionEnergy`, `inflectionFPrime`, `inflectionFDoublePrime`, `xrayDose`, `startTime`, `endTime`, `edgeEnergy`, `filename`, `beamSizeVertical`, `beamSizeHorizontal`, `choochFileFullPath`, `crystalClass`, `comments`, `flux`, `flux_end`, `workingDirectory`, `blSubSampleId`) VALUES (49661,55167,NULL,'Vortex1_MCAScaler','/dls/i03/data/2016/cm14451-1/fe1.fluo','/dls/i03/data/2016/cm14451-1/fluorescence_scans/fe1_chooch.png','Fe',7062.75,7170.88,0.016,1,NULL,298.569,100,7115.73,-4.79,4.66,7095.13,-7.26,1.66,0,'2016-01-12 14:51:20','2016-01-12 14:58:33','K',NULL,20,50,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(49662,55167,NULL,'Vortex1_MCAScaler','/dls/i03/data/2016/cm14451-1/fe1.fluo','/dls/i03/data/2016/cm14451-1/fluorescence_scans/fe1_chooch.png','Fe',7062.75,7170.88,0.256,1,NULL,299.986,100,7131.44,-6.26,5.1,7122.6,-8.69,2.52,0,'2016-01-12 15:00:34','2016-01-12 15:05:28','K',NULL,20,50,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(49668,55167,374693,'Vortex1_MCAScaler','/dls/i03/data/2016/cm14451-1/zn1.fluo','/dls/i03/data/2016/cm14451-1/fluorescence_scans/zn1_chooch.png','Zn',9626.73,9692.41,0.256,1,NULL,301.465,100,9673.5,-8.73,3.05,9672.94,-9.04,0.48,0,'2016-01-13 15:55:39','2016-01-13 16:02:15','K',NULL,20,20,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(49669,55167,374693,'Vortex1_MCAScaler','/dls/i03/data/2016/cm14451-1/zn1.fluo','/dls/i03/data/2016/cm14451-1/fluorescence_scans/zn1_chooch.png','Zn',9626.73,9692.41,0.256,1,NULL,299.054,100,9674.62,-7.78,3.36,9674.62,-7.78,3.36,0,'2016-01-13 16:02:39','2016-01-13 16:07:38','K',NULL,20,20,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(49671,55167,374693,'Vortex1_MCAScaler','/dls/i03/data/2016/cm14451-1/zn1.fluo','/dls/i03/data/2016/cm14451-1/fluorescence_scans/zn1_chooch.png','Zn',9626.73,9692.41,0.004,1,NULL,301.497,100,9663.49,-10.11,8.51,9660.14,-13.87,3.89,0,'2016-01-13 16:16:35','2016-01-13 16:22:27','K',NULL,20,20,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(49673,55167,374693,'Vortex1_MCAScaler','/dls/i03/data/2016/cm14451-1/zn2.fluo','/dls/i03/data/2016/cm14451-1/fluorescence_scans/zn2_chooch.png','Zn',9626.73,9692.41,0.064,1,NULL,298.34,100,9685.13,-6.16,3.78,9671.27,-7.05,2.64,0,'2016-01-13 16:24:38','2016-01-13 16:29:33','K',NULL,20,20,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(49674,55167,374693,'Vortex1_MCAScaler','/dls/i03/data/2016/cm14451-1/zn3.fluo','/dls/i03/data/2016/cm14451-1/fluorescence_scans/zn3_chooch.png','Zn',9626.73,9692.41,0.064,1,NULL,299.716,100,9643.43,-7.52,4.09,9636.73,-8.25,1.59,0,'2016-01-13 16:30:48','2016-01-13 16:35:37','K',NULL,20,20,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(49675,55167,NULL,'Vortex1_MCAScaler','/dls/i03/data/2016/cm14451-1/zn_1730_13th.fluo','/dls/i03/data/2016/cm14451-1/fluorescence_scans/zn_1730_13th_chooch.png','Zn',9626.73,9692.41,0.002,1,NULL,298.912,100,9667.37,-6.92,6.36,9660.69,-11.35,3.51,0,'2016-01-13 17:31:04','2016-01-13 17:37:43','K',NULL,20,50,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(49676,55167,NULL,'Vortex1_MCAScaler','/dls/i03/data/2016/cm14451-1/zn_1738_13th.fluo','/dls/i03/data/2016/cm14451-1/fluorescence_scans/zn_1738_13th_chooch.png','Zn',9626.73,9692.41,0.006,1,NULL,300.82,100,9664.04,-8.7,6.42,9660.69,-11.37,3.59,0,'2016-01-13 17:39:01','2016-01-13 17:43:37','K',NULL,20,50,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(49677,55167,NULL,'Vortex1_MCAScaler','/dls/i03/data/2016/cm14451-1/cu1.fluo','/dls/i03/data/2016/cm14451-1/fluorescence_scans/cu1_chooch.png','Cu',8942.19,9019.21,0.032,1,NULL,298.45,100,8991.12,-6.37,4.03,8977.04,-8.12,1.82,0,'2016-01-13 19:51:26','2016-01-13 19:58:15','K',NULL,20,50,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(49678,55167,NULL,'Vortex1_MCAScaler','/dls/i03/data/2016/cm14451-1/se1.fluo','/dls/i03/data/2016/cm14451-1/fluorescence_scans/se1_chooch.png','Se',12628,12688,0.004,1,NULL,298.837,100,12653,-8.84,8.25,12651,-12.16,4.46,0,'2016-01-13 20:20:25','2016-01-13 20:27:01','K',NULL,20,50,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(49679,55167,NULL,'Vortex1_MCAScaler','/dls/i03/data/2016/cm14451-1/se2.fluo','/dls/i03/data/2016/cm14451-1/fluorescence_scans/se2_chooch.png','Se',12628,12688,0.002,1,NULL,300.543,100,12664,-7.91,9.44,12662.5,-11.35,5.87,0,'2016-01-14 09:48:06','2016-01-14 09:53:34','K',NULL,20,50,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(49680,55167,NULL,'Vortex1_MCAScaler','/dls/i03/data/2016/cm14451-1/se3.fluo','/dls/i03/data/2016/cm14451-1/fluorescence_scans/se3_chooch.png','Se',12628,12688,0.002,1,NULL,299.851,100,12658.5,-7.03,11.31,12656.5,-12.74,6.37,0,'2016-01-14 10:00:43','2016-01-14 10:05:39','K',NULL,20,50,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(49681,55167,NULL,'Vortex1_MCAScaler','/dls/i03/data/2016/cm14451-1/se4.fluo','/dls/i03/data/2016/cm14451-1/fluorescence_scans/se4_chooch.png','Se',12628,12688,0.002,1,NULL,299.856,100,12660,-7.58,11.19,12658,-12.64,5.98,0,'2016-01-14 10:09:58','2016-01-14 10:14:56','K',NULL,20,50,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(49682,55167,374695,'Vortex1_MCAScaler','/dls/i03/data/2016/cm14451-1/zn_1401_1125.fluo','/dls/i03/data/2016/cm14451-1/fluorescence_scans/zn_1401_1125_chooch.png','Zn',9626.73,9692.41,0.004,1,NULL,301.75,100,9666.82,-7.77,6.51,9661.25,-11.11,3.49,0,'2016-01-14 11:24:43','2016-01-14 11:31:22','K',NULL,20,50,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(50165,55167,398811,'Vortex1_MCAScaler','/dls/i03/data/2016/cm14451-1/20160224/testZn.fluo','/dls/i03/data/2016/cm14451-1/20160224/fluorescence_scans/testZn_chooch.png','Zn',9626.73,9692.41,0.004,1,NULL,300.402,100,9668.43,-6.85,5.95,9658.43,-9.83,1.07,0,'2016-02-24 14:42:38','2016-02-24 14:44:02','K',NULL,20,50,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(50166,55167,398811,'Vortex1_MCAScaler','/dls/i03/data/2016/cm14451-1/testZn.fluo','/dls/i03/data/2016/cm14451-1/fluorescence_scans/testZn_chooch.png','Zn',9626.73,9692.41,0.004,1,NULL,298.566,100,9668.43,-6.9,5.96,9658.43,-9.91,1.13,0,'2016-02-24 14:46:33','2016-02-24 14:48:20','K',NULL,20,50,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(50167,55167,398811,'Vortex1_MCAScaler','/dls/i03/data/2016/cm14451-1/20160224b/testZn.fluo','/dls/i03/data/2016/cm14451-1/20160224b/fluorescence_scans/testZn_chooch.png','Zn',9626.73,9692.41,0.004,1,NULL,298.913,100,9663.43,-9.53,6.11,9658.43,-10,1.09,0,'2016-02-24 14:55:42','2016-02-24 14:57:34','K',NULL,20,50,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(50168,55167,398811,'Vortex1_MCAScaler','/dls/i03/data/2016/cm14451-1/20160224c/testZn.fluo','/dls/i03/data/2016/cm14451-1/20160224c/fluorescence_scans/testZn_chooch.png','Zn',9626.73,9692.41,0.004,1,NULL,299.834,100,9663.44,-9.95,7.45,9658.43,-10.89,1.32,0,'2016-02-24 15:03:55','2016-02-24 15:05:33','K',NULL,20,50,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(50169,55167,398811,'Vortex1_MCAScaler','/dls/i03/data/2016/cm14451-1/20160224d/testZn.fluo','/dls/i03/data/2016/cm14451-1/20160224d/fluorescence_scans/testZn_chooch.png','Zn',9626.73,9692.41,0.004,1,NULL,298.071,100,9663.43,-9.56,6.37,9658.44,-10.1,1.15,0,'2016-02-24 15:07:49','2016-02-24 15:09:42','K',NULL,20,50,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(50261,55167,NULL,'Vortex1_MCAScaler','/dls/i03/data/2016/cm14451-1/se_sb.fluo','/dls/i03/data/2016/cm14451-1/fluorescence_scans/se_sb_chooch.png','Se',12628,12688,0.5,1,NULL,9.67282,100,12660.5,-7.64,10.63,12659,-11.08,7.15,0,'2016-03-09 10:48:58','2016-03-09 10:54:35','K',NULL,20,80,NULL,NULL,'null _FLAG_',NULL,NULL,NULL,NULL),(50263,55168,398811,'Vortex1_MCAScaler','/dls/i03/data/2016/cm14451-2/se_test1.fluo',NULL,NULL,12628,12688,1,1,NULL,-0.000965,100,NULL,NULL,NULL,NULL,NULL,NULL,0,'2016-03-30 14:36:51','2016-03-30 14:42:06',NULL,NULL,20,80,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(50266,55168,NULL,'Vortex1_MCAScaler','/dls/i03/data/2016/cm14451-2/test_1.fluo',NULL,NULL,12628,12688,0.2,1,NULL,0.000111,100,NULL,NULL,NULL,NULL,NULL,NULL,0,'2016-03-31 10:14:15','2016-03-31 10:19:01',NULL,NULL,20,80,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(50269,55168,NULL,'Vortex1_MCAScaler','/dls/i03/data/2016/cm14451-2/se1.fluo','/dls/i03/data/2016/cm14451-2/fluorescence_scans/se1_chooch.png','Se',12628,12688,0.128,1,NULL,198.223,100,12660.5,-7.26,9.79,12656,-10.42,4.21,0,'2016-04-05 16:43:16','2016-04-05 16:49:58','K',NULL,20,20,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(50284,55168,409068,'Vortex1_MCAScaler','/dls/i03/data/2016/cm14451-2/zn.fluo','/dls/i03/data/2016/cm14451-2/fluorescence_scans/zn_chooch.png','Zn',9626.73,9692.41,0.016,1,NULL,301.691,100,9666.82,-7.09,9.24,9661.81,-12.08,3.36,0,'2016-04-06 16:36:18','2016-04-06 16:42:43','K',NULL,20,50,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(50287,55168,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(50290,55168,2012,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `EnergyScan` ENABLE KEYS */;

--
-- Dumping data for table `Experiment`
--

/*!40000 ALTER TABLE `Experiment` DISABLE KEYS */;
/*!40000 ALTER TABLE `Experiment` ENABLE KEYS */;

--
-- Dumping data for table `ExperimentKindDetails`
--

/*!40000 ALTER TABLE `ExperimentKindDetails` DISABLE KEYS */;
/*!40000 ALTER TABLE `ExperimentKindDetails` ENABLE KEYS */;

--
-- Dumping data for table `Frame`
--

/*!40000 ALTER TABLE `Frame` DISABLE KEYS */;
/*!40000 ALTER TABLE `Frame` ENABLE KEYS */;

--
-- Dumping data for table `FrameList`
--

/*!40000 ALTER TABLE `FrameList` DISABLE KEYS */;
/*!40000 ALTER TABLE `FrameList` ENABLE KEYS */;

--
-- Dumping data for table `FrameSet`
--

/*!40000 ALTER TABLE `FrameSet` DISABLE KEYS */;
/*!40000 ALTER TABLE `FrameSet` ENABLE KEYS */;

--
-- Dumping data for table `FrameToList`
--

/*!40000 ALTER TABLE `FrameToList` DISABLE KEYS */;
/*!40000 ALTER TABLE `FrameToList` ENABLE KEYS */;

--
-- Dumping data for table `GeometryClassname`
--

/*!40000 ALTER TABLE `GeometryClassname` DISABLE KEYS */;
/*!40000 ALTER TABLE `GeometryClassname` ENABLE KEYS */;

--
-- Dumping data for table `GridImageMap`
--

/*!40000 ALTER TABLE `GridImageMap` DISABLE KEYS */;
/*!40000 ALTER TABLE `GridImageMap` ENABLE KEYS */;

--
-- Dumping data for table `GridInfo`
--

/*!40000 ALTER TABLE `GridInfo` DISABLE KEYS */;
/*!40000 ALTER TABLE `GridInfo` ENABLE KEYS */;

--
-- Dumping data for table `Image`
--

/*!40000 ALTER TABLE `Image` DISABLE KEYS */;
INSERT INTO `Image` (`imageId`, `dataCollectionId`, `imageNumber`, `fileName`, `fileLocation`, `measuredIntensity`, `jpegFileFullPath`, `jpegThumbnailFileFullPath`, `temperature`, `cumulativeIntensity`, `synchrotronCurrent`, `comments`, `machineMessage`, `BLTIMESTAMP`, `motorPositionId`, `recordTimeStamp`) VALUES (274837165,1052494,1,'xtal1_1_0001.cbf','/dls/i03/data/2016/cm14451-2/20160413/test_xtal',0,'/dls/i03/data/2016/cm14451-2/jpegs/20160413/test_xtal/xtal1_1_0001.jpeg','/dls/i03/data/2016/cm14451-2/jpegs/20160413/test_xtal/xtal1_1_0001.thumb.jpeg',294,0,298.847,NULL,NULL,'2016-04-13 11:18:39',NULL,'2016-04-13 11:18:39'),(274837168,1052494,2,'xtal1_1_0002.cbf','/dls/i03/data/2016/cm14451-2/20160413/test_xtal',0,'/dls/i03/data/2016/cm14451-2/jpegs/20160413/test_xtal/xtal1_1_0002.jpeg','/dls/i03/data/2016/cm14451-2/jpegs/20160413/test_xtal/xtal1_1_0002.thumb.jpeg',294,0,298.74,NULL,NULL,'2016-04-13 11:18:50',NULL,'2016-04-13 11:18:50'),(274837177,1052503,1,'xtal1_3_0001.cbf','/dls/i03/data/2016/cm14451-2/20160413/test_xtal',0,'/dls/i03/data/2016/cm14451-2/jpegs/20160413/test_xtal/xtal1_3_0001.jpeg','/dls/i03/data/2016/cm14451-2/jpegs/20160413/test_xtal/xtal1_3_0001.thumb.jpeg',294,0,302.004,NULL,NULL,'2016-04-13 11:21:36',NULL,'2016-04-13 11:21:36'),(274837180,1052503,2,'xtal1_3_0002.cbf','/dls/i03/data/2016/cm14451-2/20160413/test_xtal',0,'/dls/i03/data/2016/cm14451-2/jpegs/20160413/test_xtal/xtal1_3_0002.jpeg','/dls/i03/data/2016/cm14451-2/jpegs/20160413/test_xtal/xtal1_3_0002.thumb.jpeg',294,0,301.922,NULL,NULL,'2016-04-13 11:21:45',NULL,'2016-04-13 11:21:45'),(274837183,1052503,3,'xtal1_3_0003.cbf','/dls/i03/data/2016/cm14451-2/20160413/test_xtal',0,'/dls/i03/data/2016/cm14451-2/jpegs/20160413/test_xtal/xtal1_3_0003.jpeg','/dls/i03/data/2016/cm14451-2/jpegs/20160413/test_xtal/xtal1_3_0003.thumb.jpeg',294,0,301.842,NULL,NULL,'2016-04-13 11:21:54',NULL,'2016-04-13 11:21:54'),(284717989,1066786,1,'thau_2_0001.cbf','/dls/i03/data/2016/cm14451-2/gw/20160418/thau/edna_test',0,'/dls/i03/data/2016/cm14451-2/jpegs/gw/20160418/thau/edna_test/thau_2_0001.jpeg','/dls/i03/data/2016/cm14451-2/jpegs/gw/20160418/thau/edna_test/thau_2_0001.thumb.jpeg',294,0,299.987,NULL,NULL,'2016-04-14 02:19:04',NULL,'2016-04-14 02:19:04'),(284718055,1066786,2,'thau_2_0002.cbf','/dls/i03/data/2016/cm14451-2/gw/20160418/thau/edna_test',0,'/dls/i03/data/2016/cm14451-2/jpegs/gw/20160418/thau/edna_test/thau_2_0002.jpeg','/dls/i03/data/2016/cm14451-2/jpegs/gw/20160418/thau/edna_test/thau_2_0002.thumb.jpeg',294,0,299.933,NULL,NULL,'2016-04-14 02:19:04',NULL,'2016-04-14 02:19:04'),(284718118,1066786,3,'thau_2_0003.cbf','/dls/i03/data/2016/cm14451-2/gw/20160418/thau/edna_test',0,'/dls/i03/data/2016/cm14451-2/jpegs/gw/20160418/thau/edna_test/thau_2_0003.jpeg','/dls/i03/data/2016/cm14451-2/jpegs/gw/20160418/thau/edna_test/thau_2_0003.thumb.jpeg',294,0,299.908,NULL,NULL,'2016-04-14 02:19:04',NULL,'2016-04-14 02:19:04');
/*!40000 ALTER TABLE `Image` ENABLE KEYS */;

--
-- Dumping data for table `ImageQualityIndicators`
--

/*!40000 ALTER TABLE `ImageQualityIndicators` DISABLE KEYS */;
INSERT INTO `ImageQualityIndicators` (`dataCollectionId`, `imageNumber`, `imageId`, `autoProcProgramId`, `spotTotal`, `inResTotal`, `goodBraggCandidates`, `iceRings`, `method1Res`, `method2Res`, `maxUnitCell`, `pctSaturationTop50Peaks`, `inResolutionOvrlSpots`, `binPopCutOffMethod2Res`, `recordTimeStamp`, `totalIntegratedSignal`, `dozor_score`, `driftFactor`) VALUES (1052494,1,NULL,NULL,296,296,259,0,2.03,2.03,0,0,0,0,NULL,2.61,NULL,NULL),(1052494,2,NULL,NULL,239,239,224,0,2.12,2.12,0,0,0,0,NULL,2.95,NULL,NULL),(1052503,1,274837177,NULL,217,217,202,0,2.07,2.07,0,0,0,0,NULL,2.99,NULL,NULL),(1052503,2,NULL,NULL,257,257,236,0,2.06,2.06,0,0,0,0,NULL,3.02,NULL,NULL),(1052503,3,NULL,NULL,306,306,278,0,2.04,2.04,0,0,0,0,NULL,2.75,NULL,NULL),(1066786,1,284717989,NULL,1132,1132,872,0,1.63,1.63,0,0,0,0,NULL,2.09,NULL,NULL),(1066786,2,284718055,NULL,848,848,652,0,1.56,1.56,0,0,0,0,NULL,2.03,NULL,NULL),(1066786,3,284718118,NULL,922,922,735,0,1.57,1.57,0,0,0,0,NULL,2.13,NULL,NULL);
/*!40000 ALTER TABLE `ImageQualityIndicators` ENABLE KEYS */;

--
-- Dumping data for table `Instruction`
--

/*!40000 ALTER TABLE `Instruction` DISABLE KEYS */;
/*!40000 ALTER TABLE `Instruction` ENABLE KEYS */;

--
-- Dumping data for table `InstructionSet`
--

/*!40000 ALTER TABLE `InstructionSet` DISABLE KEYS */;
/*!40000 ALTER TABLE `InstructionSet` ENABLE KEYS */;

--
-- Dumping data for table `IspybCrystalClass`
--

/*!40000 ALTER TABLE `IspybCrystalClass` DISABLE KEYS */;
/*!40000 ALTER TABLE `IspybCrystalClass` ENABLE KEYS */;

--
-- Dumping data for table `IspybReference`
--

/*!40000 ALTER TABLE `IspybReference` DISABLE KEYS */;
/*!40000 ALTER TABLE `IspybReference` ENABLE KEYS */;

--
-- Dumping data for table `LabContact`
--

/*!40000 ALTER TABLE `LabContact` DISABLE KEYS */;
/*!40000 ALTER TABLE `LabContact` ENABLE KEYS */;

--
-- Dumping data for table `Laboratory`
--

/*!40000 ALTER TABLE `Laboratory` DISABLE KEYS */;
/*!40000 ALTER TABLE `Laboratory` ENABLE KEYS */;

--
-- Dumping data for table `Log4Stat`
--

/*!40000 ALTER TABLE `Log4Stat` DISABLE KEYS */;
/*!40000 ALTER TABLE `Log4Stat` ENABLE KEYS */;

--
-- Dumping data for table `MXMRRun`
--

/*!40000 ALTER TABLE `MXMRRun` DISABLE KEYS */;
INSERT INTO `MXMRRun` (`mxMRRunId`, `autoProcScalingId`, `success`, `message`, `pipeline`, `inputCoordFile`, `outputCoordFile`, `inputMTZFile`, `outputMTZFile`, `runDirectory`, `logFile`, `commandLine`, `rValueStart`, `rValueEnd`, `rFreeValueStart`, `rFreeValueEnd`, `starttime`, `endtime`) VALUES (672897,603470,1,'Blob scores: 78','dimple','--slow','/dls/i24/data/2018/cm19649-3/processed/test180731/hewlmesh_1/line4/hewlmesh_1_1_/xia2/3d-run/dimple/final.pdb','--dls-naming','/dls/i24/data/2018/cm19649-3/processed/test180731/hewlmesh_1/line4/hewlmesh_1_1_/xia2/3d-run/dimple/final.mtz','/dls/i24/data/2018/cm19649-3/processed/test180731/hewlmesh_1/line4/hewlmesh_1_1_/xia2/3d-run/dimple','/dls/i24/data/2018/cm19649-3/processed/test180731/hewlmesh_1/line4/hewlmesh_1_1_/xia2/3d-run/dimple/dimple.log','/dls_sw/apps/dimple/git-master/main.py  --dls-naming --slow -fpng /dls/i24/data/2018/cm19649-3/processed/test180731/hewlmesh_1/line4/hewlmesh_1_1_/xia2/3d-run/DataFiles/cm19649v3_xhewlmesh11_free.mtz /dls/i24/data/2018/cm19649-3/tmp/hewlmesh_1.4308.pdb /d',0.1812,0.1682,0.1896,0.1888,'2018-07-31 08:55:52','2018-07-31 08:57:10'),(672900,603470,0,'Unknown error','dimple',NULL,NULL,NULL,NULL,'/dls/i24/data/2018/cm19649-3/processed/test180731/hewlmesh_1/line4/hewlmesh_1_1_/xia2/3d-run/dimple',NULL,NULL,NULL,NULL,NULL,NULL,'2018-07-31 08:57:12',NULL);
/*!40000 ALTER TABLE `MXMRRun` ENABLE KEYS */;

--
-- Dumping data for table `MXMRRunBlob`
--

/*!40000 ALTER TABLE `MXMRRunBlob` DISABLE KEYS */;
/*!40000 ALTER TABLE `MXMRRunBlob` ENABLE KEYS */;

--
-- Dumping data for table `Macromolecule`
--

/*!40000 ALTER TABLE `Macromolecule` DISABLE KEYS */;
/*!40000 ALTER TABLE `Macromolecule` ENABLE KEYS */;

--
-- Dumping data for table `MacromoleculeRegion`
--

/*!40000 ALTER TABLE `MacromoleculeRegion` DISABLE KEYS */;
/*!40000 ALTER TABLE `MacromoleculeRegion` ENABLE KEYS */;

--
-- Dumping data for table `Measurement`
--

/*!40000 ALTER TABLE `Measurement` DISABLE KEYS */;
/*!40000 ALTER TABLE `Measurement` ENABLE KEYS */;

--
-- Dumping data for table `MeasurementToDataCollection`
--

/*!40000 ALTER TABLE `MeasurementToDataCollection` DISABLE KEYS */;
/*!40000 ALTER TABLE `MeasurementToDataCollection` ENABLE KEYS */;

--
-- Dumping data for table `MeasurementUnit`
--

/*!40000 ALTER TABLE `MeasurementUnit` DISABLE KEYS */;
/*!40000 ALTER TABLE `MeasurementUnit` ENABLE KEYS */;

--
-- Dumping data for table `Merge`
--

/*!40000 ALTER TABLE `Merge` DISABLE KEYS */;
/*!40000 ALTER TABLE `Merge` ENABLE KEYS */;

--
-- Dumping data for table `Model`
--

/*!40000 ALTER TABLE `Model` DISABLE KEYS */;
/*!40000 ALTER TABLE `Model` ENABLE KEYS */;

--
-- Dumping data for table `ModelBuilding`
--

/*!40000 ALTER TABLE `ModelBuilding` DISABLE KEYS */;
/*!40000 ALTER TABLE `ModelBuilding` ENABLE KEYS */;

--
-- Dumping data for table `ModelList`
--

/*!40000 ALTER TABLE `ModelList` DISABLE KEYS */;
/*!40000 ALTER TABLE `ModelList` ENABLE KEYS */;

--
-- Dumping data for table `ModelToList`
--

/*!40000 ALTER TABLE `ModelToList` DISABLE KEYS */;
/*!40000 ALTER TABLE `ModelToList` ENABLE KEYS */;

--
-- Dumping data for table `MotionCorrection`
--

/*!40000 ALTER TABLE `MotionCorrection` DISABLE KEYS */;
/*!40000 ALTER TABLE `MotionCorrection` ENABLE KEYS */;

--
-- Dumping data for table `MotionCorrectionDrift`
--

/*!40000 ALTER TABLE `MotionCorrectionDrift` DISABLE KEYS */;
/*!40000 ALTER TABLE `MotionCorrectionDrift` ENABLE KEYS */;

--
-- Dumping data for table `MotorPosition`
--

/*!40000 ALTER TABLE `MotorPosition` DISABLE KEYS */;
/*!40000 ALTER TABLE `MotorPosition` ENABLE KEYS */;

--
-- Dumping data for table `Movie`
--

/*!40000 ALTER TABLE `Movie` DISABLE KEYS */;
/*!40000 ALTER TABLE `Movie` ENABLE KEYS */;

--
-- Dumping data for table `PDB`
--

/*!40000 ALTER TABLE `PDB` DISABLE KEYS */;
INSERT INTO `PDB` (`pdbId`, `name`, `contents`, `code`) VALUES (6,'ceo2','\r\ndata_\r\n_chemical_name_mineral ?CeO2?\r\n_cell_length_a  5.411223\r\n_cell_length_b  5.411223\r\n_cell_length_c  5.411223\r\n_cell_angle_alpha 90\r\n_cell_angle_beta  90\r\n_cell_angle_gamma 90\r\n_cell_volume 158.4478\r\n_symmetry_space_group_name_H-M     \'Fm3m\'\r\nloop_\r\n_symmetry_equiv_pos_as_xyz\r\n	\'-x, -y, -z\'\r\n	\'-x, -y, z\'\r\n	\'-x, -y+1/2, -z+1/2\'\r\n	\'-x, -y+1/2, z+1/2\'\r\n	\'-x, -z, -y\'\r\n	\'-x, -z, y\'\r\n	\'-x, -z+1/2, -y+1/2\'\r\n	\'-x, -z+1/2, y+1/2\'\r\n	\'-x, z, -y\'\r\n	\'-x, z, y\'\r\n	\'-x, z+1/2, -y+1/2\'\r\n	\'-x, z+1/2, y+1/2\'\r\n	\'-x, y, -z\'\r\n	\'-x, y, z\'\r\n	\'-x, y+1/2, -z+1/2\'\r\n	\'-x, y+1/2, z+1/2\'\r\n	\'-x+1/2, -y, -z+1/2\'\r\n	\'-x+1/2, -y, z+1/2\'\r\n	\'-x+1/2, -y+1/2, -z\'\r\n	\'-x+1/2, -y+1/2, z\'\r\n	\'-x+1/2, -z, -y+1/2\'\r\n	\'-x+1/2, -z, y+1/2\'\r\n	\'-x+1/2, -z+1/2, -y\'\r\n	\'-x+1/2, -z+1/2, y\'\r\n	\'-x+1/2, z, -y+1/2\'\r\n	\'-x+1/2, z, y+1/2\'\r\n	\'-x+1/2, z+1/2, -y\'\r\n	\'-x+1/2, z+1/2, y\'\r\n	\'-x+1/2, y, -z+1/2\'\r\n	\'-x+1/2, y, z+1/2\'\r\n	\'-x+1/2, y+1/2, -z\'\r\n	\'-x+1/2, y+1/2, z\'\r\n	\'-y, -x, -z\'\r\n	\'-y, -x, z\'\r\n	\'-y, -x+1/2, -z+1/2\'\r\n	\'-y, -x+1/2, z+1/2\'\r\n	\'-y, -z, -x\'\r\n	\'-y, -z, x\'\r\n	\'-y, -z+1/2, -x+1/2\'\r\n	\'-y, -z+1/2, x+1/2\'\r\n	\'-y, z, -x\'\r\n	\'-y, z, x\'\r\n	\'-y, z+1/2, -x+1/2\'\r\n	\'-y, z+1/2, x+1/2\'\r\n	\'-y, x, -z\'\r\n	\'-y, x, z\'\r\n	\'-y, x+1/2, -z+1/2\'\r\n	\'-y, x+1/2, z+1/2\'\r\n	\'-y+1/2, -x, -z+1/2\'\r\n	\'-y+1/2, -x, z+1/2\'\r\n	\'-y+1/2, -x+1/2, -z\'\r\n	\'-y+1/2, -x+1/2, z\'\r\n	\'-y+1/2, -z, -x+1/2\'\r\n	\'-y+1/2, -z, x+1/2\'\r\n	\'-y+1/2, -z+1/2, -x\'\r\n	\'-y+1/2, -z+1/2, x\'\r\n	\'-y+1/2, z, -x+1/2\'\r\n	\'-y+1/2, z, x+1/2\'\r\n	\'-y+1/2, z+1/2, -x\'\r\n	\'-y+1/2, z+1/2, x\'\r\n	\'-y+1/2, x, -z+1/2\'\r\n	\'-y+1/2, x, z+1/2\'\r\n	\'-y+1/2, x+1/2, -z\'\r\n	\'-y+1/2, x+1/2, z\'\r\n	\'-z, -x, -y\'\r\n	\'-z, -x, y\'\r\n	\'-z, -x+1/2, -y+1/2\'\r\n	\'-z, -x+1/2, y+1/2\'\r\n	\'-z, -y, -x\'\r\n	\'-z, -y, x\'\r\n	\'-z, -y+1/2, -x+1/2\'\r\n	\'-z, -y+1/2, x+1/2\'\r\n	\'-z, y, -x\'\r\n	\'-z, y, x\'\r\n	\'-z, y+1/2, -x+1/2\'\r\n	\'-z, y+1/2, x+1/2\'\r\n	\'-z, x, -y\'\r\n	\'-z, x, y\'\r\n	\'-z, x+1/2, -y+1/2\'\r\n	\'-z, x+1/2, y+1/2\'\r\n	\'-z+1/2, -x, -y+1/2\'\r\n	\'-z+1/2, -x, y+1/2\'\r\n	\'-z+1/2, -x+1/2, -y\'\r\n	\'-z+1/2, -x+1/2, y\'\r\n	\'-z+1/2, -y, -x+1/2\'\r\n	\'-z+1/2, -y, x+1/2\'\r\n	\'-z+1/2, -y+1/2, -x\'\r\n	\'-z+1/2, -y+1/2, x\'\r\n	\'-z+1/2, y, -x+1/2\'\r\n	\'-z+1/2, y, x+1/2\'\r\n	\'-z+1/2, y+1/2, -x\'\r\n	\'-z+1/2, y+1/2, x\'\r\n	\'-z+1/2, x, -y+1/2\'\r\n	\'-z+1/2, x, y+1/2\'\r\n	\'-z+1/2, x+1/2, -y\'\r\n	\'-z+1/2, x+1/2, y\'\r\n	\'z, -x, -y\'\r\n	\'z, -x, y\'\r\n	\'z, -x+1/2, -y+1/2\'\r\n	\'z, -x+1/2, y+1/2\'\r\n	\'z, -y, -x\'\r\n	\'z, -y, x\'\r\n	\'z, -y+1/2, -x+1/2\'\r\n	\'z, -y+1/2, x+1/2\'\r\n	\'z, y, -x\'\r\n	\'z, y, x\'\r\n	\'z, y+1/2, -x+1/2\'\r\n	\'z, y+1/2, x+1/2\'\r\n	\'z, x, -y\'\r\n	\'z, x, y\'\r\n	\'z, x+1/2, -y+1/2\'\r\n	\'z, x+1/2, y+1/2\'\r\n	\'z+1/2, -x, -y+1/2\'\r\n	\'z+1/2, -x, y+1/2\'\r\n	\'z+1/2, -x+1/2, -y\'\r\n	\'z+1/2, -x+1/2, y\'\r\n	\'z+1/2, -y, -x+1/2\'\r\n	\'z+1/2, -y, x+1/2\'\r\n	\'z+1/2, -y+1/2, -x\'\r\n	\'z+1/2, -y+1/2, x\'\r\n	\'z+1/2, y, -x+1/2\'\r\n	\'z+1/2, y, x+1/2\'\r\n	\'z+1/2, y+1/2, -x\'\r\n	\'z+1/2, y+1/2, x\'\r\n	\'z+1/2, x, -y+1/2\'\r\n	\'z+1/2, x, y+1/2\'\r\n	\'z+1/2, x+1/2, -y\'\r\n	\'z+1/2, x+1/2, y\'\r\n	\'y, -x, -z\'\r\n	\'y, -x, z\'\r\n	\'y, -x+1/2, -z+1/2\'\r\n	\'y, -x+1/2, z+1/2\'\r\n	\'y, -z, -x\'\r\n	\'y, -z, x\'\r\n	\'y, -z+1/2, -x+1/2\'\r\n	\'y, -z+1/2, x+1/2\'\r\n	\'y, z, -x\'\r\n	\'y, z, x\'\r\n	\'y, z+1/2, -x+1/2\'\r\n	\'y, z+1/2, x+1/2\'\r\n	\'y, x, -z\'\r\n	\'y, x, z\'\r\n	\'y, x+1/2, -z+1/2\'\r\n	\'y, x+1/2, z+1/2\'\r\n	\'y+1/2, -x, -z+1/2\'\r\n	\'y+1/2, -x, z+1/2\'\r\n	\'y+1/2, -x+1/2, -z\'\r\n	\'y+1/2, -x+1/2, z\'\r\n	\'y+1/2, -z, -x+1/2\'\r\n	\'y+1/2, -z, x+1/2\'\r\n	\'y+1/2, -z+1/2, -x\'\r\n	\'y+1/2, -z+1/2, x\'\r\n	\'y+1/2, z, -x+1/2\'\r\n	\'y+1/2, z, x+1/2\'\r\n	\'y+1/2, z+1/2, -x\'\r\n	\'y+1/2, z+1/2, x\'\r\n	\'y+1/2, x, -z+1/2\'\r\n	\'y+1/2, x, z+1/2\'\r\n	\'y+1/2, x+1/2, -z\'\r\n	\'y+1/2, x+1/2, z\'\r\n	\'x, -y, -z\'\r\n	\'x, -y, z\'\r\n	\'x, -y+1/2, -z+1/2\'\r\n	\'x, -y+1/2, z+1/2\'\r\n	\'x, -z, -y\'\r\n	\'x, -z, y\'\r\n	\'x, -z+1/2, -y+1/2\'\r\n	\'x, -z+1/2, y+1/2\'\r\n	\'x, z, -y\'\r\n	\'x, z, y\'\r\n	\'x, z+1/2, -y+1/2\'\r\n	\'x, z+1/2, y+1/2\'\r\n	\'x, y, -z\'\r\n	\'x, y, z\'\r\n	\'x, y+1/2, -z+1/2\'\r\n	\'x, y+1/2, z+1/2\'\r\n	\'x+1/2, -y, -z+1/2\'\r\n	\'x+1/2, -y, z+1/2\'\r\n	\'x+1/2, -y+1/2, -z\'\r\n	\'x+1/2, -y+1/2, z\'\r\n	\'x+1/2, -z, -y+1/2\'\r\n	\'x+1/2, -z, y+1/2\'\r\n	\'x+1/2, -z+1/2, -y\'\r\n	\'x+1/2, -z+1/2, y\'\r\n	\'x+1/2, z, -y+1/2\'\r\n	\'x+1/2, z, y+1/2\'\r\n	\'x+1/2, z+1/2, -y\'\r\n	\'x+1/2, z+1/2, y\'\r\n	\'x+1/2, y, -z+1/2\'\r\n	\'x+1/2, y, z+1/2\'\r\n	\'x+1/2, y+1/2, -z\'\r\n	\'x+1/2, y+1/2, z\'\r\nloop_\r\n_atom_site_label\r\n_atom_site_type_symbol\r\n_atom_site_symmetry_multiplicity\r\n_atom_site_fract_x\r\n_atom_site_fract_y\r\n_atom_site_fract_z\r\n_atom_site_occupancy\r\n_atom_site_B_iso_or_equiv\r\nCe1 Ce   0 0 0 0 1 0.127911\r\nO1 O   0 0.25 0.25 0.25 1 0.07795472',NULL);
/*!40000 ALTER TABLE `PDB` ENABLE KEYS */;

--
-- Dumping data for table `PDBEntry`
--

/*!40000 ALTER TABLE `PDBEntry` DISABLE KEYS */;
/*!40000 ALTER TABLE `PDBEntry` ENABLE KEYS */;

--
-- Dumping data for table `PDBEntry_has_AutoProcProgram`
--

/*!40000 ALTER TABLE `PDBEntry_has_AutoProcProgram` DISABLE KEYS */;
/*!40000 ALTER TABLE `PDBEntry_has_AutoProcProgram` ENABLE KEYS */;

--
-- Dumping data for table `PHPSession`
--

/*!40000 ALTER TABLE `PHPSession` DISABLE KEYS */;
/*!40000 ALTER TABLE `PHPSession` ENABLE KEYS */;

--
-- Dumping data for table `Particle`
--

/*!40000 ALTER TABLE `Particle` DISABLE KEYS */;
/*!40000 ALTER TABLE `Particle` ENABLE KEYS */;

--
-- Dumping data for table `Person`
--

/*!40000 ALTER TABLE `Person` DISABLE KEYS */;
INSERT INTO `Person` (`personId`, `laboratoryId`, `siteId`, `personUUID`, `familyName`, `givenName`, `title`, `emailAddress`, `phoneNumber`, `login`, `faxNumber`, `recordTimeStamp`, `cache`, `externalId`) VALUES (1,NULL,NULL,NULL,'McBoatface','Boaty','Mr',NULL,NULL,'boaty',NULL,'2016-03-20 13:56:45','a:1:{s:9:\"container\";N;}',NULL),(46266,NULL,NULL,NULL,NULL,NULL,'User',NULL,NULL,NULL,NULL,'2016-03-16 15:53:55',NULL,NULL),(46269,NULL,NULL,NULL,NULL,NULL,'User',NULL,NULL,NULL,NULL,'2016-03-16 15:59:22',NULL,NULL);
/*!40000 ALTER TABLE `Person` ENABLE KEYS */;

--
-- Dumping data for table `Phasing`
--

/*!40000 ALTER TABLE `Phasing` DISABLE KEYS */;
/*!40000 ALTER TABLE `Phasing` ENABLE KEYS */;

--
-- Dumping data for table `PhasingAnalysis`
--

/*!40000 ALTER TABLE `PhasingAnalysis` DISABLE KEYS */;
/*!40000 ALTER TABLE `PhasingAnalysis` ENABLE KEYS */;

--
-- Dumping data for table `PhasingProgramAttachment`
--

/*!40000 ALTER TABLE `PhasingProgramAttachment` DISABLE KEYS */;
/*!40000 ALTER TABLE `PhasingProgramAttachment` ENABLE KEYS */;

--
-- Dumping data for table `PhasingProgramRun`
--

/*!40000 ALTER TABLE `PhasingProgramRun` DISABLE KEYS */;
/*!40000 ALTER TABLE `PhasingProgramRun` ENABLE KEYS */;

--
-- Dumping data for table `PhasingStatistics`
--

/*!40000 ALTER TABLE `PhasingStatistics` DISABLE KEYS */;
/*!40000 ALTER TABLE `PhasingStatistics` ENABLE KEYS */;

--
-- Dumping data for table `PhasingStep`
--

/*!40000 ALTER TABLE `PhasingStep` DISABLE KEYS */;
/*!40000 ALTER TABLE `PhasingStep` ENABLE KEYS */;

--
-- Dumping data for table `Phasing_has_Scaling`
--

/*!40000 ALTER TABLE `Phasing_has_Scaling` DISABLE KEYS */;
/*!40000 ALTER TABLE `Phasing_has_Scaling` ENABLE KEYS */;

--
-- Dumping data for table `PlateGroup`
--

/*!40000 ALTER TABLE `PlateGroup` DISABLE KEYS */;
/*!40000 ALTER TABLE `PlateGroup` ENABLE KEYS */;

--
-- Dumping data for table `Position`
--

/*!40000 ALTER TABLE `Position` DISABLE KEYS */;
INSERT INTO `Position` (`positionId`, `relativePositionId`, `posX`, `posY`, `posZ`, `scale`, `recordTimeStamp`, `X`, `Y`, `Z`) VALUES (2,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(5,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `Position` ENABLE KEYS */;

--
-- Dumping data for table `PreparePhasingData`
--

/*!40000 ALTER TABLE `PreparePhasingData` DISABLE KEYS */;
/*!40000 ALTER TABLE `PreparePhasingData` ENABLE KEYS */;

--
-- Dumping data for table `ProcessingJob`
--

/*!40000 ALTER TABLE `ProcessingJob` DISABLE KEYS */;
INSERT INTO `ProcessingJob` (`processingJobId`, `dataCollectionId`, `displayName`, `comments`, `recordTimestamp`, `recipe`, `automatic`) VALUES (5,1052503,'test job 01','Testing the job submission system','2017-10-16 11:02:12','DIALS/xia2',0);
/*!40000 ALTER TABLE `ProcessingJob` ENABLE KEYS */;

--
-- Dumping data for table `ProcessingJobImageSweep`
--

/*!40000 ALTER TABLE `ProcessingJobImageSweep` DISABLE KEYS */;
INSERT INTO `ProcessingJobImageSweep` (`processingJobImageSweepId`, `processingJobId`, `dataCollectionId`, `startImage`, `endImage`) VALUES (5,5,1052503,1,270),(8,5,1052503,271,360);
/*!40000 ALTER TABLE `ProcessingJobImageSweep` ENABLE KEYS */;

--
-- Dumping data for table `ProcessingJobParameter`
--

/*!40000 ALTER TABLE `ProcessingJobParameter` DISABLE KEYS */;
INSERT INTO `ProcessingJobParameter` (`processingJobParameterId`, `processingJobId`, `parameterKey`, `parameterValue`) VALUES (5,5,'vortex factor','1.8*10^102'),(8,5,'80s factor','0.87*10^-93');
/*!40000 ALTER TABLE `ProcessingJobParameter` ENABLE KEYS */;

--
-- Dumping data for table `Project`
--

/*!40000 ALTER TABLE `Project` DISABLE KEYS */;
/*!40000 ALTER TABLE `Project` ENABLE KEYS */;

--
-- Dumping data for table `Project_has_BLSample`
--

/*!40000 ALTER TABLE `Project_has_BLSample` DISABLE KEYS */;
/*!40000 ALTER TABLE `Project_has_BLSample` ENABLE KEYS */;

--
-- Dumping data for table `Project_has_DCGroup`
--

/*!40000 ALTER TABLE `Project_has_DCGroup` DISABLE KEYS */;
/*!40000 ALTER TABLE `Project_has_DCGroup` ENABLE KEYS */;

--
-- Dumping data for table `Project_has_EnergyScan`
--

/*!40000 ALTER TABLE `Project_has_EnergyScan` DISABLE KEYS */;
/*!40000 ALTER TABLE `Project_has_EnergyScan` ENABLE KEYS */;

--
-- Dumping data for table `Project_has_Person`
--

/*!40000 ALTER TABLE `Project_has_Person` DISABLE KEYS */;
/*!40000 ALTER TABLE `Project_has_Person` ENABLE KEYS */;

--
-- Dumping data for table `Project_has_Protein`
--

/*!40000 ALTER TABLE `Project_has_Protein` DISABLE KEYS */;
/*!40000 ALTER TABLE `Project_has_Protein` ENABLE KEYS */;

--
-- Dumping data for table `Project_has_Session`
--

/*!40000 ALTER TABLE `Project_has_Session` DISABLE KEYS */;
/*!40000 ALTER TABLE `Project_has_Session` ENABLE KEYS */;

--
-- Dumping data for table `Project_has_Shipping`
--

/*!40000 ALTER TABLE `Project_has_Shipping` DISABLE KEYS */;
/*!40000 ALTER TABLE `Project_has_Shipping` ENABLE KEYS */;

--
-- Dumping data for table `Project_has_User`
--

/*!40000 ALTER TABLE `Project_has_User` DISABLE KEYS */;
/*!40000 ALTER TABLE `Project_has_User` ENABLE KEYS */;

--
-- Dumping data for table `Project_has_XFEFSpectrum`
--

/*!40000 ALTER TABLE `Project_has_XFEFSpectrum` DISABLE KEYS */;
/*!40000 ALTER TABLE `Project_has_XFEFSpectrum` ENABLE KEYS */;

--
-- Dumping data for table `Proposal`
--

/*!40000 ALTER TABLE `Proposal` DISABLE KEYS */;
INSERT INTO `Proposal` (`proposalId`, `personId`, `title`, `proposalCode`, `proposalNumber`, `bltimeStamp`, `proposalType`, `externalId`, `state`) VALUES (37027,1,'I03 Commissioning Directory 2016','cm','14451','2015-12-21 15:20:43',NULL,NULL,'Open'),(141666,46266,'Test Proposal cm-0001','cm','1','2016-03-16 16:01:34',NULL,NULL,'Open');
/*!40000 ALTER TABLE `Proposal` ENABLE KEYS */;

--
-- Dumping data for table `ProposalHasPerson`
--

/*!40000 ALTER TABLE `ProposalHasPerson` DISABLE KEYS */;
INSERT INTO `ProposalHasPerson` (`proposalHasPersonId`, `proposalId`, `personId`, `role`) VALUES (4,37027,1,'Principal Investigator');
/*!40000 ALTER TABLE `ProposalHasPerson` ENABLE KEYS */;

--
-- Dumping data for table `Protein`
--

/*!40000 ALTER TABLE `Protein` DISABLE KEYS */;
INSERT INTO `Protein` (`proteinId`, `proposalId`, `name`, `acronym`, `molecularMass`, `proteinType`, `personId`, `bltimeStamp`, `isCreatedBySampleSheet`, `sequence`, `MOD_ID`, `componentTypeId`, `concentrationTypeId`, `global`, `externalId`, `density`, `abundance`) VALUES (4380,141666,'Protein 01','PRT-01',NULL,NULL,NULL,'2016-03-17 15:57:52',0,NULL,NULL,NULL,NULL,0,NULL,NULL,NULL),(4383,141666,'Protein 02','PRT-02',NULL,NULL,NULL,'2016-03-17 16:02:07',0,NULL,NULL,NULL,NULL,0,NULL,NULL,NULL),(4386,141666,'Protein 03','PRT-03',NULL,NULL,NULL,'2016-03-17 16:02:07',0,NULL,NULL,NULL,NULL,0,NULL,NULL,NULL),(4389,141666,'Protein 04','PRT-04',NULL,NULL,NULL,'2016-03-17 16:02:07',0,NULL,NULL,NULL,NULL,0,NULL,NULL,NULL),(4392,141666,'Protein 05','PRT-05',NULL,NULL,NULL,'2016-03-17 16:02:07',0,NULL,NULL,NULL,NULL,0,NULL,NULL,NULL),(4395,141666,'Protein 06','PRT-06',NULL,NULL,NULL,'2016-03-17 16:02:07',0,NULL,NULL,NULL,NULL,0,NULL,NULL,NULL),(4398,141666,'Protein 07','PRT-07',NULL,NULL,NULL,'2016-03-17 16:02:07',0,NULL,NULL,NULL,NULL,0,NULL,NULL,NULL),(4401,141666,'Protein 08','PRT-08',NULL,NULL,NULL,'2016-03-17 16:02:07',0,NULL,NULL,NULL,NULL,0,NULL,NULL,NULL),(4404,141666,'Protein 09','PRT-09',NULL,NULL,NULL,'2016-03-17 16:02:07',0,NULL,NULL,NULL,NULL,0,NULL,NULL,NULL),(4407,141666,'Protein 10','PRT-10',NULL,NULL,NULL,'2016-03-17 16:02:07',0,NULL,NULL,NULL,NULL,0,NULL,NULL,NULL),(4410,141666,'Protein 11','PRT-11',NULL,NULL,NULL,'2016-03-17 16:02:07',0,NULL,NULL,NULL,NULL,0,NULL,NULL,NULL),(4413,141666,'Protein 12','PRT-12',NULL,NULL,NULL,'2016-03-17 16:02:07',0,NULL,NULL,NULL,NULL,0,NULL,NULL,NULL),(121393,37027,'therm','therm',NULL,NULL,NULL,'2016-01-13 13:50:20',0,NULL,NULL,NULL,NULL,0,NULL,NULL,NULL),(123491,37027,NULL,'thau',NULL,NULL,NULL,'2016-02-24 12:12:16',0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(123497,37027,'XPDF comp1','xpdf-comp-01',NULL,NULL,NULL,'2017-03-23 22:03:40',0,NULL,NULL,NULL,NULL,0,NULL,NULL,NULL);
/*!40000 ALTER TABLE `Protein` ENABLE KEYS */;

--
-- Dumping data for table `Protein_has_PDB`
--

/*!40000 ALTER TABLE `Protein_has_PDB` DISABLE KEYS */;
INSERT INTO `Protein_has_PDB` (`proteinhaspdbid`, `proteinid`, `pdbid`) VALUES (5,123497,6);
/*!40000 ALTER TABLE `Protein_has_PDB` ENABLE KEYS */;

--
-- Dumping data for table `Reprocessing`
--

/*!40000 ALTER TABLE `Reprocessing` DISABLE KEYS */;
/*!40000 ALTER TABLE `Reprocessing` ENABLE KEYS */;

--
-- Dumping data for table `ReprocessingImageSweep`
--

/*!40000 ALTER TABLE `ReprocessingImageSweep` DISABLE KEYS */;
/*!40000 ALTER TABLE `ReprocessingImageSweep` ENABLE KEYS */;

--
-- Dumping data for table `ReprocessingParameter`
--

/*!40000 ALTER TABLE `ReprocessingParameter` DISABLE KEYS */;
/*!40000 ALTER TABLE `ReprocessingParameter` ENABLE KEYS */;

--
-- Dumping data for table `RobotAction`
--

/*!40000 ALTER TABLE `RobotAction` DISABLE KEYS */;
/*!40000 ALTER TABLE `RobotAction` ENABLE KEYS */;

--
-- Dumping data for table `Run`
--

/*!40000 ALTER TABLE `Run` DISABLE KEYS */;
/*!40000 ALTER TABLE `Run` ENABLE KEYS */;

--
-- Dumping data for table `SAFETYREQUEST`
--

/*!40000 ALTER TABLE `SAFETYREQUEST` DISABLE KEYS */;
/*!40000 ALTER TABLE `SAFETYREQUEST` ENABLE KEYS */;

--
-- Dumping data for table `SAMPLECELL`
--

/*!40000 ALTER TABLE `SAMPLECELL` DISABLE KEYS */;
/*!40000 ALTER TABLE `SAMPLECELL` ENABLE KEYS */;

--
-- Dumping data for table `SAMPLEEXPOSUREUNIT`
--

/*!40000 ALTER TABLE `SAMPLEEXPOSUREUNIT` DISABLE KEYS */;
/*!40000 ALTER TABLE `SAMPLEEXPOSUREUNIT` ENABLE KEYS */;

--
-- Dumping data for table `SAXSDATACOLLECTIONGROUP`
--

/*!40000 ALTER TABLE `SAXSDATACOLLECTIONGROUP` DISABLE KEYS */;
/*!40000 ALTER TABLE `SAXSDATACOLLECTIONGROUP` ENABLE KEYS */;

--
-- Dumping data for table `SW_onceToken`
--

/*!40000 ALTER TABLE `SW_onceToken` DISABLE KEYS */;
/*!40000 ALTER TABLE `SW_onceToken` ENABLE KEYS */;

--
-- Dumping data for table `SafetyLevel`
--

/*!40000 ALTER TABLE `SafetyLevel` DISABLE KEYS */;
/*!40000 ALTER TABLE `SafetyLevel` ENABLE KEYS */;

--
-- Dumping data for table `SamplePlate`
--

/*!40000 ALTER TABLE `SamplePlate` DISABLE KEYS */;
/*!40000 ALTER TABLE `SamplePlate` ENABLE KEYS */;

--
-- Dumping data for table `SamplePlatePosition`
--

/*!40000 ALTER TABLE `SamplePlatePosition` DISABLE KEYS */;
/*!40000 ALTER TABLE `SamplePlatePosition` ENABLE KEYS */;

--
-- Dumping data for table `SaxsDataCollection`
--

/*!40000 ALTER TABLE `SaxsDataCollection` DISABLE KEYS */;
/*!40000 ALTER TABLE `SaxsDataCollection` ENABLE KEYS */;

--
-- Dumping data for table `ScanParametersModel`
--

/*!40000 ALTER TABLE `ScanParametersModel` DISABLE KEYS */;
INSERT INTO `ScanParametersModel` (`scanParametersModelId`, `scanParametersServiceId`, `dataCollectionPlanId`, `sequenceNumber`, `start`, `stop`, `step`, `array`, `duration`) VALUES (4,4,197788,1,0,90,10,NULL,NULL),(7,4,197788,2,90,180,5,NULL,NULL),(10,4,197788,3,180,270,1,NULL,NULL),(13,4,197788,3,270,360,0.5,NULL,NULL),(16,7,197788,4,20,120,10,NULL,NULL),(20,7,197792,1,0,90,5,NULL,NULL),(23,7,197792,2,90,120,1,NULL,NULL);
/*!40000 ALTER TABLE `ScanParametersModel` ENABLE KEYS */;

--
-- Dumping data for table `ScanParametersService`
--

/*!40000 ALTER TABLE `ScanParametersService` DISABLE KEYS */;
INSERT INTO `ScanParametersService` (`scanParametersServiceId`, `name`, `description`) VALUES (4,'Temperature','Temperature in Celsius'),(7,'Pressure','Pressure in pascal (Pa)');
/*!40000 ALTER TABLE `ScanParametersService` ENABLE KEYS */;

--
-- Dumping data for table `ScheduleComponent`
--

/*!40000 ALTER TABLE `ScheduleComponent` DISABLE KEYS */;
INSERT INTO `ScheduleComponent` (`scheduleComponentId`, `scheduleId`, `offset_hours`, `inspectionTypeId`) VALUES (1,1,0,1),(2,1,12,1),(3,1,24,1),(4,1,96,1),(5,1,48,1),(6,1,72,1),(8,2,24,1),(11,2,48,2),(14,11,0,1),(17,11,12,1),(20,11,24,1),(23,11,36,1),(26,11,60,1),(29,11,96,1),(32,11,156,1),(35,11,252,1),(38,11,408,1),(41,11,660,1),(44,11,1068,1),(47,11,1728,1),(50,11,2796,1),(54,15,3,1),(57,15,6,1),(60,15,9,1),(63,15,12,1),(66,15,18,1),(69,15,24,1),(72,15,30,1),(75,15,36,1),(78,15,42,1),(81,15,48,1),(84,1,120,1),(87,1,144,1),(90,1,168,1),(93,1,336,1),(96,1,504,1);
/*!40000 ALTER TABLE `ScheduleComponent` ENABLE KEYS */;

--
-- Dumping data for table `Screen`
--

/*!40000 ALTER TABLE `Screen` DISABLE KEYS */;
/*!40000 ALTER TABLE `Screen` ENABLE KEYS */;

--
-- Dumping data for table `ScreenComponent`
--

/*!40000 ALTER TABLE `ScreenComponent` DISABLE KEYS */;
/*!40000 ALTER TABLE `ScreenComponent` ENABLE KEYS */;

--
-- Dumping data for table `ScreenComponentGroup`
--

/*!40000 ALTER TABLE `ScreenComponentGroup` DISABLE KEYS */;
/*!40000 ALTER TABLE `ScreenComponentGroup` ENABLE KEYS */;

--
-- Dumping data for table `Screening`
--

/*!40000 ALTER TABLE `Screening` DISABLE KEYS */;
INSERT INTO `Screening` (`screeningId`, `dataCollectionId`, `bltimeStamp`, `programVersion`, `comments`, `shortComments`, `diffractionPlanId`, `dataCollectionGroupId`, `xmlSampleInformation`) VALUES (1894770,1052494,'2016-10-26 08:50:31','mosflm',NULL,'Mosflm native',NULL,1040398,NULL),(1894773,1052494,'2016-10-26 08:50:31','mosflm',NULL,'Mosflm anomalous',NULL,1040398,NULL),(1894774,1052494,'2016-10-26 08:50:31','EDNA MXv1','Standard Native Dataset Multiplicity=3 I/sig=2 Maxlifespan=202 s','EDNAStrategy1',NULL,1040398,NULL),(1894777,1052494,'2016-10-26 08:50:31','EDNA MXv1','strategy with target multiplicity=16, target I/sig=2 Maxlifespan=202 s','EDNAStrategy3',NULL,1040398,NULL),(1894780,1052494,'2016-10-26 08:50:31','EDNA MXv1','Gentle: Target Multiplicity=2 and target I/Sig 2 and Maxlifespan=20 s','EDNAStrategy4',NULL,1040398,NULL),(1894783,1052494,'2016-10-26 08:50:31','EDNA MXv1','Standard Anomalous Dataset Multiplicity=3 I/sig=2 Maxlifespan=202 s','EDNAStrategy2',NULL,1040398,NULL),(1894786,1052494,'2016-10-26 08:50:31','EDNA MXv1','UnderDEV Anomalous Dataset, RadDamage of standard protein','EDNAStrategy5',NULL,1040398,NULL),(1894807,1052503,'2016-10-26 08:50:31','EDNA MXv1','strategy with target multiplicity=16, target I/sig=2 Maxlifespan=202 s','EDNAStrategy3',NULL,1040407,NULL),(1894810,1052503,'2016-10-26 08:50:31','EDNA MXv1','Standard Anomalous Dataset Multiplicity=3 I/sig=2 Maxlifespan=202 s','EDNAStrategy2',NULL,1040407,NULL),(1894812,1052503,'2016-10-26 08:50:31','mosflm',NULL,'Mosflm native',NULL,1040407,NULL),(1894815,1052503,'2016-10-26 08:50:31','mosflm',NULL,'Mosflm anomalous',NULL,1040407,NULL),(1894816,1052503,'2016-10-26 08:50:31','EDNA MXv1','Gentle: Target Multiplicity=2 and target I/Sig 2 and Maxlifespan=20 s','EDNAStrategy4',NULL,1040407,NULL),(1894819,1052503,'2016-10-26 08:50:31','EDNA MXv1','UnderDEV Anomalous Dataset, RadDamage of standard protein','EDNAStrategy5',NULL,1040407,NULL),(1894822,1052503,'2016-10-26 08:50:31','EDNA MXv1','Standard Native Dataset Multiplicity=3 I/sig=2 Maxlifespan=202 s','EDNAStrategy1',NULL,1040407,NULL),(1927968,1066786,'2016-10-26 08:50:31','mosflm',NULL,'Mosflm native',NULL,1054243,NULL),(1927971,1066786,'2016-10-26 08:50:31','mosflm',NULL,'Mosflm anomalous',NULL,1054243,NULL),(1927972,1066786,'2016-10-26 08:50:31','EDNA MXv1','Standard Native Dataset Multiplicity=3 I/sig=2 Maxlifespan=4034 s','EDNAStrategy1',NULL,1054243,NULL),(1927981,1066786,'2016-10-26 08:50:31','EDNA MXv1','Gentle: Target Multiplicity=2 and target I/Sig 2 and Maxlifespan=403 s','EDNAStrategy4',NULL,1054243,NULL),(1927984,1066786,'2016-10-26 08:50:31','EDNA MXv1','strategy with target multiplicity=16, target I/sig=2 Maxlifespan=4034 s','EDNAStrategy3',NULL,1054243,NULL),(1927987,1066786,'2016-10-26 08:50:31','EDNA MXv1','Standard Anomalous Dataset Multiplicity=3 I/sig=2 Maxlifespan=4034 s','EDNAStrategy2',NULL,1054243,NULL),(1927990,1066786,'2016-10-26 08:50:31','EDNA MXv1','UnderDEV Anomalous Dataset, RadDamage of standard protein','EDNAStrategy5',NULL,1054243,NULL);
/*!40000 ALTER TABLE `Screening` ENABLE KEYS */;

--
-- Dumping data for table `ScreeningInput`
--

/*!40000 ALTER TABLE `ScreeningInput` DISABLE KEYS */;
INSERT INTO `ScreeningInput` (`screeningInputId`, `screeningId`, `beamX`, `beamY`, `rmsErrorLimits`, `minimumFractionIndexed`, `maximumFractionRejected`, `minimumSignalToNoise`, `diffractionPlanId`, `xmlSampleInformation`) VALUES (983791,1894774,208.731,214.298,NULL,NULL,NULL,NULL,NULL,NULL),(983794,1894777,208.731,214.298,NULL,NULL,NULL,NULL,NULL,NULL),(983797,1894780,208.731,214.298,NULL,NULL,NULL,NULL,NULL,NULL),(983800,1894783,208.731,214.298,NULL,NULL,NULL,NULL,NULL,NULL),(983803,1894786,208.731,214.298,NULL,NULL,NULL,NULL,NULL,NULL),(983821,1894807,208.32,214.339,NULL,NULL,NULL,NULL,NULL,NULL),(983824,1894810,208.32,214.339,NULL,NULL,NULL,NULL,NULL,NULL),(983827,1894816,208.32,214.339,NULL,NULL,NULL,NULL,NULL,NULL),(983830,1894819,208.32,214.339,NULL,NULL,NULL,NULL,NULL,NULL),(983833,1894822,208.32,214.339,NULL,NULL,NULL,NULL,NULL,NULL),(1013146,1927972,208.32,214.339,NULL,NULL,NULL,NULL,NULL,NULL),(1013155,1927981,208.32,214.339,NULL,NULL,NULL,NULL,NULL,NULL),(1013158,1927984,208.32,214.339,NULL,NULL,NULL,NULL,NULL,NULL),(1013161,1927987,208.32,214.339,NULL,NULL,NULL,NULL,NULL,NULL),(1013164,1927990,208.32,214.339,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `ScreeningInput` ENABLE KEYS */;

--
-- Dumping data for table `ScreeningOutput`
--

/*!40000 ALTER TABLE `ScreeningOutput` DISABLE KEYS */;
INSERT INTO `ScreeningOutput` (`screeningOutputId`, `screeningId`, `statusDescription`, `rejectedReflections`, `resolutionObtained`, `spotDeviationR`, `spotDeviationTheta`, `beamShiftX`, `beamShiftY`, `numSpotsFound`, `numSpotsUsed`, `numSpotsRejected`, `mosaicity`, `iOverSigma`, `diffractionRings`, `SCREENINGSUCCESS`, `mosaicityEstimated`, `rankingResolution`, `program`, `doseTotal`, `totalExposureTime`, `totalRotationRange`, `totalNumberOfImages`, `rFriedel`, `indexingSuccess`, `strategySuccess`, `alignmentSuccess`) VALUES (1489401,1894770,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,1,NULL,NULL,0,0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,0,0),(1489404,1894773,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,1,NULL,NULL,0,0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,0,0),(1489405,1894774,'Labelit: Indexing successful (I23). Integration successful. Strategy calculation successful.',NULL,NULL,0.197,NULL,-0.0094,-0.0618,303,303,0,1.2,NULL,NULL,1,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,0,0),(1489408,1894777,'Labelit: Indexing successful (I23). Integration successful. Strategy calculation successful.',NULL,NULL,0.197,NULL,-0.0094,-0.0618,303,303,0,1.2,NULL,NULL,1,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,0,0),(1489411,1894780,'Labelit: Indexing successful (I23). Integration successful. Strategy calculation successful.',NULL,NULL,0.197,NULL,-0.0094,-0.0618,303,303,0,1.2,NULL,NULL,1,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,0,0),(1489414,1894783,'Labelit: Indexing successful (I23). Integration successful. Strategy calculation successful.',NULL,NULL,0.197,NULL,-0.0094,-0.0618,303,303,0,1.2,NULL,NULL,1,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,0,0),(1489417,1894786,'Labelit: Indexing successful (I23). Integration successful. Strategy calculation successful.',NULL,NULL,0.197,NULL,-0.0094,-0.0618,303,303,0,1.2,NULL,NULL,1,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,0,0),(1489438,1894807,'Labelit: Indexing successful (I23). Integration successful. Strategy calculation successful.',NULL,NULL,0.184,NULL,0.0495,-0.0405,294,294,0,1.35,NULL,NULL,1,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,0,0),(1489441,1894810,'Labelit: Indexing successful (I23). Integration successful. Strategy calculation successful.',NULL,NULL,0.184,NULL,0.0495,-0.0405,294,294,0,1.35,NULL,NULL,1,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,0,0),(1489443,1894812,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,1.6,NULL,NULL,0,0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,0,0),(1489446,1894815,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,1.6,NULL,NULL,0,0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,0,0),(1489447,1894816,'Labelit: Indexing successful (I23). Integration successful. Strategy calculation successful.',NULL,NULL,0.184,NULL,0.0495,-0.0405,294,294,0,1.35,NULL,NULL,1,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,0,0),(1489450,1894819,'Labelit: Indexing successful (I23). Integration successful. Strategy calculation successful.',NULL,NULL,0.184,NULL,0.0495,-0.0405,294,294,0,1.35,NULL,NULL,1,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,0,0),(1489453,1894822,'Labelit: Indexing successful (I23). Integration successful. Strategy calculation successful.',NULL,NULL,0.184,NULL,0.0495,-0.0405,294,294,0,1.35,NULL,NULL,1,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,0,0),(1522596,1927968,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0.8,NULL,NULL,0,0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,0,0),(1522599,1927971,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0.8,NULL,NULL,0,0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,0,0),(1522600,1927972,'Labelit: Indexing successful (P4). Integration successful. Strategy calculation successful.',NULL,NULL,0.166,NULL,0.0195,-0.0105,434,434,0,0.7,NULL,NULL,1,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,0,0),(1522609,1927981,'Labelit: Indexing successful (P4). Integration successful. Strategy calculation successful.',NULL,NULL,0.166,NULL,0.0195,-0.0105,434,434,0,0.7,NULL,NULL,1,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,0,0),(1522612,1927984,'Labelit: Indexing successful (P4). Integration successful. Strategy calculation successful.',NULL,NULL,0.166,NULL,0.0195,-0.0105,434,434,0,0.7,NULL,NULL,1,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,0,0),(1522615,1927987,'Labelit: Indexing successful (P4). Integration successful. Strategy calculation successful.',NULL,NULL,0.166,NULL,0.0195,-0.0105,434,434,0,0.7,NULL,NULL,1,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,0,0),(1522618,1927990,'Labelit: Indexing successful (P4). Integration successful. Strategy calculation successful.',NULL,NULL,0.166,NULL,0.0195,-0.0105,434,434,0,0.7,NULL,NULL,1,1,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,0,0);
/*!40000 ALTER TABLE `ScreeningOutput` ENABLE KEYS */;

--
-- Dumping data for table `ScreeningOutputLattice`
--

/*!40000 ALTER TABLE `ScreeningOutputLattice` DISABLE KEYS */;
INSERT INTO `ScreeningOutputLattice` (`screeningOutputLatticeId`, `screeningOutputId`, `spaceGroup`, `pointGroup`, `bravaisLattice`, `rawOrientationMatrix_a_x`, `rawOrientationMatrix_a_y`, `rawOrientationMatrix_a_z`, `rawOrientationMatrix_b_x`, `rawOrientationMatrix_b_y`, `rawOrientationMatrix_b_z`, `rawOrientationMatrix_c_x`, `rawOrientationMatrix_c_y`, `rawOrientationMatrix_c_z`, `unitCell_a`, `unitCell_b`, `unitCell_c`, `unitCell_alpha`, `unitCell_beta`, `unitCell_gamma`, `bltimeStamp`, `labelitIndexing`) VALUES (1309566,1489401,'I23',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,76.339,76.339,76.339,90,90,90,'2016-04-13 11:19:21',0),(1309569,1489404,'I23',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,76.339,76.339,76.339,90,90,90,'2016-04-13 11:19:21',0),(1309570,1489405,'I23',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,76.3,76.3,76.3,90,90,90,'2016-04-13 11:19:24',0),(1309573,1489408,'I23',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,76.3,76.3,76.3,90,90,90,'2016-04-13 11:19:27',0),(1309576,1489411,'I23',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,76.3,76.3,76.3,90,90,90,'2016-04-13 11:19:29',0),(1309579,1489414,'I23',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,76.3,76.3,76.3,90,90,90,'2016-04-13 11:19:34',0),(1309582,1489417,'I23',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,76.3,76.3,76.3,90,90,90,'2016-04-13 11:19:34',0),(1309603,1489438,'I23',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,76.52,76.52,76.52,90,90,90,'2016-04-13 11:22:30',0),(1309606,1489441,'I23',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,76.52,76.52,76.52,90,90,90,'2016-04-13 11:22:35',0),(1309608,1489443,'C2221',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,76.645,108.218,108.03,90,90,90,'2016-04-13 11:22:36',0),(1309611,1489446,'C2221',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,76.645,108.218,108.03,90,90,90,'2016-04-13 11:22:36',0),(1309612,1489447,'I23',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,76.52,76.52,76.52,90,90,90,'2016-04-13 11:22:39',0),(1309615,1489450,'I23',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,76.52,76.52,76.52,90,90,90,'2016-04-13 11:22:40',0),(1309618,1489453,'I23',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,76.52,76.52,76.52,90,90,90,'2016-04-13 11:22:44',0),(1323825,1522596,'P41212',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,57.334,57.334,148.969,90,90,90,'2016-04-18 10:05:24',0),(1323828,1522599,'P41212',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,57.334,57.334,148.969,90,90,90,'2016-04-18 10:05:24',0),(1323829,1522600,'P4',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,57.29,57.29,149.07,90,90,90,'2016-04-14 02:19:04',0),(1323838,1522609,'P4',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,57.29,57.29,149.07,90,90,90,'2016-04-14 02:19:04',0),(1323841,1522612,'P4',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,57.29,57.29,149.07,90,90,90,'2016-04-14 02:19:04',0),(1323844,1522615,'P4',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,57.29,57.29,149.07,90,90,90,'2016-04-14 02:19:04',0),(1323847,1522618,'P4',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,57.29,57.29,149.07,90,90,90,'2016-04-14 02:19:04',0);
/*!40000 ALTER TABLE `ScreeningOutputLattice` ENABLE KEYS */;

--
-- Dumping data for table `ScreeningRank`
--

/*!40000 ALTER TABLE `ScreeningRank` DISABLE KEYS */;
/*!40000 ALTER TABLE `ScreeningRank` ENABLE KEYS */;

--
-- Dumping data for table `ScreeningRankSet`
--

/*!40000 ALTER TABLE `ScreeningRankSet` DISABLE KEYS */;
/*!40000 ALTER TABLE `ScreeningRankSet` ENABLE KEYS */;

--
-- Dumping data for table `ScreeningStrategy`
--

/*!40000 ALTER TABLE `ScreeningStrategy` DISABLE KEYS */;
INSERT INTO `ScreeningStrategy` (`screeningStrategyId`, `screeningOutputId`, `phiStart`, `phiEnd`, `rotation`, `exposureTime`, `resolution`, `completeness`, `multiplicity`, `anomalous`, `program`, `rankingResolution`, `transmission`) VALUES (1473909,1489401,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,'mosflm - native',NULL,NULL),(1473912,1489404,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,'mosflm - anomalous',NULL,NULL),(1473913,1489405,NULL,NULL,NULL,0.428,NULL,NULL,NULL,0,'BEST',1.41,NULL),(1473916,1489408,NULL,NULL,NULL,0.112,NULL,NULL,NULL,0,'BEST',1.41,NULL),(1473919,1489411,NULL,NULL,NULL,0.049,NULL,NULL,NULL,0,'BEST',1.49,NULL),(1473922,1489414,NULL,NULL,NULL,0.365,NULL,NULL,NULL,1,'BEST',1.41,NULL),(1473925,1489417,NULL,NULL,NULL,0.365,NULL,NULL,NULL,1,'BEST',1.41,NULL),(1473946,1489438,NULL,NULL,NULL,0.073,NULL,NULL,NULL,0,'BEST',1.44,NULL),(1473949,1489441,NULL,NULL,NULL,0.333,NULL,NULL,NULL,1,'BEST',1.47,NULL),(1473951,1489443,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,'mosflm - native',NULL,NULL),(1473954,1489446,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,'mosflm - anomalous',NULL,NULL),(1473955,1489447,NULL,NULL,NULL,0.086,NULL,NULL,NULL,0,'BEST',1.57,NULL),(1473958,1489450,NULL,NULL,NULL,0.333,NULL,NULL,NULL,1,'BEST',1.47,NULL),(1473961,1489453,NULL,NULL,NULL,0.296,NULL,NULL,NULL,0,'BEST',1.44,NULL),(1507101,1522596,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,'mosflm - native',NULL,NULL),(1507104,1522599,NULL,NULL,NULL,NULL,NULL,NULL,NULL,0,'mosflm - anomalous',NULL,NULL),(1507105,1522600,NULL,NULL,NULL,0.01,NULL,NULL,NULL,0,'BEST',1.13,NULL),(1507114,1522609,NULL,NULL,NULL,0.01,NULL,NULL,NULL,0,'BEST',1.23,NULL),(1507117,1522612,NULL,NULL,NULL,0.01,NULL,NULL,NULL,0,'BEST',1.14,NULL),(1507120,1522615,NULL,NULL,NULL,0.01,NULL,NULL,NULL,1,'BEST',1.16,NULL),(1507123,1522618,NULL,NULL,NULL,0.01,NULL,NULL,NULL,1,'BEST',1.16,NULL);
/*!40000 ALTER TABLE `ScreeningStrategy` ENABLE KEYS */;

--
-- Dumping data for table `ScreeningStrategySubWedge`
--

/*!40000 ALTER TABLE `ScreeningStrategySubWedge` DISABLE KEYS */;
INSERT INTO `ScreeningStrategySubWedge` (`screeningStrategySubWedgeId`, `screeningStrategyWedgeId`, `subWedgeNumber`, `rotationAxis`, `axisStart`, `axisEnd`, `exposureTime`, `transmission`, `oscillationRange`, `completeness`, `multiplicity`, `RESOLUTION`, `doseTotal`, `numberOfImages`, `comments`) VALUES (1111566,1143792,NULL,'Omega',64,109,0,NULL,1.4,1,NULL,1.22,NULL,33,NULL),(1111569,1143795,NULL,'Omega',74,119,0,NULL,1.4,0.98,NULL,1.22,NULL,33,NULL),(1111570,1143796,1,'Omega',7,40,0.428,100,0.15,1,4.07,1.41,NULL,220,NULL),(1111573,1143799,1,'Omega',30,160.05,0.112,100,0.15,1,16.02,1.41,NULL,867,NULL),(1111576,1143802,1,'Omega',93,123.15,0.049,100,0.15,1,3.71,1.49,NULL,202,NULL),(1111579,1143805,1,'Omega',225,273,0.365,100,0.1,0.997,3.08,1.41,NULL,480,NULL),(1111582,1143808,1,'Omega',225,273,0.365,100,0.1,0.997,3.08,1.41,NULL,480,NULL),(1111603,1143829,1,'Omega',42,171,0.073,100,0.15,1,15.93,1.51,NULL,860,NULL),(1111606,1143832,1,'Omega',39,91.05,0.333,100,0.15,0.999,3.35,1.51,NULL,347,NULL),(1111608,1143834,NULL,'Omega',265,355,0,NULL,0.2,0.99,NULL,1.47,NULL,450,NULL),(1111611,1143837,NULL,'Omega',265,355,0,NULL,0.2,0.92,NULL,1.47,NULL,450,NULL),(1111612,1143838,1,'Omega',7,39.1,0.086,100,0.15,1,3.95,1.57,NULL,215,NULL),(1111615,1143841,1,'Omega',39,91.05,0.333,100,0.15,0.999,3.35,1.51,NULL,347,NULL),(1111618,1143844,1,'Omega',144,175.05,0.296,100,0.15,1,3.83,1.51,NULL,208,NULL),(1123965,1156191,NULL,'Omega',48,93,0,NULL,0.5,0.99,NULL,1.47,NULL,90,NULL),(1123968,1156194,NULL,'Omega',43,88,0,NULL,0.5,0.93,NULL,1.47,NULL,90,NULL),(1123969,1156195,1,'Omega',9,88,0.01,71.7436,0.1,0.999,3.34,1.51,NULL,790,NULL),(1123978,1156204,1,'Omega',10,88,0.01,72.4236,0.1,0.999,3.3,1.51,NULL,780,NULL),(1123981,1156207,1,'Omega',0,360,0.01,16.1595,0.1,1,15.21,1.51,NULL,3600,NULL),(1123984,1156210,1,'Omega',87,239,0.01,72.2048,0.1,0.99,3.29,1.51,NULL,1520,NULL),(1123987,1156213,1,'Omega',87,239,0.01,72.2048,0.1,0.99,3.29,1.51,NULL,1520,NULL);
/*!40000 ALTER TABLE `ScreeningStrategySubWedge` ENABLE KEYS */;

--
-- Dumping data for table `ScreeningStrategyWedge`
--

/*!40000 ALTER TABLE `ScreeningStrategyWedge` DISABLE KEYS */;
INSERT INTO `ScreeningStrategyWedge` (`screeningStrategyWedgeId`, `screeningStrategyId`, `wedgeNumber`, `resolution`, `completeness`, `multiplicity`, `doseTotal`, `numberOfImages`, `phi`, `kappa`, `chi`, `comments`, `wavelength`) VALUES (1143792,1473909,1,1.22,1,NULL,NULL,33,NULL,NULL,NULL,NULL,NULL),(1143795,1473912,1,1.22,0.98,NULL,NULL,33,NULL,NULL,NULL,NULL,NULL),(1143796,1473913,1,1.41,1,4.07,0,220,NULL,NULL,NULL,NULL,NULL),(1143799,1473916,1,1.41,1,16.02,0,867,NULL,NULL,NULL,NULL,NULL),(1143802,1473919,1,1.49,1,3.71,0,202,NULL,NULL,NULL,NULL,NULL),(1143805,1473922,1,1.41,0.997,3.08,0,480,NULL,NULL,NULL,NULL,NULL),(1143808,1473925,1,1.41,0.997,3.08,0,480,NULL,NULL,NULL,NULL,NULL),(1143829,1473946,1,1.51,1,15.93,0,860,NULL,NULL,NULL,NULL,NULL),(1143832,1473949,1,1.51,0.999,3.35,0,347,NULL,NULL,NULL,NULL,NULL),(1143834,1473951,1,1.47,0.99,NULL,NULL,450,NULL,NULL,NULL,NULL,NULL),(1143837,1473954,1,1.47,0.92,NULL,NULL,450,NULL,NULL,NULL,NULL,NULL),(1143838,1473955,1,1.57,1,3.95,0,215,NULL,NULL,NULL,NULL,NULL),(1143841,1473958,1,1.51,0.999,3.35,0,347,NULL,NULL,NULL,NULL,NULL),(1143844,1473961,1,1.51,1,3.83,0,208,NULL,NULL,NULL,NULL,NULL),(1156191,1507101,1,1.47,0.99,NULL,NULL,90,NULL,NULL,NULL,NULL,NULL),(1156194,1507104,1,1.47,0.93,NULL,NULL,90,NULL,NULL,NULL,NULL,NULL),(1156195,1507105,1,1.51,0.999,3.34,0,790,NULL,NULL,NULL,NULL,NULL),(1156204,1507114,1,1.51,0.999,3.3,0,780,NULL,NULL,NULL,NULL,NULL),(1156207,1507117,1,1.51,1,15.21,0,3600,NULL,NULL,NULL,NULL,NULL),(1156210,1507120,1,1.51,0.99,3.29,0,1520,NULL,NULL,NULL,NULL,NULL),(1156213,1507123,1,1.51,0.99,3.29,0,1520,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `ScreeningStrategyWedge` ENABLE KEYS */;

--
-- Dumping data for table `Session_has_Person`
--

/*!40000 ALTER TABLE `Session_has_Person` DISABLE KEYS */;
INSERT INTO `Session_has_Person` (`sessionId`, `personId`, `role`, `remote`) VALUES (55167,1,'Co-Investigator',0),(55168,1,'Co-Investigator',0);
/*!40000 ALTER TABLE `Session_has_Person` ENABLE KEYS */;

--
-- Dumping data for table `Shipping`
--

/*!40000 ALTER TABLE `Shipping` DISABLE KEYS */;
INSERT INTO `Shipping` (`shippingId`, `proposalId`, `shippingName`, `deliveryAgent_agentName`, `deliveryAgent_shippingDate`, `deliveryAgent_deliveryDate`, `deliveryAgent_agentCode`, `deliveryAgent_flightCode`, `shippingStatus`, `bltimeStamp`, `laboratoryId`, `isStorageShipping`, `creationDate`, `comments`, `sendingLabContactId`, `returnLabContactId`, `returnCourier`, `dateOfShippingToUser`, `shippingType`, `SAFETYLEVEL`, `deliveryAgent_flightCodeTimestamp`, `deliveryAgent_label`, `readyByTime`, `closeTime`, `physicalLocation`, `deliveryAgent_pickupConfirmationTimestamp`, `deliveryAgent_pickupConfirmation`, `deliveryAgent_readyByTime`, `deliveryAgent_callinTime`, `deliveryAgent_productcode`, `deliveryAgent_flightCodePersonId`) VALUES (474,141666,'cm-0001 1 processing',NULL,NULL,NULL,NULL,NULL,'processing',NULL,NULL,0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(477,141666,'cm-0001 2 processing',NULL,NULL,NULL,NULL,NULL,'processing',NULL,NULL,0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(480,141666,'cm-0001 3 processing',NULL,NULL,NULL,NULL,NULL,'processing',NULL,NULL,0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(6988,37027,'Default Shipping:cm14451-1',NULL,NULL,NULL,NULL,NULL,'processing',NULL,NULL,0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(7227,37027,'cm14451-2_Shipment1',NULL,NULL,NULL,NULL,NULL,'processing','2016-02-10 13:03:07',NULL,0,'2016-02-10 13:03:07',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(7231,37027,'VMXi Simulator Test shipment',NULL,NULL,NULL,NULL,NULL,'opened',NULL,NULL,0,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `Shipping` ENABLE KEYS */;

--
-- Dumping data for table `ShippingHasSession`
--

/*!40000 ALTER TABLE `ShippingHasSession` DISABLE KEYS */;
INSERT INTO `ShippingHasSession` (`shippingId`, `sessionId`) VALUES (474,339525),(477,339528),(480,339531),(6988,55167),(7227,55168);
/*!40000 ALTER TABLE `ShippingHasSession` ENABLE KEYS */;

--
-- Dumping data for table `Sleeve`
--

/*!40000 ALTER TABLE `Sleeve` DISABLE KEYS */;
/*!40000 ALTER TABLE `Sleeve` ENABLE KEYS */;

--
-- Dumping data for table `SpaceGroup`
--

/*!40000 ALTER TABLE `SpaceGroup` DISABLE KEYS */;
/*!40000 ALTER TABLE `SpaceGroup` ENABLE KEYS */;

--
-- Dumping data for table `Specimen`
--

/*!40000 ALTER TABLE `Specimen` DISABLE KEYS */;
/*!40000 ALTER TABLE `Specimen` ENABLE KEYS */;

--
-- Dumping data for table `StockSolution`
--

/*!40000 ALTER TABLE `StockSolution` DISABLE KEYS */;
/*!40000 ALTER TABLE `StockSolution` ENABLE KEYS */;

--
-- Dumping data for table `Stoichiometry`
--

/*!40000 ALTER TABLE `Stoichiometry` DISABLE KEYS */;
/*!40000 ALTER TABLE `Stoichiometry` ENABLE KEYS */;

--
-- Dumping data for table `Structure`
--

/*!40000 ALTER TABLE `Structure` DISABLE KEYS */;
/*!40000 ALTER TABLE `Structure` ENABLE KEYS */;

--
-- Dumping data for table `SubstructureDetermination`
--

/*!40000 ALTER TABLE `SubstructureDetermination` DISABLE KEYS */;
/*!40000 ALTER TABLE `SubstructureDetermination` ENABLE KEYS */;

--
-- Dumping data for table `Subtraction`
--

/*!40000 ALTER TABLE `Subtraction` DISABLE KEYS */;
/*!40000 ALTER TABLE `Subtraction` ENABLE KEYS */;

--
-- Dumping data for table `SubtractionToAbInitioModel`
--

/*!40000 ALTER TABLE `SubtractionToAbInitioModel` DISABLE KEYS */;
/*!40000 ALTER TABLE `SubtractionToAbInitioModel` ENABLE KEYS */;

--
-- Dumping data for table `UserGroup`
--

/*!40000 ALTER TABLE `UserGroup` DISABLE KEYS */;
INSERT INTO `UserGroup` (`userGroupId`, `name`) VALUES (39,'autocollect'),(17,'bag_stats'),(20,'bl_stats'),(8,'developers'),(9,'ehc'),(6,'em_admin'),(10,'fault_admin'),(2,'mx_admin'),(14,'pdb_stats'),(4,'powder_admin'),(3,'saxs_admin'),(28,'ship_manage'),(12,'sm_admin'),(1,'super_admin'),(24,'temp_mx_admin'),(5,'tomo_admin'),(11,'vmxi'),(34,'xpdf_admin');
/*!40000 ALTER TABLE `UserGroup` ENABLE KEYS */;

--
-- Dumping data for table `UserGroup_has_Permission`
--

/*!40000 ALTER TABLE `UserGroup_has_Permission` DISABLE KEYS */;
INSERT INTO `UserGroup_has_Permission` (`userGroupId`, `permissionId`) VALUES (1,1),(1,7),(1,8),(1,9),(1,10),(1,11),(1,18),(1,20),(1,23),(1,49),(2,1),(2,6),(2,23),(2,80),(3,7),(3,23),(4,20),(5,10),(6,8),(6,23),(8,1),(8,2),(8,4),(8,6),(8,7),(8,8),(8,9),(8,10),(8,11),(8,18),(8,20),(8,23),(8,26),(8,29),(8,37),(8,49),(9,1),(9,6),(10,12),(10,77),(11,13),(11,15),(11,16),(11,17),(11,32),(11,43),(11,55),(11,58),(11,64),(12,18),(14,1),(17,26),(20,29),(24,1),(28,23),(28,37),(34,49),(39,69);
/*!40000 ALTER TABLE `UserGroup_has_Permission` ENABLE KEYS */;

--
-- Dumping data for table `UserGroup_has_Person`
--

/*!40000 ALTER TABLE `UserGroup_has_Person` DISABLE KEYS */;
/*!40000 ALTER TABLE `UserGroup_has_Person` ENABLE KEYS */;

--
-- Dumping data for table `Workflow`
--

/*!40000 ALTER TABLE `Workflow` DISABLE KEYS */;
/*!40000 ALTER TABLE `Workflow` ENABLE KEYS */;

--
-- Dumping data for table `WorkflowMesh`
--

/*!40000 ALTER TABLE `WorkflowMesh` DISABLE KEYS */;
/*!40000 ALTER TABLE `WorkflowMesh` ENABLE KEYS */;

--
-- Dumping data for table `WorkflowStep`
--

/*!40000 ALTER TABLE `WorkflowStep` DISABLE KEYS */;
/*!40000 ALTER TABLE `WorkflowStep` ENABLE KEYS */;

--
-- Dumping data for table `XFEFluorescenceSpectrum`
--

/*!40000 ALTER TABLE `XFEFluorescenceSpectrum` DISABLE KEYS */;
INSERT INTO `XFEFluorescenceSpectrum` (`xfeFluorescenceSpectrumId`, `sessionId`, `blSampleId`, `jpegScanFileFullPath`, `startTime`, `endTime`, `filename`, `exposureTime`, `axisPosition`, `beamTransmission`, `annotatedPymcaXfeSpectrum`, `fittedDataFileFullPath`, `scanFileFullPath`, `energy`, `beamSizeVertical`, `beamSizeHorizontal`, `crystalClass`, `comments`, `blSubSampleId`, `flux`, `flux_end`, `workingDirectory`) VALUES (1766,55167,NULL,'/dls/i03/data/2016/cm14451-1/20160112_14_49_14.png','2016-01-12 14:49:14','2016-01-12 14:50:05','/dls/i03/data/2016/cm14451-1/20160112_14_49_14.mca',3,NULL,6.4,'/dls/i03/data/2016/cm14451-1/20160112_14_49_14.html',NULL,'/dls/i03/data/2016/cm14451-1/20160112_14_49_14.dat',12700,20,50,NULL,NULL,NULL,NULL,NULL,NULL),(1779,55167,374693,'/dls/i03/data/2016/cm14451-1/20160113_15_53_23.png','2016-01-13 15:53:23','2016-01-13 15:54:53','/dls/i03/data/2016/cm14451-1/20160113_15_53_23.mca',3,NULL,1.6,'/dls/i03/data/2016/cm14451-1/20160113_15_53_23.html',NULL,'/dls/i03/data/2016/cm14451-1/20160113_15_53_23.dat',12700,20,20,NULL,NULL,NULL,NULL,NULL,NULL),(1780,55167,374693,'/dls/i03/data/2016/cm14451-1/20160113_16_50_27.png','2016-01-13 16:50:27','2016-01-13 16:51:27','/dls/i03/data/2016/cm14451-1/20160113_16_50_27.mca',3,NULL,25.6,'/dls/i03/data/2016/cm14451-1/20160113_16_50_27.html',NULL,'/dls/i03/data/2016/cm14451-1/20160113_16_50_27.dat',12700,20,20,NULL,NULL,NULL,NULL,NULL,NULL),(1781,55167,374693,'/dls/i03/data/2016/cm14451-1/20160113_16_51_54.png','2016-01-13 16:51:54','2016-01-13 16:52:29','/dls/i03/data/2016/cm14451-1/20160113_16_51_54.mca',1,NULL,100,'/dls/i03/data/2016/cm14451-1/20160113_16_51_54.html',NULL,'/dls/i03/data/2016/cm14451-1/20160113_16_51_54.dat',12700,20,20,NULL,NULL,NULL,NULL,NULL,NULL),(1782,55167,374693,'/dls/i03/data/2016/cm14451-1/20160113_16_55_14.png','2016-01-13 16:55:14','2016-01-13 16:55:24','/dls/i03/data/2016/cm14451-1/20160113_16_55_14.mca',1,NULL,1.59925,'/dls/i03/data/2016/cm14451-1/20160113_16_55_14.html',NULL,'/dls/i03/data/2016/cm14451-1/20160113_16_55_14.dat',12700,20,20,NULL,NULL,NULL,NULL,NULL,NULL),(1783,55167,374693,'/dls/i03/data/2016/cm14451-1/20160113_16_57_18.png','2016-01-13 16:57:18','2016-01-13 16:57:28','/dls/i03/data/2016/cm14451-1/20160113_16_57_18.mca',1,NULL,1.59925,'/dls/i03/data/2016/cm14451-1/20160113_16_57_18.html',NULL,'/dls/i03/data/2016/cm14451-1/20160113_16_57_18.dat',12700,20,50,NULL,NULL,NULL,NULL,NULL,NULL),(1784,55167,374693,'/dls/i03/data/2016/cm14451-1/20160113_16_58_02.png','2016-01-13 16:58:02','2016-01-13 16:58:13','/dls/i03/data/2016/cm14451-1/20160113_16_58_02.mca',1,NULL,1.59925,'/dls/i03/data/2016/cm14451-1/20160113_16_58_02.html',NULL,'/dls/i03/data/2016/cm14451-1/20160113_16_58_02.dat',12700,20,80,NULL,NULL,NULL,NULL,NULL,NULL),(1785,55167,374693,'/dls/i03/data/2016/cm14451-1/20160113_16_59_00.png','2016-01-13 16:59:00','2016-01-13 16:59:12','/dls/i03/data/2016/cm14451-1/20160113_16_59_00.mca',1,NULL,1.59925,'/dls/i03/data/2016/cm14451-1/20160113_16_59_00.html',NULL,'/dls/i03/data/2016/cm14451-1/20160113_16_59_00.dat',12700,20,80,NULL,NULL,NULL,NULL,NULL,NULL),(1786,55167,374693,'/dls/i03/data/2016/cm14451-1/20160113_16_59_53.png','2016-01-13 16:59:53','2016-01-13 17:00:04','/dls/i03/data/2016/cm14451-1/20160113_16_59_53.mca',1,NULL,1.59925,'/dls/i03/data/2016/cm14451-1/20160113_16_59_53.html',NULL,'/dls/i03/data/2016/cm14451-1/20160113_16_59_53.dat',12700,20,80,NULL,NULL,NULL,NULL,NULL,NULL),(1787,55167,374693,'/dls/i03/data/2016/cm14451-1/20160113_17_01_34.png','2016-01-13 17:01:34','2016-01-13 17:01:49','/dls/i03/data/2016/cm14451-1/20160113_17_01_34.mca',1,NULL,30.0212,'/dls/i03/data/2016/cm14451-1/20160113_17_01_34.html',NULL,'/dls/i03/data/2016/cm14451-1/20160113_17_01_34.dat',12700,20,80,NULL,NULL,NULL,NULL,NULL,NULL),(1788,55167,NULL,'/dls/i03/data/2016/cm14451-1/20160113_17_11_40.png','2016-01-13 17:11:40','2016-01-13 17:12:54','/dls/i03/data/2016/cm14451-1/20160113_17_11_40.mca',1,NULL,1.59925,'/dls/i03/data/2016/cm14451-1/20160113_17_11_40.html',NULL,'/dls/i03/data/2016/cm14451-1/20160113_17_11_40.dat',12700,20,80,NULL,NULL,NULL,NULL,NULL,NULL),(1789,55167,NULL,'/dls/i03/data/2016/cm14451-1/20160113_17_13_25.png','2016-01-13 17:13:25','2016-01-13 17:13:36','/dls/i03/data/2016/cm14451-1/20160113_17_13_25.mca',1,NULL,1.59925,'/dls/i03/data/2016/cm14451-1/20160113_17_13_25.html',NULL,'/dls/i03/data/2016/cm14451-1/20160113_17_13_25.dat',12700,20,80,NULL,NULL,NULL,NULL,NULL,NULL),(1790,55167,NULL,'/dls/i03/data/2016/cm14451-1/20160113_17_14_01.png','2016-01-13 17:14:01','2016-01-13 17:14:13','/dls/i03/data/2016/cm14451-1/20160113_17_14_01.mca',1,NULL,1.59925,'/dls/i03/data/2016/cm14451-1/20160113_17_14_01.html',NULL,'/dls/i03/data/2016/cm14451-1/20160113_17_14_01.dat',12700,20,80,NULL,NULL,NULL,NULL,NULL,NULL),(1791,55167,NULL,'/dls/i03/data/2016/cm14451-1/20160113_17_15_13.png','2016-01-13 17:15:13','2016-01-13 17:15:26','/dls/i03/data/2016/cm14451-1/20160113_17_15_13.mca',1,NULL,1.59925,'/dls/i03/data/2016/cm14451-1/20160113_17_15_13.html',NULL,'/dls/i03/data/2016/cm14451-1/20160113_17_15_13.dat',12700,20,80,NULL,NULL,NULL,NULL,NULL,NULL),(1792,55167,NULL,'/dls/i03/data/2016/cm14451-1/20160113_17_20_59.png','2016-01-13 17:20:59','2016-01-13 17:21:10','/dls/i03/data/2016/cm14451-1/20160113_17_20_59.mca',1,NULL,4.99011,'/dls/i03/data/2016/cm14451-1/20160113_17_20_59.html',NULL,'/dls/i03/data/2016/cm14451-1/20160113_17_20_59.dat',12700,20,80,NULL,NULL,NULL,NULL,NULL,NULL),(1793,55167,NULL,'/dls/i03/data/2016/cm14451-1/20160113_17_21_26.png','2016-01-13 17:21:26','2016-01-13 17:21:38','/dls/i03/data/2016/cm14451-1/20160113_17_21_26.mca',1,NULL,4.99011,'/dls/i03/data/2016/cm14451-1/20160113_17_21_26.html',NULL,'/dls/i03/data/2016/cm14451-1/20160113_17_21_26.dat',12700,20,80,NULL,NULL,NULL,NULL,NULL,NULL),(1794,55167,NULL,'/dls/i03/data/2016/cm14451-1/20160113_17_24_57.png','2016-01-13 17:24:57','2016-01-13 17:25:11','/dls/i03/data/2016/cm14451-1/20160113_17_24_57.mca',1,NULL,1.59925,'/dls/i03/data/2016/cm14451-1/20160113_17_24_57.html',NULL,'/dls/i03/data/2016/cm14451-1/20160113_17_24_57.dat',12700,20,80,NULL,NULL,NULL,NULL,NULL,NULL),(1795,55167,NULL,'/dls/i03/data/2016/cm14451-1/20160113_17_25_21.png','2016-01-13 17:25:21','2016-01-13 17:25:32','/dls/i03/data/2016/cm14451-1/20160113_17_25_21.mca',1,NULL,1.59925,'/dls/i03/data/2016/cm14451-1/20160113_17_25_21.html',NULL,'/dls/i03/data/2016/cm14451-1/20160113_17_25_21.dat',12700,20,80,NULL,NULL,NULL,NULL,NULL,NULL),(1796,55167,NULL,'/dls/i03/data/2016/cm14451-1/20160113_17_25_48.png','2016-01-13 17:25:48','2016-01-13 17:26:00','/dls/i03/data/2016/cm14451-1/20160113_17_25_48.mca',1,NULL,1.59925,'/dls/i03/data/2016/cm14451-1/20160113_17_25_48.html',NULL,'/dls/i03/data/2016/cm14451-1/20160113_17_25_48.dat',12700,20,80,NULL,NULL,NULL,NULL,NULL,NULL),(1797,55167,NULL,'/dls/i03/data/2016/cm14451-1/20160113_17_26_44.png','2016-01-13 17:26:44','2016-01-13 17:26:57','/dls/i03/data/2016/cm14451-1/20160113_17_26_44.mca',1,NULL,1.59925,'/dls/i03/data/2016/cm14451-1/20160113_17_26_44.html',NULL,'/dls/i03/data/2016/cm14451-1/20160113_17_26_44.dat',12700,20,20,NULL,NULL,NULL,NULL,NULL,NULL),(1798,55167,NULL,'/dls/i03/data/2016/cm14451-1/20160113_17_27_19.png','2016-01-13 17:27:19','2016-01-13 17:27:32','/dls/i03/data/2016/cm14451-1/20160113_17_27_19.mca',1,NULL,1.59925,'/dls/i03/data/2016/cm14451-1/20160113_17_27_19.html',NULL,'/dls/i03/data/2016/cm14451-1/20160113_17_27_19.dat',12700,20,50,NULL,NULL,NULL,NULL,NULL,NULL),(1799,55167,NULL,'/dls/i03/data/2016/cm14451-1/20160113_17_28_10.png','2016-01-13 17:28:10','2016-01-13 17:28:22','/dls/i03/data/2016/cm14451-1/20160113_17_28_10.mca',1,NULL,1.59925,'/dls/i03/data/2016/cm14451-1/20160113_17_28_10.html',NULL,'/dls/i03/data/2016/cm14451-1/20160113_17_28_10.dat',12700,20,50,NULL,NULL,NULL,NULL,NULL,NULL),(1800,55167,NULL,'/dls/i03/data/2016/cm14451-1/20160113_17_29_49.png','2016-01-13 17:29:49','2016-01-13 17:30:01','/dls/i03/data/2016/cm14451-1/20160113_17_29_49.mca',1,NULL,1.59925,'/dls/i03/data/2016/cm14451-1/20160113_17_29_49.html',NULL,'/dls/i03/data/2016/cm14451-1/20160113_17_29_49.dat',12700,20,50,NULL,NULL,NULL,NULL,NULL,NULL),(1801,55167,374694,'/dls/i03/data/2016/cm14451-1/20160113_17_55_15.png','2016-01-13 17:55:15','2016-01-13 17:56:11','/dls/i03/data/2016/cm14451-1/20160113_17_55_15.mca',1,NULL,1.59925,'/dls/i03/data/2016/cm14451-1/20160113_17_55_15.html',NULL,'/dls/i03/data/2016/cm14451-1/20160113_17_55_15.dat',12700,20,50,NULL,NULL,NULL,NULL,NULL,NULL),(1802,55167,374694,'/dls/i03/data/2016/cm14451-1/20160113_17_57_11.png','2016-01-13 17:57:11','2016-01-13 17:57:22','/dls/i03/data/2016/cm14451-1/20160113_17_57_11.mca',1,NULL,1.59925,'/dls/i03/data/2016/cm14451-1/20160113_17_57_11.html',NULL,'/dls/i03/data/2016/cm14451-1/20160113_17_57_11.dat',12700,20,50,NULL,NULL,NULL,NULL,NULL,NULL),(1803,55167,374694,'/dls/i03/data/2016/cm14451-1/20160113_17_57_48.png','2016-01-13 17:57:48','2016-01-13 17:58:00','/dls/i03/data/2016/cm14451-1/20160113_17_57_48.mca',1,NULL,1.59925,'/dls/i03/data/2016/cm14451-1/20160113_17_57_48.html',NULL,'/dls/i03/data/2016/cm14451-1/20160113_17_57_48.dat',12700,20,50,NULL,NULL,NULL,NULL,NULL,NULL),(1804,55167,374694,'/dls/i03/data/2016/cm14451-1/20160113_17_58_55.png','2016-01-13 17:58:55','2016-01-13 17:59:08','/dls/i03/data/2016/cm14451-1/20160113_17_58_55.mca',1,NULL,1.59925,'/dls/i03/data/2016/cm14451-1/20160113_17_58_55.html',NULL,'/dls/i03/data/2016/cm14451-1/20160113_17_58_55.dat',12700,20,50,NULL,NULL,NULL,NULL,NULL,NULL),(1805,55167,374695,'/dls/i03/data/2016/cm14451-1/20160113_18_05_35.png','2016-01-13 18:05:35','2016-01-13 18:05:47','/dls/i03/data/2016/cm14451-1/20160113_18_05_35.mca',1,NULL,1.59925,'/dls/i03/data/2016/cm14451-1/20160113_18_05_35.html',NULL,'/dls/i03/data/2016/cm14451-1/20160113_18_05_35.dat',12700,20,50,NULL,NULL,NULL,NULL,NULL,NULL),(1806,55167,374695,'/dls/i03/data/2016/cm14451-1/20160113_18_06_50.png','2016-01-13 18:06:50','2016-01-13 18:07:02','/dls/i03/data/2016/cm14451-1/20160113_18_06_50.mca',1,NULL,1.59925,'/dls/i03/data/2016/cm14451-1/20160113_18_06_50.html',NULL,'/dls/i03/data/2016/cm14451-1/20160113_18_06_50.dat',12700,20,50,NULL,NULL,NULL,NULL,NULL,NULL),(1807,55167,374695,'/dls/i03/data/2016/cm14451-1/20160113_18_07_44.png','2016-01-13 18:07:44','2016-01-13 18:07:56','/dls/i03/data/2016/cm14451-1/20160113_18_07_44.mca',1,NULL,1.59925,'/dls/i03/data/2016/cm14451-1/20160113_18_07_44.html',NULL,'/dls/i03/data/2016/cm14451-1/20160113_18_07_44.dat',12700,20,50,NULL,NULL,NULL,NULL,NULL,NULL),(1808,55167,374695,'/dls/i03/data/2016/cm14451-1/20160113_18_08_38.png','2016-01-13 18:08:38','2016-01-13 18:08:50','/dls/i03/data/2016/cm14451-1/20160113_18_08_38.mca',1,NULL,1.59925,'/dls/i03/data/2016/cm14451-1/20160113_18_08_38.html',NULL,'/dls/i03/data/2016/cm14451-1/20160113_18_08_38.dat',12700,20,50,NULL,NULL,NULL,NULL,NULL,NULL),(1809,55167,374695,'/dls/i03/data/2016/cm14451-1/20160113_18_09_26.png','2016-01-13 18:09:26','2016-01-13 18:09:38','/dls/i03/data/2016/cm14451-1/20160113_18_09_26.mca',1,NULL,4.0011,'/dls/i03/data/2016/cm14451-1/20160113_18_09_26.html',NULL,'/dls/i03/data/2016/cm14451-1/20160113_18_09_26.dat',12700,20,50,NULL,NULL,NULL,NULL,NULL,NULL),(1810,55167,374695,'/dls/i03/data/2016/cm14451-1/20160113_18_10_25.png','2016-01-13 18:10:25','2016-01-13 18:10:38','/dls/i03/data/2016/cm14451-1/20160113_18_10_25.mca',1,NULL,4.0011,'/dls/i03/data/2016/cm14451-1/20160113_18_10_25.html',NULL,'/dls/i03/data/2016/cm14451-1/20160113_18_10_25.dat',12700,20,50,NULL,NULL,NULL,NULL,NULL,NULL),(1811,55167,374695,'/dls/i03/data/2016/cm14451-1/20160113_18_10_51.png','2016-01-13 18:10:51','2016-01-13 18:11:04','/dls/i03/data/2016/cm14451-1/20160113_18_10_51.mca',1,NULL,4.0011,'/dls/i03/data/2016/cm14451-1/20160113_18_10_51.html',NULL,'/dls/i03/data/2016/cm14451-1/20160113_18_10_51.dat',12700,20,50,NULL,NULL,NULL,NULL,NULL,NULL),(1812,55167,374695,'/dls/i03/data/2016/cm14451-1/20160113_18_11_20.png','2016-01-13 18:11:20','2016-01-13 18:11:32','/dls/i03/data/2016/cm14451-1/20160113_18_11_20.mca',1,NULL,4.0011,'/dls/i03/data/2016/cm14451-1/20160113_18_11_20.html',NULL,'/dls/i03/data/2016/cm14451-1/20160113_18_11_20.dat',12700,20,50,NULL,NULL,NULL,NULL,NULL,NULL),(1813,55167,374696,'/dls/i03/data/2016/cm14451-1/20160113_18_14_57.png','2016-01-13 18:14:57','2016-01-13 18:15:09','/dls/i03/data/2016/cm14451-1/20160113_18_14_57.mca',1,NULL,1.59925,'/dls/i03/data/2016/cm14451-1/20160113_18_14_57.html',NULL,'/dls/i03/data/2016/cm14451-1/20160113_18_14_57.dat',12700,20,50,NULL,NULL,NULL,NULL,NULL,NULL),(1814,55167,374696,'/dls/i03/data/2016/cm14451-1/20160113_18_15_50.png','2016-01-13 18:15:50','2016-01-13 18:16:02','/dls/i03/data/2016/cm14451-1/20160113_18_15_50.mca',1,NULL,1.59925,'/dls/i03/data/2016/cm14451-1/20160113_18_15_50.html',NULL,'/dls/i03/data/2016/cm14451-1/20160113_18_15_50.dat',12700,20,50,NULL,NULL,NULL,NULL,NULL,NULL),(1815,55167,374696,'/dls/i03/data/2016/cm14451-1/20160113_18_16_20.png','2016-01-13 18:16:20','2016-01-13 18:16:31','/dls/i03/data/2016/cm14451-1/20160113_18_16_20.mca',1,NULL,1.59925,'/dls/i03/data/2016/cm14451-1/20160113_18_16_20.html',NULL,'/dls/i03/data/2016/cm14451-1/20160113_18_16_20.dat',12700,20,50,NULL,NULL,NULL,NULL,NULL,NULL),(1816,55167,374696,'/dls/i03/data/2016/cm14451-1/20160113_18_16_56.png','2016-01-13 18:16:56','2016-01-13 18:17:08','/dls/i03/data/2016/cm14451-1/20160113_18_16_56.mca',1,NULL,1.59925,'/dls/i03/data/2016/cm14451-1/20160113_18_16_56.html',NULL,'/dls/i03/data/2016/cm14451-1/20160113_18_16_56.dat',12700,20,50,NULL,NULL,NULL,NULL,NULL,NULL),(1817,55167,374696,'/dls/i03/data/2016/cm14451-1/20160113_18_17_56.png','2016-01-13 18:17:56','2016-01-13 18:18:29','/dls/i03/data/2016/cm14451-1/20160113_18_17_56.mca',1,NULL,12.8,'/dls/i03/data/2016/cm14451-1/20160113_18_17_56.html',NULL,'/dls/i03/data/2016/cm14451-1/20160113_18_17_56.dat',12700,20,50,NULL,NULL,NULL,NULL,NULL,NULL),(1818,55167,374696,'/dls/i03/data/2016/cm14451-1/20160113_18_20_49.png','2016-01-13 18:20:49','2016-01-13 18:21:22','/dls/i03/data/2016/cm14451-1/20160113_18_20_49.mca',1,NULL,6.4,'/dls/i03/data/2016/cm14451-1/20160113_18_20_49.html',NULL,'/dls/i03/data/2016/cm14451-1/20160113_18_20_49.dat',12700,20,50,NULL,NULL,NULL,NULL,NULL,NULL),(1819,55167,374696,'/dls/i03/data/2016/cm14451-1/20160113_18_21_46.png','2016-01-13 18:21:46','2016-01-13 18:21:57','/dls/i03/data/2016/cm14451-1/20160113_18_21_46.mca',1,NULL,12.8138,'/dls/i03/data/2016/cm14451-1/20160113_18_21_46.html',NULL,'/dls/i03/data/2016/cm14451-1/20160113_18_21_46.dat',12700,20,50,NULL,NULL,NULL,NULL,NULL,NULL),(1820,55167,374696,'/dls/i03/data/2016/cm14451-1/20160113_18_22_33.png','2016-01-13 18:22:33','2016-01-13 18:22:45','/dls/i03/data/2016/cm14451-1/20160113_18_22_33.mca',1,NULL,12.8138,'/dls/i03/data/2016/cm14451-1/20160113_18_22_33.html',NULL,'/dls/i03/data/2016/cm14451-1/20160113_18_22_33.dat',12700,20,50,NULL,'good spectrum',NULL,NULL,NULL,NULL),(1821,55167,374696,'/dls/i03/data/2016/cm14451-1/20160113_18_23_52.png','2016-01-13 18:23:52','2016-01-13 18:24:05','/dls/i03/data/2016/cm14451-1/20160113_18_23_52.mca',1,NULL,12.8138,'/dls/i03/data/2016/cm14451-1/20160113_18_23_52.html',NULL,'/dls/i03/data/2016/cm14451-1/20160113_18_23_52.dat',12700,20,50,NULL,NULL,NULL,NULL,NULL,NULL),(1822,55167,374693,'/dls/i03/data/2016/cm14451-1/20160113_18_39_34.png','2016-01-13 18:39:34','2016-01-13 18:40:11','/dls/i03/data/2016/cm14451-1/20160113_18_39_34.mca',1,NULL,100,'/dls/i03/data/2016/cm14451-1/20160113_18_39_34.html',NULL,'/dls/i03/data/2016/cm14451-1/20160113_18_39_34.dat',12700,20,50,NULL,NULL,NULL,NULL,NULL,NULL),(1823,55167,374693,'/dls/i03/data/2016/cm14451-1/20160113_18_40_53.png','2016-01-13 18:40:53','2016-01-13 18:41:26','/dls/i03/data/2016/cm14451-1/20160113_18_40_53.mca',1,NULL,6.4,'/dls/i03/data/2016/cm14451-1/20160113_18_40_53.html',NULL,'/dls/i03/data/2016/cm14451-1/20160113_18_40_53.dat',12700,20,50,NULL,NULL,NULL,NULL,NULL,NULL),(1824,55167,374693,'/dls/i03/data/2016/cm14451-1/20160113_18_41_43.png','2016-01-13 18:41:43','2016-01-13 18:42:16','/dls/i03/data/2016/cm14451-1/20160113_18_41_43.mca',1,NULL,6.4,'/dls/i03/data/2016/cm14451-1/20160113_18_41_43.html',NULL,'/dls/i03/data/2016/cm14451-1/20160113_18_41_43.dat',12700,20,50,NULL,NULL,NULL,NULL,NULL,NULL),(1825,55167,374698,'/dls/i03/data/2016/cm14451-1/20160113_19_20_04.png','2016-01-13 19:20:04','2016-01-13 19:20:37','/dls/i03/data/2016/cm14451-1/20160113_19_20_04.mca',1,NULL,6.4,'/dls/i03/data/2016/cm14451-1/20160113_19_20_04.html',NULL,'/dls/i03/data/2016/cm14451-1/20160113_19_20_04.dat',12700,20,50,NULL,NULL,NULL,NULL,NULL,NULL),(1826,55167,374698,'/dls/i03/data/2016/cm14451-1/20160113_19_21_10.png','2016-01-13 19:21:10','2016-01-13 19:21:43','/dls/i03/data/2016/cm14451-1/20160113_19_21_10.mca',1,NULL,6.4,'/dls/i03/data/2016/cm14451-1/20160113_19_21_10.html',NULL,'/dls/i03/data/2016/cm14451-1/20160113_19_21_10.dat',12700,20,50,NULL,NULL,NULL,NULL,NULL,NULL),(1827,55167,374698,'/dls/i03/data/2016/cm14451-1/20160113_19_22_01.png','2016-01-13 19:22:01','2016-01-13 19:22:34','/dls/i03/data/2016/cm14451-1/20160113_19_22_01.mca',1,NULL,6.4,'/dls/i03/data/2016/cm14451-1/20160113_19_22_01.html',NULL,'/dls/i03/data/2016/cm14451-1/20160113_19_22_01.dat',12700,20,50,NULL,NULL,NULL,NULL,NULL,NULL),(1828,55167,374698,'/dls/i03/data/2016/cm14451-1/20160113_19_23_10.png','2016-01-13 19:23:10','2016-01-13 19:23:45','/dls/i03/data/2016/cm14451-1/20160113_19_23_10.mca',1,NULL,12.8,'/dls/i03/data/2016/cm14451-1/20160113_19_23_10.html',NULL,'/dls/i03/data/2016/cm14451-1/20160113_19_23_10.dat',12700,20,50,NULL,NULL,NULL,NULL,NULL,NULL),(1829,55167,NULL,'/dls/i03/data/2016/cm14451-1/20160113_19_49_01.png','2016-01-13 19:49:01','2016-01-13 19:50:38','/dls/i03/data/2016/cm14451-1/20160113_19_49_01.mca',1,NULL,12.8,'/dls/i03/data/2016/cm14451-1/20160113_19_49_01.html',NULL,'/dls/i03/data/2016/cm14451-1/20160113_19_49_01.dat',12700,20,50,NULL,NULL,NULL,NULL,NULL,NULL),(1830,55167,NULL,'/dls/i03/data/2016/cm14451-1/20160113_20_12_35.png','2016-01-13 20:12:35','2016-01-13 20:13:35','/dls/i03/data/2016/cm14451-1/20160113_20_12_35.mca',1,NULL,0.1,'/dls/i03/data/2016/cm14451-1/20160113_20_12_35.html',NULL,'/dls/i03/data/2016/cm14451-1/20160113_20_12_35.dat',14000,20,50,NULL,NULL,NULL,NULL,NULL,NULL),(1831,55167,NULL,'/dls/i03/data/2016/cm14451-1/20160113_20_17_07.png','2016-01-13 20:17:07','2016-01-13 20:19:49','/dls/i03/data/2016/cm14451-1/20160113_20_17_07.mca',1,NULL,3.2,'/dls/i03/data/2016/cm14451-1/20160113_20_17_07.html',NULL,'/dls/i03/data/2016/cm14451-1/20160113_20_17_07.dat',14000,20,50,NULL,NULL,NULL,NULL,NULL,NULL),(1832,55167,374695,'/dls/i03/data/2016/cm14451-1/20160114_11_16_25.png','2016-01-14 11:16:25','2016-01-14 11:17:32','/dls/i03/data/2016/cm14451-1/20160114_11_16_25.mca',1,NULL,1.6,'/dls/i03/data/2016/cm14451-1/20160114_11_16_25.html',NULL,'/dls/i03/data/2016/cm14451-1/20160114_11_16_25.dat',12673,20,50,NULL,NULL,NULL,NULL,NULL,NULL),(1833,55167,374695,'/dls/i03/data/2016/cm14451-1/20160114_11_20_14.png','2016-01-14 11:20:14','2016-01-14 11:20:46','/dls/i03/data/2016/cm14451-1/20160114_11_20_14.mca',1,NULL,6.4,'/dls/i03/data/2016/cm14451-1/20160114_11_20_14.html',NULL,'/dls/i03/data/2016/cm14451-1/20160114_11_20_14.dat',12673,20,50,NULL,NULL,NULL,NULL,NULL,NULL),(1834,55167,374695,'/dls/i03/data/2016/cm14451-1/20160114_11_23_23.png','2016-01-14 11:23:23','2016-01-14 11:23:56','/dls/i03/data/2016/cm14451-1/20160114_11_23_23.mca',1,NULL,6.4,'/dls/i03/data/2016/cm14451-1/20160114_11_23_23.html',NULL,'/dls/i03/data/2016/cm14451-1/20160114_11_23_23.dat',14000,20,50,NULL,'null _FLAG_',NULL,NULL,NULL,NULL),(1984,55168,398811,'/dls/i03/data/2016/cm14451-2/20160330_14_34_12.png','2016-03-30 14:34:12','2016-03-30 14:34:25','/dls/i03/data/2016/cm14451-2/20160330_14_34_12.mca',1,NULL,19.9988,'/dls/i03/data/2016/cm14451-2/20160330_14_34_12.html',NULL,'/dls/i03/data/2016/cm14451-2/20160330_14_34_12.dat',12700,20,80,NULL,NULL,NULL,NULL,NULL,NULL),(1987,55168,NULL,'/dls/i03/data/2016/cm14451-2/20160331_10_13_31.png','2016-03-31 10:13:31','2016-03-31 10:13:44','/dls/i03/data/2016/cm14451-2/20160331_10_13_31.mca',1,NULL,20.0048,'/dls/i03/data/2016/cm14451-2/20160331_10_13_31.html',NULL,'/dls/i03/data/2016/cm14451-2/20160331_10_13_31.dat',12700,20,80,NULL,NULL,NULL,NULL,NULL,NULL),(1990,55168,NULL,'/dls/i03/data/2016/cm14451-2/20160405_16_40_33.png','2016-04-05 16:40:33','2016-04-05 16:42:09','/dls/i03/data/2016/cm14451-2/20160405_16_40_33.mca',3,NULL,12.8,'/dls/i03/data/2016/cm14451-2/20160405_16_40_33.html',NULL,'/dls/i03/data/2016/cm14451-2/20160405_16_40_33.dat',14000,20,20,NULL,NULL,NULL,NULL,NULL,NULL),(2002,55168,409068,'/dls/i03/data/2016/cm14451-2/20160406_16_29_44.png','2016-04-06 16:29:44','2016-04-06 16:30:27','/dls/i03/data/2016/cm14451-2/20160406_16_29_44.mca',2,NULL,12.8,'/dls/i03/data/2016/cm14451-2/20160406_16_29_44.html',NULL,'/dls/i03/data/2016/cm14451-2/20160406_16_29_44.dat',12700,20,50,NULL,NULL,NULL,NULL,NULL,NULL),(2005,55168,2012,'/dls/i03/data/2009/in1246-1/jpegs/bs/bs_MS_1_001.jpeg',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `XFEFluorescenceSpectrum` ENABLE KEYS */;

--
-- Dumping data for table `XRFFluorescenceMapping`
--

/*!40000 ALTER TABLE `XRFFluorescenceMapping` DISABLE KEYS */;
/*!40000 ALTER TABLE `XRFFluorescenceMapping` ENABLE KEYS */;

--
-- Dumping data for table `XRFFluorescenceMappingROI`
--

/*!40000 ALTER TABLE `XRFFluorescenceMappingROI` DISABLE KEYS */;
/*!40000 ALTER TABLE `XRFFluorescenceMappingROI` ENABLE KEYS */;

--
-- Dumping data for table `XrayCentringResult`
--

/*!40000 ALTER TABLE `XrayCentringResult` DISABLE KEYS */;
/*!40000 ALTER TABLE `XrayCentringResult` ENABLE KEYS */;

--
-- Dumping data for table `v_run`
--

/*!40000 ALTER TABLE `v_run` DISABLE KEYS */;
INSERT INTO `v_run` (`runId`, `run`, `startDate`, `endDate`) VALUES (1,'2008-01','2007-12-17 09:00:00','2008-02-09 08:59:59'),(2,'2008-02','2008-02-09 09:00:00','2008-03-14 08:59:59'),(3,'2008-03','2008-03-14 09:00:00','2008-04-28 08:59:59'),(4,'2008-04','2008-04-28 09:00:00','2008-05-30 08:59:59'),(5,'2008-05','2008-05-30 09:00:00','2008-07-12 08:59:59'),(6,'2008-06','2008-07-12 09:00:00','2008-08-15 08:59:59'),(7,'2008-07','2008-08-15 09:00:00','2008-09-27 08:59:59'),(8,'2008-08','2008-09-27 09:00:00','2008-10-31 08:59:59'),(9,'2008-09','2008-10-31 09:00:00','2008-12-19 08:59:59'),(10,'2009-01','2008-12-19 09:00:00','2009-02-09 08:59:59'),(11,'2009-02','2009-02-09 09:00:00','2009-03-13 08:59:59'),(12,'2009-03','2009-03-13 09:00:00','2009-04-25 08:59:59'),(13,'2009-04','2009-04-25 09:00:00','2009-05-29 08:59:59'),(14,'2009-05','2009-05-29 09:00:00','2009-07-18 08:59:59'),(15,'2009-06','2009-07-18 09:00:00','2009-08-14 08:59:59'),(16,'2009-07','2009-08-14 09:00:00','2009-09-29 08:59:59'),(17,'2009-08','2009-09-29 09:00:00','2009-10-30 08:59:59'),(18,'2009-09','2009-10-30 09:00:00','2009-12-18 08:59:59'),(19,'2010-01','2009-12-18 09:00:00','2010-02-08 08:59:59'),(20,'2010-02','2010-02-08 09:00:00','2010-03-15 08:59:59'),(21,'2010-03','2010-03-15 09:00:00','2010-06-01 08:59:59'),(22,'2010-04','2010-06-01 09:00:00','2010-08-13 08:59:59'),(23,'2010-05','2010-08-13 09:00:00','2010-11-01 08:59:59'),(24,'2010-06','2010-11-01 09:00:00','2010-12-23 08:59:59'),(25,'2011-01','2010-12-23 09:00:00','2011-03-04 08:59:59'),(26,'2011-02','2011-03-04 09:00:00','2011-06-03 08:59:59'),(27,'2011-03','2011-06-03 09:00:00','2011-08-12 08:59:59'),(28,'2011-04','2011-08-12 09:00:00','2011-11-07 08:59:59'),(29,'2011-05','2011-11-07 09:00:00','2011-12-22 08:59:59'),(30,'2012-01','2011-12-22 09:00:00','2012-03-26 08:59:59'),(31,'2012-02','2012-03-26 09:00:00','2012-06-01 08:59:59'),(32,'2012-03','2012-06-01 09:00:00','2012-08-17 08:59:59'),(33,'2012-04','2012-08-17 09:00:00','2012-11-02 08:59:59'),(34,'2012-05','2012-11-02 09:00:00','2012-12-21 08:59:59'),(35,'2013-01','2012-12-21 09:00:00','2013-03-22 08:59:59'),(36,'2013-02','2013-03-22 09:00:00','2013-05-31 08:59:59'),(37,'2013-03','2013-05-31 09:00:00','2013-08-16 08:59:59'),(38,'2013-04','2013-08-16 09:00:00','2013-11-01 08:59:59'),(39,'2013-05','2013-11-01 09:00:00','2013-12-20 08:59:59'),(40,'2014-01','2013-12-20 09:00:00','2014-03-14 08:59:59'),(41,'2014-02','2014-03-14 09:00:00','2014-05-30 08:59:59'),(42,'2014-03','2014-05-30 09:00:00','2014-08-15 08:59:59'),(43,'2014-04','2014-08-15 09:00:00','2014-10-24 08:59:59'),(44,'2014-05','2014-10-24 09:00:00','2014-12-19 08:59:59'),(45,'2015-01','2014-12-19 09:00:00','2015-03-13 08:59:59'),(46,'2015-02','2015-03-13 09:00:00','2015-05-29 08:59:59'),(47,'2015-03','2015-05-29 09:00:00','2015-08-14 08:59:59'),(48,'2015-04','2015-08-14 09:00:00','2015-10-23 08:59:59'),(49,'2015-05','2015-10-23 09:00:00','2015-12-18 08:59:59'),(50,'2016-01','2015-12-18 09:00:00','2016-03-11 08:59:59'),(51,'2016-02','2016-03-11 09:00:00','2016-05-20 08:59:59'),(52,'2016-03','2016-05-20 09:00:00','2016-08-12 08:59:59'),(53,'2016-04','2016-08-12 09:00:00','2016-10-07 08:59:59'),(54,'2016-05','2016-10-07 09:00:00','2016-12-20 08:59:59'),(55,'2017-01','2016-12-20 09:00:00','2017-03-17 08:59:59'),(56,'2017-02','2017-03-17 09:00:00','2017-05-26 08:59:59'),(57,'2017-03','2017-05-26 09:00:00','2017-08-11 08:59:59'),(58,'2017-04','2017-08-11 09:00:00','2017-10-27 08:59:59'),(59,'2017-05','2017-10-27 09:00:00','2017-12-19 08:59:59'),(60,'2018-01','2017-12-19 09:00:00','2018-03-16 08:59:59'),(61,'2018-02','2018-03-16 09:00:00','2018-05-24 08:59:59'),(62,'2018-03','2018-05-24 09:00:00','2018-08-10 08:59:59'),(63,'2018-04','2018-08-10 09:00:00','2018-10-26 08:59:59'),(64,'2018-05','2018-10-26 09:00:00','2018-12-18 08:59:59'),(65,'2019-01','2018-12-18 09:00:00','2019-03-08 08:59:59'),(66,'2019-02','2019-03-08 09:00:00','2019-05-23 08:59:59'),(67,'2019-03','2019-05-23 09:00:00','2019-08-09 08:59:59'),(68,'2019-04','2019-08-09 09:00:00','2019-10-25 08:59:59'),(69,'2019-05','2019-10-25 09:00:00','2019-12-17 08:59:59'),(70,'2020-01','2019-12-17 09:00:00','2020-03-06 08:59:59'),(71,'2020-02','2020-03-06 09:00:00','2020-05-22 08:59:59'),(72,'2020-03','2020-05-22 09:00:00','2020-08-14 08:59:59');
/*!40000 ALTER TABLE `v_run` ENABLE KEYS */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-11-07 16:35:36

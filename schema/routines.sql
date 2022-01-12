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
-- Dumping routines for database 'ispyb_build'
--
/*!50003 DROP FUNCTION IF EXISTS `insert_scaling` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE FUNCTION `insert_scaling`(p_parentId integer,

     p_Type1 enum('overall','innerShell','outerShell'),
     p_Comments1 varchar(255), 
     p_ResolutionLimitLow1 float ,
     p_ResolutionLimitHigh1 float ,
     p_rMerge1 float ,
     p_rMeasWithinIPlusIMinus1 float ,
     p_rMeasAllIPlusIMinus1 float,
     p_rPimWithinIPlusIMinus1 float,
     p_rPimAllIPlusIMinus1 float,
     p_fractionalPartialBias1 float,
     p_nTotalObservations1 integer,
     p_nTotalUniqueObservations1 integer,
     p_meanIOverSigI1 float,
     p_completeness1 float,
     p_multiplicity1 float,
     p_anomalous1 boolean,
     p_anomalousCompleteness1 float,
     p_anomalousMultiplicity1 float,
     p_ccHalf1 float,
     p_ccAnomalous1 float,

     p_Type2 enum('overall','innerShell','outerShell'),
     p_Comments2 varchar(255), 
     p_ResolutionLimitLow2 float,
     p_ResolutionLimitHigh2 float,
     p_rMerge2 float,
     p_rMeasWithinIPlusIMinus2 float,
     p_rMeasAllIPlusIMinus2 float,
     p_rPimWithinIPlusIMinus2 float,
     p_rPimAllIPlusIMinus2 float,
     p_fractionalPartialBias2 float,
     p_nTotalObservations2 integer,
     p_nTotalUniqueObservations2 integer,
     p_meanIOverSigI2 float,
     p_completeness2 float,
     p_multiplicity2 float,
     p_anomalous2 boolean,
     p_anomalousCompleteness2 float,
     p_anomalousMultiplicity2 float,
     p_ccHalf2 float,
     p_ccAnomalous2 float,

     p_Type3 enum('overall','innerShell','outerShell'),
     p_Comments3 varchar(255), 
     p_ResolutionLimitLow3 float,
     p_ResolutionLimitHigh3 float,
     p_rMerge3 float,
     p_rMeasWithinIPlusIMinus3 float,
     p_rMeasAllIPlusIMinus3 float,
     p_rPimWithinIPlusIMinus3 float,
     p_rPimAllIPlusIMinus3 float,
     p_fractionalPartialBias3 float,
     p_nTotalObservations3 integer,
     p_nTotalUniqueObservations3 integer,
     p_meanIOverSigI3 float,
     p_completeness3 float,
     p_multiplicity3 float,
     p_anomalous3 boolean,
     p_anomalousCompleteness3 float,
     p_anomalousMultiplicity3 float,
     p_ccHalf3 float,
     p_ccAnomalous3 float
  ) RETURNS int(11)
    MODIFIES SQL DATA
BEGIN
	DECLARE apsId integer unsigned;

	INSERT INTO AutoProcScaling (autoProcId, recordTimeStamp)
      VALUES (p_parentId, now());
      
	SET apsId = LAST_INSERT_ID();

    INSERT INTO AutoProcScalingStatistics (autoProcScalingId, scalingStatisticsType, comments, resolutionLimitLow, resolutionLimitHigh, rMerge, 
      rMeasWithinIPlusIMinus, rMeasAllIPlusIMinus, rPimWithinIPlusIMinus, rPimAllIPlusIMinus, fractionalPartialBias, nTotalObservations, nTotalUniqueObservations, 
      meanIOverSigI, completeness, multiplicity, anomalous, anomalousCompleteness, anomalousMultiplicity, ccHalf, ccAnomalous, recordTimeStamp)
      VALUES (apsId, p_Type1, p_Comments1, p_ResolutionLimitLow1, p_ResolutionLimitHigh1, p_rMerge1, p_rMeasWithinIPlusIMinus1, p_rMeasAllIPlusIMinus1, 
        p_rPimWithinIPlusIMinus1, p_rPimAllIPlusIMinus1, p_fractionalPartialBias1, p_nTotalObservations1, p_nTotalUniqueObservations1, p_meanIOverSigI1, 
        p_completeness1, p_multiplicity1, p_anomalous1, p_anomalousCompleteness1, p_anomalousMultiplicity1, p_ccHalf1, p_ccAnomalous1, now());

    INSERT INTO AutoProcScalingStatistics (autoProcScalingId, scalingStatisticsType, comments, resolutionLimitLow, resolutionLimitHigh, rMerge, 
      rMeasWithinIPlusIMinus, rMeasAllIPlusIMinus, rPimWithinIPlusIMinus, rPimAllIPlusIMinus, fractionalPartialBias, nTotalObservations, nTotalUniqueObservations, 
      meanIOverSigI, completeness, multiplicity, anomalous, anomalousCompleteness, anomalousMultiplicity, ccHalf, ccAnomalous, recordTimeStamp)
      VALUES (apsId, p_Type2, p_Comments2, p_ResolutionLimitLow2, p_ResolutionLimitHigh2, p_rMerge2, p_rMeasWithinIPlusIMinus2, p_rMeasAllIPlusIMinus2, 
        p_rPimWithinIPlusIMinus2, p_rPimAllIPlusIMinus2, p_fractionalPartialBias2, p_nTotalObservations2, p_nTotalUniqueObservations2, p_meanIOverSigI2, 
        p_completeness2, p_multiplicity2, p_anomalous2, p_anomalousCompleteness2, p_anomalousMultiplicity2, p_ccHalf2, p_ccAnomalous2, now());

    INSERT INTO AutoProcScalingStatistics (autoProcScalingId, scalingStatisticsType, comments, resolutionLimitLow, resolutionLimitHigh, rMerge, 
      rMeasWithinIPlusIMinus, rMeasAllIPlusIMinus, rPimWithinIPlusIMinus, rPimAllIPlusIMinus, fractionalPartialBias, nTotalObservations, nTotalUniqueObservations, 
      meanIOverSigI, completeness, multiplicity, anomalous, anomalousCompleteness, anomalousMultiplicity, ccHalf, ccAnomalous, recordTimeStamp)
      VALUES (apsId, p_Type3, p_Comments3, p_ResolutionLimitLow3, p_ResolutionLimitHigh3, p_rMerge3, p_rMeasWithinIPlusIMinus3, p_rMeasAllIPlusIMinus3, 
        p_rPimWithinIPlusIMinus3, p_rPimAllIPlusIMinus3, p_fractionalPartialBias3, p_nTotalObservations3, p_nTotalUniqueObservations3, p_meanIOverSigI3, 
        p_completeness3, p_multiplicity3, p_anomalous3, p_anomalousCompleteness3, p_anomalousMultiplicity3, p_ccHalf3, p_ccAnomalous3, now());

    RETURN apsId;
  END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP FUNCTION IF EXISTS `retrieve_proposal_title` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE FUNCTION `retrieve_proposal_title`(p_proposal_code varchar(5), p_proposal_number int) RETURNS varchar(255) CHARSET latin1
    READS SQL DATA
BEGIN
	DECLARE ret_title varchar(255);
    SELECT title INTO ret_title
    FROM Proposal 
	WHERE proposalCode = p_proposal_code AND proposalNumber = p_proposal_number
    LIMIT 1;
	RETURN ret_title;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP FUNCTION IF EXISTS `retrieve_visit_id` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE FUNCTION `retrieve_visit_id`(p_visit varchar(15)) RETURNS int(11)
    READS SQL DATA
BEGIN
	DECLARE sessionid int(10);
    SELECT max(bs.sessionid) into sessionid 
    FROM Proposal p INNER JOIN BLSession bs ON p.proposalid = bs.proposalid 
    WHERE concat(p.proposalcode, p.proposalnumber, '-', bs.visit_number) = p_visit;
    RETURN sessionid;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP FUNCTION IF EXISTS `root_replace` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE FUNCTION `root_replace`(p_str varchar(255), p_oldroot varchar(255), p_newroot varchar(255)) RETURNS varchar(255) CHARSET latin1
    COMMENT 'Returns a varchar where the old root p_oldroot (the leftmost part) of p_str has been replaced with a new root p_newroot'
BEGIN
 DECLARE path_len smallint unsigned DEFAULT LENGTH(p_oldroot);
 RETURN CASE WHEN LEFT(p_str, path_len) = BINARY p_oldroot THEN CONCAT(p_newroot, SUBSTRING(p_str, path_len + 1)) ELSE p_str END; 
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP FUNCTION IF EXISTS `upsert_dc` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE FUNCTION `upsert_dc`(p_Id int(11) unsigned,
     p_parentId int(11) unsigned,
     p_visitId int(11) unsigned,
     p_sampleId int(11) unsigned, 
     p_detectorid int(11) unsigned, 
     p_positionid int(11) unsigned,
     p_apertureid int(11) unsigned, 
     p_datacollectionNumber int(10) unsigned,
     p_starttime datetime,
     p_endtime datetime,
     p_runStatus varchar(45),  
     p_axisStart float, 
     p_axisEnd float, 
     p_axisRange float, 
     p_overlap float, 
     p_numberOfImages int(10) unsigned, 
     p_startImageNumber int(10) unsigned, 
     p_numberOfPasses int(10) unsigned, 
     p_exposureTime float, 
     p_imageDirectory varchar(255), 
     p_imagePrefix varchar(45), 
     p_imageSuffix varchar(45), 
     p_fileTemplate varchar(255), 
     p_wavelength float, 
     p_resolution float, 
     p_detectorDistance float, 
     p_xbeam float, 
     p_ybeam float,
     p_comments varchar(1024),
     p_slitgapVertical float, 
     p_slitgapHorizontal float, 
     p_transmission float, 
     p_synchrotronMode varchar(20), 
     p_xtalSnapshotFullPath1 varchar(255), 
     p_xtalSnapshotFullPath2 varchar(255), 
     p_xtalSnapshotFullPath3 varchar(255),
     p_xtalSnapshotFullPath4 varchar(255),
     p_rotationAxis enum('Omega','Kappa','Phi'), 
     p_phistart float, 
     p_kappastart float, 
     p_omegastart float, 
     p_resolutionAtCorner float, 
     p_detector2theta float, 
     p_undulatorGap1 float, 
     p_undulatorGap2 float, 
     p_undulatorGap3 float, 
     p_beamSizeAtSampleX float, 
     p_beamSizeAtSampleY float, 
     p_averageTemperature float, 
     p_actualCenteringPosition varchar(255), 
     p_beamShape varchar(45), 
     p_focalSpotSizeAtSampleX float, 
     p_focalSpotSizeAtSampleY float, 
     p_polarisation float, 
     p_flux float, 

     p_processedDataFile varchar(255), 
     p_datFullPath varchar(255),
     p_magnification int(11),
     p_totalAbsorbedDose float,
     p_binning tinyint(1), 
     p_particleDiameter float, 
     p_boxSize_CTF float,
     p_minResolution float, 
     p_minDefocus float, 
     p_maxDefocus float, 
     p_defocusStepSize float, 
     p_amountAstigmatism float, 
     p_extractSize float, 
     p_bgRadius float, 
     p_voltage float,
     p_objAperture float,
     p_c1aperture float,
     p_c2aperture float,
     p_c3aperture float,
     p_c1lens float,
     p_c2lens float,
     p_c3lens float
) RETURNS int(11)
    MODIFIES SQL DATA
BEGIN
    INSERT INTO DataCollection (datacollectionId, datacollectiongroupid, sessionId, blsampleId, detectorid, positionid, apertureid, datacollectionNumber, starttime, endtime, 
        runStatus, axisStart, axisEnd, axisRange, overlap, numberOfImages, startImageNumber, numberOfPasses, exposureTime, imageDirectory, imagePrefix, imageSuffix, fileTemplate, 
        wavelength, resolution, detectorDistance, xbeam, ybeam, comments,slitgapVertical, slitgapHorizontal, transmission, synchrotronMode, 
        xtalSnapshotFullPath1, xtalSnapshotFullPath2, xtalSnapshotFullPath3, xtalSnapshotFullPath4, rotationAxis, phistart, kappastart, omegastart, resolutionAtCorner, detector2theta, 
        undulatorGap1, undulatorGap2, undulatorGap3, beamSizeAtSampleX, beamSizeAtSampleY, averageTemperature, actualCenteringPosition, beamShape, 
        focalSpotSizeAtSampleX, focalSpotSizeAtSampleY, polarisation, flux, 
        processedDataFile, datFullPath, magnification, totalAbsorbedDose, binning, particleDiameter, boxSize_CTF, minResolution, minDefocus, maxDefocus, defocusStepSize, 
        amountAstigmatism, extractSize, bgRadius, voltage, objAperture, c1aperture, c2aperture, c3aperture, c1lens, c2lens, c3lens
    ) 
      VALUES (p_Id, p_parentId, p_visitId, p_sampleId, p_detectorid, p_positionid, p_apertureid, p_datacollectionNumber, p_starttime, p_endtime, 
      p_runStatus, p_axisStart, p_axisEnd, p_axisRange, p_overlap, p_numberOfImages, p_startImageNumber, p_numberOfPasses, p_exposureTime, p_imageDirectory, p_imagePrefix, p_imageSuffix, p_fileTemplate, 
      p_wavelength, p_resolution, p_detectorDistance, p_xbeam, p_ybeam, p_comments, p_slitgapVertical, p_slitgapHorizontal, p_transmission, p_synchrotronMode, 
      p_xtalSnapshotFullPath1, p_xtalSnapshotFullPath2, p_xtalSnapshotFullPath3, p_xtalSnapshotFullPath4, p_rotationAxis, p_phistart, p_kappastart, p_omegastart, p_resolutionAtCorner, p_detector2theta, 
      p_undulatorGap1, p_undulatorGap2, p_undulatorGap3, p_beamSizeAtSampleX, p_beamSizeAtSampleY, p_averageTemperature, p_actualCenteringPosition, p_beamShape, 
      p_focalSpotSizeAtSampleX, p_focalSpotSizeAtSampleY, p_polarisation, p_flux, 
      p_processedDataFile, p_datFullPath, p_magnification, p_totalAbsorbedDose, p_binning, p_particleDiameter, p_boxSize_CTF, p_minResolution, p_minDefocus, p_maxDefocus, p_defocusStepSize, 
      p_amountAstigmatism, p_extractSize, p_bgRadius, p_voltage, p_objAperture, p_c1aperture, p_c2aperture, p_c3aperture, p_c1lens, p_c2lens, p_c3lens
      )
      ON DUPLICATE KEY UPDATE
		datacollectiongroupid = IFNULL(p_parentId, datacollectiongroupid),
        sessionId = IFNULL(p_visitId, sessionId),
        blsampleId = IFNULL(p_sampleId, blsampleId),
        detectorid = IFNULL(p_detectorid, detectorid),
        positionid = IFNULL(p_positionid, positionid),
        apertureid = IFNULL(p_apertureid, apertureid),
        datacollectionNumber = IFNULL(p_datacollectionNumber, datacollectionNumber),
        starttime = IFNULL(p_starttime, starttime),
        endtime = IFNULL(p_endtime, endtime),
        runStatus = IFNULL(p_runStatus, runStatus),
        axisStart = IFNULL(p_axisStart, axisStart),
        axisEnd = IFNULL(p_axisEnd, axisEnd),
        axisRange = IFNULL(p_axisRange, axisRange),
        overlap = IFNULL(p_overlap, overlap),
        numberOfImages = IFNULL(p_numberOfImages, numberOfImages),
        startImageNumber = IFNULL(p_startImageNumber, startImageNumber),
        numberOfPasses = IFNULL(p_numberOfPasses, numberOfPasses),
        exposureTime = IFNULL(p_exposureTime, exposureTime),
        imagedirectory = IFNULL(p_imageDirectory, imagedirectory),
        imageprefix = IFNULL(p_imagePrefix, imageprefix),
        imagesuffix = IFNULL(p_imageSuffix, imagesuffix),
        fileTemplate = IFNULL(p_fileTemplate, fileTemplate),
        wavelength = IFNULL(p_wavelength, wavelength),
        resolution = IFNULL(p_resolution, resolution),
        detectorDistance = IFNULL(p_detectorDistance, detectorDistance),
        xbeam = IFNULL(p_xbeam, xbeam),
        ybeam = IFNULL(p_ybeam, ybeam),
        comments = IFNULL(p_comments, comments),
        slitgapVertical = IFNULL(p_slitgapVertical, slitgapVertical),
        slitgapHorizontal = IFNULL(p_slitgapHorizontal, slitgapHorizontal),
        transmission = IFNULL(p_transmission, transmission),
        synchrotronMode = IFNULL(p_synchrotronMode, synchrotronMode),
        xtalSnapshotFullPath1 = IFNULL(p_xtalSnapshotFullPath1, xtalSnapshotFullPath1),
        xtalSnapshotFullPath2 = IFNULL(p_xtalSnapshotFullPath2, xtalSnapshotFullPath2),
        xtalSnapshotFullPath3 = IFNULL(p_xtalSnapshotFullPath3, xtalSnapshotFullPath3),
        xtalSnapshotFullPath4 = IFNULL(p_xtalSnapshotFullPath4, xtalSnapshotFullPath4),
        rotationAxis = IFNULL(p_rotationAxis, rotationAxis),
        phistart = IFNULL(p_phistart, phistart),
        kappastart = IFNULL(p_kappastart, kappastart),
        omegastart = IFNULL(p_omegastart, omegastart),
        resolutionAtCorner = IFNULL(p_resolutionAtCorner, resolutionAtCorner),
        detector2theta = IFNULL(p_detector2theta, detector2theta),
        undulatorGap1 = IFNULL(p_undulatorGap1, undulatorGap1),
        undulatorGap2 = IFNULL(p_undulatorGap2, undulatorGap2),
        undulatorGap3 = IFNULL(p_undulatorGap3, undulatorGap3),
        beamSizeAtSampleX = IFNULL(p_beamSizeAtSampleX, beamSizeAtSampleX),
        beamSizeAtSampleY = IFNULL(p_beamSizeAtSampleY, beamSizeAtSampleY),
        averageTemperature = IFNULL(p_averageTemperature, averageTemperature),
        actualCenteringPosition = IFNULL(p_actualCenteringPosition, actualCenteringPosition),
        beamShape = IFNULL(p_beamShape, beamShape),
        focalSpotSizeAtSampleX = IFNULL(p_focalSpotSizeAtSampleX, focalSpotSizeAtSampleX),
        focalSpotSizeAtSampleY = IFNULL(p_focalSpotSizeAtSampleY, focalSpotSizeAtSampleY),
        polarisation = IFNULL(p_polarisation, polarisation),
        flux = IFNULL(p_flux, flux),
        processedDataFile = IFNULL(p_processedDataFile, processedDataFile),
        datFullPath = IFNULL(p_datFullPath, datFullPath),
        magnification = IFNULL(p_magnification, magnification),
        totalAbsorbedDose = IFNULL(p_totalAbsorbedDose, totalAbsorbedDose),
        binning = IFNULL(p_binning, binning),
        particleDiameter = IFNULL(p_particleDiameter, particleDiameter),
        boxSize_CTF = IFNULL(p_boxSize_CTF, boxSize_CTF),
        minResolution = IFNULL(p_minResolution, minResolution),
        minDefocus = IFNULL(p_minDefocus, minDefocus),
        maxDefocus = IFNULL(p_maxDefocus, maxDefocus),
        defocusStepSize = IFNULL(p_defocusStepSize, defocusStepSize),
        amountAstigmatism = IFNULL(p_amountAstigmatism, amountAstigmatism),
        extractSize = IFNULL(p_extractSize, extractSize),
        bgRadius = IFNULL(p_bgRadius, bgRadius),
        voltage = IFNULL(p_voltage, voltage),
        objAperture = IFNULL(p_objAperture, objAperture),
        c1aperture = IFNULL(p_c1aperture, c1aperture),
        c2aperture = IFNULL(p_c2aperture, c2aperture),
        c3aperture = IFNULL(p_c3aperture, c3aperture),
        c1lens = IFNULL(p_c1lens, c1lens),
        c2lens = IFNULL(p_c2lens, c2lens),
        c3lens = IFNULL(p_c3lens, c3lens);

	IF p_id IS NULL THEN 
		RETURN LAST_INSERT_ID();
    ELSE 
		RETURN p_id;
    END IF;
  END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP FUNCTION IF EXISTS `upsert_dcgroup` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE FUNCTION `upsert_dcgroup`(p_id int(11) unsigned,
     p_parentId int(10) unsigned,
     p_sampleId int(10) unsigned, 
     p_experimenttype varchar(45), 
     p_starttime datetime,
     p_endtime datetime,
     p_crystalClass varchar(20),
     p_detectorMode varchar(255),
     p_actualSampleBarcode varchar(45),
     p_actualSampleSlotInContainer integer(10),
     p_actualContainerBarcode varchar(45),
     p_actualContainerSlotInSC integer(10),
     p_comments varchar(1024)
     ) RETURNS int(11)
    MODIFIES SQL DATA
BEGIN
    INSERT INTO DataCollectionGroup (datacollectionGroupId, sessionId, blsampleId, experimenttype, starttime, endtime, crystalClass, detectorMode, 
      actualSampleBarcode, actualSampleSlotInContainer, actualContainerBarcode, actualContainerSlotInSC, comments) 
      VALUES (p_id, p_parentId, p_sampleId, p_experimenttype, p_starttime, p_endtime, p_crystalClass, p_detectorMode, 
      p_actualSampleBarcode, p_actualSampleSlotInContainer, p_actualContainerBarcode, p_actualContainerSlotInSC, p_comments)
	  ON DUPLICATE KEY UPDATE
		sessionId = IFNULL(p_parentId, sessionId),
        blsampleId = IFNULL(p_sampleId, blsampleId),
        experimenttype = IFNULL(p_experimenttype, experimenttype),
        starttime = IFNULL(p_starttime, starttime),
        endtime = IFNULL(p_endtime, endtime),
        crystalClass = IFNULL(p_crystalClass, crystalClass),
        detectorMode = IFNULL(p_detectorMode, detectorMode),
        actualSampleBarcode = IFNULL(p_actualSampleBarcode, actualSampleBarcode),
        actualSampleSlotInContainer = IFNULL(p_actualSampleSlotInContainer, actualSampleSlotInContainer),
        actualContainerBarcode = IFNULL(p_actualContainerBarcode, actualContainerBarcode),
        actualContainerSlotInSC = IFNULL(p_actualContainerSlotInSC, actualContainerSlotInSC),
        comments = IFNULL(p_comments, comments);

	IF p_id IS NULL THEN 
		RETURN LAST_INSERT_ID();
    ELSE 
		RETURN p_id;
    END IF;
  END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP FUNCTION IF EXISTS `upsert_image` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE FUNCTION `upsert_image`(p_Id int(11) unsigned,
     p_parentId int(11) unsigned,
     p_imageNumber int(10) unsigned, 
     p_filename varchar(255),
     p_fileLocation varchar(255),
     p_measuredIntensity float,
     p_jpegFileFullPath varchar(255),
     p_jpegThumbnailFileFullPath varchar(255),
     p_temperature float,
     p_cumulativeIntensity float,
     p_synchrotronCurrent float,
     p_comments varchar(1024),
     p_machineMessage varchar(1024) 
) RETURNS int(11)
    MODIFIES SQL DATA
BEGIN
    INSERT INTO Image (imageId, datacollectionId, imageNumber, filename, fileLocation, measuredIntensity, jpegFileFullPath, jpegThumbnailFileFullPath, temperature, cumulativeIntensity, 
      synchrotronCurrent, comments, machineMessage)
      VALUES (p_Id, p_parentId, p_imageNumber, p_filename, p_fileLocation, p_measuredIntensity, p_jpegFileFullPath, p_jpegThumbnailFileFullPath, p_temperature, p_cumulativeIntensity, 
      p_synchrotronCurrent, p_comments, p_machineMessage)
	  ON DUPLICATE KEY UPDATE
		datacollectionId = IFNULL(p_parentId, datacollectionId),
        imageNumber = IFNULL(p_imageNumber, imageNumber), 
        filename = IFNULL(p_filename, filename), 
        fileLocation = IFNULL(p_fileLocation, fileLocation), 
        measuredIntensity = IFNULL(p_measuredIntensity, measuredIntensity), 
        jpegFileFullPath = IFNULL(p_jpegFileFullPath, jpegFileFullPath), 
        jpegThumbnailFileFullPath = IFNULL(p_jpegThumbnailFileFullPath, jpegThumbnailFileFullPath), 
        temperature = IFNULL(p_temperature, temperature), 
        cumulativeIntensity = IFNULL(p_cumulativeIntensity, cumulativeIntensity), 
        synchrotronCurrent = IFNULL(p_synchrotronCurrent, synchrotronCurrent), 
        comments = IFNULL(p_comments, comments), 
        machineMessage = IFNULL(p_machineMessage, machineMessage);

	IF p_id IS NULL THEN 
		RETURN LAST_INSERT_ID();
    ELSE 
		RETURN p_id;
    END IF;
  END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP FUNCTION IF EXISTS `upsert_integration` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE FUNCTION `upsert_integration`(p_id integer,
     p_parentId integer,
     p_datacollectionId integer,
     p_programRunId integer,
     p_startImageNumber integer,
     p_endImageNumber integer,
     p_refinedDetectorDistance float,
     p_refinedXBeam float,
     p_refinedYBeam float,
     p_rotationAxisX float,
     p_rotationAxisY float,
     p_rotationAxisZ float,
     p_beamVectorX float,
     p_beamVectorY float,
     p_beamVectorZ float,
     p_cell_a float,
     p_cell_b float,
     p_cell_c float,
     p_cell_alpha float,
     p_cell_beta float,
     p_cell_gamma float,
     p_anomalous float
  ) RETURNS int(11)
    MODIFIES SQL DATA
BEGIN
      DECLARE apiId integer unsigned DEFAULT NULL;

      INSERT INTO AutoProcIntegration (autoProcIntegrationId, datacollectionId, autoProcProgramId, startImageNumber, endImageNumber, 
        refinedDetectorDistance, refinedXBeam, refinedYBeam, rotationAxisX, rotationAxisY, rotationAxisZ, beamVectorX, beamVectorY, beamVectorZ, 
        cell_a, cell_b, cell_c, cell_alpha, cell_beta, cell_gamma, anomalous, recordTimeStamp)
        VALUES (p_id, p_datacollectionId, p_programRunId, p_startImageNumber, p_endImageNumber, 
			p_refinedDetectorDistance, p_refinedXBeam, p_refinedYBeam, p_rotationAxisX, p_rotationAxisY, p_rotationAxisZ, 
			p_beamVectorX, p_beamVectorY, p_beamVectorZ, p_cell_a, p_cell_b, p_cell_c, p_cell_alpha, p_cell_beta, p_cell_gamma, p_anomalous, now())
	    ON DUPLICATE KEY UPDATE
			datacollectionId = IFNULL(p_datacollectionId, datacollectionId), 
			autoProcProgramId = IFNULL(p_programRunId, autoProcProgramId), 
			startImageNumber = IFNULL(p_startImageNumber, startImageNumber), 
			endImageNumber = IFNULL(p_endImageNumber, endImageNumber), 
			refinedDetectorDistance = IFNULL(p_refinedDetectorDistance, refinedDetectorDistance), 
			refinedXBeam = IFNULL(p_refinedXBeam, refinedXBeam), 
			refinedYBeam = IFNULL(p_refinedYBeam, refinedYBeam), 
			rotationAxisX = IFNULL(p_rotationAxisX, rotationAxisX), 
			rotationAxisY = IFNULL(p_rotationAxisY, rotationAxisY),  
			rotationAxisZ = IFNULL(p_rotationAxisZ, rotationAxisZ), 
			beamVectorX = IFNULL(p_beamVectorX, beamVectorX), 
			beamVectorY = IFNULL(p_beamVectorY, beamVectorY), 
			beamVectorZ = IFNULL(p_beamVectorZ, beamVectorZ), 
			cell_a = IFNULL(p_cell_a, cell_a), 
			cell_b = IFNULL(p_cell_b, cell_b), 
			cell_c = IFNULL(p_cell_c, cell_c), 
			cell_alpha = IFNULL(p_cell_alpha, cell_alpha), 
			cell_beta = IFNULL(p_cell_beta, cell_beta), 
			cell_gamma = IFNULL(p_cell_gamma, cell_gamma), 
			anomalous = IFNULL(p_anomalous, anomalous);

	IF LAST_INSERT_ID() = 0 THEN 
		SET apiId = p_id;
    ELSE 
		SET apiId = LAST_INSERT_ID();
    END IF;
      
    
	IF p_id IS NULL THEN
		INSERT INTO AutoProcScaling_has_Int (autoProcScalingId, autoProcIntegrationId, recordTimeStamp)
			VALUES (p_parentId, apiId, now());
	ELSE 
		DELETE FROM AutoProcScaling_has_Int WHERE autoProcIntegrationId = p_id;
		INSERT INTO AutoProcScaling_has_Int (autoProcScalingId, autoProcIntegrationId, recordTimeStamp)
			VALUES (p_parentId, apiId, now());
	END IF;
  
	RETURN apiId;
  END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP FUNCTION IF EXISTS `upsert_mrrun` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE FUNCTION `upsert_mrrun`(p_id integer,
     p_parentId integer,
     p_success boolean,
     p_message varchar(255), 
     p_pipeline varchar(50),
     p_inputCoordFile varchar(255), 
     p_outputCoordFile varchar(255), 
     p_inputMTZFile varchar(255), 
     p_outputMTZFile varchar(255), 
     p_runDirectory varchar(255),
     p_logFile varchar(255),
     p_commandLine varchar(255),
     p_rValueStart float ,
     p_rValueEnd float ,
     p_rFreeValueStart float ,
     p_rFreeValueEnd float ,
     p_starttime datetime,
     p_endtime datetime
     ) RETURNS int(11)
    MODIFIES SQL DATA
BEGIN

    
    INSERT INTO MXMRRun (mxMRRunId, autoProcScalingId, success, message, pipeline, inputCoordFile, outputCoordFile, inputMTZFile, outputMTZFile, 
		runDirectory, logFile, commandLine, rValueStart, rValueEnd, rFreeValueStart, rFreeValueEnd, starttime, endtime) 
      VALUES (
        p_id, 
        p_parentId, 
        p_success, 
        p_message, 
        p_pipeline, 
        p_inputCoordFile, 
        p_outputCoordFile, 
        p_inputMTZFile, 
        p_outputMTZFile, 
        p_runDirectory,
        p_logFile,
        p_commandLine,
        p_rValueStart, 
        p_rValueEnd, 
        p_rFreeValueStart, 
        p_rFreeValueEnd, 
        p_starttime, 
        p_endtime)
		ON DUPLICATE KEY UPDATE
			autoProcScalingId = IFNULL(p_parentId, autoProcScalingId), 
            success = IFNULL(p_success, success), 
            message = IFNULL(p_message, message), 
            pipeline = IFNULL(p_pipeline, pipeline), 
            inputCoordFile = IFNULL(p_inputCoordFile, inputCoordFile), 
            outputCoordFile = IFNULL(p_outputCoordFile, outputCoordFile), 
            inputMTZFile = IFNULL(p_inputMTZFile, inputMTZFile), 
            outputMTZFile = IFNULL(p_outputMTZFile, outputMTZFile), 
            runDirectory = IFNULL(p_runDirectory, runDirectory), 
            logFile = IFNULL(p_logFile, logFile), 
            commandLine = IFNULL(p_commandLine, commandLine), 
            rValueStart = IFNULL(p_rValueStart, rValueStart), 
            rValueEnd = IFNULL(p_rValueEnd, rValueEnd), 
            rFreeValueStart = IFNULL(p_rFreeValueStart, rFreeValueStart), 
            rFreeValueEnd = IFNULL(p_rFreeValueEnd, rFreeValueEnd), 
            starttime = IFNULL(p_starttime, starttime), 
            endtime = IFNULL(p_endtime, endtime);
 
	IF p_id IS NULL THEN 
		RETURN LAST_INSERT_ID();
    ELSE 
		RETURN p_id;
    END IF;
  END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP FUNCTION IF EXISTS `upsert_mrrun_blob` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE FUNCTION `upsert_mrrun_blob`(p_Id integer,
     p_parentId integer,
     p_view1 varchar(255), 
     p_view2 varchar(255), 
     p_view3 varchar(255) 
  ) RETURNS int(11)
BEGIN
    INSERT INTO MXMRRunBlob (mxMRRunBlobId, mxMRRunId, view1, view2, view3) 
		VALUES (p_id, p_parentId, p_view1, p_view2, p_view3)
		ON DUPLICATE KEY UPDATE
			mxMRRunId = IFNULL(p_parentId, mxMRRunId),
			view1 = IFNULL(p_view1, view1),
			view2 = IFNULL(p_view2, view2),
			view3 = IFNULL(p_view3, view3);

	IF p_id IS NULL THEN 
		RETURN LAST_INSERT_ID();
    ELSE 
		RETURN p_id;
    END IF;
  END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP FUNCTION IF EXISTS `upsert_processing` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE FUNCTION `upsert_processing`(p_id int(10),
     p_parentId int(10),
     p_spacegroup varchar(45), 
     p_refinedcell_a float, 
     p_refinedcell_b float, 
     p_refinedcell_c float, 
     p_refinedcell_alpha float, 
     p_refinedcell_beta float, 
     p_refinedcell_gamma float 
  ) RETURNS int(11)
    MODIFIES SQL DATA
BEGIN
    INSERT INTO AutoProc (autoProcId, autoProcProgramId, spacegroup, refinedcell_a, refinedcell_b, refinedcell_c, refinedcell_alpha, refinedcell_beta, refinedcell_gamma, recordtimestamp) 
      VALUES (p_id, p_parentId, p_spacegroup, p_refinedcell_a, p_refinedcell_b, p_refinedcell_c, p_refinedcell_alpha, p_refinedcell_beta, p_refinedcell_gamma, now())
	  ON DUPLICATE KEY UPDATE
		autoProcProgramId = IFNULL(p_parentId, autoProcProgramId), 
		spacegroup = IFNULL(p_spacegroup, spacegroup), 
        refinedcell_a = IFNULL(p_refinedcell_a, refinedcell_a), 
        refinedcell_b = IFNULL(p_refinedcell_b, refinedcell_b), 
        refinedcell_c = IFNULL(p_refinedcell_c, refinedcell_c), 
        refinedcell_alpha = IFNULL(p_refinedcell_alpha, refinedcell_alpha),
		refinedcell_beta = IFNULL(p_refinedcell_beta, refinedcell_beta),
        refinedcell_gamma = IFNULL(p_refinedcell_gamma, refinedcell_gamma);

	IF LAST_INSERT_ID() = 0 THEN 
		RETURN p_id;
    ELSE 
		RETURN LAST_INSERT_ID();
    END IF;
  END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP FUNCTION IF EXISTS `upsert_program_run` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE FUNCTION `upsert_program_run`(p_Id int(10) unsigned,
     p_cmd_line varchar(255),
     p_programs varchar(255),
     p_status tinyint(1) ,
     p_message varchar(255),
     p_starttime datetime,
     p_endtime datetime,
     p_environment varchar(255),

     p_file1_id int(10) unsigned,
     p_filename1 varchar(255),
     p_filepath1 varchar(255),
     p_filetype1 enum('Log','Result','Graph'),
     p_file2_id int(10) unsigned,
     p_filename2 varchar(255),
     p_filepath2 varchar(255),
     p_filetype2 enum('Log','Result','Graph'),
     p_file3_id int(10) unsigned,
     p_filename3 varchar(255),
     p_filepath3 varchar(255),
     p_filetype3 enum('Log','Result','Graph')
  ) RETURNS int(11)
    MODIFIES SQL DATA
BEGIN
    DECLARE appid int(10) DEFAULT NULL;
    INSERT INTO AutoProcProgram (autoProcProgramId, processingCommandLine, processingPrograms, processingStatus, processingMessage, processingStartTime, processingEndTime, processingEnvironment, recordtimestamp)
		VALUES (p_Id, substr(p_cmd_line, 1, 255), p_programs, p_status, p_message, p_starttime, p_endtime, p_environment, now())
		ON DUPLICATE KEY UPDATE
      processingCommandLine = IFNULL(p_cmd_line, processingCommandLine),
      processingPrograms = IFNULL(p_programs, processingPrograms),
      processingStatus = IFNULL(p_status, processingStatus),
      processingMessage = IFNULL(p_message, processingMessage),
      processingStartTime = IFNULL(p_starttime, processingStarttime),
      processingEndTime = IFNULL(p_endtime, processingEndtime),
      processingEnvironment = IFNULL(p_environment, processingEnvironment);

	IF LAST_INSERT_ID() = 0 THEN 
		SET appid = p_id;
    ELSE 
		SET appid = LAST_INSERT_ID();
    END IF;
        
	IF p_filename1 IS NOT NULL THEN
        INSERT INTO AutoProcProgramAttachment (autoProcProgramAttachmentId,autoProcProgramId, filename, filepath, filetype, recordtimestamp)
          VALUES (p_file1_id, appid, p_filename1, p_filepath1, p_filetype1, now())
          ON DUPLICATE KEY UPDATE
		autoProcProgramId = IFNULL(appid, autoProcProgramId),
        filename = IFNULL(p_filename1, filename),
        filepath = IFNULL(p_filepath1, filepath),
        filetype = IFNULL(p_filetype1, filetype);
    END IF;
    IF p_filename2 IS NOT NULL THEN
        INSERT INTO AutoProcProgramAttachment (autoProcProgramAttachmentId, autoProcProgramId, filename, filepath, filetype, recordtimestamp)
          VALUES (p_file2_id, appid, p_filename2, p_filepath2, p_filetype2, now())
          ON DUPLICATE KEY UPDATE
		autoProcProgramId = IFNULL(appid, autoProcProgramId),
        filename = IFNULL(p_filename2, filename),
        filepath = IFNULL(p_filepath2, filepath),
        filetype = IFNULL(p_filetype2, filetype);
    END IF;
    IF p_filename3 IS NOT NULL THEN
        INSERT INTO AutoProcProgramAttachment (autoProcProgramAttachmentId, autoProcProgramId, filename, filepath, filetype, recordtimestamp)
          VALUES (p_file2_id, appid, p_filename3, p_filepath3, p_filetype3, now())
          ON DUPLICATE KEY UPDATE
		autoProcProgramId = IFNULL(appid, autoProcProgramId),
        filename = IFNULL(p_filename3, filename),
        filepath = IFNULL(p_filepath3, filepath),
        filetype = IFNULL(p_filetype3, filetype);
    END IF;

	RETURN appid;
  END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP FUNCTION IF EXISTS `upsert_sample` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE FUNCTION `upsert_sample`(p_id int(10) unsigned,
	 p_crystalId int(10) unsigned,
     p_containerId int(10) unsigned, 
     p_name varchar(45),
     p_code varchar(45),
     p_location varchar(45),
     p_holderLength float, 
     p_loopLength float, 
     p_loopType varchar(45), 
     p_wireWidth float, 
     p_comments varchar(1024),
     p_blSampleStatus varchar(20),
     p_isInSampleChanger boolean 
) RETURNS int(11)
    MODIFIES SQL DATA
BEGIN
	INSERT INTO BLSample (blsampleId, crystalId, containerId, `name`, code, `location`, holderLength, loopLength, loopType, wireWidth, comments, blSampleStatus, isInSampleChanger)
      VALUES (p_id, p_crystalId, p_containerId, p_name, p_code, p_location, p_holderLength, p_loopLength, p_loopType, p_wireWidth, p_comments, p_blSampleStatus, p_isInSampleChanger)
      ON DUPLICATE KEY UPDATE
		crystalId = IFNULL(p_crystalId, crystalId),
        containerId = IFNULL(p_containerId, containerId), 
        `name` = IFNULL(p_name, `name`), 
        `code` = IFNULL(p_code, `code`), 
        location = IFNULL(p_location, location), 
        holderLength = IFNULL(p_holderLength, holderLength), 
        loopLength = IFNULL(p_loopLength, loopLength), 
        wireWidth = IFNULL(p_wireWidth, wireWidth), 
        comments = IFNULL(p_comments, comments), 
        blSampleStatus = IFNULL(p_blSampleStatus, blSampleStatus), 
        isInSampleChanger = IFNULL(p_isInSampleChanger, isInSampleChanger);

	IF p_id IS NULL THEN 
		RETURN LAST_INSERT_ID();
    ELSE 
		RETURN p_id;
    END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `clear_container_error` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `clear_container_error`(IN p_barcode varchar(10))
    MODIFIES SQL DATA
    COMMENT 'Sets error for p_barcode in automation fault table to resolved s'
BEGIN
  IF NOT (p_barcode IS NULL) THEN
	UPDATE BF_automationFault af 
      INNER JOIN Container c ON af.containerId = c.containerId
    SET af.resolved = 1
    WHERE c.barcode = p_barcode;
    ELSE 
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument p_barcode is NULL';
  END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `finish_container` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `finish_container`(IN p_barcode varchar(45))
    MODIFIES SQL DATA
    COMMENT 'Set the completedTimeStamp in the ContainerQueue table for the c'
BEGIN
  IF NOT (p_barcode IS NULL) THEN
    UPDATE ContainerQueue 
    SET completedTimeStamp = current_timestamp 
    WHERE completedTimeStamp is NULL and containerId in (SELECT containerId FROM Container WHERE barcode = p_barcode);
    ELSE
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument p_barcode is NULL';
  END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `insert_beamline_action` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `insert_beamline_action`(
     OUT p_id int(11) unsigned,
     p_proposalCode varchar(3),
     p_proposalNumber int(10),
     p_sessionNumber int(10),
     p_startTime timestamp,
     p_endTime timestamp,
     p_message varchar(255),
     p_parameter varchar(50),
     p_value varchar(50),
     p_logLevel enum('DEBUG','CRITICAL','INFO'),
     p_status enum('PAUSED','RUNNING','TERMINATED','COMPLETE','ERROR','EPICSFAIL')
)
    MODIFIES SQL DATA
    COMMENT 'Insert a beamline action row for session p_proposalCode + p_prop'
BEGIN
	DECLARE row_session_id int(10) unsigned DEFAULT NULL;
	DECLARE row_proposal_id int(10) unsigned DEFAULT NULL;
  
	IF p_proposalCode IS NOT NULL AND p_proposalNumber IS NOT NULL AND p_sessionNumber IS NOT NULL THEN
      SELECT max(bs.sessionid), p.proposalId INTO row_session_id, row_proposal_id 
      FROM Proposal p INNER JOIN BLSession bs ON p.proposalid = bs.proposalid 
      WHERE p.proposalCode = p_proposalCode AND p.proposalNumber = p_proposalNumber AND bs.visit_number = p_sessionNumber;

      INSERT INTO BeamlineAction (sessionId, startTimestamp, endTimestamp, message, parameter, `value`, loglevel, `status`) 
          VALUES (row_session_id, p_startTime, p_endTime, p_message, p_parameter, p_value, p_logLevel, p_status);

	  IF p_id IS NULL THEN 
		  SET p_id = LAST_INSERT_ID();
      END IF;      
    ELSE
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='One or more mandatory arguments are NULL: p_proposalCode, p_proposalNumber, p_sessionNumber';
    END IF;
  END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `insert_container_error` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `insert_container_error`(IN p_barcode varchar(45), p_error varchar(255), p_severity int, p_stack_trace text)
    MODIFIES SQL DATA
    COMMENT 'Inserts row with info about container loading-related error into'
BEGIN
  IF NOT (p_barcode IS NULL) THEN
    INSERT INTO BF_automationFault (automationErrorId, containerId, severity, stacktrace) 
      VALUES ((SELECT automationErrorId FROM BF_automationError WHERE errorType = p_error), (SELECT containerId FROM Container WHERE barcode = p_barcode), p_severity, p_stack_trace);
    ELSE 
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument p_barcode is NULL';
  END IF;

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `insert_container_inspections` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `insert_container_inspections`(p_containerId int(11) unsigned, p_scheduleName varchar(10))
    MODIFIES SQL DATA
    COMMENT 'Inserts records into ContainerInspection'
BEGIN
	DECLARE finished boolean DEFAULT 0;
	DECLARE datetime_now datetime DEFAULT current_timestamp();
    DECLARE v_scheduleComponentId INT UNSIGNED;
    DECLARE v_offset_hours INT UNSIGNED;
    DECLARE v_inspectionTypeId INT UNSIGNED;
	DECLARE priority_count INT DEFAULT 1;
    DECLARE schedule_component_cursor CURSOR FOR
		SELECT sc.scheduleComponentId, sc.offset_hours, sc.inspectionTypeId 
        FROM ScheduleComponent sc
          INNER JOIN `Schedule` s USING (scheduleId) 
        WHERE s.name = p_scheduleName 
        ORDER BY sc.offset_hours ASC;

	DECLARE CONTINUE HANDLER 
    FOR NOT FOUND SET finished = 1;

	OPEN schedule_component_cursor;

    WHILE finished <> 1 DO

		FETCH schedule_component_cursor INTO v_scheduleComponentId, v_offset_hours, v_inspectionTypeId;  
        
		INSERT INTO ContainerInspection (containerId, inspectionTypeId, scheduleComponentid, state, scheduledTimeStamp, manual, priority) 
			VALUES (p_containerId, v_inspectionTypeId, v_scheduleComponentId, 'Not completed', datetime_now + INTERVAL v_offset_hours HOUR, 0, priority_count);

		SET priority_count = priority_count + 1;

    END WHILE;

	CLOSE schedule_component_cursor;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `insert_processing_scaling` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `insert_processing_scaling`(
     OUT p_id integer unsigned,
     p_parentId integer unsigned,

     p_Type1 enum('overall','innerShell','outerShell'),
     p_Comments1 varchar(255), 
     p_ResolutionLimitLow1 float ,
     p_ResolutionLimitHigh1 float ,
     p_rMerge1 float ,
     p_rMeasWithinIPlusIMinus1 float ,
     p_rMeasAllIPlusIMinus1 float,
     p_rPimWithinIPlusIMinus1 float,
     p_rPimAllIPlusIMinus1 float,
     p_fractionalPartialBias1 float,
     p_nTotalObservations1 integer,
     p_nTotalUniqueObservations1 integer,
     p_meanIOverSigI1 float,
     p_completeness1 float,
     p_multiplicity1 float,
     p_anomalous1 boolean,
     p_anomalousCompleteness1 float,
     p_anomalousMultiplicity1 float,
     p_ccHalf1 float,
     p_ccAnomalous1 float,

     p_Type2 enum('overall','innerShell','outerShell'),
     p_Comments2 varchar(255), 
     p_ResolutionLimitLow2 float,
     p_ResolutionLimitHigh2 float,
     p_rMerge2 float,
     p_rMeasWithinIPlusIMinus2 float,
     p_rMeasAllIPlusIMinus2 float,
     p_rPimWithinIPlusIMinus2 float,
     p_rPimAllIPlusIMinus2 float,
     p_fractionalPartialBias2 float,
     p_nTotalObservations2 integer,
     p_nTotalUniqueObservations2 integer,
     p_meanIOverSigI2 float,
     p_completeness2 float,
     p_multiplicity2 float,
     p_anomalous2 boolean,
     p_anomalousCompleteness2 float,
     p_anomalousMultiplicity2 float,
     p_ccHalf2 float,
     p_ccAnomalous2 float,

     p_Type3 enum('overall','innerShell','outerShell'),
     p_Comments3 varchar(255), 
     p_ResolutionLimitLow3 float,
     p_ResolutionLimitHigh3 float,
     p_rMerge3 float,
     p_rMeasWithinIPlusIMinus3 float,
     p_rMeasAllIPlusIMinus3 float,
     p_rPimWithinIPlusIMinus3 float,
     p_rPimAllIPlusIMinus3 float,
     p_fractionalPartialBias3 float,
     p_nTotalObservations3 integer,
     p_nTotalUniqueObservations3 integer,
     p_meanIOverSigI3 float,
     p_completeness3 float,
     p_multiplicity3 float,
     p_anomalous3 boolean,
     p_anomalousCompleteness3 float,
     p_anomalousMultiplicity3 float,
     p_ccHalf3 float,
     p_ccAnomalous3 float
  )
    MODIFIES SQL DATA
    COMMENT 'Inserts 1 row in AutoProcScaling, 3 rows in AutoProcScalingStati'
BEGIN
    IF p_parentid IS NULL THEN
      SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument p_program_id is NULL';
	ELSE
    
	  START TRANSACTION;
	  INSERT INTO AutoProcScaling (autoProcId, recordTimeStamp)
        VALUES (p_parentId, now());
      
	  SET p_id = LAST_INSERT_ID();

      INSERT INTO AutoProcScalingStatistics (autoProcScalingId, scalingStatisticsType, comments, resolutionLimitLow, resolutionLimitHigh, rMerge, 
        rMeasWithinIPlusIMinus, rMeasAllIPlusIMinus, rPimWithinIPlusIMinus, rPimAllIPlusIMinus, fractionalPartialBias, nTotalObservations, nTotalUniqueObservations, 
        meanIOverSigI, completeness, multiplicity, anomalous, anomalousCompleteness, anomalousMultiplicity, ccHalf, ccAnomalous, recordTimeStamp)
        VALUES (p_id, p_Type1, p_Comments1, p_ResolutionLimitLow1, p_ResolutionLimitHigh1, p_rMerge1, p_rMeasWithinIPlusIMinus1, p_rMeasAllIPlusIMinus1, 
          p_rPimWithinIPlusIMinus1, p_rPimAllIPlusIMinus1, p_fractionalPartialBias1, p_nTotalObservations1, p_nTotalUniqueObservations1, p_meanIOverSigI1, 
          p_completeness1, p_multiplicity1, p_anomalous1, p_anomalousCompleteness1, p_anomalousMultiplicity1, p_ccHalf1, p_ccAnomalous1, now());

      INSERT INTO AutoProcScalingStatistics (autoProcScalingId, scalingStatisticsType, comments, resolutionLimitLow, resolutionLimitHigh, rMerge, 
        rMeasWithinIPlusIMinus, rMeasAllIPlusIMinus, rPimWithinIPlusIMinus, rPimAllIPlusIMinus, fractionalPartialBias, nTotalObservations, nTotalUniqueObservations, 
        meanIOverSigI, completeness, multiplicity, anomalous, anomalousCompleteness, anomalousMultiplicity, ccHalf, ccAnomalous, recordTimeStamp)
        VALUES (p_id, p_Type2, p_Comments2, p_ResolutionLimitLow2, p_ResolutionLimitHigh2, p_rMerge2, p_rMeasWithinIPlusIMinus2, p_rMeasAllIPlusIMinus2, 
          p_rPimWithinIPlusIMinus2, p_rPimAllIPlusIMinus2, p_fractionalPartialBias2, p_nTotalObservations2, p_nTotalUniqueObservations2, p_meanIOverSigI2, 
          p_completeness2, p_multiplicity2, p_anomalous2, p_anomalousCompleteness2, p_anomalousMultiplicity2, p_ccHalf2, p_ccAnomalous2, now());

      INSERT INTO AutoProcScalingStatistics (autoProcScalingId, scalingStatisticsType, comments, resolutionLimitLow, resolutionLimitHigh, rMerge, 
        rMeasWithinIPlusIMinus, rMeasAllIPlusIMinus, rPimWithinIPlusIMinus, rPimAllIPlusIMinus, fractionalPartialBias, nTotalObservations, nTotalUniqueObservations, 
        meanIOverSigI, completeness, multiplicity, anomalous, anomalousCompleteness, anomalousMultiplicity, ccHalf, ccAnomalous, recordTimeStamp)
        VALUES (p_id, p_Type3, p_Comments3, p_ResolutionLimitLow3, p_ResolutionLimitHigh3, p_rMerge3, p_rMeasWithinIPlusIMinus3, p_rMeasAllIPlusIMinus3, 
          p_rPimWithinIPlusIMinus3, p_rPimAllIPlusIMinus3, p_fractionalPartialBias3, p_nTotalObservations3, p_nTotalUniqueObservations3, p_meanIOverSigI3, 
          p_completeness3, p_multiplicity3, p_anomalous3, p_anomalousCompleteness3, p_anomalousMultiplicity3, p_ccHalf3, p_ccAnomalous3, now());
	  COMMIT;

    END IF; 
  END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `insert_quality_indicators` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `insert_quality_indicators`(
  OUT p_id int(11) unsigned,
  p_dataCollectionId int(11) unsigned, 
  p_autoProcProgramId int(10) unsigned, 
  p_imageNumber mediumint(8) unsigned,
  p_spotTotal int(10),
  p_inResTotal int(10),
  p_goodBraggCandidates int(10),
  p_iceRings int(10),
  p_method1Res float,
  p_method2Res float,
  p_maxUnitCell float,
  p_pctSaturationTop50Peaks float,
  p_inResolutionOvrlSpots int(10),
  p_binPopCutOffMethod2Res float,
  p_totalIntegratedSignal double,
  p_driftFactor float
)
    MODIFIES SQL DATA
    COMMENT 'Inserts a row into the image quality indicators table'
BEGIN

  IF p_dataCollectionId IS NOT NULL AND p_imageNumber IS NOT NULL THEN
    INSERT INTO ImageQualityIndicators (
      dataCollectionId, autoProcProgramId, imageNumber, spotTotal, inResTotal, goodBraggCandidates, iceRings, 
	  method1Res, method2Res, maxUnitCell, pctSaturationTop50Peaks,
	  inResolutionOvrlSpots, binPopCutOffMethod2Res, totalIntegratedSignal, driftFactor) 
      VALUES (
        p_dataCollectionId, p_autoProcProgramId, p_imageNumber, p_spotTotal, p_inResTotal, p_goodBraggCandidates, p_iceRings,
        p_method1Res, p_method2Res, p_maxUnitCell, p_pctSaturationTop50Peaks, 
        p_inResolutionOvrlSpots, p_binPopCutOffMethod2Res, p_totalIntegratedSignal, p_driftFactor
      );
	SET p_id = 1; 
  ELSE
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument(s) p_dataCollectionId and/or p_imageNumber are NULL';  
  END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `insert_sample_image_auto_score` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE PROCEDURE `insert_sample_image_auto_score`(
     OUT p_id int(11) unsigned,
     p_imageFullPath varchar(255),
     p_schemaName varchar(25),
     p_scoreClass varchar(15),
     p_probability float
)
    MODIFIES SQL DATA
    COMMENT 'Insert a row with the auto scored probability for a given sample image using a certain class and schema. Returns the ID in p_id.'
BEGIN
    DECLARE l_blSampleImageId int(11) unsigned;
    DECLARE l_blSampleImageAutoScoreClassId tinyint(3) unsigned;

	  IF p_imageFullPath IS NOT NULL AND p_schemaName IS NOT NULL AND p_scoreClass IS NOT NULL THEN

        SELECT max(blSampleImageId) INTO l_blSampleImageId FROM BLSampleImage WHERE imageFullPath = p_imageFullPath;

        SELECT blSampleImageAutoScoreClassId INTO l_blSampleImageAutoScoreClassId FROM BLSampleImageAutoScoreClass bsiasc INNER JOIN BLSampleImageAutoScoreSchema bsiass USING(blSampleImageAutoScoreSchemaId)
        WHERE bsiasc.scoreClass = p_scoreClass AND bsiass.schemaName = p_schemaName AND bsiass.enabled > 0;

        INSERT INTO BLSampleImage_has_AutoScoreClass (blSampleImageId, blSampleImageAutoScoreClassId, probability)
          VALUES (l_blSampleImageId, l_blSampleImageAutoScoreClassId, p_probability);

        SET p_id = LAST_INSERT_ID();

	  END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `insert_screening` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `insert_screening`(
     OUT p_id int(11) unsigned,
     p_dcgId int(11) unsigned,
     p_dcId int(11) unsigned,
     p_programVersion varchar(45),
     p_shortComments varchar(20),
     p_comments varchar(255)
)
    MODIFIES SQL DATA
    COMMENT 'Insert a row with info about a screening. Returns the ID in p_id'
BEGIN
	  IF p_dcgId IS NULL AND p_dcId IS NOT NULL THEN
		SELECT dataCollectionGroupId INTO p_dcgId FROM DataCollection WHERE dataCollectionId = p_dcId;
	  END IF;
      
      INSERT INTO Screening (dataCollectionGroupId, dataCollectionId, programVersion, shortComments, comments) 
        VALUES (IFNULL(p_dcgId, (SELECT dataCollectionGroupId FROM DataCollection WHERE dataCollectionId = p_dcId)), p_dcId, p_programVersion, p_shortComments, p_comments);

	  IF LAST_INSERT_ID() <> 0 THEN 
		  SET p_id = LAST_INSERT_ID();
      END IF;      

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `insert_screening_input` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `insert_screening_input`(
     OUT p_id int(11) unsigned,
     p_screeningId int(10) unsigned,
     p_beamX float,
     p_beamY float,
     p_rmsErrorLimits float,
     p_minFractionIndexed float,
     p_maxFractionRejected float,
     p_minSignalToNoise float
)
    MODIFIES SQL DATA
    COMMENT 'Insert a row with info about a screening input. Returns the ID i'
BEGIN
      INSERT INTO ScreeningInput (screeningId, beamX, beamY, rmsErrorLimits, minimumFractionIndexed, maximumFractionRejected, minimumSignalToNoise) 
        VALUES (p_screeningId, p_beamX, p_beamY, p_rmsErrorLimits, p_minFractionIndexed, p_maxFractionRejected, p_minSignalToNoise);

	  IF LAST_INSERT_ID() <> 0 THEN 
		  SET p_id = LAST_INSERT_ID();
      END IF;      
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `insert_screening_output` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `insert_screening_output`(
     OUT p_id int(11) unsigned,
     p_screeningId int(10) unsigned,
     p_statusDescription varchar(1024), 
     p_rejectedReflections int(10) unsigned, 
     p_resolutionObtained float, 
     p_spotDeviationR float, 
     p_spotDeviationTheta float, 
     p_beamShiftX float, 
     p_beamShiftY float, 
     p_numSpotsFound int(10) unsigned, 
     p_numSpotsUsed int(10) unsigned, 
     p_numSpotsRejected int(10) unsigned, 
     p_mosaicity float, 
     p_iOverSigma float, 
     p_diffractionRings boolean, 
     p_mosaicityEstimated boolean, 
     p_rankingResolution double, 
     p_program varchar(45), 
     p_doseTotal double, 
     p_totalExposureTime double, 
     p_totalRotationRange double, 
     p_totalNumberOfImages int(11), 
     p_rFriedel double, 
     p_indexingSuccess boolean, 
     p_strategySuccess boolean
)
    MODIFIES SQL DATA
    COMMENT 'Insert a row with info about a screening output. Returns the ID'
BEGIN
      INSERT INTO ScreeningOutput (screeningId, statusDescription, rejectedReflections, resolutionObtained, spotDeviationR, spotDeviationTheta, 
        beamShiftX, beamShiftY, numSpotsFound, numSpotsUsed, numSpotsRejected, mosaicity, iOverSigma, 
        diffractionRings, mosaicityEstimated, rankingResolution, program, doseTotal, totalExposureTime, totalRotationRange, 
        totalNumberOfImages, rFriedel, indexingSuccess, strategySuccess) 
        VALUES (p_screeningId, p_statusDescription, p_rejectedReflections, p_resolutionObtained, p_spotDeviationR, p_spotDeviationTheta, 
        p_beamShiftX, p_beamShiftY, p_numSpotsFound, p_numSpotsUsed, p_numSpotsRejected, p_mosaicity, p_iOverSigma, 
        p_diffractionRings, p_mosaicityEstimated, p_rankingResolution, p_program, p_doseTotal, p_totalExposureTime, p_totalRotationRange,
        p_totalNumberOfImages, p_rFriedel, p_indexingSuccess, p_strategySuccess);

	  IF LAST_INSERT_ID() <> 0 THEN 
		  SET p_id = LAST_INSERT_ID();
      END IF;      
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `insert_screening_output_lattice` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `insert_screening_output_lattice`(
     OUT p_id int(10) unsigned,
     p_screeningOutputId int(10) unsigned,
     p_spaceGroup	varchar(45),
     p_pointGroup	varchar(45),
     p_bravaisLattice	varchar(45),
     p_rawOrientationMatrix_a_x float,
     p_rawOrientationMatrix_a_y float,
     p_rawOrientationMatrix_a_z float,
     p_rawOrientationMatrix_b_x float,
     p_rawOrientationMatrix_b_y float,
     p_rawOrientationMatrix_b_z float,
     p_rawOrientationMatrix_c_x float,
     p_rawOrientationMatrix_c_y float,
     p_rawOrientationMatrix_c_z float,
     p_unitCell_a	float,
     p_unitCell_b	float,
     p_unitCell_c	float,
     p_unitCell_alpha	float,
     p_unitCell_beta	float,
     p_unitCell_gamma	float,
     p_labelitIndexing boolean
)
    MODIFIES SQL DATA
    COMMENT 'Insert a row with info about a screening output lattice. Returns'
BEGIN
      INSERT INTO ScreeningOutputLattice (screeningOutputId, spaceGroup, pointGroup, bravaisLattice, 
        rawOrientationMatrix_a_x, rawOrientationMatrix_a_y, rawOrientationMatrix_a_z,
		rawOrientationMatrix_b_x, rawOrientationMatrix_b_y, rawOrientationMatrix_b_z,
        rawOrientationMatrix_c_x, rawOrientationMatrix_c_y, rawOrientationMatrix_c_z,
        unitCell_a, unitCell_b, unitCell_c, unitCell_alpha, unitCell_beta, unitCell_gamma, labelitIndexing) 
        VALUES (p_screeningOutputId, p_spaceGroup, p_pointGroup, p_bravaisLattice, 
        p_rawOrientationMatrix_a_x, p_rawOrientationMatrix_a_y, p_rawOrientationMatrix_a_z,
		p_rawOrientationMatrix_b_x, p_rawOrientationMatrix_b_y, p_rawOrientationMatrix_b_z,
        p_rawOrientationMatrix_c_x, p_rawOrientationMatrix_c_y, p_rawOrientationMatrix_c_z,
        p_unitCell_a, p_unitCell_b, p_unitCell_c, p_unitCell_alpha, p_unitCell_beta, p_unitCell_gamma, p_labelitIndexing
        );
	  IF LAST_INSERT_ID() <> 0 THEN 
		  SET p_id = LAST_INSERT_ID();
      END IF;      
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `insert_screening_output_v2` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `insert_screening_output_v2`(
     OUT p_id int(11) unsigned,
     p_screeningId int(10) unsigned,
     p_statusDescription varchar(1024), 
     p_rejectedReflections int(10) unsigned, 
     p_resolutionObtained float, 
     p_spotDeviationR float, 
     p_spotDeviationTheta float, 
     p_beamShiftX float, 
     p_beamShiftY float, 
     p_numSpotsFound int(10) unsigned, 
     p_numSpotsUsed int(10) unsigned, 
     p_numSpotsRejected int(10) unsigned, 
     p_mosaicity float, 
     p_iOverSigma float, 
     p_diffractionRings boolean, 
     p_mosaicityEstimated boolean, 
     p_rankingResolution double, 
     p_program varchar(45), 
     p_doseTotal double, 
     p_totalExposureTime double, 
     p_totalRotationRange double, 
     p_totalNumberOfImages int(11), 
     p_rFriedel double, 
     p_indexingSuccess boolean, 
     p_strategySuccess boolean, 
     p_alignmentSuccess boolean
)
    MODIFIES SQL DATA
    COMMENT 'Insert a row with info about a screening output. Returns the ID in p_id.'
BEGIN
      INSERT INTO ScreeningOutput (screeningId, statusDescription, rejectedReflections, resolutionObtained, spotDeviationR, spotDeviationTheta, 
        beamShiftX, beamShiftY, numSpotsFound, numSpotsUsed, numSpotsRejected, mosaicity, iOverSigma, 
        diffractionRings, mosaicityEstimated, rankingResolution, program, doseTotal, totalExposureTime, totalRotationRange, 
        totalNumberOfImages, rFriedel, indexingSuccess, strategySuccess, alignmentSuccess) 
        VALUES (p_screeningId, p_statusDescription, p_rejectedReflections, p_resolutionObtained, p_spotDeviationR, p_spotDeviationTheta, 
        p_beamShiftX, p_beamShiftY, p_numSpotsFound, p_numSpotsUsed, p_numSpotsRejected, p_mosaicity, p_iOverSigma, 
        p_diffractionRings, p_mosaicityEstimated, p_rankingResolution, p_program, p_doseTotal, p_totalExposureTime, p_totalRotationRange,
        p_totalNumberOfImages, p_rFriedel, p_indexingSuccess, p_strategySuccess, p_alignmentSuccess);

	  IF LAST_INSERT_ID() <> 0 THEN 
		  SET p_id = LAST_INSERT_ID();
      END IF;      
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `insert_screening_strategy` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `insert_screening_strategy`(
     OUT p_id int(10) unsigned,
     p_screeningOutputId int(10) unsigned,
     p_phiStart float,
     p_phiEnd float,
     p_rotation float,
     p_exposureTime float,
     p_resolution float,
     p_completeness float,
     p_multiplicity float,
     p_anomalous float,
     p_program varchar(45),
     p_rankingResolution float,
     p_transmission float
)
    MODIFIES SQL DATA
    COMMENT 'Insert a row with info about a screening strategy. Returns the I'
BEGIN
      INSERT INTO ScreeningStrategy (
        screeningOutputId, phiStart, phiEnd, rotation, exposureTime, 
        resolution, completeness, multiplicity, anomalous, program, rankingResolution, transmission)
        VALUES (p_screeningOutputId, p_phiStart, p_phiEnd, p_rotation, p_exposureTime, 
        p_resolution, p_completeness, p_multiplicity, p_anomalous, p_program, p_rankingResolution, p_transmission);

	  IF LAST_INSERT_ID() <> 0 THEN 
		  SET p_id = LAST_INSERT_ID();
      END IF;      

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `insert_screening_strategy_sub_wedge` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE PROCEDURE `insert_screening_strategy_sub_wedge`(
     OUT p_id int(10) unsigned,
     p_screeningStrategyWedgeId int(10) unsigned,
     p_subWedgeNumber int(10) unsigned,
     p_rotationAxis varchar(45),
     p_axisStart float,
     p_axisEnd float,
     p_exposureTime float,
     p_transmission float, 
     p_oscillationRange float,
     p_completeness float,
     p_multiplicity float,
     p_resolution float,
     p_doseTotal float,
     p_numberOfImages	int(10) unsigned,
     p_comments varchar(255)
     )
    MODIFIES SQL DATA
    COMMENT 'Insert a row with info about a screening strategy sub-wedge. Returns the ID in p_id.'
BEGIN
      INSERT INTO ScreeningStrategySubWedge (
        screeningStrategyWedgeId, subWedgeNumber, rotationAxis, axisStart, axisEnd, exposureTime, transmission, 
        oscillationRange, completeness, multiplicity, resolution, doseTotal, numberOfImages, comments)
        VALUES (p_screeningStrategyWedgeId, p_subWedgeNumber, p_rotationAxis, p_axisStart, p_axisEnd, p_exposureTime, p_transmission, 
        p_oscillationRange, p_completeness, p_multiplicity, p_resolution, p_doseTotal, p_numberOfImages, p_comments);
        
	  IF LAST_INSERT_ID() <> 0 THEN 
		  SET p_id = LAST_INSERT_ID();
      END IF;      

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `insert_screening_strategy_wedge` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `insert_screening_strategy_wedge`(
     OUT p_id int(10) unsigned,
     p_screeningStrategyId int(10) unsigned,
     p_wedgeNumber int(10) unsigned,
     p_resolution	float,
     p_completeness float,
     p_multiplicity float,
     p_doseTotal float,
     p_numberOfImages	int(10) unsigned,
     p_phi float,
     p_kappa float,
     p_chi float,
     p_comments varchar(255),
     p_wavelength	double
     )
    MODIFIES SQL DATA
    COMMENT 'Insert a row with info about a screening strategy wedge. Returns'
BEGIN
      INSERT INTO ScreeningStrategyWedge (
        screeningStrategyId, wedgeNumber, resolution, completeness, multiplicity, doseTotal, numberOfImages, 
        phi, kappa, chi, comments, wavelength)
        VALUES (p_screeningStrategyId, p_wedgeNumber, p_resolution, p_completeness, p_multiplicity, p_doseTotal, p_numberOfImages, 
        p_phi, p_kappa, p_chi, p_comments, p_wavelength);
        
	  IF LAST_INSERT_ID() <> 0 THEN 
		  SET p_id = LAST_INSERT_ID();
      END IF;      

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_associated_dc_ids` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_associated_dc_ids`(IN p_dc_id INT)
    READS SQL DATA
proc_body:BEGIN
  DECLARE prefix VARCHAR(255) DEFAULT '';
  
  IF p_dc_id IS NULL THEN
    LEAVE proc_body;
  END IF;
  
  SELECT concat(substr(substring_index(dc.imageprefix, '_', -1), 1, 1), substr(substring_index(dc.imageprefix, '_', -1), 3, 1)) INTO prefix 
  FROM DataCollection dc 
  WHERE dc.datacollectionid = p_dc_id;

  IF prefix = 'MS' THEN

    SELECT DISTINCT(dcids.datacollectionid)
    FROM (
      SELECT dc2.datacollectionid
      FROM BLSession bs
      INNER JOIN DataCollection dc1 ON bs.sessionid = dc1.sessionid AND dc1.actualsamplebarcode is not null AND dc1.actualsamplebarcode <> 'NR'
	  INNER JOIN DataCollection dc2 ON bs.sessionid = dc2.sessionid AND dc1.actualsamplebarcode = dc2.actualsamplebarcode AND
        dc1.datacollectionid <> dc2.datacollectionid AND
        substring_index(dc1.imageprefix, '', -1) = substring_index(dc2.imageprefix, '', -1)
      WHERE dc1.datacollectionid = p_dc_id
      UNION ALL
      SELECT dc2.datacollectionid
      FROM BLSession bs
      INNER JOIN DataCollection dc1 on bs.sessionid = dc1.sessionid
	  INNER JOIN DataCollection dc2 on dc1.imagedirectory = dc2.imagedirectory AND dc1.datacollectionid <> dc2.datacollectionid AND dc1.imagedirectory is not null
      WHERE dc1.datacollectionid = p_dc_id
    ) dcids
    ORDER BY dcids.datacollectionid;

  ELSE 

    SELECT DISTINCT(dcids.datacollectionid)
    FROM (
      SELECT dc2.datacollectionid
      FROM BLSession bs
        INNER JOIN DataCollection dc1 ON bs.sessionid = dc1.sessionid
	    INNER JOIN DataCollection dc2 ON dc1.blsampleid = dc2.blsampleid AND dc1.datacollectionid <> dc2.datacollectionid AND dc1.blsampleid IS NOT NULL
      WHERE dc1.datacollectionid = p_dc_id
      UNION ALL
      SELECT dc2.datacollectionid
      FROM BLSession bs
        INNER JOIN DataCollection dc1 ON bs.sessionid = dc1.sessionid
        INNER JOIN DataCollection dc2 ON dc1.imagedirectory = dc2.imagedirectory AND dc1.datacollectionid <> dc2.datacollectionid AND dc1.imagedirectory IS NOT NULL
      WHERE dc1.datacollectionid = p_dc_id
    ) dcids
    ORDER BY dcids.datacollectionid;
  END IF;

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_components_for_sample_type` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_components_for_sample_type`(IN p_sampleTypeId int unsigned)
    READS SQL DATA
    COMMENT 'Return multi-row result-set with component ID and other info abo'
BEGIN
    IF NOT (p_sampleTypeId IS NULL) THEN
      SELECT
          prot.proteinId "componentId", prot.name "componentName", prot.density "componentDensity", prot.sequence "componentContent", prot.molecularMass "componentMolecularMass", 
          c.abundance "componentAbundance"
      FROM Protein prot  
        INNER JOIN Crystal c on prot.proteinId = c.proteinId
      WHERE c.crystalId = p_sampleTypeId
      UNION ALL
      SELECT
          prot.proteinId "componentId", prot.name "componentName", prot.density "componentDensity", prot.sequence "componentContent", prot.molecularMass "componentMolecularMass", 
          bhc.abundance "componentAbundance"
      FROM BLSampleType_has_Component bhc  
        INNER JOIN Protein prot on prot.proteinId = bhc.componentId
      WHERE bhc.blSampleTypeId = p_sampleTypeId;
    ELSE
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument p_sampleTypeId is NULL';
    END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_component_lattices_for_component` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_component_lattices_for_component`(IN p_componentId int unsigned)
    READS SQL DATA
    COMMENT 'Return multi-row result-set with component lattices for componen'
BEGIN
    IF NOT (p_componentId IS NULL) THEN
		SELECT spaceGroup "spaceGroup", cell_a "a", cell_b "b", cell_c "c", cell_alpha "alpha", cell_beta "beta", cell_gamma "gamma"
        FROM ComponentLattice
        WHERE componentId = p_componentId
        ORDER BY componentId ASC;
    ELSE
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument p_componentId is NULL';
    END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_containers_on_beamline_with_status` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_containers_on_beamline_with_status`(IN p_beamline varchar(20), IN p_status varchar(40))
    READS SQL DATA
    COMMENT 'Returns a multi-row result-set with info about when containers o'
BEGIN
  IF NOT (p_status IS NULL) AND NOT (p_beamline IS NULL) THEN
    SELECT c.barcode "barcode", c.sampleChangerLocation "location", max(ch.blTimeStamp) "added"
	FROM Container c
      LEFT OUTER JOIN ContainerHistory ch ON c.containerId = ch.containerId AND ch.status = p_status
	WHERE c.containerStatus = p_status AND ch.beamlineName = p_beamline 
	GROUP BY c.barcode, c.sampleChangerLocation
	ORDER BY ch.blTimeStamp ASC;
    ELSE 
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory arguments p_status and/or p_beamline are NULL';
  END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_containers_submitted_non_ls` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_containers_submitted_non_ls`(IN p_beamline varchar(15))
    READS SQL DATA
    COMMENT 'Returns multi-row result-set with info about submitted, not comp'
BEGIN
SELECT
  c.barcode "containerBarcode",
  c.code "containerName",
  concat(p.proposalcode, p.proposalnumber) "proposal", 
  s.shippingName "shipmentName", 
  c.capacity "containerCapacity",
  c.containerType "containerType",
  i.name "imagerName",
  i.serial "imagerSerialNumber",
  i.temperature "imagerTemperature",
  cq.createdTimeStamp "containerQueueTS",
  blsi.imageFullPath "lastImgFullPath", 
  blss.imgFilePath "uploadedImgFilePath", blss.imgFileName "uploadedImgFileName", 
  bls.location "sampleLocation",
  dp.experimentKind "experimentKind", dp.exposureTime "exposureTime", 
  dp.preferredBeamSizeX "preferredBeamSizeX", dp.preferredBeamSizeY "preferredBeamSizeY", dp.requiredResolution "requiredResolution", 
  dp.monochromator "monochromator", 12398.42 / dp.energy "wavelength", dp.transmission "transmission", 
  dp.boxSizeX "boxSizeX", dp.boxSizeY "boxSizeY", 
  dp.kappaStart "kappaStart", dp.axisStart "axisStart", dp.axisRange "axisRange", dp.numberOfImages "numberOfImages"
FROM Proposal p
  INNER JOIN Shipping s ON s.proposalId = p.proposalId
  INNER JOIN Dewar d ON d.shippingId = s.shippingId  
  INNER JOIN Container c ON c.dewarId = d.dewarId
  INNER JOIN ContainerQueue cq ON c.containerId = cq.containerId
  INNER JOIN ContainerQueueSample cqs on cq.containerQueueId = cqs.containerQueueId
  INNER JOIN BLSubSample blss ON blss.blSubSampleId = cqs.blSubSampleId
  INNER JOIN BLSample bls ON blss.blSampleId = bls.blSampleId  
  INNER JOIN DiffractionPlan dp ON dp.diffractionPlanId = blss.diffractionPlanId
  INNER JOIN Imager i ON i.imagerId = c.imagerId 
  LEFT OUTER JOIN BLSampleImage blsi ON blsi.blSampleId = blss.blSampleId
WHERE cq.completedTimeStamp is NULL AND c.containerStatus = 'in_storage'
ORDER BY cq.createdTimeStamp ASC;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_container_for_barcode` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_container_for_barcode`(IN p_barcode varchar(45))
    READS SQL DATA
    COMMENT 'Return single-row result set with info about a Container identified by p_barcode'
BEGIN
    IF NOT (p_barcode IS NULL) THEN
      SELECT c.containerId, c.sessionId, c.dewarId "dewarId",
        c.code "name", c.barcode "barcode", c.containerStatus "status",
        c.containerType "type", c.capacity "capacity",
	      c.sampleChangerLocation "location", c.beamlineLocation "beamline",
        c.comments "comments", c.experimentType "experimentType",
        concat(p.proposalCode, p.proposalNumber, '-', bs.visit_number) "visit",
        date_format(c.blTimeStamp, '%Y') "year"
      FROM Container c
        LEFT OUTER JOIN BLSession bs ON bs.sessionId = c.sessionId
        LEFT OUTER JOIN Proposal p ON p.proposalId = bs.proposalId
      WHERE c.barcode=p_barcode
        LIMIT 1;
     ELSE
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument is NULL: p_barcode';
    END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_container_for_inspection_id` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_container_for_inspection_id`(IN p_containerInspectionId int(11) unsigned)
    READS SQL DATA
    COMMENT 'Return single-row result set with info about a Container identified by p_containerInspectionId'
BEGIN
    IF NOT (p_containerInspectionId IS NULL) THEN
        SELECT c.containerType, c.containerId, c.sessionId, concat(p.proposalCode, p.proposalNumber, '-', bs.visit_number) "visit",
        date_format(c.blTimeStamp, '%Y') as year
        FROM Container c
          INNER JOIN ContainerInspection ci ON ci.containerId = c.containerId
          INNER JOIN Dewar d ON d.dewarId = c.dewarId
          INNER JOIN Shipping s ON s.shippingId = d.shippingId
          INNER JOIN Proposal p ON p.proposalId = s.proposalId
          LEFT OUTER JOIN BLSession bs ON bs.sessionId = c.sessionId
        WHERE ci.containerinspectionId = p_containerInspectionId
        LIMIT 1;
    ELSE
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument is NULL: p_containerInspectionId';
    END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_container_info` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_container_info`(IN p_barcode varchar(45))
    READS SQL DATA
    COMMENT 'Returns single row result-set with info about the container with'
BEGIN
    IF NOT (p_barcode IS NULL) THEN 
	  SELECT c.code as "name", c.barcode "barcode", c.containerStatus as "status", c.containerType "type", c.capacity "capacity",
	    c.sampleChangerLocation "location", c.beamlineLocation "beamline", 
        p.proposalCode "proposalCode", p.proposalNumber "proposalNumber", bs.visit_number "sessionNumber", 
        i.name "imagerName", i.serial "imagerSerialNumber", i.temperature "storageTemperature"
      FROM Container c
        INNER JOIN Imager i on c.imagerId = i.imagerId
        LEFT OUTER JOIN BLSession bs on bs.sessionId = c.sessionId 
        LEFT OUTER JOIN Proposal p on p.proposalId = bs.proposalId
      WHERE c.barcode = p_barcode
      ORDER BY c.containerId DESC
      LIMIT 1;
    ELSE
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument p_barcode is NULL';
    END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_container_info_for_id` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_container_info_for_id`(IN p_containerId int unsigned)
    READS SQL DATA
    COMMENT 'Return single-row result set with info about a Container identif'
BEGIN
    IF NOT (p_containerId IS NULL) THEN
	    SELECT c.dewarId "dewarId", c.code "name", c.barcode "barcode", c.containerStatus "status", c.containerType "type", c.capacity "capacity",
	      c.sampleChangerLocation "location", c.beamlineLocation "beamline", c.comments "comments", c.experimentType "experimentType",
          p.proposalCode "proposalCode", p.proposalNumber "proposalNumber", bs.visit_number "sessionNumber",
          i.name "imagerName", i.serial "imagerSerialNumber", i.temperature "storageTemperature"
      FROM Container c
          LEFT OUTER JOIN Imager i on c.imagerId = i.imagerId
          LEFT OUTER JOIN BLSession bs on bs.sessionId = c.sessionId 
          LEFT OUTER JOIN Proposal p on p.proposalId = bs.proposalId
        WHERE c.containerId = p_containerId;
     ELSE
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument is NULL: p_containerId';
    END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_container_ls_position` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_container_ls_position`(IN p_barcode varchar(45))
    READS SQL DATA
    COMMENT 'Returns single row, single column result-set with the position o'
BEGIN
    IF NOT (p_barcode IS NULL) THEN 
	  SELECT sampleChangerLocation "position"
      FROM Container 
      WHERE barcode = p_barcode AND containerStatus = 'in_localstorage'
      ORDER BY containerId DESC
      LIMIT 1;
    ELSE
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument p_barcode is NULL';
    END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_container_ls_queue` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_container_ls_queue`(IN p_beamline varchar(45))
    READS SQL DATA
    COMMENT 'Returns a multi-row result-set with info about when containers o'
BEGIN
  IF NOT (p_beamline IS NULL) THEN
    SELECT c.barcode "barcode", c.sampleChangerLocation "location", max(ch.blTimeStamp) "added"
	FROM Container c
      INNER JOIN ContainerHistory ch ON c.containerId = ch.containerId 
	WHERE c.containerStatus = 'in_localstorage' AND ch.status = 'in_localstorage' AND ch.beamlineName = p_beamline 
	GROUP BY c.barcode, c.sampleChangerLocation
	ORDER BY ch.blTimeStamp ASC;
    ELSE 
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument p_beamline is NULL';
  END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_container_on_gonio` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_container_on_gonio`(IN p_beamline varchar(45))
    READS SQL DATA
    COMMENT 'Returns multi-row result-set with info about the containers on p'
BEGIN
  IF NOT (p_beamline IS NULL) THEN
	  SELECT c.code as "name", c.barcode "barcode", c.containerStatus as "status", c.containerType "type", c.capacity "capacity",
	    c.sampleChangerLocation "location", c.beamlineLocation "beamline", 
        p.proposalCode "proposalCode", p.proposalNumber "proposalNumber", bs.visit_number "sessionNumber", 
        i.name "imagerName", i.serial "imagerSerialNumber", i.temperature "storageTemperature"
      FROM Container c
        INNER JOIN Imager i on c.imagerId = i.imagerId
        LEFT OUTER JOIN BLSession bs on bs.sessionId = c.sessionId 
        LEFT OUTER JOIN Proposal p on p.proposalId = bs.proposalId
      WHERE c.containerStatus = 'processing'
      ORDER BY c.containerId DESC;
    ELSE
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument p_beamline is NULL';
  END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_container_queue_most_recent_completed_timestamp` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_container_queue_most_recent_completed_timestamp`(IN p_barcode varchar(45))
    READS SQL DATA
    COMMENT 'Returns a single-row result-set with the most recent timestamp o'
BEGIN
  IF NOT (p_barcode IS NULL) THEN
	SELECT max(cq.completedTimeStamp) "completedTimeStamp"
    FROM Container c
      INNER JOIN ContainerQueue cq ON c.containerId = cq.containerId
    WHERE c.barcode = p_barcode
	ORDER BY c.containerId DESC;
    ELSE 
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument p_barcode is NULL';
  END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_container_queue_timestamp` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_container_queue_timestamp`(IN p_barcode varchar(45))
    READS SQL DATA
    COMMENT 'Returns a single-column, single-row result-set with timestamp of'
BEGIN
  IF NOT (p_barcode IS NULL) THEN
	SELECT cq.createdTimeStamp "createdTimeStamp"
    FROM Container c
      INNER JOIN ContainerQueue cq ON c.containerId = cq.containerId
    WHERE cq.completedTimeStamp IS NULL AND c.barcode = p_barcode
	ORDER BY cq.createdTimeStamp DESC
	LIMIT 1;
    ELSE 
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument p_barcode is NULL';
  END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_container_subsamples` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_container_subsamples`(IN p_barcode varchar(45))
    READS SQL DATA
    COMMENT 'Returns a mutli-row result-set with general info about submitted'
BEGIN
  IF NOT (p_barcode IS NULL) THEN
    SELECT blss.blSubSampleId "id", bls.location "sampleLocation", pos1.posX "ROIPos1x", pos1.posY "ROIPos1y", pos1.posZ "ROIPos1z", pos2.posX "ROIPos2x", pos2.posY "ROIPos2y", pos2.posZ "ROIPos2z", 
	  blsi.imageFullPath "lastImgFullPath", blss.imgFilePath "uploadedImgFilePath", blss.imgFileName "uploadedImgFileName", 
      dp.experimentKind "experimentKind", dp.exposureTime "exposureTime", 
      dp.preferredBeamSizeX "preferredBeamSizeX", dp.preferredBeamSizeY "preferredBeamSizeY", dp.requiredResolution "requiredResolution", 
      dp.monochromator "monochromator", 12398.42 / dp.energy "wavelength", dp.transmission "transmission", 
      dp.boxSizeX "boxSizeX", dp.boxSizeY "boxSizeY", 
      dp.kappaStart "kappaStart", dp.axisStart "axisStart", dp.axisRange "axisRange", dp.numberOfImages "numberOfImages",
      count(dc.dataCollectionId) "numDCs"
    FROM Container c 
	  INNER JOIN ContainerQueue cq ON c.containerId = cq.containerId
      INNER JOIN ContainerQueueSample cqs ON cq.containerQueueId = cqs.containerQueueId
      INNER JOIN BLSubSample blss ON blss.blSubSampleId = cqs.blSubSampleId
      INNER JOIN BLSample bls ON blss.blSampleId = bls.blSampleId
      INNER JOIN Position pos1 ON pos1.positionId = blss.positionId
      LEFT OUTER JOIN Position pos2 ON pos2.positionId = blss.position2Id
      INNER JOIN DiffractionPlan dp ON dp.diffractionPlanId = blss.diffractionPlanId
      LEFT OUTER JOIN BLSampleImage blsi ON blsi.blSampleId = bls.blSampleId AND blsi.blSampleImageId = (SELECT max(blsi2.blSampleImageId) FROM BLSampleImage blsi2 WHERE blsi2.blSampleId = bls.blSampleId)
      LEFT OUTER JOIN DataCollection dc on dc.blSubSampleId = blss.blSubSampleId
	WHERE c.barcode = p_barcode
    GROUP BY blss.blSubSampleId, location, pos1.posX, pos1.posY, pos1.posZ, pos2.posX, pos2.posY, pos2.posZ, 
	  blsi.imageFullPath, blss.imgFilePath, blss.imgFileName, 
      dp.experimentKind, dp.exposureTime, 
      dp.preferredBeamSizeX, dp.preferredBeamSizeY, dp.requiredResolution, 
      dp.monochromator, 12398.42 / dp.energy, dp.transmission, 
      dp.boxSizeX, dp.boxSizeY, 
      dp.kappaStart, dp.axisStart, dp.axisRange, dp.numberOfImages;
    ELSE 
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument p_barcode is NULL';
  END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_container_subsamples_v2` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_container_subsamples_v2`(IN p_barcode varchar(45))
    READS SQL DATA
    COMMENT 'Returns a mutli-row result-set with general info about submitted subsamples on submitted container p_barcode'
BEGIN
  IF NOT (p_barcode IS NULL) THEN
    SELECT blss.blSubSampleId "id", bls.location "sampleLocation", pos1.posX "ROIPos1x", pos1.posY "ROIPos1y", pos1.posZ "ROIPos1z", pos2.posX "ROIPos2x", pos2.posY "ROIPos2y", pos2.posZ "ROIPos2z",
	  blsi.imageFullPath "lastVisibleImgFullPath", blss.imgFilePath "uploadedImgFilePath", blss.imgFileName "uploadedImgFileName",
      dp.experimentKind "experimentKind", dp.exposureTime "exposureTime",
      dp.preferredBeamSizeX "preferredBeamSizeX", dp.preferredBeamSizeY "preferredBeamSizeY", dp.requiredResolution "requiredResolution",
      dp.monochromator "monochromator", 12398.42 / dp.energy "wavelength", dp.transmission "transmission",
      dp.boxSizeX "boxSizeX", dp.boxSizeY "boxSizeY",
      dp.kappaStart "kappaStart", dp.axisStart "axisStart", dp.axisRange "axisRange", dp.numberOfImages "numberOfImages",
      count(dc.dataCollectionId) "numDCs"
    FROM Container c
	    INNER JOIN ContainerQueue cq ON c.containerId = cq.containerId
      INNER JOIN ContainerQueueSample cqs ON cq.containerQueueId = cqs.containerQueueId
      INNER JOIN BLSubSample blss ON blss.blSubSampleId = cqs.blSubSampleId
      INNER JOIN BLSample bls ON blss.blSampleId = bls.blSampleId
      INNER JOIN Position pos1 ON pos1.positionId = blss.positionId
      LEFT OUTER JOIN Position pos2 ON pos2.positionId = blss.position2Id
      INNER JOIN DiffractionPlan dp ON dp.diffractionPlanId = blss.diffractionPlanId
      LEFT OUTER JOIN BLSampleImage blsi ON blsi.blSampleId = bls.blSampleId AND blsi.blSampleImageId = (
        SELECT max(blsi2.blSampleImageId)
        FROM BLSampleImage blsi2
          INNER JOIN ContainerInspection ci ON blsi2.containerInspectionId = ci.containerInspectionId
          INNER JOIN InspectionType it ON ci.inspectionTypeId = it.inspectionTypeId
        WHERE blsi2.blSampleId = bls.blSampleId AND it.name = 'Visible'
      )
      LEFT OUTER JOIN DataCollection dc on dc.blSubSampleId = blss.blSubSampleId
	WHERE c.barcode = p_barcode
    GROUP BY blss.blSubSampleId, location, pos1.posX, pos1.posY, pos1.posZ, pos2.posX, pos2.posY, pos2.posZ,
	  blsi.imageFullPath, blss.imgFilePath, blss.imgFileName,
      dp.experimentKind, dp.exposureTime,
      dp.preferredBeamSizeX, dp.preferredBeamSizeY, dp.requiredResolution,
      dp.monochromator, 12398.42 / dp.energy, dp.transmission,
      dp.boxSizeX, dp.boxSizeY,
      dp.kappaStart, dp.axisStart, dp.axisRange, dp.numberOfImages;
    ELSE
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument p_barcode is NULL';
  END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_current_cm_sessions` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_current_cm_sessions`(IN p_beamline varchar(15))
BEGIN
    SELECT concat(p.proposalCode, p.proposalNumber, '-', bs.visit_number) `session`
    FROM Proposal p
      INNER JOIN BLSession bs on p.proposalId = bs.proposalId
	WHERE p.proposalCode = 'cm' AND bs.beamlinename = p_beamline AND now() > bs.startDate;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_current_sessions` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_current_sessions`(IN p_beamline varchar(15), IN p_tolerance_minutes int)
    READS SQL DATA
    COMMENT 'Returns a multi-row result-set with the current (within tolerance p_tolerance_minutes)\nsession(s) (mx12345-123), their start and end dates for beamline p_beamline'
BEGIN
	set p_tolerance_minutes = IFNULL(p_tolerance_minutes, 0);
    SELECT concat(p.proposalCode, p.proposalNumber, '-', bs.visit_number) `session`, bs.startDate, bs.endDate
    FROM Proposal p
      INNER JOIN BLSession bs on p.proposalId = bs.proposalId
	WHERE bs.beamlinename = p_beamline AND bs.visit_number <> 0 AND now() BETWEEN bs.startDate - INTERVAL p_tolerance_minutes MINUTE and bs.endDate + INTERVAL p_tolerance_minutes MINUTE
    ORDER BY bs.startDate;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_current_sessions_for_person` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_current_sessions_for_person`(IN p_beamline varchar(15), IN p_fed_id varchar(24), IN p_tolerance_minutes int)
    READS SQL DATA
    COMMENT 'Returns a multi-row result-set with the current (within tolerance p_tolerance_minutes)\nsession(s) (mx12345-123), their start and end dates for person p_fed_id and beamline p_beamline'
BEGIN
	  SET p_tolerance_minutes = IFNULL(p_tolerance_minutes, 0);
    SELECT concat(p.proposalCode, p.proposalNumber, '-', bs.visit_number) `session`, bs.startDate, bs.endDate
    FROM Proposal p
      INNER JOIN BLSession bs on p.proposalId = bs.proposalId
      INNER JOIN Session_has_Person shp ON shp.sessionId = bs.sessionId
	    INNER JOIN Person per ON shp.personId = per.personId
	  WHERE bs.beamlinename = p_beamline AND bs.visit_number <> 0 AND per.login = p_fed_id AND now() BETWEEN bs.startDate - INTERVAL p_tolerance_minutes MINUTE and bs.endDate + INTERVAL p_tolerance_minutes MINUTE
    ORDER BY bs.startDate;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_dc` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_dc`(p_id int unsigned, p_authLogin varchar(45))
    READS SQL DATA
    COMMENT 'Returns a single-row result-set with the data collection for the given ID'
BEGIN
    IF p_id IS NOT NULL THEN

    	IF p_authLogin IS NOT NULL THEN
    	

				SELECT dc.dataCollectionGroupId "groupId",
					dc.detectorId "detectorId",
					dc.blSubSampleId "blSubSampleId",
					dc.dataCollectionNumber "dcNumber",
					dc.startTime "startTime",
					dc.endTime "endTime",
					dc.runStatus "status",
					dc.numberOfImages "noImages",
					dc.startImageNumber "startImgNumber",
					dc.numberOfPasses "noPasses",
					dc.imageDirectory "imgDir",
					dc.imagePrefix "imgPrefix",
					dc.imageSuffix "imgSuffix",
					dc.imageContainerSubPath "imgContainerSubPath",
					dc.fileTemplate "fileTemplate",
					dc.xtalSnapshotFullPath1 "snapshot1",
					dc.xtalSnapshotFullPath2 "snapshot2",
					dc.xtalSnapshotFullPath3 "snapshot3",
					dc.xtalSnapshotFullPath4 "snapshot4",
					dc.comments "comments",
					dc.slitGapVertical "slitGapVertical",
					dc.slitGapHorizontal "slitGapHorizontal",
					dc.transmission "transmission",
					dc.exposureTime "exposureTime",
					dc.xBeam "xBeam",
					dc.yBeam "yBeam",
					dc.axisStart "axisStart",
					dc.axisEnd "axisEnd",
					dc.axisRange "axisRange",
					dc.overlap "overlap",
					dc.flux "flux",
					dc.flux_end "fluxEnd",
					dc.rotationAxis "rotationAxis",
					dc.phiStart "phiStart",
					dc.kappaStart "kappaStart",
					dc.omegaStart "omegaStart",
					dc.chiStart "chiStart",
					dc.wavelength "wavelength",
					dc.resolution "resolution",
					dc.resolutionAtCorner "resolutionAtCorner",
					dc.detectorDistance "detectorDistance",
					dc.detector2Theta "detector2Theta",
					dc.bestWilsonPlotPath "bestWilsonPlotPath",
					dc.beamSizeAtSampleX "beamSizeAtSampleX",
					dc.beamSizeAtSampleY "beamSizeAtSampleY",
					dc.focalSpotSizeAtSampleX "focalSpotSizeAtSampleX",
					dc.focalSpotSizeAtSampleY "focalSpotSizeAtSampleY",
					a.sizeX "apertureSizeX",
					dc.synchrotronMode "synchrotronMode",
					dc.undulatorGap1 "undulatorGap1",
					dc.undulatorGap2 "undulatorGap2",
					dc.undulatorGap3 "undulatorGap3"
				FROM DataCollection dc
					INNER JOIN DataCollectionGroup dcg ON dc.dataCollectionGroupId = dcg.dataCollectionGroupId
        	INNER JOIN BLSession bs ON dcg.sessionId = bs.sessionId 
        	INNER JOIN Session_has_Person shp ON bs.sessionId = shp.sessionId
        	INNER JOIN Person p ON p.personId = shp.personId
					LEFT OUTER JOIN Aperture a ON dc.apertureId = a.apertureId
	  		WHERE p.login = p_authLogin AND	dc.dataCollectionId = p_id;

    	ELSE 

				SELECT dc.dataCollectionGroupId "groupId",
					dc.detectorId "detectorId",
					dc.blSubSampleId "blSubSampleId",
					dc.dataCollectionNumber "dcNumber",
					dc.startTime "startTime",
					dc.endTime "endTime",
					dc.runStatus "status",
					dc.numberOfImages "noImages",
					dc.startImageNumber "startImgNumber",
					dc.numberOfPasses "noPasses",
					dc.imageDirectory "imgDir",
					dc.imagePrefix "imgPrefix",
					dc.imageSuffix "imgSuffix",
					dc.imageContainerSubPath "imgContainerSubPath",
					dc.fileTemplate "fileTemplate",
					dc.xtalSnapshotFullPath1 "snapshot1",
					dc.xtalSnapshotFullPath2 "snapshot2",
					dc.xtalSnapshotFullPath3 "snapshot3",
					dc.xtalSnapshotFullPath4 "snapshot4",
					dc.comments "comments",
					dc.slitGapVertical "slitGapVertical",
					dc.slitGapHorizontal "slitGapHorizontal",
					dc.transmission "transmission",
					dc.exposureTime "exposureTime",
					dc.xBeam "xBeam",
					dc.yBeam "yBeam",
					dc.axisStart "axisStart",
					dc.axisEnd "axisEnd",
					dc.axisRange "axisRange",
					dc.overlap "overlap",
					dc.flux "flux",
					dc.flux_end "fluxEnd",
					dc.rotationAxis "rotationAxis",
					dc.phiStart "phiStart",
					dc.kappaStart "kappaStart",
					dc.omegaStart "omegaStart",
					dc.chiStart "chiStart",
					dc.wavelength "wavelength",
					dc.resolution "resolution",
					dc.resolutionAtCorner "resolutionAtCorner",
					dc.detectorDistance "detectorDistance",
					dc.detector2Theta "detector2Theta",
					dc.bestWilsonPlotPath "bestWilsonPlotPath",
					dc.beamSizeAtSampleX "beamSizeAtSampleX",
					dc.beamSizeAtSampleY "beamSizeAtSampleY",
					dc.focalSpotSizeAtSampleX "focalSpotSizeAtSampleX",
					dc.focalSpotSizeAtSampleY "focalSpotSizeAtSampleY",
					a.sizeX "apertureSizeX",
					dc.synchrotronMode "synchrotronMode",
					dc.undulatorGap1 "undulatorGap1",
					dc.undulatorGap2 "undulatorGap2",
					dc.undulatorGap3 "undulatorGap3"
				FROM DataCollection dc
					LEFT OUTER JOIN Aperture a ON dc.apertureId = a.apertureId
				WHERE dc.dataCollectionId = p_id;

    	END IF;

    ELSE
	  SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory arguments p_id can not be NULL';
	END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_dc_group` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_dc_group`(p_id int unsigned)
    READS SQL DATA
    COMMENT 'Returns a single-row result-set with the columns for the given data collection group id'
BEGIN
    IF p_id IS NOT NULL THEN
      SELECT sessionId, blSampleId "sampleId", experimentType "experimenttype", startTime "starttime", endTime "endtime",
        crystalClass, detectorMode, actualSampleBarcode, actualSampleSlotInContainer, actualContainerBarcode, actualContainerSlotInSC,
        comments, xtalSnapshotFullPath, scanParameters
      FROM DataCollectionGroup
      WHERE datacollectionGroupId = p_id;
    ELSE
	    SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644,
        MESSAGE_TEXT='Mandatory argument p_id can not be NULL';
	END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_dc_group_v2` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_dc_group_v2`(p_id int unsigned, p_authLogin varchar(45))
    READS SQL DATA
    COMMENT 'Returns a single-row result-set with the columns for the given data collection group id'
BEGIN
    IF p_id IS NOT NULL THEN
      IF p_authLogin IS NOT NULL THEN
      
        SELECT dcg.sessionId,
          dcg.blSampleId "sampleId",
          dcg.experimentType "experimenttype",
          dcg.startTime "starttime",
          dcg.endTime "endtime",
          dcg.crystalClass,
          dcg.detectorMode,
          dcg.actualSampleBarcode,
          dcg.actualSampleSlotInContainer,
          dcg.actualContainerBarcode,
          dcg.actualContainerSlotInSC,
          dcg.comments,
          dcg.xtalSnapshotFullPath,
          dcg.scanParameters
        FROM DataCollectionGroup dcg
          INNER JOIN BLSession bs ON dcg.sessionId = bs.sessionId
          INNER JOIN Session_has_Person shp ON bs.sessionId = shp.sessionId
          INNER JOIN Person p ON p.personId = shp.personId
        WHERE dcg.datacollectionGroupId = p_id AND p.login = p_authLogin;

      ELSE

        SELECT dcg.sessionId,
          dcg.blSampleId "sampleId",
          dcg.experimentType "experimenttype",
          dcg.startTime "starttime",
          dcg.endTime "endtime",
          dcg.crystalClass,
          dcg.detectorMode,
          dcg.actualSampleBarcode,
          dcg.actualSampleSlotInContainer,
          dcg.actualContainerBarcode,
          dcg.actualContainerSlotInSC,
          dcg.comments,
          dcg.xtalSnapshotFullPath,
          dcg.scanParameters
        FROM DataCollectionGroup dcg
        WHERE dcg.datacollectionGroupId = p_id;
      END IF;
    ELSE
	    SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644,
        MESSAGE_TEXT='Mandatory argument p_id can not be NULL';
	END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_dc_infos_for_subsample` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_dc_infos_for_subsample`(p_id int)
    READS SQL DATA
BEGIN
    SELECT dc.datacollectionId "id", dc.dataCollectionNumber "dcNumber", dc.startTime "startTime", dc.endTime "endTime", 
        dc.runStatus "status", dc.axisStart "axisStart", dc.axisEnd "axisEnd", dc.axisRange "axisRange", dc.overlap "overlap", 
        dc.numberOfImages "numberOfImages", dc.startImageNumber "startImageNumber", dc.numberOfPasses "numberOfPasses", 
        dc.exposureTime, dc.imageDirectory, dc.imagePrefix, dc.imageSuffix, dc.fileTemplate, 
        dc.wavelength "wavelength", dc.resolution "resolution", dc.detectorDistance "detectorDistance", dc.xBeam "xBeam", dc.yBeam "yBeam", 
        dc.comments "comments", dc.slitgapVertical "slitgapVertical", dc.slitgapHorizontal "slitgapHorizontal", 
        dc.transmission "transmission", dc.synchrotronMode "synchrotronMode", 
        dc.xtalSnapshotFullPath1 "snapshot1", dc.xtalSnapshotFullPath2 "snapshot2", 
        dc.xtalSnapshotFullPath3 "snapshot3", dc.xtalSnapshotFullPath4 "snapshot4", 
        dc.rotationAxis "rotationAxis", dc.phiStart "phiStart", dc.kappaStart "kappaStart", dc.omegaStart "omegaStart", 
        dc.undulatorGap1 "undulatorGap1", dc.undulatorGap2 "undulatorGap2", dc.undulatorGap3 "undulatorGap3", 
        dc.beamSizeAtSampleX "beamSizeAtSampleX", dc.beamSizeAtSampleY "beamSizeAtSampleY", 
        dc.focalSpotSizeAtSampleX "focalSpotSizeAtSampleX", dc.focalSpotSizeAtSampleY "focalSpotSizeAtSampleY", 
        dc.polarisation "polarisation", dc.flux "flux", dc.flux_end "fluxEnd", a.sizeX "apertureSizeX"
        
        
    FROM DataCollection dc
		LEFT OUTER JOIN Aperture a on dc.apertureId = a.apertureId
    WHERE blSubSampleId = p_id;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_dc_main` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_dc_main`(p_id int unsigned)
    READS SQL DATA
    COMMENT 'Returns a single-row result-set with the main data collection in'
BEGIN
    IF p_id IS NOT NULL THEN
		SELECT dataCollectionGroupId "groupId",
			detectorId "detectorId",
			blSubSampleId "blSubSampleId",
			dataCollectionNumber "dcNumber",
			startTime "startTime",
			endTime "endTime",
			runStatus "status",
			numberOfImages "noImages",
			startImageNumber "startImgNumber",
			numberOfPasses "noPasses",
			imageDirectory "imgDir",
			imagePrefix "imgPrefix",
			imageSuffix "imgSuffix",
			fileTemplate "fileTemplate",
			xtalSnapshotFullPath1 "snapshot1",
			xtalSnapshotFullPath2 "snapshot2",
			xtalSnapshotFullPath3 "snapshot3",
			xtalSnapshotFullPath4 "snapshot4",
			comments "comments"
		FROM DataCollection 
		WHERE dataCollectionId = p_id;
    ELSE
	  SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory arguments p_id can not be NULL';
	END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_dc_main_v2` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_dc_main_v2`(p_id int unsigned, p_authLogin varchar(45))
    READS SQL DATA
    COMMENT 'Returns a single-row result-set with the main data collection info for the given ID'
BEGIN
    IF p_id IS NOT NULL THEN

    	IF p_authLogin IS NOT NULL THEN
    	

				SELECT dc.dataCollectionGroupId "groupId",
					dc.detectorId "detectorId",
					dc.blSubSampleId "blSubSampleId",
					dc.dataCollectionNumber "dcNumber",
					dc.startTime "startTime",
					dc.endTime "endTime",
					dc.runStatus "status",
					dc.numberOfImages "noImages",
					dc.startImageNumber "startImgNumber",
					dc.numberOfPasses "noPasses",
					dc.imageDirectory "imgDir",
					dc.imagePrefix "imgPrefix",
					dc.imageSuffix "imgSuffix",
					dc.fileTemplate "fileTemplate",
					dc.xtalSnapshotFullPath1 "snapshot1",
					dc.xtalSnapshotFullPath2 "snapshot2",
					dc.xtalSnapshotFullPath3 "snapshot3",
					dc.xtalSnapshotFullPath4 "snapshot4",
					dc.comments "comments"
				FROM DataCollection dc
					INNER JOIN DataCollectionGroup dcg ON dc.dataCollectionGroupId = dcg.dataCollectionGroupId
        	INNER JOIN BLSession bs ON dcg.sessionId = bs.sessionId 
        	INNER JOIN Session_has_Person shp ON bs.sessionId = shp.sessionId
        	INNER JOIN Person p ON p.personId = shp.personId
	  		WHERE p.login = p_authLogin AND	dc.dataCollectionId = p_id;

    	ELSE 

				SELECT dataCollectionGroupId "groupId",
					detectorId "detectorId",
					blSubSampleId "blSubSampleId",
					dataCollectionNumber "dcNumber",
					startTime "startTime",
					endTime "endTime",
					runStatus "status",
					numberOfImages "noImages",
					startImageNumber "startImgNumber",
					numberOfPasses "noPasses",
					imageDirectory "imgDir",
					imagePrefix "imgPrefix",
					imageSuffix "imgSuffix",
					fileTemplate "fileTemplate",
					xtalSnapshotFullPath1 "snapshot1",
					xtalSnapshotFullPath2 "snapshot2",
					xtalSnapshotFullPath3 "snapshot3",
					xtalSnapshotFullPath4 "snapshot4",
					comments "comments"
				FROM DataCollection 
				WHERE dataCollectionId = p_id;

    	END IF;

    ELSE
	  SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory arguments p_id can not be NULL';
	END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_dc_plans_for_sample` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_dc_plans_for_sample`(IN p_sampleId int unsigned)
    READS SQL DATA
    COMMENT 'Return multi-row result-set with info about data collection plan'
BEGIN
    IF NOT (p_sampleId IS NULL) THEN
    SELECT dp.diffractionPlanId "dcPlanId", dp.name "name", dp.experimentKind "experimentKind", 
      dp.preferredBeamSizeX "preferredBeamSizeX", dp.preferredBeamSizeY "preferredBeamSizeY", dp.requiredResolution "requiredResolution", 
      dp.monoBandwidth "monoBandwidth", dp.energy "energy", 
      dhd.detectorId "detectorId", dhd.exposureTime "exposureTime", dhd.distance "distance", dhd.roll "roll", 
      spm.scanParametersModelId "scanParamModelId", sps.name "scanParamServiceName", spm.sequenceNumber "scanParamSequenceNumber", 
      spm.start "scanParamModelStart", spm.stop "scanParamModelStop", spm.step "scanParamModelStep", spm.array "scanParamModelArray"
    FROM BLSample_has_DataCollectionPlan bhd 
      INNER JOIN DiffractionPlan dp ON dp.diffractionPlanId = bhd.dataCollectionPlanId
      INNER JOIN ScanParametersModel spm on spm.dataCollectionPlanId = dp.diffractionPlanId
      INNER JOIN ScanParametersService sps on sps.scanParametersServiceId = spm.scanParametersServiceId
      LEFT OUTER JOIN DataCollectionPlan_has_Detector dhd on dhd.dataCollectionPlanId = dp.diffractionPlanId
    WHERE bhd.blSampleId = p_sampleId
    ORDER BY dp.diffractionPlanId ASC, spm.sequenceNumber ASC;    

    ELSE
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument p_sampleId is NULL';
    END IF;

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_dc_plan_groups` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_dc_plan_groups`(IN p_session varchar(15))
    READS SQL DATA
BEGIN
    IF NOT (p_session IS NULL) THEN
		SELECT dcpg.dataCollectionPlanGroupId "id"
        FROM DataCollectionPlanGroup dcpg
          INNER JOIN BLSession bs ON bs.sessionId = dcpg.sessionId
          INNER JOIN Proposal p ON p.proposalid = bs.proposalid
		WHERE dcpg.blsampleId is not NULL AND concat(p.proposalcode, p.proposalnumber, '-', bs.visit_number) = p_session;
    END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_dc_plan_info` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_dc_plan_info`(IN p_id int)
    READS SQL DATA
BEGIN
    IF NOT (p_id IS NULL) THEN
		SELECT dp.diffractionPlanId "id", dp.energy "energy", dp.preferredBeamSizeX "preferredBeamSizeX", dp.preferredBeamSizeY "preferredBeamSizeY", 
          dp.exposureTime "exposureTime", dp.distance "distance", dp.orientation "orientation", dp.monoBandwidth "monoBandwidth",
          d.detectorType "detectorType", d.detectorManufacturer "detectorManufacturer", d.detectorModel "detectorModel", 
          d.detectorDistanceMin "detectorDistanceMin", d.detectorDistanceMax "detectorDistanceMax", d.density "density", d.composition "composition",  
          sps.name "scanParamServiceName", sps.description "scanParamServiceDesc",
          spm.modelNumber "scanParamModelNumber", spm.start "scanParamModelStart", spm.stop "scanParamModelStop", spm.step "scanParamModelStep", 
          spm.array "scanParamModelArray"
        FROM DiffractionPlan dp
          INNER JOIN Detector d on d.detectorId = dp.detectorId
          INNER JOIN ScanParametersModel spm on spm.dataCollectionPlanId = dp.diffractionPlanId
          INNER JOIN ScanParametersService sps on sps.scanParametersServiceId = spm.scanParametersServiceId
        WHERE dp.dataCollectionPlanGroupId = p_id
        ORDER BY spm.modelNumber ASC;
    END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_detector` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_detector`(IN p_serialNumber varchar(15))
    READS SQL DATA
BEGIN
  IF p_serialNumber IS NOT NULL THEN
    SELECT detectorId "detectorId", detectorType "type", detectorManufacturer "manufacturer", 
      detectorModel "model", detectorPixelSizeHorizontal "pixelSizeHorizontal", 
      detectorPixelSizeVertical "pixelSizeVertical",
      detectorDistanceMin "distanceMin", detectorDistanceMax "distanceMax", 
      trustedPixelValueRangeLower "trustedPixelValueRangeLower", trustedPixelValueRangeUpper "trustedPixelValueRangeUpper", 
      sensorThickness "sensorThickness", overload "overload", detectorMode "mode"
      
	FROM Detector
    WHERE detectorSerialNumber = p_serialNumber;
  ELSE
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument p_serialNumber is NULL';  
  END IF;

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_dewars_for_proposal_code_number` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_dewars_for_proposal_code_number`(p_proposalCode varchar(3), p_proposalNumber int unsigned)
    READS SQL DATA
    COMMENT 'Return multi-row result-set with dewar ID + other dewar info ass'
BEGIN
    IF NOT (p_proposalNumber IS NULL) THEN
      SELECT
          d.dewarId "id", d.shippingId "shippingId", d.code "name", d.comments "comments", d.storageLocation "storageLocation",
          d.dewarStatus "status", d.isStorageDewar "isStorageDewar", d.barCode "barCode", d.firstExperimentId "firstSessionId",
					d.type "type", d.facilityCode "facilityCode", d.weight "weight", d.deliveryAgent_barcode "deliveryAgentBarcode"
      FROM Dewar d
        INNER JOIN Shipping s ON s.shippingId = d.shippingId
				INNER JOIN Proposal p ON p.proposalId = s.proposalId
      WHERE p.proposalCode = p_proposalCode AND p.proposalNumber = p_proposalNumber;
    ELSE
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument p_proposalNumber is NULL';
    END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_dewars_for_proposal_code_number_v2` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_dewars_for_proposal_code_number_v2`(
    p_proposalCode varchar(3), 
    p_proposalNumber int unsigned, 
    p_authLogin varchar(45))
    READS SQL DATA
    COMMENT 'Return multi-row result-set with dewar ID + other dewar info associated with shipments in a given proposal specified by proposal code, proposal_number'
BEGIN
    IF NOT (p_proposalCode IS NULL OR p_proposalNumber IS NULL) THEN

        IF p_authLogin IS NOT NULL THEN
            SELECT
                d.dewarId "id", d.shippingId "shippingId", d.code "name", d.comments "comments", d.storageLocation "storageLocation",
                d.dewarStatus "status", d.isStorageDewar "isStorageDewar", d.barCode "barCode", d.firstExperimentId "firstSessionId",
				d.type "type", d.facilityCode "facilityCode", d.weight "weight", d.deliveryAgent_barcode "deliveryAgentBarcode"
            FROM Dewar d
                INNER JOIN Shipping s ON s.shippingId = d.shippingId
		        INNER JOIN Proposal p ON p.proposalId = s.proposalId
                INNER JOIN BLSession bs ON bs.proposalId = s.proposalId
                INNER JOIN Session_has_Person shp ON bs.sessionId = shp.sessionId
                INNER JOIN Person per ON per.personId = shp.personId
            WHERE per.login = p_authLogin AND p.proposalCode = p_proposalCode AND p.proposalNumber = p_proposalNumber
            GROUP BY d.dewarId, d.shippingId, d.code, d.comments, d.storageLocation,
                d.dewarStatus, d.isStorageDewar, d.barCode, d.firstExperimentId,
				d.type, d.facilityCode, d.weight, d.deliveryAgent_barcode;
        ELSE
            SELECT
                d.dewarId "id", d.shippingId "shippingId", d.code "name", d.comments "comments", d.storageLocation "storageLocation",
                d.dewarStatus "status", d.isStorageDewar "isStorageDewar", d.barCode "barCode", d.firstExperimentId "firstSessionId",
				d.type "type", d.facilityCode "facilityCode", d.weight "weight", d.deliveryAgent_barcode "deliveryAgentBarcode"
            FROM Dewar d
                INNER JOIN Shipping s ON s.shippingId = d.shippingId
		        INNER JOIN Proposal p ON p.proposalId = s.proposalId
            WHERE p.proposalCode = p_proposalCode AND p.proposalNumber = p_proposalNumber;
        END IF;

    ELSE
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory arguments p_proposalCode and/or p_proposalNumber are NULL';
    END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_expired_sessions_for_instrument_and_period` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_expired_sessions_for_instrument_and_period`(IN p_instrument varchar(15), IN p_startDate datetime, IN p_endDate datetime)
    READS SQL DATA
    COMMENT 'Returns a multi-row result-set with the sessions that ended within the window defined by p_startDate and p_endDate on instrument given by p_instrument (can contain wildcards)'
BEGIN
  SELECT bs.beamlinename "instrument", concat(p.proposalCode, p.proposalNumber, '-', bs.visit_number) "session", bs.startDate, bs.endDate
    FROM Proposal p
      INNER JOIN BLSession bs on p.proposalId = bs.proposalId
	WHERE bs.beamlinename LIKE p_instrument AND bs.visit_number <> 0 AND bs.endDate BETWEEN p_startDate AND p_endDate
    ORDER BY bs.startDate;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_grid_info_for_dcg` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_grid_info_for_dcg`(IN p_dcgId int unsigned)
    READS SQL DATA
    COMMENT 'Return multi-row result-set with grid info values for the dcg'
BEGIN
    IF NOT (p_dcgId IS NULL) THEN
      SELECT
        gi.gridInfoId,
        gi.dx_mm,
        gi.dy_mm,
        gi.steps_x,
        gi.steps_y,
        gi.meshAngle,
        gi.pixelsPerMicronX,
        gi.pixelsPerMicronY,
        gi.snapshot_offsetXPixel,
        gi.snapshot_offsetYPixel,
        gi.orientation,
        gi.snaked
    FROM GridInfo gi
    WHERE gi.dataCollectionGroupId = p_dcgId
    ORDER BY gi.gridInfoId ASC;
    ELSE
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument p_dcgId is NULL';
    END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_grid_info_for_dcg_v2` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_grid_info_for_dcg_v2`(IN p_dcgId int unsigned, p_authLogin varchar(45))
    READS SQL DATA
    COMMENT 'Return multi-row result-set with grid info values for the dcg'
BEGIN
    IF NOT (p_dcgId IS NULL) THEN
        IF p_authLogin IS NOT NULL THEN
            SELECT
                gi.gridInfoId,
                gi.dx_mm,
                gi.dy_mm,
                gi.steps_x,
                gi.steps_y,
                gi.meshAngle,
                gi.pixelsPerMicronX,
                gi.pixelsPerMicronY,
                gi.snapshot_offsetXPixel,
                gi.snapshot_offsetYPixel,
                gi.orientation,
                gi.snaked
            FROM GridInfo gi
                INNER JOIN DataCollectionGroup dcg ON gi.dataCollectionGroupId = dcg.dataCollectionGroupId
                INNER JOIN Session_has_Person shp ON dcg.sessionId = shp.sessionId
                INNER JOIN Person per ON per.personId = shp.personId
            WHERE per.login = p_authLogin AND gi.dataCollectionGroupId = p_dcgId
            GROUP BY gi.gridInfoId,
                gi.dx_mm,
                gi.dy_mm,
                gi.steps_x,
                gi.steps_y,
                gi.meshAngle,
                gi.pixelsPerMicronX,
                gi.pixelsPerMicronY,
                gi.snapshot_offsetXPixel,
                gi.snapshot_offsetYPixel,
                gi.orientation,
                gi.snaked
            ORDER BY gi.gridInfoId ASC;
        ELSE         
            SELECT
                gi.gridInfoId,
                gi.dx_mm,
                gi.dy_mm,
                gi.steps_x,
                gi.steps_y,
                gi.meshAngle,
                gi.pixelsPerMicronX,
                gi.pixelsPerMicronY,
                gi.snapshot_offsetXPixel,
                gi.snapshot_offsetYPixel,
                gi.orientation,
                gi.snaked
            FROM GridInfo gi
            WHERE gi.dataCollectionGroupId = p_dcgId
            ORDER BY gi.gridInfoId ASC;
        END IF;
    ELSE
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument p_dcgId is NULL';
    END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_grid_info_for_dc_ids` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_grid_info_for_dc_ids`(IN p_dcIds TEXT)
    READS SQL DATA
    COMMENT 'Return multi-row result-set with dc ID, grid info and some addit'
BEGIN
    IF NOT (p_dcIds IS NULL) THEN
      SELECT
        dc.datacollectionid,
        gi.dx_mm,
        gi.dy_mm,
        gi.steps_x,
        gi.steps_y,
        gi.pixelsPerMicronX,
        gi.pixelsPerMicronY,
        gi.snapshot_offsetXPixel,
        gi.snapshot_offsetYPixel,
        gi.orientation,
        gi.snaked,
        dc.beamSizeAtSampleX,
        dc.beamSizeAtSampleY,
        dc.imageDirectory,
        dc.imagePrefix,
        dc.imageSuffix,
        dc.fileTemplate,
        dc.xtalSnapshotFullPath1,
        dc.xtalSnapshotFullPath2,
        dc.xtalSnapshotFullPath3,
        dc.xtalSnapshotFullPath4
    FROM GridInfo gi
      INNER JOIN DataCollection dc ON dc.dataCollectionGroupId = gi.dataCollectionGroupId
    WHERE FIND_IN_SET(dc.dataCollectionId, p_dcIds);
    ELSE
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument p_dcIds is NULL';
    END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_lcs_for_session` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_lcs_for_session`(p_proposal_code varchar(5), p_proposal_number int, p_session_number int)
    READS SQL DATA
BEGIN
    IF p_proposal_code IS NOT NULL AND p_proposal_number IS NOT NULL AND p_session_number IS NOT NULL THEN
      SELECT per.title, per.givenName, per.familyName, per.login, shp.role
      FROM Person per 
        INNER JOIN Session_has_Person shp on shp.personId = per.personId
        INNER JOIN BLSession bs on bs.sessionId = shp.sessionId
        INNER JOIN Proposal p on p.proposalId = bs.proposalId
	  WHERE p.proposalCode = p_proposal_code AND p.proposalNumber = p_proposal_number AND bs.visit_number = p_session_number AND shp.role like 'Local Contact%';
    ELSE
	  SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory arguments p_proposalCode + p_proposalNumber + p_sessionNumber can not be NULL';
	END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_most_recent_session` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_most_recent_session`(IN p_beamline varchar(15), IN p_proposal_code varchar(5))
    READS SQL DATA
    COMMENT 'Returns a single-row result-set with the session (mx12345-123), its start and end dates\nfor beamline p_beamline and proposal code p_proposal_code (e.g. cm, mx, nt, in, ee)'
BEGIN
    SELECT concat(p.proposalCode, p.proposalNumber, '-', bs.visit_number) `session`, bs.startDate, bs.endDate
    FROM Proposal p
      INNER JOIN BLSession bs on p.proposalId = bs.proposalId
	WHERE p.proposalCode = p_proposal_code AND bs.beamlinename = p_beamline AND bs.visit_number <> 0 AND now() > bs.startDate
    ORDER BY bs.startDate DESC
    LIMIT 1;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_pdbs_for_component` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_pdbs_for_component`(IN p_componentId int unsigned)
    READS SQL DATA
    COMMENT 'Return multi-row result set with PDB columns for component p_com'
BEGIN
    IF NOT (p_componentId IS NULL) THEN
		SELECT pdb.pdbId "pdbId", pdb.name "name", pdb.contents "contents", pdb.code "code"
        FROM PDB pdb
          INNER JOIN Protein_has_PDB php ON pdb.pdbId = php.pdbId
        WHERE php.proteinId = p_componentId
        ORDER BY pdb.pdbId;
    ELSE
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument is NULL: p_componentId';
    END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_persons_for_proposal` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_persons_for_proposal`(p_proposal_code varchar(5), p_proposal_number int)
    READS SQL DATA
    COMMENT 'Returns a multi-row result-set with info about the persons for \n'
BEGIN
    IF p_proposal_code IS NOT NULL AND p_proposal_number IS NOT NULL THEN
      SELECT per.title, per.givenName, per.familyName, per.login, php.role
      FROM Person per 
        INNER JOIN ProposalHasPerson php on php.personId = per.personId
        INNER JOIN Proposal p on p.proposalId = php.proposalId
	  WHERE p.proposalCode = p_proposal_code AND p.proposalNumber = p_proposal_number;
    ELSE
	  SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory arguments p_proposalCode + p_proposalNumber can not be NULL';
	END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_persons_for_session` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_persons_for_session`(p_proposal_code varchar(5), p_proposal_number int, p_visit_number int)
    READS SQL DATA
    COMMENT 'Returns a multi-row result-set with info about the persons for\nsession identified by p_proposal_code, p_proposal_number, p_visit_number'
BEGIN
    IF p_proposal_code IS NOT NULL AND p_proposal_number IS NOT NULL AND p_visit_number IS NOT NULL THEN
      SELECT per.title, per.givenName, per.familyName, per.login, shp.role, shp.remote
      FROM Person per
        INNER JOIN Session_has_Person shp on shp.personId = per.personId
        INNER JOIN BLSession bs on bs.sessionId = shp.sessionId
        INNER JOIN Proposal p on p.proposalId = bs.proposalId
	  WHERE p.proposalCode = p_proposal_code AND p.proposalNumber = p_proposal_number AND bs.visit_number = p_visit_number;
    ELSE
	  SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory arguments p_proposalCode + p_proposalNumber + p_visit_number can not be NULL';
	END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_processing_job` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_processing_job`(p_id int unsigned)
    READS SQL DATA
    COMMENT 'Returns a single-row result-set with info about the processing j'
BEGIN
    IF p_id IS NOT NULL THEN
      SELECT dataCollectionId "dataCollectionId", displayName "displayName", comments "comments", 
        recordTimestamp "recordTimestamp", recipe "recipe", automatic "automatic"
      FROM ProcessingJob  
	  WHERE processingJobId = p_id
      LIMIT 1;
    ELSE
	  SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory arguments p_id can not be NULL';
	END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_processing_job_image_sweeps` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_processing_job_image_sweeps`(p_id int unsigned)
    READS SQL DATA
    COMMENT 'Returns a multi-row result-set with sweep info for the given pro'
BEGIN
    IF p_id IS NOT NULL THEN
      SELECT processingJobImageSweepId "sweepId", dataCollectionId "dataCollectionId", startImage "startImage", endImage "endImage"
      FROM ProcessingJobImageSweep  
	  WHERE processingJobId = p_id
      ORDER BY processingJobImageSweepId ASC
      LIMIT 1000;
    ELSE
	  SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory arguments p_id can not be NULL';
	END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_processing_job_image_sweeps_v2` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_processing_job_image_sweeps_v2`(p_id int unsigned, p_authLogin varchar(45))
    READS SQL DATA
    COMMENT 'Returns a multi-row result-set with sweep info for the given processing job ID'
BEGIN
    IF p_id IS NOT NULL THEN
        IF p_authLogin IS NOT NULL THEN
            SELECT pjs.processingJobImageSweepId "sweepId", pjs.dataCollectionId "dataCollectionId", pjs.startImage "startImage", pjs.endImage "endImage"
            FROM ProcessingJobImageSweep pjs
                INNER JOIN ProcessingJob pj ON pj.processingJobId = pjp.processingJobId
                INNER JOIN DataCollection dc ON dc.dataCollectionId = pj.dataCollectionId
                INNER JOIN DataCollectionGroup dcg ON dcg.dataCollectionGroupId = dc.dataCollectionGroupId
                INNER JOIN Session_has_Person shp ON shp.sessionId = dcg.sessionId
                INNER JOIN Person per ON per.personId = shp.personId 
	        WHERE pjs.processingJobId = p_id AND per.login = p_authLogin
            GROUP BY pjs.processingJobImageSweepId, pjs.dataCollectionId, pjs.startImage, pjs.endImage
            ORDER BY pjs.processingJobImageSweepId ASC
            LIMIT 1000;
        ELSE
            SELECT pjs.processingJobImageSweepId "sweepId", pjs.dataCollectionId "dataCollectionId", pjs.startImage "startImage", pjs.endImage "endImage"
            FROM ProcessingJobImageSweep pjs  
	        WHERE pjs.processingJobId = p_id
            ORDER BY pjs.processingJobImageSweepId ASC
            LIMIT 1000;
        END IF;
    ELSE
	  SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory arguments p_id can not be NULL';
	END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_processing_job_parameters` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_processing_job_parameters`(p_id int unsigned)
    READS SQL DATA
    COMMENT 'Returns a multi-row result-set (max 1000) with parameters for th'
BEGIN
    IF p_id IS NOT NULL THEN
      SELECT processingJobParameterId "parameterId", parameterKey "parameterKey", parameterValue "parameterValue"
      FROM ProcessingJobParameter  
	  WHERE processingJobId = p_id
      ORDER BY processingJobParameterId ASC
      LIMIT 1000;
    ELSE
	  SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory arguments p_id can not be NULL';
	END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_processing_job_parameters_v2` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_processing_job_parameters_v2`(p_id int unsigned, p_authLogin varchar(45))
    READS SQL DATA
    COMMENT 'Returns a multi-row result-set (max 1000) with parameters for the given processing job ID'
BEGIN
    IF p_id IS NOT NULL THEN
        IF p_authLogin IS NOT NULL THEN
            SELECT pjp.processingJobParameterId "parameterId", pjp.parameterKey "parameterKey", pjp.parameterValue "parameterValue"
            FROM ProcessingJobParameter pjp 
                INNER JOIN ProcessingJob pj ON pj.processingJobId = pjp.processingJobId
                INNER JOIN DataCollection dc ON dc.dataCollectionId = pj.dataCollectionId
                INNER JOIN DataCollectionGroup dcg ON dcg.dataCollectionGroupId = dc.dataCollectionGroupId
                INNER JOIN Session_has_Person shp ON shp.sessionId = dcg.sessionId
                INNER JOIN Person per ON per.personId = shp.personId 
	        WHERE pjp.processingJobId = p_id AND per.login = p_authLogin
            GROUP BY pjp.processingJobParameterId, pjp.parameterKey, pjp.parameterValue 
            ORDER BY pjp.processingJobParameterId ASC
            LIMIT 1000;
        ELSE
            SELECT pjp.processingJobParameterId "parameterId", pjp.parameterKey "parameterKey", pjp.parameterValue "parameterValue"
            FROM ProcessingJobParameter pjp 
	        WHERE pjp.processingJobId = p_id
            ORDER BY pjp.processingJobParameterId ASC
            LIMIT 1000;
        END IF;
    ELSE
	  SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory arguments p_id can not be NULL';
	END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_processing_job_v2` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_processing_job_v2`(p_id int unsigned, p_authLogin varchar(45))
    READS SQL DATA
    COMMENT 'Returns a single-row result-set with info about the processing job for the given ID'
BEGIN
    IF p_id IS NOT NULL THEN
        IF p_authLogin IS NOT NULL THEN
            SELECT pj.dataCollectionId "dataCollectionId", pj.displayName "displayName", pj.comments "comments",
                pj.recordTimestamp "recordTimestamp", pj.recipe "recipe", pj.automatic "automatic"
            FROM ProcessingJob pj
                INNER JOIN DataCollection dc ON dc.dataCollectionId = pj.dataCollectionId
                INNER JOIN DataCollectionGroup dcg ON dcg.dataCollectionGroupId = dc.dataCollectionGroupId
                INNER JOIN Session_has_Person shp ON shp.sessionId = dcg.sessionId
                INNER JOIN Person per ON per.personId = shp.personId 
	        WHERE pj.processingJobId = p_id AND per.login = p_authLogin
            LIMIT 1;
        ELSE
            SELECT pj.dataCollectionId "dataCollectionId", pj.displayName "displayName", pj.comments "comments",
                pj.recordTimestamp "recordTimestamp", pj.recipe "recipe", pj.automatic "automatic"
            FROM ProcessingJob pj
	        WHERE pj.processingJobId = p_id
            LIMIT 1;
        END IF;
    ELSE
	  SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory arguments p_id can not be NULL';
	END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_processing_programs_for_job_id` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_processing_programs_for_job_id`(p_id int unsigned)
    READS SQL DATA
    COMMENT 'Returns a multi-row result-set with processing program instances for the given processing job ID'
BEGIN
    IF p_id IS NOT NULL THEN
      SELECT autoProcProgramId "id", processingCommandLine "commandLine", processingPrograms "programs",
          processingStatus "status", processingMessage "message", processingStartTime "startTime",
          processingEndTime "endTime", processingEnvironment "environment",
          recordTimeStamp "recordTimeStamp", processingJobId "jobId"
      FROM AutoProcProgram  
	  WHERE processingJobId = p_id
      ORDER BY autoProcProgramId ASC
      LIMIT 1000;
    ELSE
	  SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument p_id can not be NULL';
	END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_processing_programs_for_job_id_v2` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_processing_programs_for_job_id_v2`(p_id int unsigned, p_authLogin varchar(45))
    READS SQL DATA
    COMMENT 'Returns a multi-row result-set with processing program instances for the given processing job ID'
BEGIN
    IF p_id IS NOT NULL THEN
        IF p_authLogin IS NOT NULL THEN
            SELECT app.autoProcProgramId "id", app.processingCommandLine "commandLine", app.processingPrograms "programs",
                app.processingStatus "status", app.processingMessage "message", app.processingStartTime "startTime",
                app.processingEndTime "endTime", app.processingEnvironment "environment",
                app.recordTimeStamp "recordTimeStamp", app.processingJobId "jobId"
            FROM AutoProcProgram app  
                INNER JOIN ProcessingJob pj ON pj.processingJobId = app.processingJobId
                INNER JOIN DataCollection dc ON dc.dataCollectionId = pj.dataCollectionId
                INNER JOIN DataCollectionGroup dcg ON dcg.dataCollectionGroupId = dc.dataCollectionGroupId
                INNER JOIN Session_has_Person shp ON shp.sessionId = dcg.sessionId
                INNER JOIN Person per ON per.personId = shp.personId 
	        WHERE app.processingJobId = p_id AND per.login = p_authLogin
            GROUP BY app.autoProcProgramId, app.processingCommandLine, app.processingPrograms,
                app.processingStatus, app.processingMessage, app.processingStartTime,
                app.processingEndTime, app.processingEnvironment,
                app.recordTimeStamp, app.processingJobId
            ORDER BY app.autoProcProgramId ASC
            LIMIT 1000;
        ELSE
            SELECT app.autoProcProgramId "id", app.processingCommandLine "commandLine", app.processingPrograms "programs",
                app.processingStatus "status", app.processingMessage "message", app.processingStartTime "startTime",
                app.processingEndTime "endTime", app.processingEnvironment "environment",
                app.recordTimeStamp "recordTimeStamp", app.processingJobId "jobId"
            FROM AutoProcProgram app  
	        WHERE app.processingJobId = p_id
            ORDER BY app.autoProcProgramId ASC
            LIMIT 1000;
        END IF;
    ELSE
	  SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument p_id can not be NULL';
	END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_processing_program_attachments_for_dc_group_and_program` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_processing_program_attachments_for_dc_group_and_program`(p_id int unsigned, p_program varchar(255))
    READS SQL DATA
    COMMENT 'Returns a multi-row result-set with the processing program attachments for the given DC group ID'
BEGIN
    IF p_id IS NOT NULL AND p_program IS NOT NULL THEN
      SELECT dc.dataCollectionId, app.autoProcProgramId,
        app.processingStatus,
        concat('[', group_concat(json_object('fileType', appa.fileType, 'fullFilePath', concat(appa.filePath, '/', appa.fileName))), ']') "processingAttachments"
      FROM DataCollection dc
        INNER JOIN AutoProcIntegration api
          ON api.dataCollectionId = dc.dataCollectionId
        INNER JOIN AutoProcProgram app
          ON app.autoProcProgramId = api.autoProcProgramId
        INNER JOIN AutoProcProgramAttachment appa
          ON appa.autoProcProgramId = api.autoProcProgramId
      WHERE
        dc.dataCollectionGroupId = p_id AND app.processingPrograms = p_program
      GROUP BY
        dc.dataCollectionId, app.autoProcProgramId, app.processingStatus;
    ELSE
	    SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644,
        MESSAGE_TEXT='Mandatory arguments p_id and p_program can not be NULL';
	END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_processing_program_attachments_for_dc_group_program_v2` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_processing_program_attachments_for_dc_group_program_v2`(
    p_id int unsigned, 
    p_program varchar(255),
    p_authLogin varchar(45)
)
    READS SQL DATA
    COMMENT 'Returns a multi-row result-set with the processing program attachments for the given DC group ID'
BEGIN
    IF p_id IS NOT NULL AND p_program IS NOT NULL THEN
        IF p_authLogin IS NOT NULL THEN
            SELECT dc.dataCollectionId, app.autoProcProgramId,
                app.processingStatus,
                concat('[', group_concat(json_object('fileType', appa.fileType, 'fullFilePath', concat(appa.filePath, '/', appa.fileName))), ']') "processingAttachments"
            FROM DataCollection dc
                INNER JOIN AutoProcIntegration api ON api.dataCollectionId = dc.dataCollectionId
                INNER JOIN AutoProcProgram app ON app.autoProcProgramId = api.autoProcProgramId
                INNER JOIN AutoProcProgramAttachment appa ON appa.autoProcProgramId = api.autoProcProgramId
                INNER JOIN DataCollectionGroup dcg ON dcg.dataCollectionGroupId = dc.dataCollectionGroupId
                INNER JOIN Session_has_Person shp ON shp.sessionId = dcg.sessionId
                INNER JOIN Person per ON per.personId = shp.personId 
            WHERE
                dc.dataCollectionGroupId = p_id AND app.processingPrograms = p_program AND per.login = p_authLogin
            GROUP BY
                dc.dataCollectionId, app.autoProcProgramId, app.processingStatus;
        ELSE 
            SELECT dc.dataCollectionId, app.autoProcProgramId,
                app.processingStatus,
                concat('[', group_concat(json_object('fileType', appa.fileType, 'fullFilePath', concat(appa.filePath, '/', appa.fileName))), ']') "processingAttachments"
            FROM DataCollection dc
                INNER JOIN AutoProcIntegration api ON api.dataCollectionId = dc.dataCollectionId
                INNER JOIN AutoProcProgram app ON app.autoProcProgramId = api.autoProcProgramId
                INNER JOIN AutoProcProgramAttachment appa ON appa.autoProcProgramId = api.autoProcProgramId
            WHERE
                dc.dataCollectionGroupId = p_id AND app.processingPrograms = p_program
            GROUP BY
                dc.dataCollectionId, app.autoProcProgramId, app.processingStatus;
        END IF;
    ELSE
	    SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644,
        MESSAGE_TEXT='Mandatory arguments p_id and p_program can not be NULL';
	END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_processing_program_attachments_for_program_id` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_processing_program_attachments_for_program_id`(p_id int unsigned)
    READS SQL DATA
    COMMENT 'Returns a multi-row result-set with the processing program attachments for the given processing program id'
BEGIN
    IF p_id IS NOT NULL THEN
      SELECT
        appa.autoProcProgramAttachmentId "attachmentId", appa.fileType "fileType", appa.filePath "filePath", appa.fileName "fileName"
      FROM AutoProcProgramAttachment appa
      WHERE appa.autoProcProgramId = p_id;
    ELSE
	    SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644,
        MESSAGE_TEXT='Mandatory argument p_id can not be NULL';
	END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_processing_program_attachments_for_program_id_v2` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_processing_program_attachments_for_program_id_v2`(
    p_id int unsigned,	
    p_authLogin varchar(45)
)
    READS SQL DATA
    COMMENT 'Returns a multi-row result-set with the processing program attachments for the given processing program id'
BEGIN
    IF p_id IS NOT NULL THEN
        IF p_authLogin IS NOT NULL THEN
            SELECT
                appa.autoProcProgramAttachmentId "attachmentId", appa.fileType "fileType", appa.filePath "filePath", appa.fileName "fileName"
            FROM AutoProcProgramAttachment appa
                INNER JOIN AutoProcProgram app ON app.autoProcProgramId = appa.autoProcProgramId
                INNER JOIN ProcessingJob pj ON pj.processingJobId = app.processingJobId
                INNER JOIN DataCollection dc ON dc.dataCollectionId = pj.dataCollectionId
                INNER JOIN DataCollectionGroup dcg ON dcg.dataCollectionGroupId = dc.dataCollectionGroupId
                INNER JOIN Session_has_Person shp ON shp.sessionId = dcg.sessionId
                INNER JOIN Person per ON per.personId = shp.personId 
            WHERE appa.autoProcProgramId = p_id AND per.login = p_authLogin
            GROUP BY appa.autoProcProgramAttachmentId, appa.fileType, appa.filePath, appa.fileName;
        ELSE
            SELECT
                appa.autoProcProgramAttachmentId "attachmentId", appa.fileType "fileType", appa.filePath "filePath", appa.fileName "fileName"
            FROM AutoProcProgramAttachment appa
            WHERE appa.autoProcProgramId = p_id;
        END IF;
    ELSE
	    SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument p_id can not be NULL';
	END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_proposal_title` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_proposal_title`(p_proposal_code varchar(5), p_proposal_number int, p_authLogin varchar(45))
    READS SQL DATA
    COMMENT 'Returns a single-row, single-column result set with the title of the proposal p_proposal_code + p_proposal_number'
BEGIN

    IF p_authLogin IS NOT NULL THEN
    

      SELECT pr.title
      FROM Proposal pr
        INNER JOIN BLSession bs ON pr.proposalid = bs.proposalid 
        INNER JOIN Session_has_Person shp ON bs.sessionId = shp.sessionId
        INNER JOIN Person p ON p.personId = shp.personId
	    WHERE p.login = p_authLogin AND pr.proposalCode = p_proposal_code AND pr.proposalNumber = p_proposal_number
      LIMIT 1;

    ELSE 

      SELECT title
      FROM Proposal 
	    WHERE proposalCode = p_proposal_code AND proposalNumber = p_proposal_number
      LIMIT 1;

    END IF;

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_reprocessing_by_dc` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_reprocessing_by_dc`(
     p_dcId int(11) unsigned 
)
    READS SQL DATA
    COMMENT 'Retrieves reprocessing requests for a data collection (p_dcId).'
BEGIN
	IF NOT p_dcId IS NULL THEN

		SELECT r.reprocessingId "id", r.displayName, r.status, r.comments, r.recordTimestamp, 
        r.startedTimestamp, r.lastUpdateTimestamp, r.lastUpdateMessage,
		rp.reprocessingParameterId "paramId", rp.parameterKey, rp.parameterValue
        FROM Reprocessing r
          LEFT OUTER JOIN ReprocessingParameter rp ON rp.reprocessingId = r.reprocessingId
        WHERE r.dataCollectionId = p_dcId
        ORDER BY r.recordTimestamp;

        SELECT ris.reprocessingId "id", ris.reprocessingImageSweepId "sweepId", ris.dataCollectionId "sweepDCId", 
        ris.startImage, ris.endImage 
        FROM Reprocessing r
		  INNER JOIN ReprocessingImageSweep ris ON ris.reprocessingId = r.reprocessingId
        WHERE r.dataCollectionId = p_dcId
        ORDER BY r.recordTimestamp;
    ELSE
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument p_dcId is NULL';
    END IF;

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_samples_assigned_for_proposal` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_samples_assigned_for_proposal`(IN p_proposalCode varchar(3), IN p_proposalNumber int)
    READS SQL DATA
    COMMENT 'Retrieve the user friendly name and ID of all assigned instances'
BEGIN
    IF NOT (p_proposalCode IS NULL) AND NOT (p_proposalNumber IS NULL) THEN
        SELECT bls.blSampleId "sampleId", bls.containerId "containerId", bls.name "sampleName", bls.code "sampleCode", bls.comments "sampleComments", bls.location "sampleLocation",
          bls.packingFraction "samplePackingFraction", bls.dimension1 "dimension1", bls.dimension2 "dimension2", bls.dimension3 "dimension3", 
          bls.shape "shape",
          cr.crystalId "sampleTypeId", cr.name "sampleTypeName", cr.comments "sampleTypeComments", cr.spaceGroup "sampleTypeSpaceGroup",
          dp.diffractionPlanId "dcPlanId", dp.name "dcPlanName"
        FROM BLSample bls
          INNER JOIN BLSample_has_DataCollectionPlan bhd on bls.blSampleId = bhd.blSampleId
          INNER JOIN DiffractionPlan dp on bhd.dataCollectionPlanId = dp.diffractionPlanId
          INNER JOIN Container c on c.containerId = bls.containerId
          INNER JOIN Crystal cr on cr.crystalId = bls.crystalId
          INNER JOIN Protein prot on prot.proteinId = cr.proteinId
          INNER JOIN Proposal p on p.proposalId = prot.proposalId
        WHERE
          p.proposalCode = p_proposalCode AND p_proposalNumber = p.proposalNumber AND c.containerStatus = 'processing'
        ORDER BY
          bls.blSampleId ASC;
    ELSE
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='One or more mandatory arguments are NULL: p_proposalCode, p_proposalNumber';
    END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_samples_for_sample_group` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_samples_for_sample_group`(IN p_sampleGroupId int unsigned)
    READS SQL DATA
    COMMENT 'Return multi-row result set with sample IDs, order in the group'
BEGIN
    IF NOT (p_sampleGroupId IS NULL) THEN
		SELECT bls.blSampleId "sampleId", bls.containerId "containerId", bls.crystalId "sampleTypeId", bls.name "sampleName",
		  bls.code "sampleCode", bls.comments "sampleComments", bls.location "sampleLocation", 
          bls.packingFraction "samplePackingFraction", 
          bls.dimension1 "dimension1", bls.dimension2 "dimension2", bls.dimension3 "dimension3", 
          bls.shape "shape",
          c.name "sampleTypeName", c.comments "sampleTypeComments", c.spaceGroup "sampleTypeSpaceGroup", c.proteinId "componentId",
          bhb.type "typeInGroup", bhb.groupOrder "orderInGroup"
        FROM BLSampleGroup_has_BLSample bhb 
          INNER JOIN BLSample bls ON bls.blSampleId = bhb.blSampleId 
          INNER JOIN Crystal c ON c.crystalId = bls.crystalId
        WHERE bhb.blSampleGroupId = p_sampleGroupId
        ORDER BY bhb.blSampleId;
    ELSE
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument is NULL: p_sampleGroupId';
    END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_samples_not_loaded_for_container_reg_barcode` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_samples_not_loaded_for_container_reg_barcode`(p_barcode varchar(20))
BEGIN
  IF NOT (p_barcode IS NULL) THEN

    WITH most_recent_container AS (
      SELECT max(c.containerId) as containerId
      FROM Container c
        INNER JOIN ContainerRegistry cr USING(containerRegistryId)
      WHERE cr.barcode=p_barcode
    )
    SELECT bls.blSampleId "sampleId",
      bls.containerId "containerId",
      bls.name "sampleName",
      bls.code "sampleCode",
      bls.comments "sampleComments",
      bls.location "sampleLocation",
      max(ra.robotActionId) as rId
    FROM BLSample bls
      INNER JOIN most_recent_container mrc ON bls.containerId = mrc.containerId
      LEFT OUTER JOIN RobotAction ra ON bls.blSampleId = ra.blSampleId
    GROUP BY bls.blSampleId,
      bls.containerId,
      bls.name,
      bls.code,
      bls.comments,
      bls.location
    HAVING rId IS NULL
    ORDER BY bls.blSampleId;
  ELSE
    SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument is NULL: p_barcode';
  END IF;

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_sample_for_container_id_and_location` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_sample_for_container_id_and_location`(IN p_containerId int(11) unsigned, p_location varchar(45))
    READS SQL DATA
    COMMENT 'Return single-row result set with info about a BLSample identified by p_containerId and p_location'
BEGIN
    IF NOT (p_containerId IS NULL OR p_location IS NULL) THEN
      SELECT bls.blSampleId "sampleId",
        bls.name "sampleName",
        bls.code "sampleCode",
        bls.comments "sampleComments",
        bls.location "sampleLocation"
      FROM BLSample bls
      WHERE bls.location = p_location AND bls.containerId = p_containerId
      LIMIT 1;
    ELSE
      SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument(s) are NULL: p_containerId and/or p_location';
    END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_sample_groups_for_sample` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_sample_groups_for_sample`(IN p_sampleId int unsigned)
    READS SQL DATA
    COMMENT 'Return multi-row result-set with sample group IDs, order in the'
BEGIN
    IF NOT (p_sampleId IS NULL) THEN
        SELECT blSampleGroupId "sampleGroupId", groupOrder "order", `type` 
        FROM BLSampleGroup_has_BLSample 
        WHERE blSampleId=p_sampleId;
	ELSE
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument p_sampleId is NULL';
    END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_sample_type_for_sample` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_sample_type_for_sample`(IN p_sampleId int unsigned)
    READS SQL DATA
    COMMENT 'Return single-row result set with sample type columns for sample'
BEGIN
    IF NOT (p_sampleId IS NULL) THEN
		SELECT c.crystalId "sampleTypeId", c.proteinId "componentId", c.name "name", c.comments "comments"
        FROM Crystal c
          INNER JOIN BLSample bls ON c.crystalId = bls.crystalId
        WHERE bls.blSampleId = p_sampleId
        ORDER BY c.crystalId;
    ELSE
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument is NULL: p_sampleId';
    END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_sessions_for_beamline_and_run` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_sessions_for_beamline_and_run`(
  IN p_beamline varchar(15),
  IN p_run varchar(7)
)
    READS SQL DATA
    COMMENT 'Returns a multi-row result-set with the sessions (mx12345-123), their start and end dates for beamline p_beamline and run p_run'
BEGIN
  SELECT
      bs.sessionId "sessionId",
      concat(p.proposalCode, p.proposalNumber, '-', bs.visit_number) "session",
      bs.startDate "startDate",
      bs.endDate "endDate"
  FROM Proposal p
      INNER JOIN BLSession bs on p.proposalId = bs.proposalId
      INNER JOIN v_run vr ON bs.startDate BETWEEN vr.startDate AND vr.endDate
	WHERE bs.beamlinename = p_beamline AND vr.run = p_run
  ORDER BY bs.startDate, bs.sessionId;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_sessions_for_person_login` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_sessions_for_person_login`(p_login varchar(45))
    READS SQL DATA
    COMMENT 'Returns a multi-row result-set with info about the sessions associated with a person with login=p_login'
BEGIN
    IF p_login IS NOT NULL THEN
      SELECT bs.sessionId "id", bs.proposalId "proposalId",
        bs.startDate "startDate", bs.endDate "endDate",
        bs.beamlineName "beamline", pr.proposalCode "proposalCode", pr.proposalNumber "proposalNumber", bs.visit_number "sessionNumber",
        bs.comments "comments",
        shp.role "personRoleOnSession", shp.remote "personRemoteOnSession"
      FROM BLSession bs
        INNER JOIN Session_has_Person shp ON shp.sessionId = bs.sessionId
        INNER JOIN Person p ON p.personId = shp.personId
        INNER JOIN Proposal pr ON pr.proposalId = bs.proposalId
	    WHERE p.login = p_login
      ORDER BY bs.startDate;
    ELSE
	    SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument p_login can not be NULL';
	  END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_session_id` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_session_id`(p_session varchar(15), OUT p_id int)
    READS SQL DATA
BEGIN
    SELECT max(bs.sessionid) into p_id 
    FROM Proposal p INNER JOIN BLSession bs ON p.proposalid = bs.proposalid 
    WHERE concat(p.proposalcode, p.proposalnumber, '-', bs.visit_number) = p_session;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_session_id_v2` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_session_id_v2`(p_session varchar(15), p_authLogin varchar(45))
    READS SQL DATA
    COMMENT 'Returns the session ID (an integer) for p_session (e.g. mx12345-123)'
BEGIN

    IF p_authLogin IS NOT NULL THEN
    

      SELECT max(bs.sessionid) 
      FROM Proposal p 
        INNER JOIN BLSession bs ON p.proposalid = bs.proposalid 
        INNER JOIN Session_has_Person shp ON bs.sessionId = shp.sessionId
        INNER JOIN Person per ON per.personId = shp.personId
      WHERE per.login = p_authLogin AND concat(p.proposalcode, p.proposalnumber, '-', bs.visit_number) = p_session;

    ELSE 

      SELECT max(bs.sessionid) 
      FROM Proposal p 
        INNER JOIN BLSession bs ON p.proposalid = bs.proposalid 
      WHERE concat(p.proposalcode, p.proposalnumber, '-', bs.visit_number) = p_session;

    END IF;

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_sleeve` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_sleeve`(p_id tinyint unsigned)
BEGIN
  IF NOT (p_id IS NULL) THEN
    SELECT sleeveId "id", location "location", lastMovedToFreezer "lastMovedToFreezer", lastMovedFromFreezer "lastMovedFromFreezer"
    FROM Sleeve
    WHERE sleeveId = p_id;
  ELSE
    SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument is NULL: p_id must be non-NULL.';

  END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_sleeves` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_sleeves`()
BEGIN
    SELECT sleeveId "id", location "location", lastMovedToFreezer "lastMovedToFreezer", lastMovedFromFreezer "lastMovedFromFreezer"
    FROM Sleeve;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `retrieve_test` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `retrieve_test`()
    COMMENT 'For testing the connection'
BEGIN
  SELECT now() as "curr_ts", '2016-10-07 14:02:58' as "curr_ts2", '2' as "2_1", 2 as "2_2", '2.0' as "20_1", 2.0 as "20_2";
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `update_container_assign` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE PROCEDURE `update_container_assign`(IN p_beamline varchar(20), IN p_registry_barcode varchar(45), IN p_position int)
    MODIFIES SQL DATA
    COMMENT 'Toggles "assign" status of container (p_barcode).\nSets the s.c. position and beamline.\nIf assigned then: 1) Also assign its dewar and shipping. 2) Unassigns other containers in the same proposal on that beamline and s.c. position.\nIf unassign then:\n'
BEGIN
    DECLARE row_containerId int(10) unsigned DEFAULT NULL;
    DECLARE row_containerStatus varchar(45) DEFAULT NULL;
    DECLARE currentContainerStatus varchar(45) DEFAULT NULL;
    DECLARE row_dewarId int(10) unsigned DEFAULT NULL;
    DECLARE row_beamlineLocation varchar(20) DEFAULT NULL;
    DECLARE row_sampleChangerLocation varchar(20) DEFAULT NULL;
    DECLARE row_proposalId int(10) unsigned DEFAULT NULL;
    DECLARE row_queuedCount int(11) unsigned DEFAULT NULL;

    IF NOT (p_registry_barcode IS NULL) THEN
        START TRANSACTION;

        SELECT c.containerId, c.containerStatus, c.dewarId, c.beamlineLocation, c.sampleChangerLocation, s.proposalId, count(*)
          INTO row_containerId, row_containerStatus, row_dewarId, row_beamlineLocation, row_sampleChangerLocation, row_proposalId, row_queuedCount
        FROM Container c
            INNER JOIN ContainerRegistry cr ON c.containerRegistryId = cr.containerRegistryId
            INNER JOIN Dewar d ON d.dewarId = c.dewarId
            INNER JOIN Shipping s ON s.shippingId = d.shippingId
            LEFT OUTER JOIN ContainerQueue cq ON cq.containerId = c.containerId
        WHERE cr.barcode = p_registry_barcode
        GROUP BY c.containerId, c.containerStatus, c.dewarId, c.beamlineLocation, c.sampleChangerLocation, s.proposalId
        ORDER BY c.containerId DESC
        LIMIT 1;

        SELECT row_containerStatus INTO currentContainerStatus;

        
        IF NOT row_containerId IS NULL THEN
          IF (NOT row_containerStatus <=> 'processing') OR (row_beamlineLocation = p_beamline AND row_sampleChangerLocation = p_position) THEN

            
            UPDATE Container c
              INNER JOIN Dewar d ON d.dewarId = c.dewarId
              INNER JOIN Shipping s ON s.shippingId = d.shippingId
            SET
              c.sampleChangerLocation = IF(row_containerStatus<=>'processing', '', p_position),
              c.beamlineLocation = p_beamline,
              c.containerStatus = IF(row_containerStatus<=>'processing', 'at facility', 'processing'),
              d.dewarStatus = IF(row_containerStatus<=>'processing', d.dewarStatus, 'processing'),
              d.storageLocation = IF(row_containerStatus<=>'processing', d.storageLocation, p_beamline),
              s.shippingStatus = IF(row_containerStatus<=>'processing', s.shippingStatus, 'processing')
            WHERE
              c.containerId = row_containerId;

            SELECT IF(row_containerStatus<=>'processing', 'at facility', 'processing') INTO currentContainerStatus;

            IF NOT row_containerStatus <=> 'processing' THEN
              
              
              UPDATE Container c
                INNER JOIN Dewar d ON d.dewarId = c.dewarId
                INNER JOIN Shipping s ON s.shippingId = d.shippingId
              SET c.containerStatus = 'at facility',
                c.sampleChangerLocation = ''
              WHERE s.proposalId = row_proposalId AND c.beamlineLocation = p_beamline AND
                c.sampleChangerLocation = p_position AND c.containerId <> row_containerId;

              
              INSERT INTO DewarTransportHistory (dewarId, dewarStatus, storageLocation, arrivalDate)
                VALUES (row_dewarId, 'processing', p_beamline, NOW());
            END IF;

            
            INSERT INTO ContainerHistory (containerId, location, status, beamlineName)
              VALUES (row_containerId, p_position, IF(row_containerStatus<=>'processing', 'at facility', 'processing'), p_beamline);
          END IF;
        ELSE
          SIGNAL SQLSTATE '02000' SET MYSQL_ERRNO=1643, MESSAGE_TEXT='Container with p_registry_barcode not found';
        END IF;

        COMMIT;
    ELSE
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument p_registry_barcode is NULL';
    END IF;
    SELECT row_containerId as "containerId",
      currentContainerStatus as "containerStatus",
      row_queuedCount as "queuedCount";
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `update_container_ls_position` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `update_container_ls_position`(IN p_barcode varchar(45), IN p_position int)
    MODIFIES SQL DATA
    COMMENT 'Updates container sampleChangerLocation for barcode = p_barcode,'
BEGIN
	IF NOT (p_barcode IS NULL) THEN
	  UPDATE Container
      SET sampleChangerLocation = p_position
      WHERE barcode = p_barcode;

	  
    ELSE
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument p_barcode is NULL';
    END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `update_container_status` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `update_container_status`(IN p_barcode varchar(45), IN p_status varchar(45))
    MODIFIES SQL DATA
    COMMENT 'Set container containerStatus = p_status for barcode = p_barcode'
BEGIN
  DECLARE row_containerId int(11) unsigned DEFAULT NULL;
  DECLARE row_scLoc varchar(20) DEFAULT NULL;
   
  IF NOT (p_barcode IS NULL) AND p_status IN ('in_storage', 'in_localstorage', 'processing', 'disposed', 
	'in_transit_to_localstorage', 'in_transit_to_storage', 'in_transit_loading', 'in_transit_unloading') THEN

	SELECT containerId, sampleChangerLocation INTO row_containerId, row_scLoc 
    FROM Container 
    WHERE barcode = p_barcode;

	IF row_containerId is not NULL THEN
		UPDATE Container
		SET containerStatus = p_status 
		WHERE containerId = row_containerId;

		INSERT INTO ContainerHistory (containerId, location, status, beamlineName) VALUES (row_containerId, row_scLoc, p_status, 'i02-2');

	END IF;
    ELSEIF p_barcode IS NULL THEN
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument p_barcode is NULL';
    ELSE
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument p_status does not have a valid value';
  END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `update_container_unassign_all_for_beamline` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE PROCEDURE `update_container_unassign_all_for_beamline`(IN p_beamline varchar(20))
    MODIFIES SQL DATA
    COMMENT 'Unassigns all containers on a given beamline one by one by calling update_container_assign on each.'
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE row_registry_barcode VARCHAR(20);
    DECLARE row_position VARCHAR(20);
    DECLARE cur CURSOR FOR SELECT cr.barcode, c.sampleChangerLocation  
        FROM Container c
            INNER JOIN ContainerRegistry cr ON cr.containerRegistryId = c.containerRegistryId
            INNER JOIN BLSession bs ON bs.sessionId = c.sessionId
        WHERE bs.beamlineName = p_beamline AND c.containerStatus = 'processing';
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    IF NOT (p_beamline IS NULL) THEN
        OPEN cur;
        call_loop: LOOP
            FETCH cur INTO row_registry_barcode, row_position;
            IF done THEN
                LEAVE call_loop;
            END IF;
            CALL update_container_assign(p_beamline, row_registry_barcode, row_position);
        END LOOP;
        CLOSE cur;
    ELSE
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument p_beamline is NULL';
    END IF;

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `update_dc_experiment` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES' */ ;
DELIMITER ;;
CREATE PROCEDURE `update_dc_experiment`(
     p_id int(11) unsigned,
     p_slitGapVertical float,
     p_slitGapHorizontal float,
     p_transmission float,
     p_exposureTime float,
     p_xBeam float,
     p_yBeam float,
     p_axisStart float,
     p_axisEnd float,
     p_axisRange float,
     p_overlap float,
     p_flux double,
     p_fluxEnd double,
     p_rotationAxis varchar(10),
     p_phiStart float,
     p_kappaStart float,
     p_omegaStart float,
     p_wavelength float,                                                
     p_resolution float,
     p_detectorDistance float,
     p_bestWilsonPlotPath varchar(255),
     p_beamSizeAtSampleX float,
     p_beamSizeAtSampleY float,
     p_focalSpotSizeAtSampleX float,
     p_focalSpotSizeAtSampleY float,
     p_apertureSizeX float
)
    MODIFIES SQL DATA
BEGIN
	DECLARE row_apertureId int(11) unsigned;
    
	UPDATE DataCollection SET 
		slitGapVertical=IFNULL(p_slitGapVertical, imagedirectory),
		slitGapHorizontal=IFNULL(p_slitGapHorizontal, imagedirectory),
		transmission=IFNULL(p_transmission, imagedirectory),
		exposureTime=IFNULL(p_exposureTime, imagedirectory),
		xBeam=IFNULL(p_xBeam, xBeam),
		yBeam=IFNULL(p_yBeam, yBeam),
		axisStart=IFNULL(p_axisStart, axisStart),
		axisEnd=IFNULL(p_axisEnd, axisEnd),
		axisRange=IFNULL(p_axisRange, axisRange),
		overlap=IFNULL(p_overlap, overlap),
		flux=IFNULL(p_flux, flux),
		flux_end=IFNULL(p_fluxEnd, flux_end),
		rotationAxis=IFNULL(p_rotationAxis, rotationAxis),
		phiStart=IFNULL(p_phiStart, phiStart),
		kappaStart=IFNULL(p_kappaStart, kappaStart),
		omegaStart=IFNULL(p_omegaStart, omegaStart),
		wavelength=IFNULL(p_wavelength, wavelength),
		resolution=IFNULL(p_resolution, resolution),
		detectorDistance=IFNULL(p_detectorDistance, detectorDistance),
		bestWilsonPlotPath=IFNULL(p_bestWilsonPlotPath, bestWilsonPlotPath),
		beamSizeAtSampleX=IFNULL(p_beamSizeAtSampleX, beamSizeAtSampleX),
		beamSizeAtSampleY=IFNULL(p_beamSizeAtSampleY, beamSizeAtSampleY),
		focalSpotSizeAtSampleX=IFNULL(p_focalSpotSizeAtSampleX, focalSpotSizeAtSampleX),
		focalSpotSizeAtSampleY=IFNULL(p_focalSpotSizeAtSampleY, focalSpotSizeAtSampleY)
	WHERE dataCollectionId = p_id;

	SELECT apertureId INTO row_apertureId 
    FROM DataCollection 
    WHERE dataCollectionId = p_id;

	IF row_apertureId IS NOT NULL THEN
		UPDATE Aperture SET 
			sizeX = IFNULL(p_apertureSizeX, sizeX) 
		WHERE apertureId = row_apertureId;
	END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `update_dc_experiment_v2` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES' */ ;
DELIMITER ;;
CREATE PROCEDURE `update_dc_experiment_v2`(
     p_id int(11) unsigned,
     p_slitGapVertical float,
     p_slitGapHorizontal float,
     p_transmission float,
     p_exposureTime float,
     p_xBeam float,
     p_yBeam float,
     p_axisStart float,
     p_axisEnd float,
     p_axisRange float,
     p_overlap float,
     p_flux double,
     p_fluxEnd double,
     p_rotationAxis varchar(10),
     p_phiStart float,
     p_kappaStart float,
     p_omegaStart float,
     p_wavelength float,                                                
     p_resolution float,
     p_detectorDistance float,
     p_detector2Theta float,
     p_bestWilsonPlotPath varchar(255),
     p_beamSizeAtSampleX float,
     p_beamSizeAtSampleY float,
     p_focalSpotSizeAtSampleX float,
     p_focalSpotSizeAtSampleY float,
     p_apertureSizeX float
)
    MODIFIES SQL DATA
BEGIN
	DECLARE row_apertureId int(11) unsigned;
    
	UPDATE DataCollection SET 
		slitGapVertical=IFNULL(p_slitGapVertical, imagedirectory),
		slitGapHorizontal=IFNULL(p_slitGapHorizontal, imagedirectory),
		transmission=IFNULL(p_transmission, imagedirectory),
		exposureTime=IFNULL(p_exposureTime, imagedirectory),
		xBeam=IFNULL(p_xBeam, xBeam),
		yBeam=IFNULL(p_yBeam, yBeam),
		axisStart=IFNULL(p_axisStart, axisStart),
		axisEnd=IFNULL(p_axisEnd, axisEnd),
		axisRange=IFNULL(p_axisRange, axisRange),
		overlap=IFNULL(p_overlap, overlap),
		flux=IFNULL(p_flux, flux),
		flux_end=IFNULL(p_fluxEnd, flux_end),
		rotationAxis=IFNULL(p_rotationAxis, rotationAxis),
		phiStart=IFNULL(p_phiStart, phiStart),
		kappaStart=IFNULL(p_kappaStart, kappaStart),
		omegaStart=IFNULL(p_omegaStart, omegaStart),
		wavelength=IFNULL(p_wavelength, wavelength),
		resolution=IFNULL(p_resolution, resolution),
		detectorDistance=IFNULL(p_detectorDistance, detectorDistance),
		detector2Theta=IFNULL(p_detector2Theta, detector2Theta),
		bestWilsonPlotPath=IFNULL(p_bestWilsonPlotPath, bestWilsonPlotPath),
		beamSizeAtSampleX=IFNULL(p_beamSizeAtSampleX, beamSizeAtSampleX),
		beamSizeAtSampleY=IFNULL(p_beamSizeAtSampleY, beamSizeAtSampleY),
		focalSpotSizeAtSampleX=IFNULL(p_focalSpotSizeAtSampleX, focalSpotSizeAtSampleX),
		focalSpotSizeAtSampleY=IFNULL(p_focalSpotSizeAtSampleY, focalSpotSizeAtSampleY)
	WHERE dataCollectionId = p_id;

	SELECT apertureId INTO row_apertureId 
    FROM DataCollection 
    WHERE dataCollectionId = p_id;

	IF row_apertureId IS NOT NULL THEN
		UPDATE Aperture SET 
			sizeX = IFNULL(p_apertureSizeX, sizeX) 
		WHERE apertureId = row_apertureId;
	END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `update_dc_machine` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES' */ ;
DELIMITER ;;
CREATE PROCEDURE `update_dc_machine`(
     p_id int(11) unsigned,
	 p_synchrotronMode varchar(20),
     p_undulatorGap1 float,
     p_undulatorGap2 float,
     p_undulatorGap3 float
)
    MODIFIES SQL DATA
BEGIN
	IF p_id IS NOT NULL THEN
		UPDATE DataCollection SET 
			synchrotronMode=IFNULL(p_synchrotronMode, synchrotronMode),
			undulatorGap1=IFNULL(p_undulatorGap1, undulatorGap1),
			undulatorGap2=IFNULL(p_undulatorGap2, undulatorGap2),
			undulatorGap3=IFNULL(p_undulatorGap3, undulatorGap3)
		WHERE 
			dataCollectionId = p_id;
	END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `update_dc_position` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `update_dc_position`(
     p_dcId int(11) unsigned, 
     p_posX double,
     p_posY double,
     p_posZ double,
     p_scale double
)
    MODIFIES SQL DATA
    COMMENT 'Sets the Position for the data collection (p_id).'
BEGIN
	DECLARE row_position_id int(11) unsigned DEFAULT NULL;
	IF p_dcId IS NOT NULL THEN
		SELECT positionId INTO row_position_id FROM DataCollection WHERE dataCollectionId = p_dcId;
        INSERT INTO Position (positionId, posX, posY, posZ, scale)
          VALUES (row_position_id, p_posX, p_posY, p_posZ, p_scale)
          ON DUPLICATE KEY UPDATE
		  posX = IFNULL(p_posX, posX),
		  posY = IFNULL(p_posY, posY),
		  posZ = IFNULL(p_posZ, posZ),
          scale = IFNULL(p_scale, scale);
	    IF LAST_INSERT_ID() <> 0 THEN 
          UPDATE DataCollection SET positionId = LAST_INSERT_ID() WHERE dataCollectionId = p_dcId;
        END IF;
	ELSE
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument p_dcId is NULL';  
    END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `update_processing_program_for_id_range` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE PROCEDURE `update_processing_program_for_id_range`(p_startId int unsigned, p_endId int unsigned)
    MODIFIES SQL DATA
    COMMENT 'Maintenance procedure to update processingPrograms based on contents of processingCommandLine'
BEGIN
  UPDATE AutoProcProgram
  SET AutoProcProgram.processingPrograms = CONCAT(
    'xia2 ',
    REGEXP_REPLACE(
      processingCommandLine,
      '^xia2.*?(-|pipeline=)(2d[[:alnum:]]*|3d[[:alnum:]]*|dials)[[:space:]]*.*',
      '\\2'
    )
  )
  WHERE autoProcProgramId BETWEEN p_startId AND p_endId AND
          AutoProcProgram.processingPrograms = 'xia2';
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `update_reprocessing_status` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `update_reprocessing_status`(
     p_id int(11) unsigned,
	 p_status  enum('submitted', 'running', 'finished', 'failed'), 
     p_startedTimeStamp timestamp, 
     p_lastUpdateMessage varchar(80)
)
    MODIFIES SQL DATA
    COMMENT 'Updates the reprocessing status'
BEGIN
	IF NOT p_id IS NULL THEN
      UPDATE Reprocessing SET 
	   `status` = p_status,
       startedTimeStamp = p_startedTimeStamp, 
       lastUpdateTimeStamp = current_timestamp, 
       lastUpdateMessage = p_lastUpdateMessage
      WHERE reprocessingId = p_id;
    ELSE
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument p_id is NULL';
    END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `update_session_archived` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE PROCEDURE `update_session_archived`(
    IN p_proposalCode varchar(3), 
    IN p_proposalNumber int, 
    IN p_sessionNumber int,
    IN p_archived boolean)
    MODIFIES SQL DATA
    COMMENT 'Updates the session `archived` column for session specified by p_proposalCode, p_proposalNumber, p_sessionNumber'
BEGIN
	IF NOT (p_proposalCode IS NULL) AND NOT (p_proposalNumber IS NULL) AND NOT (p_sessionNumber IS NULL) THEN
	    UPDATE BLSession bs
            INNER JOIN Proposal p USING(proposalId)
        SET bs.archived = p_archived
        WHERE p.proposalCode = p_proposalCode AND p.proposalNumber = p_proposalNumber AND bs.visit_number =  p_sessionNumber;
    ELSE
        SIGNAL SQLSTATE '45000' 
        SET MYSQL_ERRNO=1644, 
            MESSAGE_TEXT='Mandatory arguments p_proposalCode, p_proposalNumber int, p_sessionNumber must be non-NULL';
    END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `update_session_paths` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `update_session_paths`(
  p_proposalCode varchar(3),
  p_proposalNumber int(10),
  p_sessionNumber int(10),
  p_oldRoot varchar(255),
  p_newRoot varchar(255)
)
    MODIFIES SQL DATA
    COMMENT 'Attempts to update the root (the leftmost part) of all paths related to session \np_proposalCode + p_proposalNumber + p_sessionNumber from p_oldRoot to p_newRoot.\nNOTE:\nWe assume that p_oldRoot and p_newRoot both contain a trailing "/"'
BEGIN
  DECLARE row_session_id int(10) unsigned DEFAULT NULL;
  DECLARE row_proposal_id int(10) unsigned DEFAULT NULL;
  DECLARE row_sample_id int(10) unsigned DEFAULT NULL;
        
  IF p_proposalCode IS NOT NULL AND p_proposalNumber IS NOT NULL AND p_sessionNumber IS NOT NULL THEN
      SELECT max(bs.sessionid), p.proposalId INTO row_session_id, row_proposal_id 
      FROM Proposal p INNER JOIN BLSession bs ON p.proposalid = bs.proposalid 
      WHERE p.proposalCode = p_proposalCode AND p.proposalNumber = p_proposalNumber AND bs.visit_number = p_sessionNumber;

      IF row_session_id IS NOT NULL AND row_proposal_id IS NOT NULL THEN


        UPDATE DataCollection dc
          INNER JOIN DataCollectionGroup dcg on dcg.dataCollectionGroupId = dc.dataCollectionGroupId 
        SET 
          imageDirectory = root_replace(imageDirectory, p_oldRoot, p_newRoot),
          xtalSnapshotFullPath1 = root_replace(xtalSnapshotFullPath1, p_oldRoot, p_newRoot), 
          xtalSnapshotFullPath2 = root_replace(xtalSnapshotFullPath2, p_oldRoot, p_newRoot), 
          xtalSnapshotFullPath3 = root_replace(xtalSnapshotFullPath3, p_oldRoot, p_newRoot),
          xtalSnapshotFullPath4 = root_replace(xtalSnapshotFullPath4, p_oldRoot, p_newRoot),
          datFullPath = root_replace(datFullPath, p_oldRoot, p_newRoot)
        WHERE 
          dcg.sessionId = row_session_id;


        UPDATE DataCollectionFileAttachment dcfa
		  INNER JOIN DataCollection dc on dc.dataCollectionId = dcfa.datacollectionId
          INNER JOIN DataCollectionGroup dcg on dcg.dataCollectionGroupId = dc.dataCollectionGroupId 
        SET 
          fileFullPath = root_replace(fileFullPath, p_oldRoot, p_newRoot)
        WHERE 
          dcg.sessionId = row_session_id;
          

	UPDATE XFEFluorescenceSpectrum 
	SET 
          jpegScanFileFullPath = root_replace(jpegScanFileFullPath, p_oldRoot, p_newRoot), 
          annotatedPymcaXfeSpectrum = root_replace(annotatedPymcaXfeSpectrum, p_oldRoot, p_newRoot),
          fittedDataFileFullPath = root_replace(fittedDataFileFullPath, p_oldRoot, p_newRoot),
          scanFileFullPath = root_replace(scanFileFullPath, p_oldRoot, p_newRoot),
          workingDirectory = root_replace(workingDirectory, p_oldRoot, p_newRoot)
	WHERE 
          sessionId = row_session_id;
          

	UPDATE EnergyScan
	SET 
          scanFileFullPath = root_replace(scanFileFullPath, p_oldRoot, p_newRoot), 
          jpegChoochFileFullPath = root_replace(jpegChoochFileFullPath, p_oldRoot, p_newRoot),
          filename = root_replace(filename, p_oldRoot, p_newRoot),
          choochFileFullPath = root_replace(choochFileFullPath, p_oldRoot, p_newRoot),
          workingDirectory = root_replace(workingDirectory, p_oldRoot, p_newRoot)
	WHERE 
          sessionId = row_session_id;


	UPDATE PhasingProgramAttachment ppa
          INNER JOIN Phasing p on p.phasingProgramRunId = ppa.phasingProgramRunId
          INNER JOIN Phasing_has_Scaling phs on phs.phasingAnalysisId = p.phasingAnalysisId
          INNER JOIN AutoProcScaling_has_Int apshi on apshi.autoProcScalingId = phs.autoProcScalingId
          INNER JOIN AutoProcIntegration api on api.autoProcIntegrationId = apshi.autoProcIntegrationId
          INNER JOIN DataCollection dc on dc.dataCollectionId = api.dataCollectionId
          INNER JOIN DataCollectionGroup dcg on dcg.dataCollectionGroupId = dc.dataCollectionGroupId 
	SET
          filePath = root_replace(filePath, p_oldRoot, p_newRoot)
        WHERE
          dcg.sessionId = row_session_id;  


        UPDATE AutoProcProgramAttachment appa
          INNER JOIN AutoProcIntegration api on api.autoProcProgramId = appa.autoProcProgramId
          INNER JOIN DataCollection dc on dc.dataCollectionId = api.dataCollectionId
          INNER JOIN DataCollectionGroup dcg on dcg.dataCollectionGroupId = dc.dataCollectionGroupId
        SET
          filePath = root_replace(filePath, p_oldRoot, p_newRoot)
        WHERE
          dcg.sessionId = row_session_id;


        UPDATE MXMRRun mr
          INNER JOIN AutoProcScaling_has_Int apshi on mr.autoProcScalingId = apshi.autoProcScalingId 
          INNER JOIN AutoProcIntegration api on api.autoProcIntegrationId = apshi.autoProcIntegrationId 
          INNER JOIN DataCollection dc on dc.dataCollectionId = api.datacollectionId
          INNER JOIN DataCollectionGroup dcg on dcg.dataCollectionGroupId = dc.dataCollectionGroupId
        SET
          inputCoordFile = root_replace(inputCoordFile, p_oldRoot, p_newRoot),
          outputCoordFile = root_replace(outputCoordFile, p_oldRoot, p_newRoot),
          inputMTZFile = root_replace(inputMTZFile, p_oldRoot, p_newRoot),
          outputMTZFile = root_replace(outputMTZFile, p_oldRoot, p_newRoot),
          runDirectory = root_replace(runDirectory, p_oldRoot, p_newRoot),
          logFile = root_replace(logFile, p_oldRoot, p_newRoot)
        WHERE
          dcg.sessionId = row_session_id;


        UPDATE MXMRRunBlob mrb
          INNER JOIN MXMRRun mr on mrb.mxMRRunId = mr.mxMRRunId
          INNER JOIN AutoProcScaling_has_Int apshi on mr.autoProcScalingId = apshi.autoProcScalingId 
          INNER JOIN AutoProcIntegration api on api.autoProcIntegrationId = apshi.autoProcIntegrationId 
          INNER JOIN DataCollection dc on dc.dataCollectionId = api.datacollectionId
          INNER JOIN DataCollectionGroup dcg on dcg.dataCollectionGroupId = dc.dataCollectionGroupId
        SET
          view1 = root_replace(view1, p_oldRoot, p_newRoot),
          view2 = root_replace(view2, p_oldRoot, p_newRoot),
          view3 = root_replace(view3, p_oldRoot, p_newRoot)
        WHERE
          dcg.sessionId = row_session_id;


        UPDATE BLSampleImage blsi
          INNER JOIN BLSample bls on blsi.blsampleId = bls.blsampleId
          INNER JOIN Container c on c.containerId = bls.containerId
		SET
          imageFullPath = root_replace(imageFullPath, p_oldRoot, p_newRoot)
        WHERE 
          c.sessionId = row_session_id;


        UPDATE BLSampleImageAnalysis blsia
          INNER JOIN BLSampleImage blsi on blsia.blSampleImageId = blsi.blSampleImageId
          INNER JOIN BLSample bls on blsi.blsampleId = bls.blsampleId
          INNER JOIN Container c on c.containerId = bls.containerId
		SET
          imageFullPath = root_replace(imageFullPath, p_oldRoot, p_newRoot)
        WHERE 
          c.sessionId = row_session_id;

      ELSE
        
		SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1643, MESSAGE_TEXT='Corresponding rows for p_proposalCode + p_proposalNumber + p_sessionNumber not found';
      END IF;
  END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `upsert_ctf` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `upsert_ctf`(
  INOUT p_ctfId int(11) unsigned,
  p_motionCorrectionId int(11) unsigned,
  p_autoProcProgramId int(11) unsigned,
  p_boxSizeX float,
  p_boxSizeY float,
  p_minResolution float,
  p_maxResolution float,
  p_minDefocus float,
  p_maxDefocus float,
  p_defocusStepSize float,
  p_astigmatism float,
  p_astigmatismAngle float,
  p_estimatedResolution float,
  p_estimatedDefocus float,
  p_amplitudeContrast float,
  p_ccValue float,
  p_fftTheoreticalFullPath varchar(255),
  p_comments varchar(255)
)
    MODIFIES SQL DATA
BEGIN
    INSERT INTO CTF (ctfId, motionCorrectionId, autoProcProgramId, boxSizeX, boxSizeY, minResolution, maxResolution, minDefocus, maxDefocus, defocusStepSize, astigmatism, astigmatismAngle, estimatedResolution, estimatedDefocus, amplitudeContrast, ccValue, fftTheoreticalFullPath, comments)
      VALUES (p_ctfId, p_motionCorrectionId, p_autoProcProgramId, p_boxSizeX, p_boxSizeY, p_minResolution, p_maxResolution, p_minDefocus, p_maxDefocus, p_defocusStepSize, p_astigmatism, p_astigmatismAngle, p_estimatedResolution, p_estimatedDefocus, p_amplitudeContrast, p_ccValue, p_fftTheoreticalFullPath, p_comments)
      ON DUPLICATE KEY UPDATE
        ctfId = IFNULL(p_ctfId, ctfId),
        motionCorrectionId = IFNULL(p_motionCorrectionId, motionCorrectionId),
        autoProcProgramId = IFNULL(p_autoProcProgramId, autoProcProgramId),
        boxSizeX = IFNULL(p_boxSizeX, boxSizeX),
        boxSizeY = IFNULL(p_boxSizeY, boxSizeY),
        minResolution = IFNULL(p_minResolution, minResolution),
        maxResolution = IFNULL(p_maxResolution, maxResolution),
        minDefocus = IFNULL(p_minDefocus, minDefocus),
        maxDefocus = IFNULL(p_maxDefocus, maxDefocus),
        defocusStepSize = IFNULL(p_defocusStepSize, defocusStepSize),
        astigmatism = IFNULL(p_astigmatism, astigmatism),
        astigmatismAngle = IFNULL(p_astigmatismAngle, astigmatismAngle),
        estimatedResolution = IFNULL(p_estimatedResolution, estimatedResolution),
        estimatedDefocus = IFNULL(p_estimatedDefocus, estimatedDefocus),
        amplitudeContrast = IFNULL(p_amplitudeContrast, amplitudeContrast),
        ccValue = IFNULL(p_ccValue, ccValue),
        fftTheoreticalFullPath = IFNULL(p_fftTheoreticalFullPath, fftTheoreticalFullPath),
        comments = IFNULL(p_comments, comments);

        IF p_ctfId IS NULL THEN
            SET p_ctfId = LAST_INSERT_ID();
        END IF;
   END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `upsert_dc` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE PROCEDURE `upsert_dc`(
     INOUT p_id int(11) unsigned,
     p_dcgId int(11) unsigned,
     p_sessionId int(11) unsigned,
     p_sampleId int(11) unsigned,
     p_detectorid int(11) unsigned,
     p_positionid int(11) unsigned,
     p_apertureid int(11) unsigned,
     p_datacollectionNumber int(10) unsigned,
     p_starttime datetime,
     p_endtime datetime,
     p_runStatus varchar(45),
     p_axisStart float,
     p_axisEnd float,
     p_axisRange float,
     p_overlap float,
     p_numberOfImages int(10) unsigned,
     p_startImageNumber int(10) unsigned,
     p_numberOfPasses int(10) unsigned,
     p_exposureTime float,
     p_imageDirectory varchar(255),
     p_imagePrefix varchar(45),
     p_imageSuffix varchar(45),
     p_imageContainerSubPath varchar(255),
     p_fileTemplate varchar(255),
     p_wavelength float,
     p_resolution float,
     p_detectorDistance float,
     p_xbeam float,
     p_ybeam float,
     p_comments varchar(1024),
     p_slitgapVertical float,
     p_slitgapHorizontal float,
     p_transmission float,
     p_synchrotronMode varchar(20),
     p_xtalSnapshotFullPath1 varchar(255),
     p_xtalSnapshotFullPath2 varchar(255),
     p_xtalSnapshotFullPath3 varchar(255),
     p_xtalSnapshotFullPath4 varchar(255),
     p_rotationAxis enum('Omega','Kappa','Phi'),
     p_phistart float,
     p_kappastart float,
     p_omegastart float,
     p_resolutionAtCorner float,
     p_detector2theta float,
     p_undulatorGap1 float,
     p_undulatorGap2 float,
     p_undulatorGap3 float,
     p_beamSizeAtSampleX float,
     p_beamSizeAtSampleY float,
     p_averageTemperature float,
     p_actualCenteringPosition varchar(255),
     p_beamShape varchar(45),
     p_focalSpotSizeAtSampleX float,
     p_focalSpotSizeAtSampleY float,
     p_polarisation float,
     p_flux float,

     p_processedDataFile varchar(255),
     p_datFullPath varchar(255),
     p_magnification int(11),
     p_totalAbsorbedDose float,
     p_binning tinyint(1), 
     p_particleDiameter float, 
     p_boxSize_CTF float,
     p_minResolution float, 
     p_minDefocus float, 
     p_maxDefocus float, 
     p_defocusStepSize float, 
     p_amountAstigmatism float, 
     p_extractSize float, 
     p_bgRadius float, 
     p_voltage float,
     p_objAperture float,
     p_c1aperture float,
     p_c2aperture float,
     p_c3aperture float,
     p_c1lens float,
     p_c2lens float,
     p_c3lens float
)
    MODIFIES SQL DATA
    COMMENT 'Inserts or updates info about a data collection (p_id).\nMandatory columns:\nFor insert: p_dcgId\nFor update: p_id \nReturns: Record ID in p_id.'
BEGIN
    IF p_id IS NOT NULL OR p_dcgId IS NOT NULL THEN

      INSERT INTO DataCollection (datacollectionId, datacollectiongroupid,
        sessionId, blsampleId, detectorid, positionid, apertureid,
        datacollectionNumber, starttime, endtime, runStatus, axisStart,
        axisEnd, axisRange, overlap, numberOfImages, startImageNumber,
        numberOfPasses, exposureTime, imageDirectory, imagePrefix, imageSuffix,
        imageContainerSubPath, fileTemplate, wavelength, resolution,
        detectorDistance, xbeam, ybeam, comments,slitgapVertical,
        slitgapHorizontal, transmission, synchrotronMode,
        xtalSnapshotFullPath1, xtalSnapshotFullPath2, xtalSnapshotFullPath3,
        xtalSnapshotFullPath4, rotationAxis, phistart,
        kappastart, omegastart, resolutionAtCorner, detector2theta,
        undulatorGap1, undulatorGap2, undulatorGap3, beamSizeAtSampleX,
        beamSizeAtSampleY, averageTemperature, actualCenteringPosition,
        beamShape, focalSpotSizeAtSampleX, focalSpotSizeAtSampleY,
        polarisation, flux, processedDataFile, datFullPath, magnification,
        totalAbsorbedDose, binning, particleDiameter, boxSize_CTF,
        minResolution, minDefocus, maxDefocus, defocusStepSize,
        amountAstigmatism, extractSize, bgRadius, voltage, objAperture,
        c1aperture, c2aperture, c3aperture, c1lens, c2lens, c3lens
      )
      VALUES (p_Id, p_dcgId, p_sessionId, p_sampleId, p_detectorid, p_positionid, p_apertureid, p_datacollectionNumber, p_starttime, p_endtime,
      p_runStatus, p_axisStart, p_axisEnd, p_axisRange, p_overlap, p_numberOfImages, p_startImageNumber, p_numberOfPasses, p_exposureTime, p_imageDirectory, p_imagePrefix, p_imageSuffix, p_imageContainerSubPath, p_fileTemplate,
      p_wavelength, p_resolution, p_detectorDistance, p_xbeam, p_ybeam, p_comments, p_slitgapVertical, p_slitgapHorizontal, p_transmission, p_synchrotronMode,
      p_xtalSnapshotFullPath1, p_xtalSnapshotFullPath2, p_xtalSnapshotFullPath3, p_xtalSnapshotFullPath4, p_rotationAxis, p_phistart, p_kappastart, p_omegastart, p_resolutionAtCorner, p_detector2theta,
      p_undulatorGap1, p_undulatorGap2, p_undulatorGap3, p_beamSizeAtSampleX, p_beamSizeAtSampleY, p_averageTemperature, p_actualCenteringPosition, p_beamShape,
      p_focalSpotSizeAtSampleX, p_focalSpotSizeAtSampleY, p_polarisation, p_flux,
      p_processedDataFile, p_datFullPath, p_magnification, p_totalAbsorbedDose, p_binning, p_particleDiameter, p_boxSize_CTF, p_minResolution, p_minDefocus, p_maxDefocus, p_defocusStepSize,
      p_amountAstigmatism, p_extractSize, p_bgRadius, p_voltage, p_objAperture, p_c1aperture, p_c2aperture, p_c3aperture, p_c1lens, p_c2lens, p_c3lens
      )
      ON DUPLICATE KEY UPDATE
		    dataCollectionGroupId = IFNULL(p_dcgId, dataCollectionGroupId),
        sessionId = IFNULL(p_sessionId, sessionId),
        blsampleId = IFNULL(p_sampleId, blsampleId),
        detectorid = IFNULL(p_detectorid, detectorid),
        positionid = IFNULL(p_positionid, positionid),
        apertureid = IFNULL(p_apertureid, apertureid),
        datacollectionNumber = IFNULL(p_datacollectionNumber, datacollectionNumber),
        starttime = IFNULL(p_starttime, starttime),
        endtime = IFNULL(p_endtime, endtime),
        runStatus = IFNULL(p_runStatus, runStatus),
        axisStart = IFNULL(p_axisStart, axisStart),
        axisEnd = IFNULL(p_axisEnd, axisEnd),
        axisRange = IFNULL(p_axisRange, axisRange),
        overlap = IFNULL(p_overlap, overlap),
        numberOfImages = IFNULL(p_numberOfImages, numberOfImages),
        startImageNumber = IFNULL(p_startImageNumber, startImageNumber),
        numberOfPasses = IFNULL(p_numberOfPasses, numberOfPasses),
        exposureTime = IFNULL(p_exposureTime, exposureTime),
        imagedirectory = IFNULL(p_imageDirectory, imagedirectory),
        imageprefix = IFNULL(p_imagePrefix, imageprefix),
        imagesuffix = IFNULL(p_imageSuffix, imagesuffix),
        imageContainerSubPath = IFNULL(p_imageContainerSubPath, imageContainerSubPath),
        fileTemplate = IFNULL(p_fileTemplate, fileTemplate),
        wavelength = IFNULL(p_wavelength, wavelength),
        resolution = IFNULL(p_resolution, resolution),
        detectorDistance = IFNULL(p_detectorDistance, detectorDistance),
        xbeam = IFNULL(p_xbeam, xbeam),
        ybeam = IFNULL(p_ybeam, ybeam),
        comments = IFNULL(p_comments, comments),
        slitgapVertical = IFNULL(p_slitgapVertical, slitgapVertical),
        slitgapHorizontal = IFNULL(p_slitgapHorizontal, slitgapHorizontal),
        transmission = IFNULL(p_transmission, transmission),
        synchrotronMode = IFNULL(p_synchrotronMode, synchrotronMode),
        xtalSnapshotFullPath1 = IFNULL(p_xtalSnapshotFullPath1, xtalSnapshotFullPath1),
        xtalSnapshotFullPath2 = IFNULL(p_xtalSnapshotFullPath2, xtalSnapshotFullPath2),
        xtalSnapshotFullPath3 = IFNULL(p_xtalSnapshotFullPath3, xtalSnapshotFullPath3),
        xtalSnapshotFullPath4 = IFNULL(p_xtalSnapshotFullPath4, xtalSnapshotFullPath4),
        rotationAxis = IFNULL(p_rotationAxis, rotationAxis),
        phistart = IFNULL(p_phistart, phistart),
        kappastart = IFNULL(p_kappastart, kappastart),
        omegastart = IFNULL(p_omegastart, omegastart),
        resolutionAtCorner = IFNULL(p_resolutionAtCorner, resolutionAtCorner),
        detector2theta = IFNULL(p_detector2theta, detector2theta),
        undulatorGap1 = IFNULL(p_undulatorGap1, undulatorGap1),
        undulatorGap2 = IFNULL(p_undulatorGap2, undulatorGap2),
        undulatorGap3 = IFNULL(p_undulatorGap3, undulatorGap3),
        beamSizeAtSampleX = IFNULL(p_beamSizeAtSampleX, beamSizeAtSampleX),
        beamSizeAtSampleY = IFNULL(p_beamSizeAtSampleY, beamSizeAtSampleY),
        averageTemperature = IFNULL(p_averageTemperature, averageTemperature),
        actualCenteringPosition = IFNULL(p_actualCenteringPosition, actualCenteringPosition),
        beamShape = IFNULL(p_beamShape, beamShape),
        focalSpotSizeAtSampleX = IFNULL(p_focalSpotSizeAtSampleX, focalSpotSizeAtSampleX),
        focalSpotSizeAtSampleY = IFNULL(p_focalSpotSizeAtSampleY, focalSpotSizeAtSampleY),
        polarisation = IFNULL(p_polarisation, polarisation),
        flux = IFNULL(p_flux, flux),
        processedDataFile = IFNULL(p_processedDataFile, processedDataFile),
        datFullPath = IFNULL(p_datFullPath, datFullPath),
        magnification = IFNULL(p_magnification, magnification),
        totalAbsorbedDose = IFNULL(p_totalAbsorbedDose, totalAbsorbedDose),
        binning = IFNULL(p_binning, binning),
        particleDiameter = IFNULL(p_particleDiameter, particleDiameter),
        boxSize_CTF = IFNULL(p_boxSize_CTF, boxSize_CTF),
        minResolution = IFNULL(p_minResolution, minResolution),
        minDefocus = IFNULL(p_minDefocus, minDefocus),
        maxDefocus = IFNULL(p_maxDefocus, maxDefocus),
        defocusStepSize = IFNULL(p_defocusStepSize, defocusStepSize),
        amountAstigmatism = IFNULL(p_amountAstigmatism, amountAstigmatism),
        extractSize = IFNULL(p_extractSize, extractSize),
        bgRadius = IFNULL(p_bgRadius, bgRadius),
        voltage = IFNULL(p_voltage, voltage),
        objAperture = IFNULL(p_objAperture, objAperture),
        c1aperture = IFNULL(p_c1aperture, c1aperture),
        c2aperture = IFNULL(p_c2aperture, c2aperture),
        c3aperture = IFNULL(p_c3aperture, c3aperture),
        c1lens = IFNULL(p_c1lens, c1lens),
        c2lens = IFNULL(p_c2lens, c2lens),
        c3lens = IFNULL(p_c3lens, c3lens);

	    IF p_id IS NULL THEN
		    SET p_id = LAST_INSERT_ID();
      END IF;
    ELSE
      SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT=
      'Mandatory argument(s) are NULL: p_id OR p_dcgId must be non-NULL.';
    END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `upsert_dcg_grid` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES' */ ;
DELIMITER ;;
CREATE PROCEDURE `upsert_dcg_grid`(
  INOUT p_id int(11) unsigned, 
  p_dcgId int(11) unsigned, 
  p_dxInMm double, 
  p_dyInMm double, 
  p_stepsX double, 
  p_stepsY double, 
  p_meshAngle double, 
  p_pixelsPerMicronX float, 
  p_pixelsPerMicronY float, 
  p_snapshotOffsetXPixel float, 
  p_snapshotOffsetYPixel float, 
  p_orientation enum('vertical','horizontal'), 
  p_snaked boolean
)
    MODIFIES SQL DATA
BEGIN
	IF p_dcgId IS NOT NULL THEN
      INSERT INTO GridInfo (gridInfoId, dataCollectionGroupId, dx_mm, dy_mm, steps_x, steps_y, meshAngle, pixelsPerMicronX, pixelsPerMicronY, 
        snapshot_offsetXPixel, snapshot_offsetYPixel, orientation, snaked)
        VALUES (p_id, p_dcgId, p_dxInMm, p_dyInMm, p_stepsX, p_stepsY, p_meshAngle, p_pixelsPerMicronX, p_pixelsPerMicronY,
        p_snapshotOffsetXPixel, p_snapshotOffsetYPixel, p_orientation, p_snaked)
        ON DUPLICATE KEY UPDATE
		  dataCollectionGroupId = IFNULL(p_dcgId, dataCollectionGroupId),
		  dx_mm = IFNULL(p_dxInMm, dx_mm),
		  dy_mm = IFNULL(p_dyInMm, dy_mm),
		  steps_x = IFNULL(p_stepsX, steps_x),
		  steps_y = IFNULL(p_stepsY, steps_y),
		  meshAngle = IFNULL(p_meshAngle, meshAngle),
		  pixelsPerMicronX = IFNULL(p_pixelsPerMicronX, pixelsPerMicronX),
		  pixelsPerMicronY = IFNULL(p_pixelsPerMicronY, pixelsPerMicronY),
		  snapshot_offsetXPixel = IFNULL(p_snapshotOffsetXPixel, snapshot_offsetXPixel),
		  snapshot_offsetYPixel = IFNULL(p_snapshotOffsetYPixel, snapshot_offsetYPixel),
		  orientation = IFNULL(p_orientation, orientation),
		  snaked = IFNULL(p_snaked, snaked);
	  IF LAST_INSERT_ID() <> 0 THEN 
		  SET p_id = LAST_INSERT_ID();
      END IF;      
	END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `upsert_dc_file_attachment` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `upsert_dc_file_attachment`(
	 INOUT p_id int(11) unsigned,
     p_dataCollectionId int(11) unsigned,
     p_fileFullPath varchar(255),
     p_fileType varchar(45)
	)
    MODIFIES SQL DATA
    COMMENT 'Inserts or updates info about a file attachmet for a data collection. Returns: The PK value in p_id.'
BEGIN
	IF p_id IS NOT NULL OR p_dataCollectionId IS NOT NULL THEN

      INSERT INTO DataCollectionFileAttachment (dataCollectionFileAttachmentId, dataCollectionId, fileFullPath, fileType) 
        VALUES (p_id, p_dataCollectionId, p_fileFullPath, p_fileType)
	    ON DUPLICATE KEY UPDATE
		  dataCollectionId = IFNULL(p_dataCollectionId, dataCollectionId),
          fileFullPath = IFNULL(p_fileFullPath, fileFullPath),
          fileType = IFNULL(p_fileType, fileType);

	  IF p_id IS NULL THEN 
		  SET p_id = LAST_INSERT_ID();
      END IF;
    ELSE
      SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument is NULL: p_id OR p_dataCollectionId must be non-NULL.';
    END IF;      
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `upsert_dc_group` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `upsert_dc_group`(
	 INOUT p_id int(11) unsigned,
     p_proposalCode varchar(3),
     p_proposalNumber int(10),
     p_sessionNumber int(10),
     p_sampleId int(10) unsigned, 
     p_sampleBarcode varchar(45),
     p_experimenttype varchar(45), 
     p_starttime datetime,
     p_endtime datetime,
     p_crystalClass varchar(20),
     p_detectorMode varchar(255),
     p_actualSampleBarcode varchar(45),
     p_actualSampleSlotInContainer integer(10),
     p_actualContainerBarcode varchar(45),
     p_actualContainerSlotInSC integer(10),
     p_comments varchar(1024)
     )
    MODIFIES SQL DATA
    COMMENT 'Inserts or updates info about data collection group (p_id).\nMand'
BEGIN

	DECLARE row_session_id int(10) unsigned DEFAULT NULL;
	DECLARE row_proposal_id int(10) unsigned DEFAULT NULL;
	DECLARE row_sample_id int(10) unsigned DEFAULT NULL;
        
	IF p_proposalCode IS NOT NULL AND p_proposalNumber IS NOT NULL AND p_sessionNumber IS NOT NULL THEN
      SELECT max(bs.sessionid), p.proposalId INTO row_session_id, row_proposal_id 
      FROM Proposal p INNER JOIN BLSession bs ON p.proposalid = bs.proposalid 
      WHERE p.proposalCode = p_proposalCode AND p.proposalNumber = p_proposalNumber AND bs.visit_number = p_sessionNumber;
      
      IF p_sampleId IS NULL AND p_sampleBarcode IS NOT NULL THEN
        SELECT max(bls.blSampleId) INTO p_sampleId
        FROM BLSample bls
          INNER JOIN Container c on c.containerId = bls.containerId
          INNER JOIN Dewar d on d.dewarId = c.dewarId
          INNER JOIN Shipping s on s.shippingId = d.shippingId
        WHERE bls.code = p_sampleBarcode AND s.proposalId = row_proposal_id;
        
      END IF;
      
      IF p_sampleId IS NULL AND (p_actualContainerBarcode IS NOT NULL) AND (p_actualSampleSlotInContainer IS NOT NULL) THEN
	    SELECT max(bls.blSampleId) INTO p_sampleId
        FROM BLSample bls
          INNER JOIN Container c on c.containerId = bls.containerId
		WHERE c.barcode = p_actualContainerBarcode AND bls.location = p_actualSampleSlotInContainer;
      END IF;
	END IF;

	IF p_id IS NOT NULL OR row_session_id IS NOT NULL THEN

      INSERT INTO DataCollectionGroup (datacollectionGroupId, sessionId, blsampleId, experimenttype, starttime, endtime, crystalClass, detectorMode, 
        actualSampleBarcode, actualSampleSlotInContainer, actualContainerBarcode, actualContainerSlotInSC, comments) 
        VALUES (p_id, row_session_id, p_sampleId, p_experimenttype, p_starttime, p_endtime, p_crystalClass, p_detectorMode, 
        p_actualSampleBarcode, p_actualSampleSlotInContainer, p_actualContainerBarcode, p_actualContainerSlotInSC, p_comments)
	    ON DUPLICATE KEY UPDATE
		  sessionId = IFNULL(row_session_id, sessionId),
          blsampleId = IFNULL(p_sampleId, blsampleId),
          experimenttype = IFNULL(p_experimenttype, experimenttype),
          starttime = IFNULL(p_starttime, starttime),
          endtime = IFNULL(p_endtime, endtime),
          crystalClass = IFNULL(p_crystalClass, crystalClass),
          detectorMode = IFNULL(p_detectorMode, detectorMode),
          actualSampleBarcode = IFNULL(p_actualSampleBarcode, actualSampleBarcode),
          actualSampleSlotInContainer = IFNULL(p_actualSampleSlotInContainer, actualSampleSlotInContainer),
          actualContainerBarcode = IFNULL(p_actualContainerBarcode, actualContainerBarcode),
          actualContainerSlotInSC = IFNULL(p_actualContainerSlotInSC, actualContainerSlotInSC),
          comments = IFNULL(p_comments, comments);

	  IF p_id IS NULL THEN 
		  SET p_id = LAST_INSERT_ID();
      END IF;      
    END IF;
  END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `upsert_dc_group_v2` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `upsert_dc_group_v2`(
	 INOUT p_id int(11) unsigned,
     p_sessionId int(10) unsigned,
     p_proposalCode varchar(3),
     p_proposalNumber int(10),
     p_sessionNumber int(10),
     p_sampleId int(10) unsigned, 
     p_sampleBarcode varchar(45),
     p_experimenttype varchar(45), 
     p_starttime datetime,
     p_endtime datetime,
     p_crystalClass varchar(20),
     p_detectorMode varchar(255),
     p_actualSampleBarcode varchar(45),
     p_actualSampleSlotInContainer integer(10),
     p_actualContainerBarcode varchar(45),
     p_actualContainerSlotInSC integer(10),
     p_comments varchar(1024),
     p_xtalSnapshotFullPath	varchar(255)
     )
    MODIFIES SQL DATA
    COMMENT 'Inserts or updates info about data collection group (p_id).\nMand'
BEGIN
	DECLARE row_proposal_id int(10) unsigned DEFAULT NULL;
	DECLARE row_sample_id int(10) unsigned DEFAULT NULL;

	IF p_sessionId IS NULL AND p_proposalCode IS NOT NULL AND p_proposalNumber IS NOT NULL AND p_sessionNumber IS NOT NULL THEN
      SELECT max(bs.sessionid), p.proposalId INTO p_sessionId, row_proposal_id 
      FROM Proposal p INNER JOIN BLSession bs ON p.proposalid = bs.proposalid 
      WHERE p.proposalCode = p_proposalCode AND p.proposalNumber = p_proposalNumber AND bs.visit_number = p_sessionNumber;
	END IF;

	IF p_id IS NOT NULL OR p_sessionId IS NOT NULL THEN
	  
      IF p_sessionId IS NOT NULL AND p_sampleId IS NULL AND p_sampleBarcode IS NOT NULL THEN
	    IF row_proposal_id IS NULL THEN
          SELECT proposalId INTO row_proposal_id 
          FROM BLSession 
          WHERE sessionId = p_sessionId;
	    END IF;
        SELECT max(bls.blSampleId) INTO p_sampleId
        FROM BLSample bls
		  INNER JOIN Container c on c.containerId = bls.containerId
          INNER JOIN Dewar d on d.dewarId = c.dewarId
          INNER JOIN Shipping s on s.shippingId = d.shippingId
        WHERE bls.code = p_sampleBarcode AND s.proposalId = row_proposal_id;
	  END IF;

	  IF p_sampleId IS NULL AND (p_actualContainerBarcode IS NOT NULL) AND (p_actualSampleSlotInContainer IS NOT NULL) THEN
	    SELECT max(bls.blSampleId) INTO p_sampleId
        FROM BLSample bls
          INNER JOIN Container c on c.containerId = bls.containerId
	    WHERE c.barcode = p_actualContainerBarcode AND bls.location = p_actualSampleSlotInContainer;
      END IF;

      INSERT INTO DataCollectionGroup (datacollectionGroupId, sessionId, blsampleId, experimenttype, starttime, endtime, 
        crystalClass, detectorMode, actualSampleBarcode, actualSampleSlotInContainer, actualContainerBarcode, actualContainerSlotInSC, 
        comments, xtalSnapshotFullPath) 
        VALUES (p_id, p_sessionId, p_sampleId, p_experimenttype, p_starttime, p_endtime, p_crystalClass, p_detectorMode, 
        p_actualSampleBarcode, p_actualSampleSlotInContainer, p_actualContainerBarcode, p_actualContainerSlotInSC, 
        p_comments, p_xtalSnapshotFullPath)
	    ON DUPLICATE KEY UPDATE
		  sessionId = IFNULL(p_sessionId, sessionId),
          blsampleId = IFNULL(p_sampleId, blsampleId),
          experimenttype = IFNULL(p_experimenttype, experimenttype),
          starttime = IFNULL(p_starttime, starttime),
          endtime = IFNULL(p_endtime, endtime),
          crystalClass = IFNULL(p_crystalClass, crystalClass),
          detectorMode = IFNULL(p_detectorMode, detectorMode),
          actualSampleBarcode = IFNULL(p_actualSampleBarcode, actualSampleBarcode),
          actualSampleSlotInContainer = IFNULL(p_actualSampleSlotInContainer, actualSampleSlotInContainer),
          actualContainerBarcode = IFNULL(p_actualContainerBarcode, actualContainerBarcode),
          actualContainerSlotInSC = IFNULL(p_actualContainerSlotInSC, actualContainerSlotInSC),
          comments = IFNULL(p_comments, comments),
          xtalSnapshotFullPath = IFNULL(p_xtalSnapshotFullPath, xtalSnapshotFullPath);

	  IF p_id IS NULL THEN 
		  SET p_id = LAST_INSERT_ID();
      END IF;
    ELSE
      SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument(s) are NULL: p_id OR p_sessionId OR a valid session described by (p_proposalCode and p_proposalNumber and p_sessionNumber) must be non-NULL.';  
    END IF;      
  END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `upsert_dc_group_v3` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE PROCEDURE `upsert_dc_group_v3`(
	 INOUT p_id int(11) unsigned,
     p_sessionId int(10) unsigned,
     p_proposalCode varchar(3),
     p_proposalNumber int(10),
     p_sessionNumber int(10),
     p_sampleId int(10) unsigned,
     p_sampleBarcode varchar(45),
     p_experimenttype varchar(45), 
     p_starttime datetime,
     p_endtime datetime,
     p_crystalClass varchar(20),
     p_detectorMode varchar(255),
     p_actualSampleBarcode varchar(45),
     p_actualSampleSlotInContainer integer(10),
     p_actualContainerBarcode varchar(45),
     p_actualContainerSlotInSC integer(10),
     p_comments varchar(1024),
     p_xtalSnapshotFullPath	varchar(255),
		 p_scanParameters longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin
     )
    MODIFIES SQL DATA
    COMMENT 'Inserts or updates info about data collection group (p_id).\nMandatory columns:\nFor insert: Either p_sessionId or a valid session described by (p_proposalCode, p_proposalNumber, p_sessionNumber)\nFor update: p_id\nNote: In order to associate the data collection group with a sample, one of the following sets of parameters are required:\n* p_sampleId\n* p_proposalCode, p_proposalNumber, p_sessionNumber + p_sampleBarcode\n* p_actualContainerBarcode + p_actualSampleSlotInContainer\nReturns: Record ID in p_id.'
BEGIN
	DECLARE row_proposal_id int(10) unsigned DEFAULT NULL;
	DECLARE row_sample_id int(10) unsigned DEFAULT NULL;

	IF p_sessionId IS NULL AND p_proposalCode IS NOT NULL AND p_proposalNumber IS NOT NULL AND p_sessionNumber IS NOT NULL THEN
      SELECT max(bs.sessionid), p.proposalId INTO p_sessionId, row_proposal_id
      FROM Proposal p INNER JOIN BLSession bs ON p.proposalid = bs.proposalid
      WHERE p.proposalCode = p_proposalCode AND p.proposalNumber = p_proposalNumber AND bs.visit_number = p_sessionNumber;
	END IF;

	IF p_id IS NOT NULL OR p_sessionId IS NOT NULL THEN
	  
      IF p_sessionId IS NOT NULL AND p_sampleId IS NULL AND p_sampleBarcode IS NOT NULL THEN
	    IF row_proposal_id IS NULL THEN
          SELECT proposalId INTO row_proposal_id
          FROM BLSession
          WHERE sessionId = p_sessionId;
	    END IF;
        SELECT max(bls.blSampleId) INTO p_sampleId
        FROM BLSample bls
		  INNER JOIN Container c on c.containerId = bls.containerId
          INNER JOIN Dewar d on d.dewarId = c.dewarId
          INNER JOIN Shipping s on s.shippingId = d.shippingId
        WHERE bls.code = p_sampleBarcode AND s.proposalId = row_proposal_id;
	  END IF;

	  IF p_sampleId IS NULL AND (p_actualContainerBarcode IS NOT NULL) AND (p_actualSampleSlotInContainer IS NOT NULL) THEN
	    SELECT max(bls.blSampleId) INTO p_sampleId
        FROM BLSample bls
          INNER JOIN Container c on c.containerId = bls.containerId
	    WHERE c.barcode = p_actualContainerBarcode AND bls.location = p_actualSampleSlotInContainer;
      END IF;

      INSERT INTO DataCollectionGroup (datacollectionGroupId, sessionId, blsampleId, experimenttype, starttime, endtime,
        crystalClass, detectorMode, actualSampleBarcode, actualSampleSlotInContainer, actualContainerBarcode, actualContainerSlotInSC,
        comments, xtalSnapshotFullPath, scanParameters)
        VALUES (p_id, p_sessionId, p_sampleId, p_experimenttype, p_starttime, p_endtime, p_crystalClass, p_detectorMode,
        p_actualSampleBarcode, p_actualSampleSlotInContainer, p_actualContainerBarcode, p_actualContainerSlotInSC,
        p_comments, p_xtalSnapshotFullPath, p_scanParameters)
	    ON DUPLICATE KEY UPDATE
		  sessionId = IFNULL(p_sessionId, sessionId),
          blsampleId = IFNULL(p_sampleId, blsampleId),
          experimenttype = IFNULL(p_experimenttype, experimenttype),
          starttime = IFNULL(p_starttime, starttime),
          endtime = IFNULL(p_endtime, endtime),
          crystalClass = IFNULL(p_crystalClass, crystalClass),
          detectorMode = IFNULL(p_detectorMode, detectorMode),
          actualSampleBarcode = IFNULL(p_actualSampleBarcode, actualSampleBarcode),
          actualSampleSlotInContainer = IFNULL(p_actualSampleSlotInContainer, actualSampleSlotInContainer),
          actualContainerBarcode = IFNULL(p_actualContainerBarcode, actualContainerBarcode),
          actualContainerSlotInSC = IFNULL(p_actualContainerSlotInSC, actualContainerSlotInSC),
          comments = IFNULL(p_comments, comments),
          xtalSnapshotFullPath = IFNULL(p_xtalSnapshotFullPath, xtalSnapshotFullPath),
					scanParameters = IFNULL (p_scanParameters, scanParameters);

	    IF p_id IS NULL THEN
		    SET p_id = LAST_INSERT_ID();
      END IF;
    ELSE
      SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument(s) are NULL: p_id OR p_sessionId OR a valid session described by (p_proposalCode and p_proposalNumber and p_sessionNumber) must be non-NULL.';
    END IF;
  END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `upsert_dc_main` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES' */ ;
DELIMITER ;;
CREATE PROCEDURE `upsert_dc_main`(
     INOUT p_id int(11) unsigned,
     p_groupId int(11) unsigned,
     p_detectorId int(11),
     p_dcNumber int(10) unsigned,
     p_startTime datetime,                                          
     p_endTime datetime,                                             
     p_status varchar(45),                                          
     p_noImages int(10) unsigned,                                     
	 p_startImgNumber int(10) unsigned,                                     
	 p_noPasses int(10) unsigned,                                     
     p_imgDir varchar(255),                                      
	 p_imgPrefix varchar(45),                                       
     p_imgSuffix varchar(45),
     p_fileTemplate varchar(255),
     p_snapshot1 varchar(255),                                         
     p_snapshot2 varchar(255),                                         
     p_snapshot3 varchar(255),                                         
     p_snapshot4 varchar(255),
     p_comments varchar(1024)                                        
)
    MODIFIES SQL DATA
BEGIN
    INSERT INTO DataCollection (dataCollectionId, dataCollectionGroupId, sessionId, blSampleId, detectorId, datacollectionNumber, startTime, endTime, 
        runStatus, numberOfImages, startImageNumber, numberOfPasses, imageDirectory, imagePrefix, imageSuffix, fileTemplate, 
        xtalSnapshotFullPath1, xtalSnapshotFullPath2, xtalSnapshotFullPath3, xtalSnapshotFullPath4, comments) 
      VALUES (p_id, p_groupId, 
      (SELECT sessionId FROM DataCollectionGroup WHERE dataCollectionGroupId = p_groupId), 
      (SELECT blSampleId FROM DataCollectionGroup WHERE dataCollectionGroupId = p_groupId), 
      p_detectorId, 
      p_dcNumber, p_startTime, p_endTime, 
      p_status, p_noImages, p_startImgNumber, p_noPasses, p_imgDir, p_imgPrefix, p_imgSuffix, p_fileTemplate, 
      p_snapshot1, p_snapshot2, p_snapshot3, p_snapshot4, comments)
      ON DUPLICATE KEY UPDATE
		datacollectiongroupid = IFNULL(p_groupId, datacollectiongroupid),
        detectorId = IFNULL(p_detectorId, detectorId),
        datacollectionNumber = IFNULL(p_dcNumber, datacollectionNumber),
        starttime = IFNULL(p_starttime, starttime),
        endtime = IFNULL(p_endtime, endtime),
        runStatus = IFNULL(p_status, runStatus),
        numberOfImages = IFNULL(p_noImages, numberOfImages),
        startImageNumber = IFNULL(p_noImages, startImageNumber),
        numberOfPasses = IFNULL(p_noPasses, numberOfPasses),
        imagedirectory = IFNULL(p_imgDir, imagedirectory),
        imageprefix = IFNULL(p_imgPrefix, imageprefix),
        imagesuffix = IFNULL(p_imgSuffix, imagesuffix),
        fileTemplate = IFNULL(p_fileTemplate, fileTemplate),
        xtalSnapshotFullPath1 = IFNULL(p_snapshot1, xtalSnapshotFullPath1),
        xtalSnapshotFullPath2 = IFNULL(p_snapshot2, xtalSnapshotFullPath2),
        xtalSnapshotFullPath3 = IFNULL(p_snapshot3, xtalSnapshotFullPath3),
        xtalSnapshotFullPath4 = IFNULL(p_snapshot4, xtalSnapshotFullPath4),
        comments = IFNULL(p_comments, comments);
	IF LAST_INSERT_ID() <> 0 THEN 
		SET p_id = LAST_INSERT_ID();
    END IF;
  END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `upsert_dc_main_v2` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `upsert_dc_main_v2`(
     INOUT p_id int(11) unsigned,
     p_groupId int(11) unsigned,
     p_detectorId int(11),
     p_blSubSampleId int(11) unsigned,
     p_dcNumber int(10) unsigned,
     p_startTime datetime,                                          
     p_endTime datetime,                                             
     p_status varchar(45),                                          
     p_noImages int(10) unsigned,                                     
	 p_startImgNumber int(10) unsigned,                                     
	 p_noPasses int(10) unsigned,                                     
     p_imgDir varchar(255),                                      
	 p_imgPrefix varchar(45),                                       
     p_imgSuffix varchar(45),
     p_fileTemplate varchar(255),
     p_snapshot1 varchar(255),                                         
     p_snapshot2 varchar(255),                                         
     p_snapshot3 varchar(255),                                         
     p_snapshot4 varchar(255),
     p_comments varchar(1024)                                        
)
    MODIFIES SQL DATA
    COMMENT 'Inserts (if p_id not provided) or updates a row in DataCollectio'
BEGIN
    INSERT INTO DataCollection (dataCollectionId, dataCollectionGroupId, sessionId, blSampleId, blSubSampleId, detectorId, datacollectionNumber, startTime, endTime, 
        runStatus, numberOfImages, startImageNumber, numberOfPasses, imageDirectory, imagePrefix, imageSuffix, fileTemplate, 
        xtalSnapshotFullPath1, xtalSnapshotFullPath2, xtalSnapshotFullPath3, xtalSnapshotFullPath4, comments) 
      VALUES (p_id, p_groupId, 
      (SELECT sessionId FROM DataCollectionGroup WHERE dataCollectionGroupId = p_groupId), 
      (SELECT blSampleId FROM DataCollectionGroup WHERE dataCollectionGroupId = p_groupId), 
      p_blSubSampleId,
      p_detectorId, 
      p_dcNumber, p_startTime, p_endTime, 
      p_status, p_noImages, p_startImgNumber, p_noPasses, p_imgDir, p_imgPrefix, p_imgSuffix, p_fileTemplate, 
      p_snapshot1, p_snapshot2, p_snapshot3, p_snapshot4, comments)
      ON DUPLICATE KEY UPDATE
		datacollectiongroupid = IFNULL(p_groupId, datacollectiongroupid),
		blSubSampleId = IFNULL(p_blSubSampleId, blSubSampleId),
        detectorId = IFNULL(p_detectorId, detectorId),
        datacollectionNumber = IFNULL(p_dcNumber, datacollectionNumber),
        starttime = IFNULL(p_starttime, starttime),
        endtime = IFNULL(p_endtime, endtime),
        runStatus = IFNULL(p_status, runStatus),
        numberOfImages = IFNULL(p_noImages, numberOfImages),
        startImageNumber = IFNULL(p_noImages, startImageNumber),
        numberOfPasses = IFNULL(p_noPasses, numberOfPasses),
        imagedirectory = IFNULL(p_imgDir, imagedirectory),
        imageprefix = IFNULL(p_imgPrefix, imageprefix),
        imagesuffix = IFNULL(p_imgSuffix, imagesuffix),
        fileTemplate = IFNULL(p_fileTemplate, fileTemplate),
        xtalSnapshotFullPath1 = IFNULL(p_snapshot1, xtalSnapshotFullPath1),
        xtalSnapshotFullPath2 = IFNULL(p_snapshot2, xtalSnapshotFullPath2),
        xtalSnapshotFullPath3 = IFNULL(p_snapshot3, xtalSnapshotFullPath3),
        xtalSnapshotFullPath4 = IFNULL(p_snapshot4, xtalSnapshotFullPath4),
        comments = IFNULL(p_comments, comments);
	IF p_id IS NULL THEN 
		SET p_id = LAST_INSERT_ID();
    END IF;
  END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `upsert_dc_main_v3` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `upsert_dc_main_v3`(
     INOUT p_id int(11) unsigned,
     p_groupId int(11) unsigned,
     p_detectorId int(11),
     p_blSubSampleId int(11) unsigned,
     p_dcNumber int(10) unsigned,
     p_startTime datetime,
     p_endTime datetime,
     p_status varchar(45),
     p_noImages int(10) unsigned,
	   p_startImgNumber int(10) unsigned,
	   p_noPasses int(10) unsigned,
     p_imgDir varchar(255),
	   p_imgPrefix varchar(45),
     p_imgSuffix varchar(45),
     p_imgContainerSubPath varchar(255),
     p_fileTemplate varchar(255),
     p_snapshot1 varchar(255),
     p_snapshot2 varchar(255),
     p_snapshot3 varchar(255),
     p_snapshot4 varchar(255),
     p_comments varchar(1024)
)
    MODIFIES SQL DATA
    COMMENT 'Inserts (if p_id not provided) or updates a row in DataCollection, returns ID in p_id. '
BEGIN
    INSERT INTO DataCollection (dataCollectionId, dataCollectionGroupId, sessionId, blSampleId, blSubSampleId, detectorId, datacollectionNumber, startTime, endTime,
        runStatus, numberOfImages, startImageNumber, numberOfPasses, imageDirectory, imagePrefix, imageSuffix, imageContainerSubPath, fileTemplate,
        xtalSnapshotFullPath1, xtalSnapshotFullPath2, xtalSnapshotFullPath3, xtalSnapshotFullPath4, comments)
      VALUES (p_id, p_groupId,
      (SELECT sessionId FROM DataCollectionGroup WHERE dataCollectionGroupId = p_groupId),
      (SELECT blSampleId FROM DataCollectionGroup WHERE dataCollectionGroupId = p_groupId),
      p_blSubSampleId,
      p_detectorId,
      p_dcNumber, p_startTime, p_endTime,
      p_status, p_noImages, p_startImgNumber, p_noPasses, p_imgDir, p_imgPrefix, p_imgSuffix, p_imgContainerSubPath, p_fileTemplate,
      p_snapshot1, p_snapshot2, p_snapshot3, p_snapshot4, p_comments)
      ON DUPLICATE KEY UPDATE
		    datacollectiongroupid = IFNULL(p_groupId, datacollectiongroupid),
		    blSubSampleId = IFNULL(p_blSubSampleId, blSubSampleId),
        detectorId = IFNULL(p_detectorId, detectorId),
        datacollectionNumber = IFNULL(p_dcNumber, datacollectionNumber),
        starttime = IFNULL(p_starttime, starttime),
        endtime = IFNULL(p_endtime, endtime),
        runStatus = IFNULL(p_status, runStatus),
        numberOfImages = IFNULL(p_noImages, numberOfImages),
        startImageNumber = IFNULL(p_noImages, startImageNumber),
        numberOfPasses = IFNULL(p_noPasses, numberOfPasses),
        imagedirectory = IFNULL(p_imgDir, imagedirectory),
        imageprefix = IFNULL(p_imgPrefix, imageprefix),
        imagesuffix = IFNULL(p_imgSuffix, imagesuffix),
        imageContainerSubPath = IFNULL(p_imgContainerSubPath, imageContainerSubPath),
        fileTemplate = IFNULL(p_fileTemplate, fileTemplate),
        xtalSnapshotFullPath1 = IFNULL(p_snapshot1, xtalSnapshotFullPath1),
        xtalSnapshotFullPath2 = IFNULL(p_snapshot2, xtalSnapshotFullPath2),
        xtalSnapshotFullPath3 = IFNULL(p_snapshot3, xtalSnapshotFullPath3),
        xtalSnapshotFullPath4 = IFNULL(p_snapshot4, xtalSnapshotFullPath4),
        comments = IFNULL(p_comments, comments);
	IF p_id IS NULL THEN
		SET p_id = LAST_INSERT_ID();
    END IF;
  END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `upsert_dewar` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE PROCEDURE `upsert_dewar`(
	 INOUT p_id int(10) unsigned,
	 p_shippingId int(10) unsigned,
	 p_name varchar(45),
	 p_comments tinytext,
	 p_storageLocation varchar(45),
	 p_status varchar(45),
	 p_isStorageDewar tinyint(1),
	 p_barcode varchar(45),
	 p_firstSessionId int(10) unsigned,
	 p_customsValue int(11) unsigned,
	 p_transportValue int(11) unsigned,
	 p_trackingNumberToSynchrotron varchar(30),
	 p_trackingNumberFromSynchrotron varchar(30),
	 p_type varchar(40),
	 p_facilityCode varchar(20),
	 p_weight float,
	 p_deliveryAgentBarcode varchar(30)
 )
    MODIFIES SQL DATA
    COMMENT 'Inserts or updates info about a dewar/parcel (p_id).\nMandatory columns:\nFor insert: none\nFor update: p_id \nReturns: Record ID in p_id.'
BEGIN
    DECLARE row_storageLocation varchar(45) DEFAULT NULL;
	  DECLARE row_dewarStatus varchar(45) DEFAULT NULL;

    IF p_id IS NULL THEN
		  IF p_type IS NOT NULL THEN
        INSERT INTO Dewar(dewarId,shippingId,code,comments,storageLocation,dewarStatus,isStorageDewar,barCode,firstExperimentId,customsValue,transportValue,
			    trackingNumberToSynchrotron,trackingNumberFromSynchrotron,`type`,FACILITYCODE,weight,deliveryAgent_barcode)
			    VALUES (p_id, p_shippingId, p_name, p_comments, p_storageLocation, p_status, p_isStorageDewar, p_barcode, p_firstSessionId, p_customsValue, p_transportValue,
				    p_trackingNumberToSynchrotron, p_trackingNumberFromSynchrotron, p_type, p_facilityCode, p_weight, p_deliveryAgentBarcode);
			  SET p_id = LAST_INSERT_ID();
			ELSE
				SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument is NULL: p_type must be non-NULL.';
			END IF;
	  ELSE

      SELECT storageLocation, dewarStatus INTO row_storageLocation, row_dewarStatus FROM Dewar WHERE dewarId = p_id;

			UPDATE Dewar
			  SET shippingId = IFNULL(p_shippingId, shippingId),
				code = IFNULL(p_name, code),
				comments = IFNULL(p_comments, comments),
				storageLocation = IFNULL(p_storageLocation, storageLocation),
				dewarStatus = IFNULL(p_status, dewarStatus),
				isStorageDewar = IFNULL(p_isStorageDewar, isStorageDewar),
				barCode = IFNULL(p_barcode, barCode),
				firstExperimentId = IFNULL(p_firstSessionId, firstExperimentId),
				customsValue = IFNULL(p_customsValue, customsValue),
				transportValue = IFNULL(p_transportValue, transportValue),
				trackingNumberToSynchrotron = IFNULL(p_trackingNumberToSynchrotron, trackingNumberToSynchrotron),
				trackingNumberFromSynchrotron = IFNULL(p_trackingNumberFromSynchrotron, trackingNumberFromSynchrotron),
				`type` = IFNULL(p_type, `type`),
				FACILITYCODE = IFNULL(p_facilityCode, FACILITYCODE),
				weight = IFNULL(p_weight, weight),
				deliveryAgent_barcode = IFNULL(p_deliveryAgentBarcode, deliveryAgent_barcode)
			WHERE dewarId = p_id;

			
      IF row_storageLocation <> p_storageLocation OR row_dewarStatus <> p_status THEN
        INSERT INTO DewarTransportHistory (dewarId, dewarStatus, storageLocation, arrivalDate)
				  VALUES (p_id, p_status, p_storageLocation, NOW());
      END IF;

			
		  IF row_storageLocation <> p_storageLocation THEN
			  
        UPDATE Container
				SET sampleChangerLocation = '', containerStatus = 'at facility'
				WHERE dewarId = p_id;
			END IF;
		END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `upsert_dewar_v2` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE PROCEDURE `upsert_dewar_v2`(

	 INOUT p_id int(10) unsigned,
	 p_authLogin varchar(45),
	 p_shippingId int(10) unsigned,
	 p_name varchar(45),
	 p_comments tinytext,
	 p_storageLocation varchar(45),
	 p_status varchar(45),
	 p_isStorageDewar tinyint(1),
	 p_barcode varchar(45),
	 p_firstSessionId int(10) unsigned,
	 p_customsValue int(11) unsigned,
	 p_transportValue int(11) unsigned,
	 p_trackingNumberToSynchrotron varchar(30),
	 p_trackingNumberFromSynchrotron varchar(30),
	 p_type varchar(40),
	 p_facilityCode varchar(20),
	 p_weight float,
	 p_deliveryAgentBarcode varchar(30)
 )
    MODIFIES SQL DATA
    COMMENT 'Inserts or updates info about a dewar/parcel (p_id).\nMandatory columns:\nFor insert: none\nFor update: p_id \nReturns: Record ID in p_id.'
BEGIN
	DECLARE row_storageLocation varchar(45) DEFAULT NULL;
	DECLARE row_dewarStatus varchar(45) DEFAULT NULL;
  DECLARE row_count int unsigned DEFAULT 0;

  IF p_authLogin IS NOT NULL AND p_shippingId IS NOT NULL THEN

    
    
    SELECT count(*) INTO row_count
    FROM Shipping s
      INNER JOIN BLSession bs ON bs.proposalId = s.proposalId
      INNER JOIN Session_has_Person shp ON bs.sessionId = shp.sessionId
      INNER JOIN Person p ON p.personId = shp.personId
    WHERE p.login = p_authLogin AND s.shippingId = p_shippingId; 

    IF row_count = 0 THEN
        SIGNAL SQLSTATE '02000'
            SET MYSQL_ERRNO=1643, MESSAGE_TEXT = 'Dewar not in a shipping belonging to one of the p_authLogin Person sessions';
    END IF;
  END IF;

  IF p_id IS NULL THEN
		  IF p_type IS NOT NULL THEN
        INSERT INTO Dewar(dewarId,shippingId,code,comments,storageLocation,dewarStatus,isStorageDewar,barCode,firstExperimentId,customsValue,transportValue,
			    trackingNumberToSynchrotron,trackingNumberFromSynchrotron,`type`,FACILITYCODE,weight,deliveryAgent_barcode)
			    VALUES (p_id, p_shippingId, p_name, p_comments, p_storageLocation, p_status, p_isStorageDewar, p_barcode, p_firstSessionId, p_customsValue, p_transportValue,
				    p_trackingNumberToSynchrotron, p_trackingNumberFromSynchrotron, p_type, p_facilityCode, p_weight, p_deliveryAgentBarcode);
			  SET p_id = LAST_INSERT_ID();
			ELSE
				SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument is NULL: p_type must be non-NULL.';
			END IF;
	ELSE

    SELECT storageLocation, dewarStatus INTO row_storageLocation, row_dewarStatus FROM Dewar WHERE dewarId = p_id;

		UPDATE Dewar
			SET shippingId = IFNULL(p_shippingId, shippingId),
			code = IFNULL(p_name, code),
			comments = IFNULL(p_comments, comments),
			storageLocation = IFNULL(p_storageLocation, storageLocation),
			dewarStatus = IFNULL(p_status, dewarStatus),
			isStorageDewar = IFNULL(p_isStorageDewar, isStorageDewar),
			barCode = IFNULL(p_barcode, barCode),
			firstExperimentId = IFNULL(p_firstSessionId, firstExperimentId),
			customsValue = IFNULL(p_customsValue, customsValue),
			transportValue = IFNULL(p_transportValue, transportValue),
			trackingNumberToSynchrotron = IFNULL(p_trackingNumberToSynchrotron, trackingNumberToSynchrotron),
			trackingNumberFromSynchrotron = IFNULL(p_trackingNumberFromSynchrotron, trackingNumberFromSynchrotron),
			`type` = IFNULL(p_type, `type`),
			FACILITYCODE = IFNULL(p_facilityCode, FACILITYCODE),
			weight = IFNULL(p_weight, weight),
			deliveryAgent_barcode = IFNULL(p_deliveryAgentBarcode, deliveryAgent_barcode)
		WHERE dewarId = p_id;

		
    IF row_storageLocation <> p_storageLocation OR row_dewarStatus <> p_status THEN
      INSERT INTO DewarTransportHistory (dewarId, dewarStatus, storageLocation, arrivalDate)
				VALUES (p_id, p_status, p_storageLocation, NOW());
    END IF;

		
		IF row_storageLocation <> p_storageLocation THEN
			
      UPDATE Container
			SET sampleChangerLocation = '', containerStatus = 'at facility'
			WHERE dewarId = p_id;
		END IF;
	END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `upsert_energy_scan` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `upsert_energy_scan`(
	 INOUT p_id int(11) unsigned,
	 p_sessionId int(10) unsigned,
	 p_sampleId int(10) unsigned,
	 p_subSampleId int(11) unsigned,
	 p_startTime datetime,
	 p_endTime datetime,
	 p_startEnergy float,
	 p_endEnergy float,
	 p_detector varchar(40),
	 p_element varchar(10),
	 p_edgeEnergy varchar(10),
	 p_synchrotronCurrent float,
	 p_temperature float,
	 p_peakEnergy float,
	 p_peakFPrime float,
	 p_peakFDoublePrime float,
	 p_inflectionEnergy float,
	 p_inflectionFPrime float,
	 p_inflectionFDoublePrime float,
	 p_choochFileFullPath varchar(255),
	 p_jpegChoochFileFullPath varchar(255),
	 p_scanFileFullPath varchar(255),
	 p_beamSizeHorizontal float,
	 p_beamSizeVertical float,
	 p_exposureTime float,
	 p_transmission float,
	 p_flux double,
	 p_fluxEnd double,
	 p_comments varchar(1024))
    MODIFIES SQL DATA
    COMMENT 'Inserts or updates info about an energy scan (p_id).\nMandatory c'
BEGIN
	IF p_id IS NOT NULL OR p_sessionId IS NOT NULL THEN

      INSERT INTO EnergyScan (energyScanId, sessionId, blSampleId, blSubSampleId, startTime, endTime,
				startEnergy, endEnergy, fluorescenceDetector, element, edgeEnergy, synchrotronCurrent, temperature,
				peakEnergy, peakFPrime, peakFDoublePrime, inflectionEnergy, inflectionFPrime, inflectionFDoublePrime,
		 	 	choochFileFullPath, jpegChoochFileFullPath, scanFileFullPath, beamSizeHorizontal, beamSizeVertical,
		 	 	exposureTime, transmissionFactor, flux, flux_end, comments)
        VALUES (p_id, p_sessionId, p_sampleId, p_subSampleId, p_startTime, p_endTime,
					p_startEnergy, p_endEnergy, p_detector, p_element, p_edgeEnergy, p_synchrotronCurrent, p_temperature,
					p_peakEnergy, p_peakFPrime, p_peakFDoublePrime, p_inflectionEnergy, p_inflectionFPrime, p_inflectionFDoublePrime,
			 	 	p_choochFileFullPath, p_jpegChoochFileFullPath, p_scanFileFullPath, p_beamSizeHorizontal, p_beamSizeVertical,
			 	 	p_exposureTime, p_transmission, p_flux, p_fluxEnd, p_comments)
	    ON DUPLICATE KEY UPDATE
		  		sessionId = IFNULL(p_sessionId, sessionId),
          blSampleId = IFNULL(p_sampleId, blSampleId),
					blSubSampleId = IFNULL(p_subSampleId, blSubSampleId),
          startTime = IFNULL(p_startTime, startTime),
          endTime = IFNULL(p_endTime, endTime),
					startEnergy = IFNULL(p_startEnergy, startEnergy),
					endEnergy = IFNULL(p_endEnergy, endEnergy),
					fluorescenceDetector = IFNULL(p_detector, fluorescenceDetector),
					element = IFNULL(p_element, element),
					edgeEnergy = IFNULL(p_edgeEnergy, edgeEnergy),
					synchrotronCurrent = IFNULL(p_synchrotronCurrent, synchrotronCurrent),
					temperature = IFNULL(p_temperature, temperature),
					peakEnergy = IFNULL(p_peakEnergy, peakEnergy),
					peakFPrime = IFNULL(p_peakFPrime, peakFPrime),
					peakFDoublePrime = IFNULL(p_peakFDoublePrime, peakFDoublePrime),
					inflectionEnergy = IFNULL(p_inflectionEnergy, inflectionEnergy),
					inflectionFPrime = IFNULL(p_inflectionFPrime, inflectionFPrime),
					inflectionFDoublePrime = IFNULL(p_inflectionFDoublePrime, inflectionFDoublePrime),
					choochFileFullPath = IFNULL(p_choochFileFullPath, choochFileFullPath),
					jpegChoochFileFullPath = IFNULL(p_jpegChoochFileFullPath, jpegChoochFileFullPath),
					scanFileFullPath = IFNULL(p_scanFileFullPath, scanFileFullPath),
					beamSizeHorizontal = IFNULL(p_beamSizeHorizontal, beamSizeHorizontal),
					beamSizeVertical = IFNULL(p_beamSizeVertical, beamSizeVertical),
					exposureTime = IFNULL(p_exposureTime, exposureTime),
					transmissionFactor = IFNULL(p_transmission, transmissionFactor),
					flux = IFNULL(p_flux, flux),
					flux_end = IFNULL(p_fluxEnd, flux_end),
          comments = IFNULL(p_comments, comments);

	  IF p_id IS NULL THEN
		  SET p_id = LAST_INSERT_ID();
    END IF;
  ELSE
      SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument(s) are NULL: p_id OR p_sessionId must be non-NULL.';
  END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `upsert_fluo_mapping` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `upsert_fluo_mapping`(
	 INOUT p_id int(11) unsigned,
	 p_roiId int(11) unsigned,
	 p_roiStartEnergy float,
	 p_roiEndEnergy float,
	 p_dcId int(11) unsigned,
	 p_imgNumber int(10) unsigned,
	 p_counts int(10) unsigned
 )
    MODIFIES SQL DATA
    COMMENT 'Inserts or updates info about a fluorescence spectrum mapping (p_id).\nMandatory columns:\nFor insert: (p_roiId OR (p_roiStartEnergy AND p_roiEndEnergy)) AND p_dcId\nFor update: p_id \nReturns: Record ID in p_id.'
BEGIN
  DECLARE row_xrfFluorescenceMappingROIId int(10) unsigned DEFAULT NULL;

	IF p_id IS NOT NULL OR ((p_roiId IS NOT NULL OR (p_roiStartEnergy IS NOT NULL AND p_roiEndEnergy IS NOT NULL)) AND p_dcId IS NOT NULL) THEN

    IF p_roiId IS NULL THEN
      SELECT MAX(xrfFluorescenceMappingROIId) INTO row_xrfFluorescenceMappingROIId
			FROM XRFFluorescenceMappingROI
			WHERE p_roiStartEnergy >= startEnergy AND p_roiEndEnergy <= endEnergy;
		ELSE
		  SET row_xrfFluorescenceMappingROIId = p_roiId;
    END IF;

  	INSERT INTO XRFFluorescenceMapping (xrfFluorescenceMappingId, xrfFluorescenceMappingROIId, dataCollectionId, imageNumber, counts)
	  	VALUES (p_id, row_xrfFluorescenceMappingROIId, p_dcId, p_imgNumber, p_counts)
	  	ON DUPLICATE KEY UPDATE
				xrfFluorescenceMappingROIId = IFNULL(row_xrfFluorescenceMappingROIId, xrfFluorescenceMappingROIId),
				dataCollectionId = IFNULL(p_dcId, dataCollectionId),
				imageNumber = IFNULL(p_imgNumber, imageNumber),
				counts = IFNULL(p_counts, counts);

		IF p_id IS NULL THEN
			SET p_id = LAST_INSERT_ID();
		END IF;
	ELSE
		SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument(s) are NULL: p_id OR (p_roiId OR (p_roiStartEnergy AND p_roiEndEnergy)) AND p_dcId) must be non-NULL.';
	END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `upsert_fluo_mapping_roi` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `upsert_fluo_mapping_roi`(
	 INOUT p_id int(11) unsigned,
	 p_startEnergy float,
	 p_endEnergy float,
	 p_element varchar(2),
   p_edge varchar(2),
   p_r tinyint unsigned,
   p_g tinyint unsigned,
   p_b tinyint unsigned
 )
    MODIFIES SQL DATA
    COMMENT 'Inserts or updates info about a fluorescence spectrum mapping re'
BEGIN

  INSERT INTO XRFFluorescenceMappingROI (xrfFluorescenceMappingROIId, startEnergy, endEnergy, element, edge, r, g, b)
	  VALUES (p_id, p_startEnergy, p_endEnergy, p_element, p_edge, p_r, p_g, p_b)
	  ON DUPLICATE KEY UPDATE
			startEnergy = IFNULL(p_startEnergy, startEnergy),
			endEnergy = IFNULL(p_endEnergy, endEnergy),
			element = IFNULL(p_element, element),
			edge = IFNULL(p_edge, edge),
			r = IFNULL(p_r, r),
			g = IFNULL(p_g, g),
			b = IFNULL(p_b, b);

	IF p_id IS NULL THEN
		SET p_id = LAST_INSERT_ID();
	END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `upsert_motion_correction` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `upsert_motion_correction`(
  INOUT p_motionCorrectionId int(11) unsigned,
  p_movieId int(11) unsigned,
  p_autoProcProgramId int(11) unsigned,
  p_imageNumber smallint unsigned,
  p_firstFrame smallint unsigned,
  p_lastFrame smallint unsigned,
  p_dosePerFrame float,
  p_totalMotion float,
  p_averageMotionPerFrame float,
  p_driftPlotFullPath varchar(255),
  p_micrographFullPath varchar(255),
  p_micrographSnapshotFullPath varchar(255),
  p_fftFullPath varchar(255),
  p_fftCorrectedFullPath varchar(255),
  p_patchesUsedX mediumint unsigned,
  p_patchesUsedY mediumint unsigned,
  p_comments varchar(255)
)
    MODIFIES SQL DATA
BEGIN
    INSERT INTO MotionCorrection (motionCorrectionId, movieId, autoProcProgramId, imageNumber, firstFrame, lastFrame, dosePerFrame, totalMotion, averageMotionPerFrame, driftPlotFullPath, micrographFullPath, micrographSnapshotFullPath, fftFullPath, fftCorrectedFullPath, patchesUsedX, patchesUsedY, comments) 
      VALUES (p_motionCorrectionId, p_movieId, p_autoProcProgramId, p_imageNumber, p_firstFrame, p_lastFrame, p_dosePerFrame, p_totalMotion, p_averageMotionPerFrame, p_driftPlotFullPath, p_micrographFullPath, p_micrographSnapshotFullPath, p_fftFullPath, p_fftCorrectedFullPath, p_patchesUsedX, p_patchesUsedY, p_comments)
      ON DUPLICATE KEY UPDATE
        motionCorrectionId = IFNULL(p_motionCorrectionId, motionCorrectionId),
	movieId = IFNULL(p_movieId, movieId),
	autoProcProgramId = IFNULL(p_autoProcProgramId, autoProcProgramId), 
	imageNumber = IFNULL(p_imageNumber, imageNumber), 
	firstFrame = IFNULL(p_firstFrame, firstFrame), 
	lastFrame = IFNULL(p_lastFrame, lastFrame), 
	dosePerFrame= IFNULL(p_dosePerFrame, dosePerFrame), 
	totalMotion = IFNULL(p_totalMotion, totalMotion), 
	averageMotionPerFrame = IFNULL(p_averageMotionPerFrame, averageMotionPerFrame), 
	driftPlotFullPath = IFNULL(p_driftPlotFullPath, driftPlotFullPath), 
	micrographFullPath = IFNULL(p_micrographFullPath, micrographFullPath), 
	micrographSnapshotFullPath = IFNULL(p_micrographSnapshotFullPath, micrographSnapshotFullPath), 
	fftFullPath = IFNULL(p_fftFullPath, fftFullPath), 
	fftCorrectedFullPath = IFNULL(p_fftCorrectedFullPath, fftCorrectedFullPath), 
	patchesUsedX = IFNULL(p_patchesUsedX, patchesUsedX), 
    patchesUsedY = IFNULL(p_patchesUsedY, patchesUsedY),    
	comments = IFNULL(p_comments, comments);

	IF p_motionCorrectionId IS NULL THEN
	    SET p_motionCorrectionId = LAST_INSERT_ID();
    	END IF;
     END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `upsert_motion_correction_drift` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `upsert_motion_correction_drift`(
     INOUT p_id int(11) unsigned,
	 p_motionCorrectionId int(11) unsigned,
     p_frameNumber smallint unsigned,
     p_deltaX float,
     p_deltaY float
  )
    MODIFIES SQL DATA
    COMMENT 'If p_id is not provided, inserts new row. Otherwise updates exis'
BEGIN
  IF p_id IS NOT NULL OR p_motionCorrectionId IS NOT NULL THEN
    INSERT INTO MotionCorrectionDrift (
      motionCorrectionDriftId, motionCorrectionId, frameNumber, deltaX, deltaY) 
	VALUES (
	  p_id, p_motionCorrectionId, p_frameNumber, p_deltaX, p_deltaY)
	ON DUPLICATE KEY UPDATE
      motionCorrectionId = IFNULL(p_motionCorrectionId, motionCorrectionId),
      frameNumber = IFNULL(p_frameNumber, frameNumber),
      deltaX = IFNULL(p_deltaX, deltaX),
      deltaY = IFNULL(p_deltaY, deltaY);
	IF p_id IS NULL THEN 
      SET p_id = LAST_INSERT_ID();
    END IF;
  ELSE
    SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument(s) p_id and/or p_motionCorrectionId are NULL';  
  END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `upsert_movie` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `upsert_movie`(
  INOUT p_movieId int(11) unsigned,
  p_dataCollectionId int(11) unsigned,
  p_movieNumber mediumint unsigned,
  p_movieFullPath varchar(255),
  p_createdTimeStamp timestamp,
  p_positionX float,
  p_positionY float,
  p_nominalDefocus float unsigned
)
    MODIFIES SQL DATA
BEGIN
    INSERT INTO Movie (movieId, dataCollectionId, movieNumber, movieFullPath, createdTimeStamp, positionX, positionY, nominalDefocus) 
      VALUES (p_movieId, p_dataCollectionId, p_movieNumber, p_movieFullPath, p_createdTimeStamp, p_positionX, p_positionY, p_nominalDefocus)
      ON DUPLICATE KEY UPDATE
        dataCollectionId = IFNULL(p_dataCollectionId, dataCollectionId),
        movieNumber = IFNULL(p_movieNumber, movieNumber),
        movieFullPath = IFNULL(p_movieFullPath, movieFullPath),
        createdTimeStamp = IFNULL(p_createdTimeStamp, createdTimeStamp),
        positionX = IFNULL(p_positionX, positionX),
        positionY = IFNULL(p_positionY, positionY),
        nominalDefocus = IFNULL(p_nominalDefocus, nominalDefocus);

	IF p_movieId IS NULL THEN
	    SET p_movieId = LAST_INSERT_ID();
	END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `upsert_mrrun` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `upsert_mrrun`(
     INOUT p_id integer,
     p_parentId integer,
     p_success boolean,
     p_message varchar(255), 
     p_pipeline varchar(50),
     p_inputCoordFile varchar(255), 
     p_outputCoordFile varchar(255), 
     p_inputMTZFile varchar(255), 
     p_outputMTZFile varchar(255), 
     p_runDirectory varchar(255),
     p_logFile varchar(255),
     p_commandLine varchar(255),
     p_rValueStart float ,
     p_rValueEnd float ,
     p_rFreeValueStart float ,
     p_rFreeValueEnd float ,
     p_starttime datetime,
     p_endtime datetime
     )
    MODIFIES SQL DATA
    COMMENT 'Update or insert new entry with info about a MX molecular replacements run, e.g. Dimple'
BEGIN
    IF p_parentId IS NOT NULL THEN
      INSERT INTO MXMRRun (mxMRRunId, autoProcScalingId, success, message, pipeline, inputCoordFile, outputCoordFile, inputMTZFile, outputMTZFile, 
		runDirectory, logFile, commandLine, rValueStart, rValueEnd, rFreeValueStart, rFreeValueEnd, starttime, endtime) 
      VALUES (
        p_id, 
        p_parentId, 
        p_success, 
        substr(p_message, 1, 255),
        substr(p_pipeline, 1, 50),
        substr(p_inputCoordFile, 1, 255),
        substr(p_outputCoordFile, 1, 255),
        substr(p_inputMTZFile, 1, 255),
        substr(p_outputMTZFile, 1, 255),
        substr(p_runDirectory, 1, 255),
        substr(p_logFile, 1, 255),
        substr(p_commandLine, 1, 255),
        p_rValueStart, 
        p_rValueEnd, 
        p_rFreeValueStart, 
        p_rFreeValueEnd, 
        IFNULL(p_starttime, NOW()), 
        p_endtime)
		ON DUPLICATE KEY UPDATE
			autoProcScalingId = IFNULL(p_parentId, autoProcScalingId), 
            success = IFNULL(p_success, success), 
            message = IFNULL(substr(p_message, 1, 255), message), 
            pipeline = IFNULL(substr(p_pipeline, 1, 50), pipeline), 
            inputCoordFile = IFNULL(substr(p_inputCoordFile, 1, 255), inputCoordFile), 
            outputCoordFile = IFNULL(substr(p_outputCoordFile, 1, 255), outputCoordFile), 
            inputMTZFile = IFNULL(substr(p_inputMTZFile, 1, 255), inputMTZFile), 
            outputMTZFile = IFNULL(substr(p_outputMTZFile, 1, 255), outputMTZFile), 
            runDirectory = IFNULL(substr(p_runDirectory, 1, 255), runDirectory), 
            logFile = IFNULL(substr(p_logFile, 1, 255), logFile), 
            commandLine = IFNULL(substr(p_commandLine, 1, 255), commandLine), 
            rValueStart = IFNULL(p_rValueStart, rValueStart), 
            rValueEnd = IFNULL(p_rValueEnd, rValueEnd), 
            rFreeValueStart = IFNULL(p_rFreeValueStart, rFreeValueStart), 
            rFreeValueEnd = IFNULL(p_rFreeValueEnd, rFreeValueEnd), 
            starttime = IFNULL(p_starttime, starttime), 
            endtime = IFNULL(p_endtime, endtime);
 
 	  IF p_id IS NULL THEN 
		SET p_id = LAST_INSERT_ID();
      END IF;
	ELSE
	  SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument p_parentId can not be NULL';
	END IF;
  END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `upsert_mrrun_blob` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `upsert_mrrun_blob`(
     INOUT p_id integer,
     p_parentId integer,
     p_view1 varchar(255), 
     p_view2 varchar(255), 
     p_view3 varchar(255) 
  )
    MODIFIES SQL DATA
    COMMENT 'Update or insert new entry with info about views (image paths) for an MX molecular replacement run, e.g. Dimple.'
BEGIN
  IF p_parentId IS NOT NULL THEN
    INSERT INTO MXMRRunBlob (mxMRRunBlobId, mxMRRunId, view1, view2, view3) 
		VALUES (p_id, p_parentId, substr(p_view1, 1, 255), substr(p_view2, 1, 255), substr(p_view3, 1, 255))
		ON DUPLICATE KEY UPDATE
			mxMRRunId = IFNULL(p_parentId, mxMRRunId),
			view1 = IFNULL(substr(p_view1, 1, 255), view1),
			view2 = IFNULL(substr(p_view2, 1, 255), view2),
			view3 = IFNULL(substr(p_view3, 1, 255), view3);

 	IF p_id IS NULL THEN 
		SET p_id = LAST_INSERT_ID();
    END IF;
  ELSE
	SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument p_parentId can not be NULL';
  END IF;  
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `upsert_person` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `upsert_person`(
         INOUT p_id int(10) unsigned,
         p_laboratoryId int(10) unsigned,
         p_familyName varchar(100),
         p_givenName varchar(45),
         p_title varchar(45),
         p_emailAddress varchar(60),
         p_phoneNumber varchar(45),
         p_login varchar(45),
         p_externalPkId int(11) unsigned,
         p_externalPkUUID varchar(32)
 )
    MODIFIES SQL DATA
    COMMENT 'Inserts or updates info about a person (p_id).\nMandatory columns:\nFor insert: login\nFor update: p_id \nReturns: Record ID in p_id.'
BEGIN
        IF p_id is NOT NULL THEN
                UPDATE Person SET
                                        laboratoryId = IFNULL(p_laboratoryId, laboratoryId),
                                        familyName = IFNULL(p_familyName, familyName),
                                        givenName = IFNULL(p_givenName, givenName),
                                        title = IFNULL(p_title, title),
                                        emailAddress = IFNULL(p_emailAddress, emailAddress),
                                        phoneNumber = IFNULL(p_phoneNumber, phoneNumber),
                                        login = IFNULL(p_login, login),
                                        siteId = IFNULL(p_externalPkId, siteId),
                                        externalId = IFNULL(p_externalPkUUID, externalId)
                WHERE personId = p_id;
        ELSEIF p_login IS NOT NULL THEN
        INSERT INTO Person(personId, laboratoryId, familyName, givenName, title, emailAddress, phoneNumber, login, siteId, externalId)
                  VALUES (p_id, p_laboratoryId, p_familyName, p_givenName, p_title, p_emailAddress, p_phoneNumber, p_login, p_externalPkId, p_externalPkUUID);

                SET p_id = LAST_INSERT_ID();
        ELSE
                SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument is NULL: p_id OR p_login must be non-NULL.';
        END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `upsert_processing` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `upsert_processing`(
     INOUT p_id int(10) unsigned,
     p_parentId int(10) unsigned,
     p_spacegroup varchar(45), 
     p_refinedcell_a float, 
     p_refinedcell_b float, 
     p_refinedcell_c float, 
     p_refinedcell_alpha float, 
     p_refinedcell_beta float, 
     p_refinedcell_gamma float 
  )
    MODIFIES SQL DATA
    COMMENT 'Inserts or updates existing row in AutoProc.'
BEGIN
    INSERT INTO AutoProc (autoProcId, autoProcProgramId, spacegroup, refinedcell_a, refinedcell_b, refinedcell_c, refinedcell_alpha, refinedcell_beta, refinedcell_gamma, recordtimestamp) 
      VALUES (p_id, p_parentId, p_spacegroup, p_refinedcell_a, p_refinedcell_b, p_refinedcell_c, p_refinedcell_alpha, p_refinedcell_beta, p_refinedcell_gamma, now())
	  ON DUPLICATE KEY UPDATE
		autoProcProgramId = IFNULL(p_parentId, autoProcProgramId), 
		spacegroup = IFNULL(p_spacegroup, spacegroup), 
        refinedcell_a = IFNULL(p_refinedcell_a, refinedcell_a), 
        refinedcell_b = IFNULL(p_refinedcell_b, refinedcell_b), 
        refinedcell_c = IFNULL(p_refinedcell_c, refinedcell_c), 
        refinedcell_alpha = IFNULL(p_refinedcell_alpha, refinedcell_alpha),
		refinedcell_beta = IFNULL(p_refinedcell_beta, refinedcell_beta),
        refinedcell_gamma = IFNULL(p_refinedcell_gamma, refinedcell_gamma);

	IF p_id IS NULL THEN 
		SET p_id = LAST_INSERT_ID();
    END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `upsert_processing_integration` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `upsert_processing_integration`(
     INOUT p_id integer unsigned,
     p_parentId integer unsigned,
     p_datacollectionId integer unsigned,
     p_programRunId integer unsigned,
     p_startImageNumber integer,
     p_endImageNumber integer,
     p_refinedDetectorDistance float,
     p_refinedXBeam float,
     p_refinedYBeam float,
     p_rotationAxisX float,
     p_rotationAxisY float,
     p_rotationAxisZ float,
     p_beamVectorX float,
     p_beamVectorY float,
     p_beamVectorZ float,
     p_cell_a float,
     p_cell_b float,
     p_cell_c float,
     p_cell_alpha float,
     p_cell_beta float,
     p_cell_gamma float,
     p_anomalous float
  )
    MODIFIES SQL DATA
    COMMENT 'Inserts/updates row in AutoProcIntegration, ID returned in p_id.'
BEGIN
      INSERT INTO AutoProcIntegration (autoProcIntegrationId, datacollectionId, autoProcProgramId, startImageNumber, endImageNumber, 
        refinedDetectorDistance, refinedXBeam, refinedYBeam, rotationAxisX, rotationAxisY, rotationAxisZ, beamVectorX, beamVectorY, beamVectorZ, 
        cell_a, cell_b, cell_c, cell_alpha, cell_beta, cell_gamma, anomalous, recordTimeStamp)
        VALUES (p_id, p_datacollectionId, p_programRunId, p_startImageNumber, p_endImageNumber, 
			p_refinedDetectorDistance, p_refinedXBeam, p_refinedYBeam, p_rotationAxisX, p_rotationAxisY, p_rotationAxisZ, 
			p_beamVectorX, p_beamVectorY, p_beamVectorZ, p_cell_a, p_cell_b, p_cell_c, p_cell_alpha, p_cell_beta, p_cell_gamma, p_anomalous, now())
	    ON DUPLICATE KEY UPDATE
			datacollectionId = IFNULL(p_datacollectionId, datacollectionId), 
			autoProcProgramId = IFNULL(p_programRunId, autoProcProgramId), 
			startImageNumber = IFNULL(p_startImageNumber, startImageNumber), 
			endImageNumber = IFNULL(p_endImageNumber, endImageNumber), 
			refinedDetectorDistance = IFNULL(p_refinedDetectorDistance, refinedDetectorDistance), 
			refinedXBeam = IFNULL(p_refinedXBeam, refinedXBeam), 
			refinedYBeam = IFNULL(p_refinedYBeam, refinedYBeam), 
			rotationAxisX = IFNULL(p_rotationAxisX, rotationAxisX), 
			rotationAxisY = IFNULL(p_rotationAxisY, rotationAxisY),  
			rotationAxisZ = IFNULL(p_rotationAxisZ, rotationAxisZ), 
			beamVectorX = IFNULL(p_beamVectorX, beamVectorX), 
			beamVectorY = IFNULL(p_beamVectorY, beamVectorY), 
			beamVectorZ = IFNULL(p_beamVectorZ, beamVectorZ), 
			cell_a = IFNULL(p_cell_a, cell_a), 
			cell_b = IFNULL(p_cell_b, cell_b), 
			cell_c = IFNULL(p_cell_c, cell_c), 
			cell_alpha = IFNULL(p_cell_alpha, cell_alpha), 
			cell_beta = IFNULL(p_cell_beta, cell_beta), 
			cell_gamma = IFNULL(p_cell_gamma, cell_gamma), 
			anomalous = IFNULL(p_anomalous, anomalous);

	IF p_id IS NULL THEN 
		SET p_id = LAST_INSERT_ID();
    END IF;
      
    
    IF p_parentId IS NOT NULL THEN
	  IF p_id IS NULL THEN
		INSERT INTO AutoProcScaling_has_Int (autoProcScalingId, autoProcIntegrationId, recordTimeStamp)
			VALUES (p_parentId, p_id, now());
	  ELSE 
		DELETE FROM AutoProcScaling_has_Int WHERE autoProcIntegrationId = p_id;
		INSERT INTO AutoProcScaling_has_Int (autoProcScalingId, autoProcIntegrationId, recordTimeStamp)
			VALUES (p_parentId, p_id, now());
	  END IF;
	END IF;
  END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `upsert_processing_job` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `upsert_processing_job`(
     INOUT p_id int(11) unsigned,
	 p_dataCollectionId int(11) unsigned,
     p_displayName varchar(80),
     p_comments varchar(255),
     p_recipe varchar(50),
     p_automatic tinyint(1)
  )
    MODIFIES SQL DATA
    COMMENT 'If p_id is not provided, inserts new row. Otherwise updates exis'
BEGIN
  IF p_id IS NOT NULL OR p_dataCollectionId IS NOT NULL THEN
    INSERT INTO ProcessingJob (
      processingJobId, dataCollectionId, displayName, comments, recipe, automatic) 
	VALUES (
	  p_id, p_dataCollectionId, p_displayName, p_comments, p_recipe, p_automatic)
	ON DUPLICATE KEY UPDATE
      dataCollectionId = IFNULL(p_dataCollectionId, dataCollectionId),
      displayName = IFNULL(p_displayName, displayName),
      comments = IFNULL(p_comments, comments),
      recipe = IFNULL(p_recipe, recipe),
      automatic = IFNULL(p_automatic, automatic);
	IF p_id IS NULL THEN 
      SET p_id = LAST_INSERT_ID();
    END IF;
  ELSE
    SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument(s) p_id and/or p_dataCollectionId are NULL';  
  END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `upsert_processing_job_image_sweep` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `upsert_processing_job_image_sweep`(
     INOUT p_id int(11) unsigned,
	 p_processingJobId int(11) unsigned,
	 p_dataCollectionId int(11) unsigned,
     p_startImage mediumint(8) unsigned,
     p_endImage mediumint(8) unsigned
  )
    MODIFIES SQL DATA
    COMMENT 'If p_id is not provided, inserts new row. Otherwise updates exis'
BEGIN
  IF p_id IS NOT NULL OR (p_processingJobId IS NOT NULL AND p_dataCollectionId IS NOT NULL) THEN
    INSERT INTO ProcessingJobImageSweep (
      processingJobImageSweepId, processingJobId, dataCollectionId, startImage, endImage) 
	VALUES (
	  p_id, p_processingJobId, p_dataCollectionId, p_startImage, p_endImage)
	ON DUPLICATE KEY UPDATE
      processingJobId = IFNULL(p_processingJobId, processingJobId),
      dataCollectionId = IFNULL(p_dataCollectionId, dataCollectionId),
      startImage = IFNULL(p_startImage, startImage),
      endImage = IFNULL(p_endImage, endImage);
	IF p_id IS NULL THEN 
      SET p_id = LAST_INSERT_ID();
    END IF;
  ELSE
	SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument(s) p_id and/or p_processingJobId + p_dataCollectionId are NULL';  
  END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `upsert_processing_job_parameter` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE PROCEDURE `upsert_processing_job_parameter`(
     INOUT p_id int(11) unsigned,
	 p_processingJobId int(11) unsigned,
     p_parameterKey varchar(80),
     p_parameterValue varchar(1024)
  )
    MODIFIES SQL DATA
    COMMENT 'If p_id is not provided, inserts new row. Otherwise updates existing row.'
BEGIN
  IF p_id IS NOT NULL OR p_processingJobId IS NOT NULL THEN
    INSERT INTO ProcessingJobParameter (
      processingJobParameterId, processingJobId, parameterKey, parameterValue) 
	VALUES (
	  p_id, p_processingJobId, p_parameterKey, p_parameterValue)
	ON DUPLICATE KEY UPDATE
      processingJobId = IFNULL(p_processingJobId, processingJobId),
      parameterKey = IFNULL(p_parameterKey, parameterKey),
      parameterValue = IFNULL(p_parameterValue, parameterValue);
	IF p_id IS NULL THEN 
      SET p_id = LAST_INSERT_ID();
    END IF;
  ELSE
    SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument(s) p_id and/or p_processingJobId are NULL';  
  END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `upsert_processing_program` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `upsert_processing_program`(
     INOUT p_id int(11) unsigned,
	 p_commandLine varchar(255),
     p_programs varchar(255),
     p_status int(11),
     p_updateMessage varchar(80),
     p_startTimestamp datetime,
     p_updateTimestamp datetime,
     p_environment varchar(255),
	 p_processingJobId int(11) unsigned,
	 p_recordTimestamp datetime
  )
    MODIFIES SQL DATA
    COMMENT 'If p_id is not provided, inserts new row. Otherwise updates exis'
BEGIN
	DECLARE row_processingStatus tinyint(1) DEFAULT NULL;
	DECLARE row_processingEndTime datetime DEFAULT NULL;
	
    
    
	IF p_id IS NULL THEN
        
	    INSERT INTO AutoProcProgram (processingStatus, processingStartTime, processingEndTime, processingMessage, processingJobId,
		  processingCommandLine, processingPrograms, processingEnvironment, recordTimestamp)
		  VALUES (
              p_status, 
              p_startTimestamp,
              p_updateTimestamp,
              p_updateMessage, 
              p_processingJobId, 
              p_commandLine,
              p_programs,
              p_environment,
              
              IFNULL(p_recordTimestamp, NOW())
		  );
        SET p_id = LAST_INSERT_ID();
	ELSE
		START TRANSACTION;
	    SELECT processingStatus, processingEndTime INTO row_processingStatus, row_processingEndTime 
		FROM AutoProcProgram 
        WHERE autoProcProgramId = p_id;

          
          
          
          
		IF row_processingStatus IS NULL AND (
            row_processingEndTime IS NULL OR p_updateTimestamp IS NULL OR 
              row_processingEndTime <= p_updateTimestamp OR p_status IS NOT NULL) THEN 

		    UPDATE AutoProcProgram 
            SET 
              
              processingStatus = p_status,
			  
			  
              processingStartTime = COALESCE(processingStartTime, p_startTimestamp, NOW()),
              
              processingEndTime = IFNULL(p_updateTimestamp, NOW()), 
              
              processingMessage = IFNULL(p_updateMessage, processingMessage), 
              processingJobId = IFNULL(p_processingJobId, processingJobId),
              processingCommandLine = IFNULL(p_commandLine, processingCommandLine),
              processingPrograms = IFNULL(p_programs, processingPrograms),
			  processingEnvironment = IFNULL(p_environment, processingEnvironment)
		    WHERE autoProcProgramId = p_id;
        END IF;
        COMMIT;
    END IF;

    COMMIT;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `upsert_processing_program_attachment` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `upsert_processing_program_attachment`(
     INOUT p_id int(10) unsigned,
     p_parentid int(10) unsigned,
     p_name varchar(255),
     p_path varchar(255),
     p_type enum('Log','Result','Graph')
  )
    MODIFIES SQL DATA
    COMMENT 'Inserts or updates existing row in AutoProcProgramAttachment. Pa'
BEGIN
	IF NOT (p_parentid IS NULL) THEN
      INSERT INTO AutoProcProgramAttachment (autoProcProgramAttachmentId, autoProcProgramId, filename, filepath, filetype, recordtimestamp)
          VALUES (p_id, p_parentid, p_name, p_path, p_type, now())
          ON DUPLICATE KEY UPDATE
		autoProcProgramId = IFNULL(p_parentid, autoProcProgramId),
        filename = IFNULL(p_name, filename),
        filepath = IFNULL(p_path, filepath),
        filetype = IFNULL(p_type, filetype);

	  IF p_id IS NULL THEN 
		SET p_id = LAST_INSERT_ID();
      END IF;
	ELSE 
      SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument p_parentid is NULL';
    END IF;      
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `upsert_processing_program_attachment_v2` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE PROCEDURE `upsert_processing_program_attachment_v2`(
     INOUT p_id int(10) unsigned,
     p_parentid int(10) unsigned,
     p_name varchar(255),
     p_path varchar(255),
     p_type enum('Log','Result','Graph', 'Debug'),
     p_importanceRank tinyint unsigned
  )
    MODIFIES SQL DATA
    COMMENT 'Inserts or updates existing row in AutoProcProgramAttachment. Pa'
BEGIN
  IF NOT (p_parentid IS NULL) THEN
    INSERT INTO AutoProcProgramAttachment (autoProcProgramAttachmentId, autoProcProgramId, filename, filepath, filetype, importanceRank, recordtimestamp)
      VALUES (p_id, p_parentid, p_name, p_path, p_type, p_importanceRank, now())
      ON DUPLICATE KEY UPDATE
		      autoProcProgramId = IFNULL(p_parentid, autoProcProgramId),
          filename = IFNULL(p_name, filename),
          filepath = IFNULL(p_path, filepath),
          filetype = IFNULL(p_type, filetype),
          importanceRank = IFNULL(p_importanceRank, importanceRank);

	  IF p_id IS NULL THEN
		  SET p_id = LAST_INSERT_ID();
    END IF;
	ELSE
      SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument p_parentid is NULL';
  END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `upsert_processing_program_message` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE PROCEDURE `upsert_processing_program_message`(
     INOUT p_id int(10) unsigned,
     p_programId int(10) unsigned,
     p_severity varchar(255),
     p_message varchar(255),
     p_description text
  )
    MODIFIES SQL DATA
    COMMENT 'Inserts or updates existing row in AutoProcProgramMessage.'
BEGIN
  IF p_id IS NULL AND NOT (p_programId IS NULL) THEN
    INSERT INTO AutoProcProgramMessage (autoProcProgramMessageId, autoProcProgramId, severity, message, description)
      VALUES (p_id, p_programId, p_severity, p_message, p_description);
    SET p_id = LAST_INSERT_ID();
  ELSEIF NOT (p_id IS NULL) THEN
    UPDATE AutoProcProgramMessage
      SET
		    autoProcProgramId = IFNULL(p_programId, autoProcProgramId),
        severity = IFNULL(p_severity, severity),
        message = IFNULL(p_message, message),
        description = IFNULL(p_description, description)
      WHERE
        autoProcProgramMessageId = p_id;
	ELSE
      SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Both arguments p_id and p_programId cannot be NULL';
  END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `upsert_proposal` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `upsert_proposal`(
	 INOUT p_id int(11) unsigned,
	 p_personId int(11) unsigned,
	 p_title varchar(200),
	 p_proposalCode varchar(45),
	 p_proposalNumber int(11) unsigned,
	 p_proposalType varchar(2),
   p_externalPkUUID varchar(32)
 )
    MODIFIES SQL DATA
    COMMENT 'Inserts or updates info about a proposal (p_id).\nMandatory columns:\nFor insert: p_personId AND p_proposalCode AND p_proposalNumber\nFor update: p_id \nReturns: Record ID in p_id.'
BEGIN

IF p_id IS NOT NULL OR (p_personId IS NOT NULL AND p_proposalCode IS NOT NULL AND p_proposalNumber IS NOT NULL)  THEN

  INSERT INTO Proposal (proposalId, personId, title, proposalCode, proposalNumber, proposalType, externalId)
    VALUES (p_id, p_personId, p_title, p_proposalCode, p_proposalNumber, p_proposalType, unhex(p_externalPkUUID))
    ON DUPLICATE KEY UPDATE
      personId = IFNULL(p_personId, personId),
      title = IFNULL(p_title, title),
      proposalCode = IFNULL(p_proposalCode, proposalCode),
      proposalNumber = IFNULL(p_proposalNumber, proposalNumber),
      proposalType = IFNULL(p_proposalType, proposalType),
      externalId = IFNULL(unhex(p_externalPkUUID), externalId);

  IF p_id IS NULL THEN
    SET p_id = LAST_INSERT_ID();
  END IF;
ELSE
  SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument(s) are NULL: p_id OR (p_personId AND p_proposalCode AND p_proposalNumber) must be non-NULL.';
END IF;

END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `upsert_proposal_has_person` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `upsert_proposal_has_person`(
         INOUT p_id int(10) unsigned,
         p_proposalId int(10) unsigned,
         p_personId int(10) unsigned,
         p_role varchar(100)
 )
    MODIFIES SQL DATA
    COMMENT 'Inserts or updates info about a proposal - person association (p_id).\nMandatory columns:\nFor insert: p_proposalId, p_personId\nFor update: p_id\nReturns: Record ID in p_id.'
BEGIN
        IF p_id IS NOT NULL OR (p_proposalId IS NOT NULL AND p_personId IS NOT NULL) THEN
                INSERT INTO ProposalHasPerson(proposalId, personId, `role`)
                        VALUES (p_proposalId, p_personId, p_role)
                        ON DUPLICATE KEY UPDATE
                                `role` = IFNULL(p_role, `role`);

                IF p_id IS NULL THEN
                        SET p_id = LAST_INSERT_ID();
                END IF;

        ELSE
                SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument(s) are NULL: p_id OR (p_proposalId AND p_personId) must be non-NULL.';
        END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `upsert_quality_indicators` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `upsert_quality_indicators`(
  OUT p_id int(11) unsigned,
  p_dataCollectionId int(11) unsigned, 
  p_autoProcProgramId int(10) unsigned, 
  p_imageNumber mediumint(8) unsigned,
  p_spotTotal int(10),
  p_inResTotal int(10),
  p_goodBraggCandidates int(10),
  p_iceRings int(10),
  p_method1Res float,
  p_method2Res float,
  p_maxUnitCell float,
  p_pctSaturationTop50Peaks float,
  p_inResolutionOvrlSpots int(10),
  p_binPopCutOffMethod2Res float,
  p_totalIntegratedSignal double,
  p_dozorScore double,
  p_driftFactor float
)
    MODIFIES SQL DATA
    COMMENT 'Inserts into or updates a row in the image quality indicators table'
BEGIN
  DECLARE row_DataCollectionId int(11) unsigned DEFAULT NULL;
  DECLARE row_imageNumber mediumint(8) unsigned DEFAULT NULL;
  
  IF (p_dataCollectionId IS NOT NULL AND p_imageNumber IS NOT NULL) THEN
    SELECT dataCollectionId, imageNumber INTO row_DataCollectionId, row_imageNumber FROM ImageQualityIndicators WHERE dataCollectionId = p_dataCollectionId AND imageNumber = p_imageNumber;
    IF row_DataCollectionId IS NULL THEN
        INSERT INTO ImageQualityIndicators (
          dataCollectionId, imageNumber, spotTotal, goodBraggCandidates,  
	      method1Res, method2Res, totalIntegratedSignal, dozor_score, driftFactor) 
        VALUES (
          p_dataCollectionId, p_imageNumber, p_spotTotal, p_goodBraggCandidates, 
          p_method1Res, p_method2Res, p_totalIntegratedSignal, p_dozorScore, p_driftFactor
        );
        SET p_id = 1;
    ELSE
        
        
        UPDATE ImageQualityIndicators 
        SET
          spotTotal = IFNULL(p_spotTotal, spotTotal),
          goodBraggCandidates = IFNULL(p_goodBraggCandidates, goodBraggCandidates),
          method1Res = IFNULL(p_method1Res, method1Res),
          method2Res = IFNULL(p_method2Res, method2Res),
          totalIntegratedSignal = IFNULL(p_totalIntegratedSignal, totalIntegratedSignal),
          dozor_score = IFNULL(p_dozorScore, dozor_score),
          driftFactor = IFNULL(p_driftFactor, driftFactor)
		WHERE dataCollectionId = p_dataCollectionId AND imageNumber = p_imageNumber;
        SET p_id = 1;
    END IF;
  ELSE
	SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory arguments p_dataCollectionId and/or p_imageNumber are NULL';  
  END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `upsert_quality_indicators_dozor_score` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE PROCEDURE `upsert_quality_indicators_dozor_score`(
  OUT p_id int(11) unsigned,
  p_dataCollectionId int(11) unsigned,
  p_imageNumber mediumint(8) unsigned,
  p_dozorScore double
)
    MODIFIES SQL DATA
    COMMENT 'Inserts into or updates a row in the image quality indicators table'
BEGIN
  DECLARE row_dataCollectionId int(11) unsigned DEFAULT NULL;
  DECLARE row_imageNumber mediumint(8) unsigned DEFAULT NULL;
  
  SELECT dataCollectionId, imageNumber INTO row_DataCollectionId, row_imageNumber FROM ImageQualityIndicators WHERE dataCollectionId = p_dataCollectionId AND imageNumber = p_imageNumber;

  IF row_dataCollectionId IS NULL THEN
        INSERT INTO ImageQualityIndicators (dataCollectionId, imageNumber, dozor_score)
          VALUES (p_dataCollectionId, p_imageNumber, p_dozorScore);
        SET p_id = 1;
  ELSE
        UPDATE ImageQualityIndicators
          SET dozor_score = p_dozorScore
        WHERE dataCollectionId = p_dataCollectionId AND imageNumber = p_imageNumber;
        SET p_id = 1;
  END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `upsert_robot_action` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `upsert_robot_action`(
	 INOUT p_id int(11) unsigned,
	 p_sessionId int(11) unsigned,
	 p_sampleId int(11) unsigned,
	 p_actionType varchar(15),
	 p_startTimestamp timestamp,
	 p_endTimestamp timestamp,
	 p_status varchar(24),
	 p_message varchar(255),
	 p_containerLocation smallint,
	 p_dewarLocation smallint,
	 p_sampleBarcode varchar(45),
	 p_snapshotBefore varchar(255),
	 p_snapshotAfter varchar(255)
 )
    MODIFIES SQL DATA
    COMMENT 'Inserts or updates info about a robot action (p_id).\nMandatory c'
BEGIN
	IF p_id IS NOT NULL OR p_sessionId IS NOT NULL THEN
		INSERT INTO RobotAction (robotActionId, blsessionId, blsampleId, actionType, startTimestamp, endTimestamp, status, message,
			containerLocation, dewarLocation, sampleBarcode, xtalSnapshotBefore, xtalSnapshotAfter)
			VALUES (p_id, p_sessionId, p_sampleId, p_actionType, p_startTimestamp, p_endTimestamp, p_status, p_message,
				p_containerLocation, p_dewarLocation, p_sampleBarcode, p_snapshotBefore, p_snapshotAfter)
			ON DUPLICATE KEY UPDATE
				blsessionId = IFNULL(p_sessionId, blsessionId),
				blsampleId = IFNULL(p_sampleId, blsampleId),
				actionType = IFNULL(p_actionType, actionType),
				startTimestamp = IFNULL(p_startTimestamp, startTimestamp),
				endTimestamp = IFNULL(p_endTimestamp, endTimestamp),
				status = IFNULL(p_status, status),
				message = IFNULL(p_message, message),
				containerLocation = IFNULL(p_containerLocation, containerLocation),
				dewarLocation = IFNULL(p_dewarLocation, dewarLocation),
				sampleBarcode = IFNULL(p_sampleBarcode, sampleBarcode),
				xtalSnapshotBefore = IFNULL(p_snapshotBefore, xtalSnapshotBefore),
				xtalSnapshotAfter = IFNULL(p_snapshotAfter, xtalSnapshotAfter);

			IF p_id IS NULL THEN
				SET p_id = LAST_INSERT_ID();
			END IF;
	ELSE
		SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument(s) are NULL: p_id OR p_sessionId must be non-NULL.';
	END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `upsert_sample` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE PROCEDURE `upsert_sample`(
	 INOUT p_id int(10) unsigned,
     p_authLogin varchar(45), 
	   p_crystalId int(10) unsigned,
     p_containerId int(10) unsigned, 
     p_name varchar(45),
     p_code varchar(45),
     p_location varchar(45),
     p_holderLength float, 
     p_loopLength float, 
     p_loopType varchar(45), 
     p_wireWidth float, 
     p_comments varchar(1024),
     p_blSampleStatus varchar(20),
     p_isInSampleChanger boolean 
)
    MODIFIES SQL DATA
    COMMENT 'Inserts or updates info about sample (p_id).'
BEGIN

  DECLARE row_count int unsigned DEFAULT 0;
  DECLARE row_count2 int unsigned DEFAULT 0;

  IF p_authLogin IS NOT NULL AND (p_containerId IS NOT NULL OR p_id IS NOT NULL) THEN

    
    

    SELECT count(*) INTO row_count
    FROM Container c
      INNER JOIN Dewar d ON d.dewarId = c.dewarId
      INNER JOIN Shipping s ON s.shippingId = d.shippingId
      INNER JOIN BLSession bs ON bs.proposalId = s.proposalId
      INNER JOIN Session_has_Person shp ON bs.sessionId = shp.sessionId
      INNER JOIN Person p ON p.personId = shp.personId
    WHERE p.login = p_authLogin AND c.containerId = p_containerId; 

    IF row_count = 0 THEN
      SELECT count(*) INTO row_count2
      FROM Container c
        INNER JOIN BLSession bs ON bs.sessionId = c.sessionId
        INNER JOIN BLSession bs2 ON bs.proposalId = bs2.proposalId
        INNER JOIN Session_has_Person shp ON bs2.sessionId = shp.sessionId
        INNER JOIN Person p ON p.personId = shp.personId
      WHERE p.login = p_authLogin AND c.containerId = p_containerId; 

      IF row_count2 = 0 THEN
        SIGNAL SQLSTATE '02000'
          SET MYSQL_ERRNO=1643, MESSAGE_TEXT = 'Sample not in a container belonging to one of the p_authLogin Person sessions';
      END IF;
    END IF;
  END IF;

  IF p_containerId IS NOT NULL OR p_id IS NOT NULL THEN

    INSERT INTO BLSample (blsampleId, crystalId, containerId, `name`, code, `location`, holderLength, loopLength, loopType, wireWidth, comments, blSampleStatus, isInSampleChanger)
      VALUES (p_id, p_crystalId, p_containerId, p_name, p_code, p_location, p_holderLength, p_loopLength, p_loopType, p_wireWidth, p_comments, p_blSampleStatus, p_isInSampleChanger)
      ON DUPLICATE KEY UPDATE
		    crystalId = IFNULL(p_crystalId, crystalId),
        containerId = IFNULL(p_containerId, containerId), 
        `name` = IFNULL(p_name, `name`), 
        `code` = IFNULL(p_code, `code`), 
        location = IFNULL(p_location, location), 
        holderLength = IFNULL(p_holderLength, holderLength), 
        loopLength = IFNULL(p_loopLength, loopLength), 
        wireWidth = IFNULL(p_wireWidth, wireWidth), 
        comments = IFNULL(p_comments, comments), 
        blSampleStatus = IFNULL(p_blSampleStatus, blSampleStatus), 
        isInSampleChanger = IFNULL(p_isInSampleChanger, isInSampleChanger);

    IF p_id IS NULL THEN 
	    SET p_id = LAST_INSERT_ID();
    END IF;

  ELSE
    SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument is NULL: p_id or p_containerId must be non-NULL.';

  END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `upsert_sample_image` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE PROCEDURE `upsert_sample_image`(
     INOUT p_id int(11) unsigned,
     p_sampleId int(11) unsigned,
     p_containerInspectionId int(11) unsigned,
     p_micronsPerPixelX float,
     p_micronsPerPixelY float,
     p_imageFullPath varchar(255),
     p_comments varchar(255)
  )
    MODIFIES SQL DATA
    COMMENT 'If p_id is not provided, inserts new row and returns ID in p_id. Otherwise updates existing row.'
BEGIN
	IF p_id IS NULL THEN
    INSERT INTO BLSampleImage (blSampleId, containerInspectionId, micronsPerPixelX, micronsPerPixelY, imageFullPath, comments, blTimeStamp)
            VALUES (p_sampleId, p_containerInspectionId, p_micronsPerPixelX, p_micronsPerPixelY, p_imageFullPath, p_comments, current_timestamp);
    SET p_id = LAST_INSERT_ID();

  ELSE
    UPDATE BLSampleImage
    SET
      blSampleId = IFNULL(p_sampleId, blSampleId),
      containerInspectionId = IFNULL(p_containerInspectionId, containerInspectionId),
      micronsPerPixelX = IFNULL(p_micronsPerPixelX, micronsPerPixelX),
      micronsPerPixelY = IFNULL(p_micronsPerPixelY, micronsPerPixelY),
      imageFullPath = IFNULL(p_imageFullPath, imageFullPath),
      comments = IFNULL(p_comments, comments)
    WHERE blSampleImageId = p_id;
  END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `upsert_sample_image_analysis` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `upsert_sample_image_analysis`(
	 INOUT p_id int(11) unsigned,
     p_containerBarcode varchar(45),
     p_sampleLocation varchar(45),
     p_oavSnapshotBefore varchar(255),
     p_oavSnapshotAfter varchar(255),
     p_deltaX int,
     p_deltaY int,
     p_goodnessOfFit float,
     p_scaleFactor float,
     p_resultCode varchar(15),
     p_matchStartTS timestamp,
     p_matchEndTS timestamp
     )
    MODIFIES SQL DATA
    COMMENT 'Insert or update info about the sample image analysis for the mo'
BEGIN
      DECLARE row_sampleImageId int(11) unsigned;
      
      IF (p_containerBarcode IS NOT NULL) AND (p_sampleLocation IS NOT NULL) THEN

        SELECT max(blsi.blsampleImageId) INTO row_sampleImageId
        FROM BLSampleImage blsi 
          INNER JOIN BLSample bls ON bls.blsampleId = blsi.blSampleId 
          INNER JOIN Container c ON c.containerId = bls.containerId 
        WHERE c.barcode = p_containerBarcode AND bls.location = p_sampleLocation;

	
        
        
      
        IF row_sampleImageId is NOT NULL THEN
  
          INSERT INTO BLSampleImageAnalysis (blSampleImageAnalysisId, blSampleImageId, oavSnapshotBefore, oavSnapshotAfter, deltaX, deltaY, 
	        goodnessOfFit, scaleFactor, resultCode, matchStartTimeStamp, matchEndTimeStamp) 
	        VALUES (p_id, row_sampleImageId, p_oavSnapshotBefore, p_oavSnapshotAfter, p_deltaX, p_deltaY, 
              p_goodnessOfFit, p_scaleFactor, p_resultCode, p_matchStartTS, p_matchEndTS)
	        ON DUPLICATE KEY UPDATE
		      blSampleImageId = IFNULL(row_sampleImageId, blSampleImageId),
              oavSnapshotBefore = IFNULL(p_oavSnapshotBefore, oavSnapshotBefore),
              oavSnapshotAfter = IFNULL(p_oavSnapshotAfter, oavSnapshotAfter),
              deltaX = IFNULL(p_deltaX, deltaX),
              deltaY = IFNULL(p_deltaY, deltaY),
              goodnessOfFit = IFNULL(p_goodnessOfFit, goodnessOfFit),
              scaleFactor = IFNULL(p_scaleFactor, scaleFactor),
              resultCode = IFNULL(p_resultCode, resultCode),
              matchStartTimeStamp = IFNULL(p_matchStartTS, matchStartTimeStamp),
              matchEndTimeStamp = IFNULL(p_matchEndTS, matchEndTimeStamp);

	      IF p_id is NULL THEN 
		    SET p_id = LAST_INSERT_ID();
          END IF;      
        END IF;
      END IF;
  END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `upsert_sample_image_auto_score` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE PROCEDURE `upsert_sample_image_auto_score`(
     p_imageFullPath varchar(255),
     p_schemaName varchar(25),
     p_scoreClass varchar(15),
     p_probability float
)
    MODIFIES SQL DATA
    COMMENT 'Insert or update a row with the auto scored probability for a given sample image with a certain class and schema. Returns nothing.'
BEGIN
    DECLARE l_blSampleImageId int(11) unsigned;
    DECLARE l_blSampleImageAutoScoreClassId tinyint(3) unsigned;

	  IF p_imageFullPath IS NOT NULL AND p_schemaName IS NOT NULL AND p_scoreClass IS NOT NULL THEN

        SELECT max(blSampleImageId) INTO l_blSampleImageId FROM BLSampleImage WHERE imageFullPath = p_imageFullPath;

        SELECT blSampleImageAutoScoreClassId INTO l_blSampleImageAutoScoreClassId FROM BLSampleImageAutoScoreClass bsiasc INNER JOIN BLSampleImageAutoScoreSchema bsiass USING(blSampleImageAutoScoreSchemaId)
        WHERE bsiasc.scoreClass = p_scoreClass AND bsiass.schemaName = p_schemaName AND bsiass.enabled > 0;

        INSERT INTO BLSampleImage_has_AutoScoreClass (blSampleImageId, blSampleImageAutoScoreClassId, probability)
          VALUES (l_blSampleImageId, l_blSampleImageAutoScoreClassId, p_probability) ON DUPLICATE KEY UPDATE
              blSampleImageId = IFNULL(l_blSampleImageId, blSampleImageId),
              blSampleImageAutoScoreClassId = IFNULL(l_blSampleImageAutoScoreClassId, blSampleImageAutoScoreClassId),
              probability = IFNULL(p_probability, probability);
    ELSE
        SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Arguments p_imageFullPath, p_schemaName and p_scoreClass cannot be NULL';
	  END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `upsert_session_for_proposal_code_number` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `upsert_session_for_proposal_code_number`(
	 INOUT p_id int(11) unsigned,
	 p_proposalCode varchar(3),
	 p_proposalNumber int(11),
	 p_visitNumber int(10) unsigned,
	 p_beamLineSetupId int(10) unsigned,
	 p_startDate datetime,
	 p_endDate datetime,
	 p_beamlineName varchar(45),
	 p_title varchar(255),
	 p_beamlineOperator varchar(45),
	 p_nbShifts int(10) unsigned,
	 p_scheduled tinyint(1),
	 p_usedFlag tinyint(1),
	 p_comments varchar(255),
	 p_externalPkId int(11) unsigned,
	 p_externalPkUUID varchar(32)
 )
    MODIFIES SQL DATA
    COMMENT 'Inserts or updates a session for a proposal with given code and'
BEGIN
	DECLARE row_proposal_id int(10) unsigned DEFAULT NULL;
	IF p_id IS NOT NULL OR (p_proposalCode IS NOT NULL AND p_proposalNumber IS NOT NULL) THEN
		SELECT min(proposalId) INTO row_proposal_id FROM Proposal WHERE proposalCode=p_proposalCode AND proposalNumber=p_proposalNumber;

	  IF p_id IS NULL THEN
		  INSERT INTO BLSession(sessionId, proposalId, visit_number, beamLineSetupId, startDate, endDate,
			  beamLineName, sessionTitle, beamLineOperator, nbShifts, scheduled, usedFlag, comments, expSessionPk, externalId)
			  VALUES (p_id, row_proposal_id, p_visitNumber, p_beamLineSetupId, p_startDate, p_endDate,
				  p_beamlineName, p_title, p_beamlineOperator, p_nbShifts, p_scheduled, p_usedFlag, p_comments, p_externalPkId, unhex(p_externalPkUUID));
		  SET p_id = LAST_INSERT_ID();

	  ELSEIF p_id IS NOT NULL THEN
	    UPDATE BLSession
			SET
				proposalId = IFNULL(row_proposal_id, proposalId),
				visit_number = IFNULL(p_visitNumber, visit_number),
				beamLineSetupId = IFNULL(p_beamLineSetupId, beamLineSetupId),
				startDate = IFNULL(p_startDate, startDate),
				endDate = IFNULL(p_endDate, endDate),
				beamLineName = IFNULL(p_beamlineName, beamLineName),
				sessionTitle = IFNULL(p_title, sessionTitle),
				beamLineOperator = IFNULL(p_beamlineOperator, beamLineOperator),
				nbShifts = IFNULL(p_nbShifts, nbShifts),
				scheduled = IFNULL(p_scheduled, scheduled),
				usedFlag = IFNULL(p_usedFlag, usedFlag),
				comments = IFNULL(p_comments, comments),
				expSessionPk = IFNULL(p_externalPkId, expSessionPk),
				externalId = IFNULL(unhex(p_externalPkUUID), externalId)
		  WHERE sessionId = p_id;
    END IF;
	ELSE
		SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument(s) are NULL: p_id OR (p_proposalCode AND p_proposalNumber) must be non-NULL.';
	END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `upsert_session_has_person` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `upsert_session_has_person`(
         p_sessionId int(10) unsigned,
         p_personId int(10) unsigned,
         p_role varchar(100),
         p_remote tinyint(1)
 )
    MODIFIES SQL DATA
    COMMENT 'Inserts or updates info about a session - person association (p_sessionId, p_personId).\nMandatory columns:\nFor insert: p_sessionId, p_personId\nFor update: p_sessionId, p_personId\nReturns: Nothing.'
BEGIN
        IF p_sessionId IS NOT NULL AND p_personId IS NOT NULL THEN
                INSERT INTO Session_has_Person(sessionId, personId, `role`, remote)
                        VALUES (p_sessionId, p_personId, p_role, p_remote)
                        ON DUPLICATE KEY UPDATE
                                `role` = IFNULL(p_role, `role`),
                                remote = IFNULL(p_remote, remote);
        ELSE
                SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument(s) are NULL: p_sessionId AND p_personId must be non-NULL.';
        END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `upsert_sleeve` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE PROCEDURE `upsert_sleeve`(INOUT p_id tinyint unsigned, p_location tinyint unsigned, p_lastMovedToFreezer datetime, p_lastMovedFromFreezer datetime)
BEGIN
  IF NOT (p_id IS NULL) THEN
    INSERT INTO Sleeve (sleeveId, location, lastMovedToFreezer, lastMovedFromFreezer) VALUES (p_id, p_location, p_lastMovedToFreezer, p_lastMovedFromFreezer)
    ON DUPLICATE KEY UPDATE
		  location = IFNULL(p_location, location),
      lastMovedToFreezer = IFNULL(p_lastMovedToFreezer, lastMovedToFreezer),
      lastMovedFromFreezer = IFNULL(p_lastMovedFromFreezer, lastMovedFromFreezer);

  ELSE
    SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument is NULL: p_id must be non-NULL.';

  END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `upsert_xfe_fluo_spectrum` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = '' */ ;
DELIMITER ;;
CREATE PROCEDURE `upsert_xfe_fluo_spectrum`(
	 INOUT p_id int(11) unsigned,
	 p_sessionId int(10) unsigned,
	 p_sampleId int(10) unsigned,
	 p_subSampleId int(11) unsigned,
	 p_startTime datetime,
	 p_endTime datetime,
	 p_energy float,
	 p_fileName varchar(255),
	 p_annotatedPymcaSpectrum varchar(255),
	 p_fittedDataFileFullPath varchar(255),
	 p_jpegScanFileFullPath varchar(255),
	 p_scanFileFullPath varchar(255),
	 p_beamSizeHorizontal float,
	 p_beamSizeVertical float,
	 p_exposureTime float,
	 p_transmission float,
	 p_flux double,
	 p_fluxEnd double,
	 p_comments varchar(1024))
    MODIFIES SQL DATA
    COMMENT 'Inserts or updates info about a fluorescence spectrum measuremen'
BEGIN
  IF p_id IS NOT NULL OR p_sessionId IS NOT NULL THEN

      INSERT INTO XFEFluorescenceSpectrum (xfeFluorescenceSpectrumId, sessionId, blSampleId, blSubSampleId, startTime, endTime,
				energy, filename, annotatedPymcaXfeSpectrum, fittedDataFileFullPath,
				jpegScanFileFullPath, scanFileFullPath, beamSizeHorizontal, beamSizeVertical,
				exposureTime, beamTransmission, flux, flux_end, comments)
			  VALUES (p_id, p_sessionId, p_sampleId, p_subSampleId, p_startTime, p_endTime,
					p_energy, p_fileName, p_annotatedPymcaSpectrum, p_fittedDataFileFullPath,
					p_jpegScanFileFullPath, p_scanFileFullPath, p_beamSizeHorizontal, p_beamSizeVertical,
					p_exposureTime, p_transmission, p_flux, p_fluxEnd, p_comments)
				ON DUPLICATE KEY UPDATE
			  		sessionId = IFNULL(p_sessionId, sessionId),
	          blSampleId = IFNULL(p_sampleId, blSampleId),
						blSubSampleId = IFNULL(p_subSampleId, blSubSampleId),
	          startTime = IFNULL(p_startTime, startTime),
	          endTime = IFNULL(p_endTime, endTime),
						energy = IFNULL(p_energy, energy),
						filename = IFNULL(p_fileName, filename),
						annotatedPymcaXfeSpectrum = IFNULL(p_annotatedPymcaSpectrum, annotatedPymcaXfeSpectrum),
						fittedDataFileFullPath = IFNULL(p_fittedDataFileFullPath, fittedDataFileFullPath),
						jpegScanFileFullPath = IFNULL(p_jpegScanFileFullPath, jpegScanFileFullPath),
						scanFileFullPath = IFNULL(p_scanFileFullPath, scanFileFullPath),
						beamSizeHorizontal = IFNULL(p_beamSizeHorizontal, beamSizeHorizontal),
						beamSizeVertical = IFNULL(p_beamSizeVertical, beamSizeVertical),
						exposureTime = IFNULL(p_exposureTime, exposureTime),
						beamTransmission = IFNULL(p_transmission, beamTransmission),
						flux = IFNULL(p_flux, flux),
						flux_end = IFNULL(p_fluxEnd, flux_end),
	          comments = IFNULL(p_comments, comments);

			IF p_id IS NULL THEN
				SET p_id = LAST_INSERT_ID();
			END IF;
	ELSE
		SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument(s) are NULL: p_id OR p_sessionId must be non-NULL.';
	END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `upsert_xray_centring_result` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE PROCEDURE `upsert_xray_centring_result`(
	 INOUT p_id int(11) unsigned,
	 p_gridInfoId int(11) unsigned,
	 p_method varchar(15),
	 p_status varchar(45),
	 p_x float,
	 p_y float
 )
    MODIFIES SQL DATA
    COMMENT 'Inserts or updates info about an x-ray centring result (p_id).\nMandatory columns:\nFor insert: p_gridInfoId and p_status\nFor update: p_id \nReturns: Record ID in p_id.'
BEGIN

	IF p_status IS NOT NULL AND p_id IS NULL AND p_gridInfoId IS NOT NULL THEN
  	INSERT INTO XrayCentringResult (xrayCentringResultId, gridInfoId, method, status, x, y)
	  	VALUES (p_id, p_gridInfoId, p_method, p_status, p_x, p_y);
		SET p_id = LAST_INSERT_ID();
	ELSEIF p_status IS NOT NULL AND p_id IS NOT NULL THEN
	  UPDATE XrayCentringResult
		SET
				gridInfoId = IFNULL(p_gridInfoId, gridInfoId),
				method = IFNULL(p_method, method),
				status = IFNULL(p_status, status),
				x = IFNULL(p_x, x),
				y = IFNULL(p_y, y)
		WHERE xrayCentringResultId = p_id;
	ELSE
		SIGNAL SQLSTATE '45000' SET MYSQL_ERRNO=1644, MESSAGE_TEXT='Mandatory argument(s) are NULL: status AND (p_id OR p_gridInfoId) must be non-NULL.';
	END IF;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `Warnings` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE PROCEDURE `Warnings`()
BEGIN
select * from mysql.user;
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-01-20 16:21:09

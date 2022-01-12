INSERT INTO SchemaStatus (scriptName, schemaStatus) VALUES ('2019_11_07_AutoProcProgramAttachment_importanceRank.sql', 'ONGOING');

ALTER TABLE AutoProcProgramAttachment
    MODIFY `fileType` enum('Log','Result','Graph', 'Debug') DEFAULT NULL COMMENT 'Type of file Attachment',
    ADD `importanceRank` tinyint unsigned COMMENT 'For the particular autoProcProgramId and fileType, indicate the importance of the attachment. Higher numbers are more important';

UPDATE SchemaStatus SET schemaStatus = 'DONE' WHERE scriptName = '2019_11_07_AutoProcProgramAttachment_importanceRank.sql';

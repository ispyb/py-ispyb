INSERT INTO SchemaStatus (scriptName, schemaStatus) VALUES ('2018_09_19_DataCollection_imageDirectory_comment.sql', 'ONGOING');

ALTER TABLE DataCollection MODIFY imageDirectory varchar(255) DEFAULT NULL COMMENT 'The directory where files reside - should end with a slash';

UPDATE SchemaStatus SET schemaStatus = 'DONE' WHERE scriptName = '2018_09_19_DataCollection_imageDirectory_comment.sql';

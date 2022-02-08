INSERT IGNORE INTO SchemaStatus (scriptName, schemaStatus) VALUES ('2019_01_14_ProcessingJobParameter_parameterValue.sql', 'ONGOING');

ALTER TABLE ProcessingJobParameter MODIFY parameterValue varchar(1024);

UPDATE SchemaStatus SET schemaStatus = 'DONE' WHERE scriptName = '2019_01_14_ProcessingJobParameter_parameterValue.sql';

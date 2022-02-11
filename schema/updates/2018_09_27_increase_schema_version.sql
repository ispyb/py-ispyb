INSERT INTO SchemaStatus (scriptName, schemaStatus) VALUES ('2018_09_27_increase_schema_version.sql', 'ONGOING');

UPDATE AdminVar SET `value` = '1.1.0' WHERE `name` = 'schemaVersion';

UPDATE SchemaStatus SET schemaStatus = 'DONE' WHERE scriptName = '2018_09_27_increase_schema_version.sql';

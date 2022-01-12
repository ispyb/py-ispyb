INSERT IGNORE INTO SchemaStatus (scriptName, schemaStatus) VALUES ('2019_05_28_AdminVar_bump_version.sql', 'ONGOING');

UPDATE AdminVar SET `value` = '1.5.2' WHERE `name` = 'schemaVersion';

UPDATE SchemaStatus SET schemaStatus = 'DONE' WHERE scriptName = '2019_05_28_AdminVar_bump_version.sql';


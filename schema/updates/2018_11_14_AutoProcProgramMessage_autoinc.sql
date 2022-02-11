INSERT IGNORE INTO SchemaStatus (scriptName, schemaStatus) VALUES ('2018_11_14_AutoProcProgramMessage_autoinc.sql', 'ONGOING');

ALTER TABLE AutoProcProgramMessage MODIFY autoProcProgramMessageId int(10) unsigned NOT NULL auto_increment;

UPDATE SchemaStatus SET schemaStatus = 'DONE' WHERE scriptName = '2018_11_14_AutoProcProgramMessage_autoinc.sql';

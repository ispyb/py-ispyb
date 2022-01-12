INSERT IGNORE INTO SchemaStatus (scriptName, schemaStatus) VALUES ('2018_11_22_AutoProcProgram_processingStatus_update.sql', 'ONGOING');

UPDATE AutoProcProgram app
  INNER JOIN AutoProcIntegration api USING (autoProcProgramId)
SET app.processingStatus = 1
WHERE app.processingStatus IS NULL;

UPDATE SchemaStatus SET schemaStatus = 'DONE' WHERE scriptName = '2018_11_22_AutoProcProgram_processingStatus_update.sql';

-- CAUTION! DO NOT RUN THIS AS-IS ON LARGE AutoProcProgram tables.
-- Instead of the single CALL on the whole range of IDs, run the CALL on
-- smaller ranges of IDs, one at a time.

INSERT IGNORE INTO SchemaStatus (scriptName, schemaStatus) VALUES ('2018_11_09_AutoProcProgram_update_processing_program.sql', 'ONGOING');

SET @max_id = (SELECT max(autoProcProgramId) FROM AutoProcProgram);
SET @min_id = (SELECT min(autoProcProgramId) FROM AutoProcProgram);
CALL update_processing_program_for_id_range(@min_id, @max_id);

UPDATE SchemaStatus SET schemaStatus = 'DONE' WHERE scriptName = '2018_11_09_AutoProcProgram_update_processing_program.sql';

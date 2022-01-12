INSERT IGNORE INTO SchemaStatus (scriptName, schemaStatus) VALUES ('2018_11_01_AutoProcProgramMessage.sql', 'ONGOING');

CREATE TABLE AutoProcProgramMessage (
  autoProcProgramMessageId int unsigned PRIMARY KEY,
  autoProcProgramId int unsigned,
  recordTimeStamp timestamp DEFAULT current_timestamp,
  severity enum ('ERROR', 'WARNING', 'INFO'),
  message varchar(200),
  description text,
  CONSTRAINT AutoProcProgramMessage_fk1 FOREIGN KEY (autoProcProgramId) REFERENCES AutoProcProgram (autoProcProgramId)
);

UPDATE SchemaStatus SET schemaStatus = 'DONE' WHERE scriptName = '2018_11_01_AutoProcProgramMessage.sql';

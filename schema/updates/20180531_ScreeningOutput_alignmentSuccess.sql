INSERT INTO SchemaStatus (scriptName, schemaStatus) VALUES ('20180531_ScreeningOutput_alignmentSuccess.sql', 'ONGOING');

ALTER TABLE ScreeningOutput
  ADD alignmentSuccess boolean NOT NULL DEFAULT 0;

UPDATE SchemaStatus SET schemaStatus = 'DONE' where scriptName = '20180531_ScreeningOutput_alignmentSuccess.sql';

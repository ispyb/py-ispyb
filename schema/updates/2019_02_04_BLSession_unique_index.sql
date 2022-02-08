INSERT INTO SchemaStatus (scriptName, schemaStatus) VALUES ('2019_02_04_BLSession_unique_index.sql', 'ONGOING');

ALTER TABLE BLSession
  ADD CONSTRAINT UNIQUE INDEX (proposalId, visit_number);

UPDATE SchemaStatus SET schemaStatus = 'DONE' WHERE scriptName = '2019_02_04_BLSession_unique_index.sql';

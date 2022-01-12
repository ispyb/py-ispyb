INSERT INTO SchemaStatus (scriptName, schemaStatus) VALUES ('20180913_BeamCalendar.sql', 'ONGOING');

ALTER table BLSession 
  DROP foreign key IF EXISTS BLSession_ibfk_3,
  DROP column IF EXISTS beamCalendarId;

DROP TABLE IF EXISTS BeamCalendar;

CREATE TABLE BeamCalendar (
  beamCalendarId int(10) unsigned auto_increment,
  run varchar(7) NOT NULL,
  beamStatus varchar(24) NOT NULL,
  startDate datetime NOT NULL,
  endDate dateTime NOT NULL,
  PRIMARY KEY (beamCalendarId)
);

ALTER TABLE BLSession 
  add column beamCalendarId int(10) unsigned after `proposalId`, 
  add constraint BLSession_ibfk_3 FOREIGN KEY (beamCalendarId) REFERENCES BeamCalendar (beamCalendarId);

UPDATE SchemaStatus SET schemaStatus = 'DONE' WHERE scriptName = '20180913_BeamCalendar.sql';

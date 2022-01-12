INSERT INTO SchemaStatus (scriptName, schemaStatus) VALUES ('2018_11_01_XrayCenteringResult.sql', 'ONGOING');

CREATE TABLE XrayCenteringResult (
    xrayCenteringResultId int(11) unsigned auto_increment PRIMARY KEY,
    gridInfoId int(11) unsigned NOT NULL,
    method varchar(15) COMMENT 'Type of X-ray centering calculation',
    status enum('success', 'failure', 'pending') NOT NULL DEFAULT 'pending',
    x float COMMENT 'position in number of boxes in direction of the fast scan within GridInfo grid',
    y float COMMENT 'position in number of boxes in direction of the slow scan within GridInfo grid',
    CONSTRAINT XrayCenteringResult_ibfk_1 FOREIGN KEY (gridInfoId) REFERENCES GridInfo(gridInfoId) ON DELETE CASCADE ON UPDATE CASCADE
);

UPDATE SchemaStatus SET schemaStatus = 'DONE' WHERE scriptName = '2018_11_01_XrayCenteringResult.sql';

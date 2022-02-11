INSERT INTO SchemaStatus (scriptName, schemaStatus) VALUES ('2018_11_05_spelling_of_centring.sql', 'ONGOING');

RENAME TABLE XrayCenteringResult TO XrayCentringResult;
ALTER TABLE XrayCentringResult CHANGE xrayCenteringResultId xrayCentringResultId int(11) unsigned NOT NULL AUTO_INCREMENT;

ALTER TABLE DiffractionPlan CHANGE centeringMethod centringMethod enum('xray','loop','diffraction','optical') DEFAULT NULL

UPDATE SchemaStatus SET schemaStatus = 'DONE' WHERE scriptName = '2018_11_05_spelling_of_centring.sql';

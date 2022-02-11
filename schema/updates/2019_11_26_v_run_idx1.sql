INSERT IGNORE INTO SchemaStatus (scriptName, schemaStatus) VALUES ('2019_11_26_v_run_idx1.sql', 'ONGOING');

CREATE INDEX v_run_idx1 ON v_run(startDate, endDate);

UPDATE SchemaStatus SET schemaStatus = 'DONE' WHERE scriptName = '2019_11_26_v_run_idx1.sql';

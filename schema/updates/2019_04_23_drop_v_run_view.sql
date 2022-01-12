INSERT INTO SchemaStatus (scriptName, schemaStatus) VALUES ('2019_04_23_drop_v_run_view.sql', 'ONGOING');

DROP VIEW IF EXISTS v_run;

UPDATE SchemaStatus SET schemaStatus = 'DONE' WHERE scriptName = '2019_04_23_drop_v_run_view.sql';

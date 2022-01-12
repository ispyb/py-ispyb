-- Create the import application role.
CREATE ROLE IF NOT EXISTS ispyb_import;

-- You must also create a database user and grant this role to them, e.g.
-- CREATE USER ispyb_uo@'%' IDENTIFIED BY 'the_uo_password';
-- GRANT ispyb_import TO ispyb_uo@'%';
-- SET DEFAULT ROLE ispyb_import FOR ispyb_uo@'%';

-- Grants for ispyb_processing
GRANT SELECT ON AdminVar TO 'ispyb_import'; -- Hack TO allow ispyb_import to connect through MaxScale
GRANT EXECUTE ON PROCEDURE retrieve_container_for_barcode TO 'ispyb_import';
GRANT EXECUTE ON PROCEDURE retrieve_container_for_inspection_id TO 'ispyb_import';
GRANT EXECUTE ON PROCEDURE retrieve_sample_for_container_id_and_location TO 'ispyb_import';
GRANT EXECUTE ON PROCEDURE upsert_sample_image TO 'ispyb_import';
GRANT EXECUTE ON PROCEDURE upsert_sample_image_auto_score TO 'ispyb_import';

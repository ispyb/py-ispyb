wget https://github.com/DiamondLightSource/ispyb-database/releases/download/v1.10.4/ispyb-database-1.10.4.tar.gz
tar xvfz ispyb-database-1.10.4.tar.gz
mysql -u root -e "CREATE DATABASE pydb_test; SET GLOBAL log_bin_trust_function_creators=ON;"
mysql -u root -D pydb_test < schema/tables.sql
mysql -u root -D pydb_test < schema/lookups.sql
mysql -u root -D pydb_test < schema/data.sql
mysql -u root -D pydb_test < schema/routines.sql
mysql -u root -e "CREATE USER mxuser@'localhost' IDENTIFIED BY 'mxpass';"
mysql -u root -e "GRANT ALL ON pydb_test.* TO 'mxuser'@'localhost';"

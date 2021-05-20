mysql -u root -e "CREATE DATABASE ispyb_ssx; SET GLOBAL log_bin_trust_function_creators=ON;"
mysql -u root -D ispyb_ssx < ../examples/ispyb_ssx.sql
mysql -u root -e "GRANT ALL ON ispyb_ssx.* TO 'mxuser'@'localhost';"

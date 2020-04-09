import os
import configparser
import MySQLdb

ispyb_root = os.path.dirname(os.path.abspath(__file__)).split(os.sep)
ispyb_root = '/' + os.path.join(*ispyb_root[1:-2])
config_filename = '%s/config.cfg' % ispyb_root

config = configparser.ConfigParser()
config.read(config_filename)
uri = config["general"]["db_uri"]
#mysql://ispyb_api:password_1234@localhost/ispyb_test
user = uri.split('//')[1].split(':')[0]
passwd = uri.split('//')[1].split(':')[1].split('@')[0]
host = uri.split('@')[1].split('/')[0]

connection = MySQLdb.connect(host=host, user=user, passwd=passwd)
cursor = connection.cursor()
cursor.execute("USE ispyb_test")
cursor.execute("SHOW TABLES")
tables = cursor.fetchall()

file_header = """
from marshmallow import Schema, fields as ma_fields
from flask_restplus import f_fields

"""

gen_tables = ['Proposal']

for table in tables:
    table_name = table[0]
    if table_name in gen_tables:
        print('Generting ma_model for table %s' % table_name)
        cursor.execute("SHOW COLUMNS FROM %s" % table)
        columns = cursor.fetchall()

        schema_filename = "%s/ispyb/schemas/%s-test.py" % (ispyb_root, table_name.lower())
        schema_file = open(schema_filename, "w")
        schema_file.write(file_header)
        dict_text = "%s_dict = {\n" % table_name.lower()
        for column in columns:
            print(column)
            column_name = column[0]
            description = None
            if 'int' in column[1]:
                column_datatype = 'Integer'
            elif 'varchar' in column[1]:
                column_datatype = 'String'
            elif 'timestamp' in column[1]:
                column_datatype = 'DateTime'
            dict_text += "        '%s': f_fields.%s(" % (column_name, column_datatype)
            if description:
                dict_text += "description='%s'),\n" % description
            else:
                dict_text += "),\n"
        dict_text += "        }"
        schema_file.write(dict_text)
        schema_file.close()

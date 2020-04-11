import os
import re
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

schema_file_header = """
from marshmallow import Schema, fields as ma_fields
from flask_restplus import fields as f_fields

"""

init_file_path = "%s/ispyb/schemas/__init__.py" % ispyb_root
init_file = open(init_file_path, "w")
init_file.write("from ispyb import api\n\n")

gen_tables = ['BLSample', 'Person', 'Proposal', 'DataCollection']

for table in tables:
    table_name = table[0]
    if table_name in gen_tables:
        print('Generting ma_model for table %s' % table_name)
        cursor.execute("SHOW COLUMNS FROM %s" % table)
        columns = cursor.fetchall()
        table_name = table_name.replace('BF_', '').replace('BL', '')

        print(table_name)
        schema_name = "_".join(re.findall('[A-Z][^A-Z]*', table_name)).lower()
        dict_text = "%s_dict = {\n" % schema_name
        ma_text = "class %sSchema(Schema):\n" % table_name

        for column in columns:
            column_name = column[0]
            dtype = column[1]#.replace('"', '')
            data_size = '()'
            description = None
            if dtype.startswith('int') or dtype.startswith('binary'):
                column_datatype = 'Integer'
            elif dtype.startswith('varchar'):
                column_datatype = 'String'
                data_size = dtype.replace('varchar', '')
            elif dtype.startswith('timestamp'):
                column_datatype = 'DateTime'
            elif dtype.startswith('enum'):
                column_datatype = 'String'
                #description = dtype
            dict_text += "        '%s': f_fields.%s(" % (column_name, column_datatype)
            if description:
                dict_text += "description='%s'),\n" % description
            else:
                dict_text += "),\n"
            ma_text += "    %s = ma_fields.%s()\n" % (column_name, column_datatype)
        dict_text += "        }\n\n"

        schema_file_path = "%s/ispyb/schemas/%s.py" % (ispyb_root, schema_name)
        schema_file = open(schema_file_path, "w")
        schema_file.write(schema_file_header)
        schema_file.write(dict_text)
        schema_file.write(ma_text)
        schema_file.close()


        init_file.write("from ispyb.schemas.%s import %s_dict, %sSchema\n" % 
                (schema_name, schema_name, table_name))
        init_file.write("f_%s_schema = api.model('%s', %s_dict)\n" % (schema_name, table_name, schema_name))
        init_file.write("ma_%s_schema = %sSchema()\n\n" % (schema_name, table_name))

init_file.close()


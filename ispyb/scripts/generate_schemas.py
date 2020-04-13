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
db_name = uri.split('/')[-1]

connection = MySQLdb.connect(host=host, user=user, passwd=passwd)
cursor = connection.cursor()
cursor.execute("USE %s" % db_name)
cursor.execute("SHOW TABLES")
tables = cursor.fetchall()

schema_file_header = """
from marshmallow import Schema, fields as ma_fields
from flask_restplus import fields as f_fields

"""

init_file_path = "%s/ispyb/schemas/__init__.py" % ispyb_root
init_file = open(init_file_path, "w")
init_file.write("from ispyb import api\n\n")


gen_tables = [
        'AutoProc',
        'AutoProcIntegration',
        'AutoProcProgram',
        'AutoProcProgramAttachment',
        'AutoProcProgramMessage',
        'AutoProcScaling',
        'AutoProcScalingStatistics',
        'AutoProcStatus'
        'BLSample',
        'BLSession',
        'BeamLineSetup',
        'Container',
        'Crystal',
        'DataCollection',
        'DataCollectionGroup',
        'Detector',
        'EnergyScan',
        'ImageQualityIndicators',
        'Person',
        'Proposal',
        'Protein',
        'RobotAction',
        'Screening',
        'Shipping'
        ]


for table in tables:
    table_name = table[0]
    if table_name in gen_tables:
        print('Generting flask and marshmallow models for table %s' % table_name)
        cursor.execute("SHOW FULL COLUMNS FROM %s" % table)
        columns = cursor.fetchall()
        table_name = table_name.replace('BF_', '').replace('BL', '')
        schema_name = "_".join(re.findall('[A-Z][^A-Z]*', table_name)).lower()
        dict_text = "%s_dict = {\n" % schema_name
        ma_text = "class %sSchema(Schema):\n" % table_name

        for column in columns:
            name = column[0]
            data_type = "String"
            data_size = "()"
            required = "required=False"
            if column[3] == "NO":
                required = "required=True"
            #default = None
            #if column[5] != "NULL":
            #    default =
            description = "description='%s'" % column[8].replace("'", "")
            if 'int' in column[1]  or column[1].startswith('binary'):
                data_type = 'Integer'
            elif column[1].startswith('float'):
                data_type = 'Float' 
            elif column[1].startswith('varchar') or column[1].startswith('text'):
                data_type = 'String'
                data_size = column[1].replace('varchar', '')
            elif column[1].startswith('timestamp') or column[1].startswith('datetime'):
                data_type = 'DateTime'
            elif column[1].startswith('enum'):
                data_type = 'String'
                description = "description='%s%s'"  % (column[8].replace("'", ""), column[1].replace("'", ""))
            dict_text += "        '%s': f_fields.%s(%s, %s),\n" % (name, data_type, required, description)
            ma_text += "    %s = ma_fields.%s()\n" % (name, data_type)
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


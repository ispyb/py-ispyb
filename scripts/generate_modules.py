from config import BaseConfig
import os
import re
import sys
import csv
import MySQLdb

ispyb_root = os.path.dirname(os.path.abspath(__file__)).split(os.sep)
ispyb_root = "/" + os.path.join(*ispyb_root[1:-1])
sys.path.insert(0, ispyb_root)


config = BaseConfig()

uri = config.SQLALCHEMY_DATABASE_URI
# mysql://ispyb_api:password_1234@localhost/ispyb_test
user = uri.split("//")[1].split(":")[0]
passwd = uri.split("//")[1].split(":")[1].split("@")[0]
host = uri.split("@")[1].split("/")[0]
db_name = uri.split("/")[-1]

gen_tables = []
gen_modules = []

with open("%s/enabled_db_modules.csv" % ispyb_root) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        gen_modules.append(row[0])
        gen_tables.append(row[1])


connection = MySQLdb.connect(host=host, user=user, passwd=passwd)
cursor = connection.cursor()
cursor.execute("USE %s" % db_name)
cursor.execute("SHOW TABLES")
tables = cursor.fetchall()

schema_file_header = '''"""
ISPyB flask server
"""\n
'''

schema_file_header += """
from marshmallow import Schema, fields as ma_fields
from flask_restx import fields as f_fields

from app.extensions.api import api_v1 as api

"""

for table in tables:
    table_name = table[0]
    if table_name in gen_tables:
        print("Generting flask and marshmallow models for table %s" % table_name)
        cursor.execute("SHOW FULL COLUMNS FROM %s" % table)
        columns = cursor.fetchall()
        table_name = table_name.replace("BF_", "").replace("BL", "")
        schema_name = "_".join(re.findall("[A-Z][^A-Z]*", table_name)).lower()
        dict_text = "%s_dict = {\n" % schema_name
        ma_text = "class %sSchema(Schema):\n" % table_name
        ma_text += (
            '    """Marshmallows schema class representing %s table"""\n\n' % table_name
        )

        for column in columns:
            name = column[0]
            if name == "global":
                name = "Global"
            data_type = "String"
            data_size = "()"
            required = "required=False"
            if column[3] == "NO":
                required = "required=True"
            # default = None
            # if column[5] != "NULL":
            #    default =
            description = "description='%s'" % column[8].replace("'", "")
            if "int" in column[1] or column[1].startswith("binary"):
                data_type = "Integer"
            elif column[1].startswith("float"):
                data_type = "Float"
            elif column[1].startswith("varchar") or column[1].startswith("text"):
                data_type = "String"
                data_size = column[1].replace("varchar", "")
            elif column[1].startswith("timestamp") or column[1].startswith("datetime"):
                data_type = "DateTime"
            elif column[1].startswith("enum"):
                data_type = "String"
                description = "description='%s%s'" % (
                    column[8].replace("'", ""),
                    column[1].replace("'", ""),
                )
            dict_text += "        '%s': f_fields.%s(%s, %s),\n" % (
                name,
                data_type,
                required,
                description,
            )
            ma_text += "    %s = ma_fields.%s()\n" % (name, data_type)
        dict_text += "        }\n\n"

        class_text = "f_%s_schema = api.model('%s', %s_dict)\n" % (
            schema_name,
            table_name,
            schema_name,
        )
        class_text += "ma_%s_schema = %sSchema()\n" % (schema_name, table_name)

        schema_file_path = "%s/app/modules/%s/schemas.py" % (ispyb_root, schema_name)
        if not os.path.exists(os.path.dirname(schema_file_path)):
            os.makedirs(os.path.dirname(schema_file_path))
        schema_file = open(schema_file_path, "w")
        schema_file.write(schema_file_header)
        schema_file.write(dict_text)
        schema_file.write(ma_text)
        schema_file.write("\n")
        schema_file.write(class_text)
        schema_file.write("\n")
        schema_file.close()

        """
        resources_file_path = "%s/app/modules/%s/resources.py" % (
            ispyb_root,
            schema_name,
        )

        if not os.path.exists(resources_file_path):
            resources_file = open(resources_file_path, "w")
            resources_file.write("from flask_restx import Namespace, Resource\n\n")
            resources_file.write(
                "from app.models import %s as %sModel\n" % (table_name, table_name)
            )
            resources_file.write(
                "from app.modules.%s.schemas import f_%s_schema,  ma_%s_schema\n\n\n"
                % (schema_name, schema_name, schema_name)
            )
            resources_file.write(
                "api = Namespace('%s', description='%s related namespace', path='/%s')\n\n\n"
                % (table_name, table_name, schema_name)
            )
            resources_file.write('@api.route("")\n')
            resources_file.write("class %sList(Resource):\n\n" % table_name)
            resources_file.write('    @api.doc(security="apikey")\n')
            resources_file.write("    def get(self):\n")
            resources_file.write(
                "        %s_list = %sModel.query.all()\n" % (schema_name, table_name)
            )
            resources_file.write(
                "        return ma_%s_schema.dump(%s_list)\n"
                % (schema_name, schema_name)
            )
       
        init_file_path = "%s/app/modules/%s/__init__.py" % (ispyb_root, schema_name)
        init_file = open(init_file_path, "w")
        init_file.write('"""ISPyB flask server"""\n\n')
        init_file.write("from app.extensions.api import api_v1\n\n")
        init_file.write("def init_app(app, **kwargs):\n\n")
        init_file.write("    from . import resources\n\n")
        init_file.write("    api_v1.add_namespace(resources.api)")
        init_file.write("\n")
        """

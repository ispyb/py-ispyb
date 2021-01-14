# encoding: utf-8
#
#  Project: py-ispyb
#  https://github.com/ispyb/py-ispyb
#
#  This file is part of py-ispyb software.
#
#  py-ispyb is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  py-ispyb is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with py-ispyb. If not, see <http://www.gnu.org/licenses/>.


import os
import re
import sys
import csv
import MySQLdb

ispyb_root = os.path.dirname(os.path.abspath(__file__)).split(os.sep)
ispyb_root = "/" + os.path.join(*ispyb_root[1:-1])
sys.path.insert(0, ispyb_root)

from pyispyb.config import BaseConfig
config = BaseConfig(os.path.join(ispyb_root, "ispyb_ssx_config.yml"))

uri = config.SQLALCHEMY_DATABASE_URI
# mysql://ispyb_api:password_1234@localhost/ispyb_test
user = uri.split("//")[1].split(":")[0]
passwd = uri.split("//")[1].split(":")[1].split("@")[0]
host = uri.split("@")[1].split("/")[0]
db_name = uri.split("/")[-1]

gen_tables = []
gen_modules = []

with open("%s/scripts/ssx_db_mapping.csv" % ispyb_root) as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        gen_modules.append(row[0])
        gen_tables.append(row[1])
connection = MySQLdb.connect(host=host, user=user, passwd=passwd)
cursor = connection.cursor()
cursor.execute("USE %s" % db_name)
cursor.execute("SHOW TABLES")
tables = cursor.fetchall()

schema_file_header = ""

licence_header_file = open(ispyb_root + "/py_file_header.txt", "r")
schema_file_header = licence_header_file.read()
licence_header_file.close()


schema_file_header += """
from marshmallow import Schema, fields as ma_fields
from flask_restx import fields as f_fields
from marshmallow_jsonschema import JSONSchema

from pyispyb.app.extensions.api import api_v1 as api

"""

print("Generating ssx schemas..")

for table in tables:
    table_name = table[0]
    if table_name in gen_tables:
        cursor.execute("SHOW FULL COLUMNS FROM %s" % table)
        columns = cursor.fetchall()
        table_name = table_name.replace("BF_", "").replace("BL", "")
        schema_name = "_".join(re.findall("[A-Z][^A-Z]*", table_name)).lower()
        print(
            "Generting flask and marshmallow models for table %s in %s"
            % (table_name, schema_name)
        )
        dict_text = "dict_schema = {\n"
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

        class_text = "f_schema = api.model('%s', dict_schema)\n" % (table_name,)
        class_text += "ma_schema = %sSchema()\n" % (table_name)
        json_text = "json_schema = JSONSchema().dump(ma_schema)\n"

        schema_file_path = "%s/pyispyb/ssx/schemas/%s.py" % (ispyb_root, schema_name)
        if not os.path.exists(os.path.dirname(schema_file_path)):
            os.makedirs(os.path.dirname(schema_file_path))
        schema_file = open(schema_file_path, "w")
        schema_file.write(schema_file_header)
        schema_file.write(dict_text)
        schema_file.write(ma_text)
        schema_file.write("\n")
        schema_file.write(class_text)
        schema_file.write(json_text)
        schema_file.close()

print("done")

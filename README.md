# py-ispyb

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/301f7c319e504a94950e7798bdb8cd31)](https://www.codacy.com/manual/IvarsKarpics/py-ispyb?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ispyb/py-ispyb&amp;utm_campaign=Badge_Grade)
[![Build Status](https://travis-ci.org/ispyb/py-ispyb.svg?branch=master)](https://travis-ci.org/ispyb/py-ispyb)
[![codecov](https://codecov.io/gh/ispyb/py-ispyb/branch/master/graph/badge.svg)](https://codecov.io/gh/ispyb/py-ispyb)
[![License: LGPL v3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)


ISPyB backend server based on python flask-restx.


## Dependencies

* [**Python**](https://www.python.org/) 3.5+ / pypy2
* [**flask-restx**](https://github.com/python-restx/flask-restx) (+
  [*flask*](http://flask.pocoo.org/))
* [**sqlalchemy**](http://www.sqlalchemy.org/) (+
  [*flask-sqlalchemy*](http://flask-sqlalchemy.pocoo.org/)) - Database ORM.
* [**marshmallow**](http://marshmallow.rtfd.org/)
* [**ruamel.yaml**] (https://pypi.org/project/ruamel.yaml/)


## How to run py-ispyb

Install requirements:

```bash
sudo pip install -r requirements.txt
```

Copy and edit yaml configuration file:
```bash
cp ispyb_core_config_example.yml ispyb_core_config.yml
```

Regenerate data base models and schemas:
```bash
cd scripts
./generate_core_models.sh
python3 generate_core_schemas.py
cd ..
```

Run application in debug mode:
```bash
python3 wsgi.py

or

invoke app.run
```

## Authentication
JWT (Jason web tokens) are used to authenticate requests. See jwt.io to test the token.

## Status codes
https://www.flaskapi.org/api-guide/status-codes/

## Format code
```bash
autopep8 -a -r -j 0 -i --max-line-length 88 ./
black --safe ./
```


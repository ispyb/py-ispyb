# py-ispyb

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/301f7c319e504a94950e7798bdb8cd31)](https://www.codacy.com/manual/IvarsKarpics/py-ispyb?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ispyb/py-ispyb&amp;utm_campaign=Badge_Grade)
[![Build Status](https://travis-ci.org/ispyb/py-ispyb.svg?branch=master)](https://travis-ci.org/ispyb/py-ispyb)
[![codecov](https://codecov.io/gh/ispyb/py-ispyb/branch/master/graph/badge.svg)](https://codecov.io/gh/ispyb/py-ispyb)
[![License: LGPL v3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)


ISPyB backend server based on python flask-restx.

<p align="center"><img src="https://github.com/ispyb/py-ispyb/blob/master/docs/ispyb_doc.png"/></p>


## Dependencies

* [**Python**](https://www.python.org/) 3.5+ / pypy2
* [**flask-restx**](https://github.com/python-restx/flask-restx) (+
  [*flask*](http://flask.pocoo.org/))
* [**sqlalchemy**](http://www.sqlalchemy.org/) (+
  [*flask-sqlalchemy*](http://flask-sqlalchemy.pocoo.org/)) - Database ORM.
* [**marshmallow**](http://marshmallow.rtfd.org/)


```bash
sudo pip install -r requirements.txt
```

## Deployment

- `python3 wsgi.py`
- `gunicorn wsgi.py`


## Available scripts

- `generate_db_models.sh` : generates sqlalchemy db models.
- `generate_modules.py` :  generates flask api models and marshmallow schemas. Generates a simple resource.py if it does not exist.
- `format_code.sh`: formats code based on autopep and black.

## Authentication
JWT (Jason web tokens) are used to authenticate requests. See jwt.io to test the token.

Status codes: https://www.flaskapi.org/api-guide/status-codes/

## Format code
```bash
autopep8 -a -r -j 0 -i --max-line-length 88 ./
black --safe ./
```


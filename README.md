# py-ispyb

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/2126d052de464a27bf9a60ef27012e2f)](https://app.codacy.com/manual/IvarsKarpics/ispyb_backend_prototype?utm_source=github.com&utm_medium=referral&utm_content=IvarsKarpics/ispyb_backend_prototype&utm_campaign=Badge_Grade_Dashboard)
[![Build Status](https://travis-ci.org/mxcube/mxcube.svg?branch=master)](https://travis-ci.org/IvarsKarpics/ispyb_backend_prototype)
[![codecov](https://codecov.io/gh/IvarsKarpics/ispyb_backend_prototype/branch/master/graph/badge.svg)](https://codecov.io/gh/IvarsKarpics/ispyb_backend_prototype)

ISPyB backend server based on python flask-restx.

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

## Available scripts
```bash
generate_db_models.csh : generates sqlalchemy db models.
generate_modules.py :  generates flask api models and marshmallow schemas. Generates a simple resource.py if it does not exist.
```

## Authentication
JWT (Jason web tokens) are used to authenticate requests. See jwt.io to test the token.

## Format code
```bash
autopep8 -a -r -j 0 -i --max-line-length 88 ./
black --safe ./
```


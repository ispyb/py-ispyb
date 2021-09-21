# py-ispyb

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
* [**ruamel.yaml**](https://pypi.org/project/ruamel.yaml/)


## How to run py-ispyb

### Install requirements

In case of MySQL or MariaDB you might have to install dev tools:

`sudo apt-get install -y python3-mysqldb`

or

`apt-get install libmariadbclient-dev`

Install python dependencies:

`sudo pip install -r requirements.txt`

### Copy and edit yaml configuration file

`cp ispyb_core_config_example.yml ispyb_core_config.yml`

If you do not have a running ispyb database then you can create one by running:

`scripts/create_core_db.sh`

### Regenerate data base models and schemas

```bash
cd scripts
./generate_core_models.sh PATH_TO_CONFIG_FILE.yml
python3 generate_core_schemas.py
cd ..
```

### Run application in debug mode

* `python3 wsgi.py`
* `invoke app.run`

Now you can go to http://localhost:5000/ispyb/api/v1/doc and explore py-ispyb via swagger ui.
For authentication json web tokens (jwt) are used. In the web browser call http://localhost:5000/ispyb/api/v1/auth/login , enter user credentials and retrieve access token from the response:

```bash
{
    "token": "YOUR_JWT_TOKEN",
    "roles": [
        "user"
    ]
}
```

Corresponding curl command:

`curl -u USER:PASS -i -H "Accept:application/json" http://localhost:5000/ispyb/api/v1/auth/login`

In the case of dummy authentication username _user_ will grant _user_ role and _manager_ will grant _user_ and _manager_ roles. 

For requests use the token in the `Authorization` header: `Bearer YOUR_JWT_TOKEN`. For example to retrieve proposals call:

`curl -X GET -H 'Authorization: Bearer YOUR_JWT_TOKEN' -i http://localhost:5000/ispyb/api/v1/proposals`

## Misc

* Swagger documentation: https://raw.githubusercontent.com/ispyb/py-ispyb/master/docs/swagger.json
* For deployment options see `deploy` directory.
* Status codes: https://www.flaskapi.org/api-guide/status-codes/


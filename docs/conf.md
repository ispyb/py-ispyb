Configuration is defined through environment variables.

Ready-to-run preset are defined under `config` for the following environments:

- `config/dev.env`
- `config/test.env`
- `config/ci.env`

These preset are automatically used when the variable `ISPYB_ENVIRONMENT` is set to any of `dev`, `test` or `ci`.  
This variable is already set to the proper value in the development and test scripts.

If `ISPYB_ENVIRONMENT` is unset or empty, the default provided in `config/.env` will be used.

Any setting can be overridden by defining the proper variable environment.

Here are some examples from the `dev` environment:

```bash
SERVICE_NAME=core

API_ROOT=/ispyb/api/v1

QUERY_DEBUG=false

JWT_CODING_ALGORITHM=HS256
TOKEN_EXP_TIME=300

CORS=true

SECRET_KEY=dev_secret

SQLALCHEMY_DATABASE_URI=mysql+mysqlconnector://test:test@127.0.0.1/test

AUTH_CONFIG=auth.yml

```

## ISPYB_DATA_PATH

The env variable `ISPYB_DATA_PATH` allows you to define a path prefix that ISPyB should add to all data files path in the database.

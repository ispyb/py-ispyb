# py-ispyb

ISPyB backend server based on FastAPI.

## Getting started

You need to have `python >= 3.10`.

Install requirements with

```bash
pip install -r requirements.txt
```

Define required environment variables

```bash
export SQLALCHEMY_DATABASE_URI="mysql+mysqlconnector://<user>:<password>@<hostname>/<db_name>"
export SECRET_KEY="changeme"
```

Start the server with

```bash
sh uvicorn.sh
```

You can start using the server through the [OpenAPI documenation](http://localhost:8000/docs)

## Further documentation

Documentation can be found in the `/docs` directory.
A web documentation is available for the latest version at [https://ispyb.github.io/py-ispyb/](https://ispyb.github.io/py-ispyb/).

To serve it locally, follow these steps:

```bash
pip install mkdocs
mkdocs serve
```

Open [http://127.0.0.1:8080/](http://127.0.0.1:8080/)

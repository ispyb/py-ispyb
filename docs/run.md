## How to run py-ispyb

---

### Get project code

Clone [py-ISPyB repository](https://gitlab.esrf.fr/ispyb/py-ispyb)

---

### Install requirements

In order to use a MySQL or MariaDB database, you might have to install dev tools:

`sudo apt-get install -y python3-mysqldb` or `apt-get install libmariadbclient-dev`

Install python dependencies:

`sudo pip install -r requirements.txt`

---

### Copy and edit yaml configuration file

`cp examples/ispyb_core_config_example.yml ispyb_core_config.yml`

If you do not have a running ispyb database then you can create one by running:

`scripts/create_core_db.sh`

---

### Regenerate data base models and schemas

When the database model is updated, you need to genenerate the python model to take it into acount. Please follow these steps:

```bash
cd scripts
./generate_core_models.sh ../ispyb_core_config.yml
python3 generate_core_schemas.py
cd ..
```

---

### Run application in dev mode

`python3 wsgi.py`

Now you can go to [http://localhost:5000/ispyb/api/v1/docs](http://localhost:5000/ispyb/api/v1/docs) and explore py-ispyb via swagger ui. Please see the [routes section](routes.md) for more information.

For requests use the token in the `Authorization` header: `Bearer YOUR_JWT_TOKEN`.
Please see the [authentication and authorization section](auth.md) for more information.
For example to retrieve proposals call:

```bash
curl -X GET -H 'Authorization: Bearer YOUR_JWT_TOKEN' -i http://localhost:5000/ispyb/api/v1/proposals
```

---

### Run application in production mode

Production mode is can be run through a docker container. To build the image for this container, run the following with the project root as working directory:

`sudo docker build -t "pyispyb" .`

This image needs to be provided with a configuration file to be placed in `/app/config/ispyb_core_config.yml` and will run the webservice on the port `80`. An example of run command can be:

`sudo docker run --rm -it -p 80:80 -v $(pwd):/app/config pyispyb`

Webserver logs can be found in `/var/log/pyispyb/`.

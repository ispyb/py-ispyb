## How to run py-ispyb

---

### Get project code

Clone [py-ISPyB repository](https://github.com/ispyb/py-ispyb)

```bash
# SSH (recommended)
git clone git@github.com:ispyb/py-ispyb.git

# HTTPS
git clone https://github.com/ispyb/py-ispyb.git
```

Recommended IDE is [Visual Studio Code](https://code.visualstudio.com/), which will automatically get configured when opening the project.

---

### Setup Python

You need to have `python >= 3.10`

> To achieve this easily, you can use a conda virtual environment:  
> See [installation instuctions](https://docs.anaconda.com/anaconda/install/linux/).  
> Then set up the environment:
>
> ```bash
> conda create -n py-ispyb python=3.10
> conda activate py-ispyb
> ```

---

### Install requirements

Install linux requirements:

```bash
sudo apt-get update && sudo apt-get install -y libldap2-dev libsasl2-dev libmariadb-dev  build-essential
```

Install python dependencies:

```bash
# For development and production
pip install -r requirements.txt

# For development only
pip install -r requirements-dev.txt
```

---

### Configure py-ISPyB

Configure authentication
(more information in [auth section](auth.md)).

```bash
# edit this file to configure authentication
cp examples/auth.yml auth.yml
```

[Configuration](conf.md) is provided through environment variables.

- Ready-to-run configuration preset is provided for test and development environments.
- Production needs some further configuration before running (see [configuration section](conf.md)).

---

### Setup database

#### Mockup database

For development and test, a mockup database is available.  
You can have it up and running easily with docker:

```bash
sudo docker run -p 3306:3306 --rm --name ispyb-pydb ispyb/ispyb-pydb:latest
```

#### For tests

To run the tests, you need to have the mockup database up and running.

#### For development

By default, the development environment will connect to the mockup database.  
If you want to use a different one, make sure to override it by setting the `SQLALCHEMY_DATABASE_URI` environment variable.

#### For production

Make sure to set the `SQLALCHEMY_DATABASE_URI` environment variable.

---

### Run application

#### Tests

```bash
. scripts/test.sh
```

#### Development

```bash
. uvicorn.sh
```

#### Production

```bash
uvicorn pyispyb.app.main:app
```

---

### More information

Please see the [routes section](routes.md) and the [authentication and authorization section](auth.md) for more information on how to use py-ispyb.

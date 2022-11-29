## How to run py-ispyb

---

### Get project code

Clone the [repository](https://github.com/ispyb/py-ispyb)

```bash
# SSH (recommended)
git clone git@github.com:ispyb/py-ispyb.git

# HTTPS
git clone https://github.com/ispyb/py-ispyb.git
```

Recommended IDE is [Visual Studio Code](https://code.visualstudio.com/), which will automatically get configured when opening the project.

---

### Installation

`python >= 3.10` and `pip` are required

If you need to manage multiple versions of python in your system go to [Setup Python](#setup-python)

Install dependencies:

```bash
# For development and production
pip install -r requirements.txt

# For development only
pip install -r requirements-dev.txt
```

#### System requirements

For development purposes some packages need to be present on your system. These packages are needed for SALS (Simple Authentication and Security Layer) support, LDAP and MariaDB database development files

- For Debian and derivatives:

```bash
sudo apt-get update && sudo apt-get install -y libldap2-dev libsasl2-dev \
libmariadb-dev build-essential
```

- For Fedora and derivatives (use `yum` if you don't have `dnf`):

```bash
sudo dnf update && sudo dnf install -y openldap-devel mariadb-connector-c-devel \
python3-devel
```

For Fedora you might also need to create a text file `/usr/lib/libldap_r.so`, adding only the line `INPUT ( libldap.so )`

### Setup Python

Virtual environments allows to install and manage different versions of python and dependencies from the system easily.

#### Conda virtual environment

Conda is an open source package management system and environment management system. [Installation instructions](https://docs.conda.io/en/latest/miniconda.html)

Then set up the environment:

```bash
conda create -n py-ispyb python=3.10
conda activate py-ispyb
pip install -r requirements.txt
pip install -r requirements-dev.txt # For development
```

#### pyenv

[pyenv](https://github.com/pyenv/pyenv) lets you easily switch between multiple versions of Python. [Installation instrucctions](https://github.com/pyenv/pyenv#installation)

If you are using Ubuntu/Debian, you [need](https://github.com/pyenv/pyenv/wiki/common-build-problems) the following packages:

```
sudo apt install zlib1g zlib1g-dev libssl-dev libbz2-dev libsqlite3-dev
```

Then set up the environment

```bash
pyenv install 3.10
pyenv global 3.10
pip install -r requirements.txt
pip install -r requirements-dev.txt  # For development
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
You can have it up and running easily with `docker`:

```bash
sudo docker run -p 3306:3306 --rm --name ispyb-pydb ispyb/ispyb-pydb:latest
```

If you have `podman`, you can replace `sudo docker` with `podman` in the command above - no `sudo` needed.

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

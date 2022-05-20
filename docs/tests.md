## py-ispyb tests

---

### Coverage information

Test coverage information is available at
[https://app.codecov.io/gh/ispyb/py-ispyb/](https://app.codecov.io/gh/ispyb/py-ispyb/)

### Run test

In order to run the test, you need to have the test database up and running:

```bash
sudo docker run -p 3306:3306 -d --rm --name pydb-test ispyb/ispyb-pydb:latest
```

Install dev dependencies:

```bash
pip install -r requirements-dev.txt
```

Then, to run the tests, simply type:

```bash
export ISPYB_ENVIRONMENT="test"
pytest
```

To run the linting, type:

```bash
flake8
```

Convenience script to run both of them:

```bash
. scripts/test.sh
```

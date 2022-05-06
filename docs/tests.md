## py-ispyb tests

---

### Run test

In order to run the test, you need to have the test database up and running:

```bash
sudo docker run -p 3306:3306 -d --rm --name pydb-test ispyb/ispyb-pydb:latest
```

Install dev dependencies:

```
pip install -r requirements-dev.txt
```

Then, to run the tests, simply type:

```
pytest
```

To run the linting, type:

```
flake8
```

Convenience script to run both of them:

```
. scripts/test.sh
```

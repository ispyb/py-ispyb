## How to run py-ispyb

---

### Get project code

Clone [py-ISPyB repository](https://gitlab.esrf.fr/ispyb/py-ispyb)

---

### Install requirements

You need to have `python >= 3.10`

Install python dependencies:

`sudo pip install -r requirements.txt`

---

### Copy and edit yaml auth configuration file

`cp examples/auth.yml auth.yml`

If you do not have a running ispyb database then you can create one using:

`examples/pydb_empty.sql`

---

### Run application

`. uvicorn.sh`

Now you can go to [http://localhost:8000/docs](http://localhost:8000/docs) and explore py-ispyb via OpenAPI ui. Please see the [routes section](routes.md) for more information.

For requests use the token in the `Authorization` header: `YOUR_JWT_TOKEN`.
Please see the [authentication and authorization section](auth.md) for more information.
For example to retrieve proposals call:

```bash
curl -X GET -H 'Authorization: Bearer YOUR_JWT_TOKEN' -i http://localhost:8000/ispyb/api/v1/proposals
```

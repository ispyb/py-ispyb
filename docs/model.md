## Database model

py-ISPyB aims at working with ISPyB collaboration's database model.

## Python model generation

Python model describing the database model can be found in `pyispyb/core/models.py`.

This model has been generated using `sqlacodegen` with the `noinflect` option:

```bash
sudo apt install sqlacodegen

sqlacodegen --noinflect mysql+mysqlconnector://<user>:<password>@<host>:<port>/<db> | black - > pyispyb/core/models.py
```

The result then requires a few modifications, as specified in `scripts/model.patch`:

```bash
patch pyispyb/core/models.py < scripts/model.patch
```

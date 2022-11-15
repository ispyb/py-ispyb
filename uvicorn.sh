#!/bin/bash

export ISPYB_ENVIRONMENT="dev"

# uvicorn pyispyb.app.main:app --reload
gunicorn pyispyb.app.main:app --workers 5 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
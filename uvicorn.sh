#!/bin/bash

export ISPYB_ENVIRONMENT="dev"

uvicorn pyispyb.app.main:app --reload

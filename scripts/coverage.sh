#!/bin/bash

export ISPYB_ENVIRONMENT="test"

pytest --cov=pyispyb --cov-report html tests/
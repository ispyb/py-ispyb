#!/bin/bash

export ISPYB_ENVIRONMENT="test"

pytest
flake8
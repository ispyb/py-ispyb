"""
Project: py-ispyb.

https://github.com/ispyb/py-ispyb

This file is part of py-ispyb software.

py-ispyb is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

py-ispyb is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along
"""


__license__ = "LGPLv3+"


import os


from functools import lru_cache
from pydantic import BaseSettings, BaseModel
import yaml


PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
RESOURCES_ROOT = os.path.join(PROJECT_ROOT, "resources")

yaml_settings = dict()
AUTH_CONFIG = os.path.realpath(
    os.path.join(PROJECT_ROOT, "..", os.getenv("ISPYB_AUTH", "auth.yml"))
)
try:
    with open(AUTH_CONFIG) as f:
        yaml_settings.update(yaml.load(f, Loader=yaml.FullLoader))
except IOError:
    raise Exception(f"Could not access auth config: {AUTH_CONFIG}")


def get_env(name: str):
    res = os.getenv(name, None)
    if res is None or res == "":
        raise Exception(f"You must define env variable {name}")
    else:
        return res


class Settings(BaseSettings):
    static_root: str = os.path.join(PROJECT_ROOT, "static")
    queries_dir: str = os.path.join(RESOURCES_ROOT, "queries")

    api_root: str
    service_name: str

    sqlalchemy_database_uri: str = get_env("SQLALCHEMY_DATABASE_URI")
    query_debug: bool

    auth = yaml_settings["AUTH"]

    jwt_coding_algorithm: str
    token_exp_time: int  # in minutes
    secret_key: str = get_env("SECRET_KEY")

    cors: bool = False

    class Config:
        env_file = ".env"


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()


class LogConfig(BaseModel):
    """Logging configuration to be set for the server"""

    LOGGER_NAME: str = "mycoolapp"
    LOG_FORMAT: str = "%(levelprefix)s | %(asctime)s | %(message)s"
    LOG_LEVEL: str = "INFO"

    version = 1
    disable_existing_loggers = False
    formatters = {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": LOG_FORMAT,
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    }
    handlers = {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
    }
    loggers = {
        "ispyb": {"handlers": ["default"], "level": LOG_LEVEL},
        "db": {"handlers": ["default"], "level": "DEBUG"},
    }

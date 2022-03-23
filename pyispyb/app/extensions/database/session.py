from typing import Generator, Any
import os
import sqlalchemy
import sqlalchemy.orm
import sqlalchemy.schema

from pyispyb.core.models import Base
from pyispyb.config import settings

engine = sqlalchemy.create_engine(
    url=settings.sqlalchemy_database_uri,
    # Blobs get decoded as str without this resulting in TypeError: string argument without an encoding
    # https://stackoverflow.com/a/53468522
    connect_args={"use_pure": True},  # type: ignore
    isolation_level="READ UNCOMMITTED",
    # https://docs.sqlalchemy.org/en/13/core/pooling.html#dealing-with-disconnects
    pool_pre_ping=True,
    pool_recycle=3600,
    # pooling
    # https://docs.sqlalchemy.org/en/13/errors.html#error-3o7r
    # maybe consider https://docs.sqlalchemy.org/en/13/core/pooling.html#sqlalchemy.pool.NullPool ?
    pool_size=os.environ.get("ISPYB_DATABASE_POOL", 10),
    max_overflow=os.environ.get("ISPYB_DATABASE_OVERFLOW", 20),
)

_session = sqlalchemy.orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)  # type: ignore


def get_session() -> Generator[sqlalchemy.orm.Session, Any, None]:
    session = _session()
    try:
        yield session
        session.commit()
    except:  # noqa
        session.rollback()
        raise
    finally:
        session.close()

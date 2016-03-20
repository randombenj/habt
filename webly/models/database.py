from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from flask.ext.jsontools import JsonSerializableBase

from webly.config import Config

engine = create_engine(Config().connection_string, convert_unicode=True)
session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )
)

Base = declarative_base(cls=(JsonSerializableBase,))
Base.query = session.query_property()

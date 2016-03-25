from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# To serialize the models as json
from flask.ext.jsontools import JsonSerializableBase

from webly.config import Config
config = Config()

engine = create_engine(
    config.connection_string,
    convert_unicode=True,
    echo=config.debug
)

session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )
)

Base = declarative_base(cls=(JsonSerializableBase,))
Base.query = session.query_property()
Base.metadata.bind = engine

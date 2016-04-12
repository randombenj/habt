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
    echo=False
)

session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )
)

class GetOrCreateMixin():
    '''
        Mixin to add the get_or_create and get_or_add methods to required models
    '''
    @classmethod
    def get_or_create(cls, **kwargs):
        '''
            Creates a table instance if there is no such object
            with the same table attributes already in the database

            kwargs:
             The tables attributes

            returns:
             A new or found instance
        '''
        instance = session.query(cls).filter_by(**kwargs).first()
        return instance if instance else cls(**kwargs)


    @classmethod
    def get_or_add(cls, **kwargs):
        '''
            Creates a new instance of an object if it does not exist
            in addition to get_or_create the get_or_add method also
            adds the instance to the database if it does not exist.
            If the instance is new is determined wether the id attribute is
            greater than 0

            kwargs:
             The tables attributes

            returns:
             A new or added instance
        '''
        instance = cls.get_or_add(**kwargs)
        if not instance.id:
            session.add(instance)
            session.commit()
        return instance


Base = declarative_base(cls=(JsonSerializableBase))
Base.query = session.query_property()
Base.metadata.bind = engine

def drop():
    '''
        Drops the database
    '''
    Base.metadata.drop_all()

def create():
    '''
        Creates the database
    '''
    Base.metadata.create_all()

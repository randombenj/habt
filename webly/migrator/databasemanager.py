import logging
from webly.models import Base, Package, session
from webly.config import Config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from webly.migrator.migrator import Migrator

log = logging.getLogger(__name__)

def init():
    '''
        Initializes the Database according
        to the Models
    '''
    log.info('Initialize the database')
    Base.metadata.create_all()
    log.info('Initialized the database')

def destroy():
    '''
        Destroys the databases
    '''
    log.warn('Destroy the database')
    Base.metadata.drop_all()
    log.info('Destroyed the database')

def migrate(self):
    '''
        Initializes the Database according
        to the Models
    '''
    # make a new database
    self.destroy()
    self.init()

    log.info('Starting a database migration')
    Migrator(session)

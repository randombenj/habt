import logging
from webly.models import Base, Package
from webly.config import Config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from webly.migrator.migrator import Migrator

log = logging.getLogger(__name__)

class DatabaseManager():

    def __init__(self):
        self._connection = create_engine(Config().connection_string, echo=True)

    def init(self):
        '''
            Initializes the Database according
            to the Models
        '''
        log.info('Initialize the database')
        Base.metadata.create_all(self._connection)

    def destroy(self):
        '''
            Destroys the databases
        '''
        log.warn('Destroy the database')

    def migrate(self):
        '''
            Initializes the Database according
            to the Models
        '''
        log.info('Starting a database migration')

        Migrator()
        # Session = sessionmaker(bind=self._connection)
        #
        # package = Package(name="Test Package")
        # session = Session()
        #
        # session.add(package)
        # session.commit()

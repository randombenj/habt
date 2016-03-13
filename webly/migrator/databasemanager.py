import logging
import web.models

log = logging.getLogger(__name__)

class DatabaseManager():
    def __init__(self):
        pass

    @staticmethod
    def init():
        '''
            Initializes the Database according
            to the Models
        '''
        log.info('Initialize the database')

    @staticmethod
    def destroy():
        '''
            Destroys the databases
        '''
        log.warn('Destroy the database')

    @staticmethod
    def migrate():
        '''
            Initializes the Database according
            to the Models
        '''
        log.info('Starting a database migration')

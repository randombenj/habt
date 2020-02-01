import os
import logging
import logging.config


class Config():

    def __init__(self):
        self._db_name = os.environ['DB_NAME']
        self._db_user = os.environ['DB_USER']
        self._db_password = os.environ['DB_PASS']
        self._db_service = os.environ['DB_SERVICE']
        self._db_port = os.environ['DB_PORT']
        self._sqlalchemy_db_uri = 'postgresql://{0}:{1}@{2}:{3}/{4}'.format(
            self._db_user,
            self._db_password,
            self._db_service,
            self._db_port,
            self._db_name
        )
        self._debug = os.environ['DEBUG'] == 'True'

    @property
    def connection_string(self):
        '''
            Returns the Sql Alchemy Postgres SQL connection URI
        '''
        return self._sqlalchemy_db_uri

    @property
    def debug(self):
        '''
            Returns wether the application is in debug mode
        '''
        return self._debug

    @staticmethod
    def setup_logger(level=logging.INFO):
        '''
            Setup of the application logger
        '''
        log_config = {
            'version': 1,
            'disable_existing_loggers': False,  # this fixes the problem
            'formatters': {
                'standard': {
                    'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
                },
            },
            'handlers': {
                'console': {
                    'class': 'logging.StreamHandler',
                    'level': logging.INFO,
                    'formatter': 'standard',
                },
                'file': {
                    'class': 'logging.FileHandler',
                    'filename': 'habt.log',
                    'level': logging.DEBUG,
                    'formatter': 'standard',
                }
            },
            'loggers': {
                '': {
                    'handlers': ['console', 'file'],
                    'level': level,
                    'propagate': True
                }
            }
        }
        logging.config.dictConfig(log_config)
        logging.getLogger(__name__).info('Initialized logger', log_config)

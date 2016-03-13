import logging
import logging.config

class Config():
    def __init__(self):
        pass

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
                    'filename': 'webly.log',
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

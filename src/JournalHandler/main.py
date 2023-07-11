import logging
import logging.config
from systemd.journal import JournalHandler

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'standard',
        },
        'journal': {
            'class': 'systemd.journal.JournalHandler',
            'level': 'WARN',
        }
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'loggers': {
        'MyLogger': {
            'handlers': ['journal'],
            'level': 'WARN',
        }
    }
}

logging.config.dictConfig(LOGGING_CONFIG)

logger = logging.getLogger('MyLogger')

logging.debug('This is debug log')
logging.info('This is info log')
logging.warning('This is warn log')
logging.error('This is err log')
logging.critical('This is crit log')

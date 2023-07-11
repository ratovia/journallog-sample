import logging
import logging.config

logging_config = dict(
    version=1,
    formatters={
        'f': {'format':
              '%(asctime)s %(levelname)-8s JOURNAL-LOG-SAMPLE %(message)s'}
    },
    handlers={
        'h': {'class': 'logging.StreamHandler',
              'formatter': 'f',
              'level': logging.DEBUG}
    },
    root={
        'handlers': ['h'],
        'level': logging.DEBUG,
    },
)

logging.config.dictConfig(logging_config)

logger = logging.getLogger()

logging.debug('Debugging')
logging.info('Informational')
logging.warning('Warning')
logging.error('Error')
logging.critical('Critical')

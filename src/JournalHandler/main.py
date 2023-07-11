import logging
import logging.config
from systemd import journal

logging_config = dict(
    version=1,
    formatters={
        'format': {
            'format': 'APP-LOG-LEVEL:%(levelname)-8s %(message)s'
        }
    },
    handlers={
        'journalHandler': {
            'class': 'journal.journalHandler',
            'formatter': 'format',
            'level': logging.DEBUG
        }
    },
    root={
        'handlers': ['journalHandler'],
        'level': logging.DEBUG,
    },
)

logging.config.dictConfig(logging_config)

logger = logging.getLogger()
logger.debug('This is debug log')
logger.info('This is info log')
logger.warning('This is warn log')
logger.error('This is err log')
logger.critical('This is crit log')

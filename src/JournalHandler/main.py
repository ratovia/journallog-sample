import logging
import logging.config
from systemd import journal

logging_config = dict(
    version=1,
    formatters={
        'f': {
            'format': 'APP-LOG-LEVEL:%(levelname)-8s %(message)s'
        }
    },
    handlers={
        'h': {
            'class': 'journal.JournalHandler',
            'formatter': 'f'
        }
    },
    root={
        'handlers': ['h'],
    },
)

logging.config.dictConfig(logging_config)

logger = logging.getLogger()
# logger.addHandler(journal.JournalHandler())

logger.debug('This is debug log')
logger.info('This is info log')
logger.warning('This is warn log')
logger.error('This is err log')
logger.critical('This is crit log')

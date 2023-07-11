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
        'journald-myapp': {
            'class': 'systemd.journal.JournalHandler',
            'formatter': 'f',
            'level': 'DEBUG',
            'SYSLOG_IDENTIFIER': 'myapp',
        }
    },
    root={
        'handlers': ['journald-myapp'],
        'level': 'NOTSET',
    },
    loggers={
        'myapp': {
            'handlers': ['journald-myapp'],
            'level': 'NOTSET',
            'propagate': False
        },
    },
)

logging.config.dictConfig(logging_config)

logger = logging.getLogger('myapp')
logger.addHandler(journal.JournalHandler())

logger.debug('This is debug log')
logger.info('This is info log')
logger.warning('This is warn log')
logger.error('This is err log')
logger.critical('This is crit log')

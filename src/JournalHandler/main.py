import logging
from systemd import journal
logger = logging.getLogger('custom_logger_name')
logger.addHandler(journal.JournalHandler(SYSLOG_IDENTIFIER='custom_unit_name'))
logger.warning("Some message: %s", 'detail')

logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')

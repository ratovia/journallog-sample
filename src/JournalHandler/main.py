import logging
from systemd.journal import JournalHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

journal_handler = JournalHandler()
journal_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(name)s: %(message)s')
journal_handler.setFormatter(formatter)

logger.addHandler(journal_handler)

# ログメッセージの記録
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')

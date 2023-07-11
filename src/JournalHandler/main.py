import logging
import logging.config
from systemd.journal import JournalHandler

# ログ設定辞書
logging_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
        }
    },
    "handlers": {
        "journal": {
            "class": "systemd.journal.JournalHandler",
            "level": "DEBUG",
            "formatter": "standard"
        }
    },
    "loggers": {
        "": {
            "handlers": ["journal"],
            "level": "DEBUG",
            "propagate": True
        }
    }
}

# ログ設定の適用
logging.config.dictConfig(logging_config)

# ログメッセージの記録
logger = logging.getLogger(__name__)
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')

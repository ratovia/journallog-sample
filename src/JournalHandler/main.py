#!/usr/bin/env python

import logging
from systemd.journal import JournalHandler

log = logging.getLogger('test')
log_fmt = logging.Formatter("%(levelname)s %(message)s")
log_ch = JournalHandler()
log_ch.setFormatter(log_fmt)
log.addHandler(log_ch)
log.setLevel(logging.DEBUG)
log.warning("warn")
log.info("info")
log.error("error")
log.debug("debug")

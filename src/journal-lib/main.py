from systemd import journal

journal.send('hello world')
journal.send('oops!', PRIORITY=journal.LOG_ERR)

journal.send('This is debug log', PRIORITY=journal.LOG_DEBUG)
journal.send('This is info log', PRIORITY=journal.LOG_INFO)
journal.send('This is notice log', PRIORITY=journal.LOG_NOTICE)
journal.send('This is warn log', PRIORITY=journal.LOG_WARNING)
journal.send('This is err log', PRIORITY=journal.LOG_ERR)
journal.send('This is crit log', PRIORITY=journal.LOG_CRIT)

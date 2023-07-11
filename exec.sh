# StreamHandler
python3 src/StreamHandler/main.py 2>&1 | logger -t "Journal-StreamHandler"

# journal-lib
python3 src/journal-lib/main.py 2>&1 | logger -t "Journal-journal-lib"

# JournalHandler
python3 src/JournalHandler/main.py 2>&1 | logger -t "Journal-JournalHandler"

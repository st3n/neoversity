from pathlib import Path

DB_FILENAME = Path(__file__).parent / 'movies.sqlite3'
MOVIES_FILENAME = Path(__file__).parent / 'movies.csv'

print(DB_FILENAME)

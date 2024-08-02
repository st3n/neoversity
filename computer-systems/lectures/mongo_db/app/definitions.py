import os
from pathlib import Path

from dotenv import load_dotenv


BASE_DIR = Path(__file__).parent.parent
MOVIES_FILENAME_CSV = BASE_DIR / 'data' / 'movies.csv'

load_dotenv(BASE_DIR / '.env')

DB_HOST = os.getenv('MONGO_DB_HOST')
DB_NAME = os.getenv('MONGO_INITDB_DATABASE')
DB_USER = os.getenv('MONGO_INITDB_ROOT_USERNAME')
DB_PASSWORD = os.getenv('MONGO_INITDB_ROOT_PASSWORD')
DB_PORT = os.getenv('MONGO_DB_PORT')

DB_CONNECT_URI = f"mongodb://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/"

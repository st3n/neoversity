import sqlite3
from abc import ABC, abstractmethod

from db.finish.definitions import DB_FILENAME


class DatabaseInitializerInterface(ABC):
    @abstractmethod
    def __enter__(self):
        pass

    @abstractmethod
    def __exit__(self, exc_type, exc_value, traceback):
        pass

    @abstractmethod
    def create_all_tables(self) -> None:
        pass


class SQLiteDatabaseInitializer(DatabaseInitializerInterface):
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def _create_genre_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Genre (
            id INTEGER PRIMARY KEY,
            name VARCHAR(100) NOT NULL
        );
        """)

    def _create_certification_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Certification (
            id INTEGER PRIMARY KEY,
            name VARCHAR(10) NOT NULL
        );
        """)

    def _create_director_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Director (
            id INTEGER PRIMARY KEY,
            name VARCHAR(50) NOT NULL
        );
        """)

    def _create_star_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Star (
            id INTEGER PRIMARY KEY,
            name VARCHAR(50) NOT NULL
        );
        """)

    def _create_movie_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Movie (
            id INTEGER PRIMARY KEY,
            name VARCHAR(250) NOT NULL,
            year INTEGER NOT NULL,
            time INTEGER NOT NULL,
            imdb FLOAT NOT NULL,
            votes INTEGER NOT NULL ,
            meta_score FLOAT,
            gross FLOAT,
            certification_id INTEGER,
            description TEXT,
            FOREIGN KEY (certification_id) REFERENCES Certification(id),
            UNIQUE(name, year, time, imdb)
        );
        """)

    def _create_movie_genre_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS MovieGenre (
            id INTEGER PRIMARY KEY,
            movie_id INTEGER,
            genre_id INTEGER,
            FOREIGN KEY (movie_id) REFERENCES Movie(id),
            FOREIGN KEY (genre_id) REFERENCES Genre(id),
            UNIQUE(movie_id, genre_id)
        );
        """)

    def _create_movie_director_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS MovieDirector (
            id INTEGER PRIMARY KEY,
            movie_id INTEGER,
            director_id INTEGER,
            FOREIGN KEY (movie_id) REFERENCES Movie(id),
            FOREIGN KEY (director_id) REFERENCES Director(id),
            UNIQUE(movie_id, director_id)
        );
        """)

    def _create_movie_star_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS MovieStar (
            id INTEGER PRIMARY KEY,
            movie_id INTEGER,
            star_id INTEGER,
            FOREIGN KEY (movie_id) REFERENCES Movie(id),
            FOREIGN KEY (star_id) REFERENCES Star(id),
            UNIQUE(movie_id, star_id)
        );
        """)

    def create_all_tables(self) -> None:
        self._create_genre_table()
        self._create_certification_table()
        self._create_director_table()
        self._create_star_table()
        self._create_movie_table()
        self._create_movie_genre_table()
        self._create_movie_director_table()
        self._create_movie_star_table()

        self.conn.commit()

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.conn:
            self.conn.close()


if __name__ == "__main__":
    with SQLiteDatabaseInitializer(DB_FILENAME) as db_initializer:
        db_initializer.create_all_tables()


import sqlite3

from tqdm import tqdm

from db.finish.definitions import DB_FILENAME, MOVIES_FILENAME
from db.finish.dto import MoviesDTO
from db.finish.init_tables import SQLiteDatabaseInitializer
from db.finish.mapper import MovieCSVParser


class DatabaseSeeder:
    def __init__(self, db_name: str):
        self.conn = sqlite3.connect(db_name)

    def populate_from_dto(self, movies_dto: MoviesDTO):
        self._populate_genres(movies_dto.genres)
        self._populate_certifications(movies_dto.certifications)
        self._populate_directors(movies_dto.directors)
        self._populate_stars(movies_dto.stars)
        self._populate_movies(movies_dto.movies)

    def _populate_genres(self, genres):
        with self.conn:
            values = [(genre,) for genre in genres]
            self.conn.executemany("INSERT OR IGNORE INTO Genre (name) VALUES (?)", values)

    def _populate_certifications(self, certifications):
        with self.conn:
            values = [(cert,) for cert in certifications]
            self.conn.executemany("INSERT OR IGNORE INTO Certification (name) VALUES (?)", values)

    def _populate_directors(self, directors):
        with self.conn:
            values = [(director,) for director in directors]
            self.conn.executemany("INSERT OR IGNORE INTO Director (name) VALUES (?)", values)

    def _populate_stars(self, stars):
        with self.conn:
            values = [(star,) for star in stars]
            self.conn.executemany("INSERT OR IGNORE INTO Star (name) VALUES (?)", values)

    def _populate_movies(self, movies):
        with self.conn:
            for movie in tqdm(movies, desc="Populating Movies"):
                cur = self.conn.cursor()
                cur.execute("""
                    INSERT INTO Movie (name, year, time, imdb, votes, meta_score, gross, certification_id, description) 
                    VALUES (?, ?, ?, ?, ?, ?, ?, (SELECT id FROM Certification WHERE name = ? LIMIT 1), ?)
                """, (movie.name, movie.year, movie.time, movie.imdb, movie.votes, movie.meta_score, movie.gross,
                      movie.certification, movie.description))
                movie_id = cur.lastrowid

                genre_values = [(movie_id, genre) for genre in movie.genres]
                cur.executemany("INSERT INTO MovieGenre (movie_id, genre_id) SELECT ?, id FROM Genre WHERE name = ?",
                                genre_values)

                director_values = [(movie_id, director) for director in movie.directors]
                cur.executemany(
                    "INSERT INTO MovieDirector (movie_id, director_id) SELECT ?, id FROM Director WHERE name = ?",
                    director_values)

                star_values = [(movie_id, star) for star in movie.stars]
                cur.executemany("INSERT INTO MovieStar (movie_id, star_id) SELECT ?, id FROM Star WHERE name = ?",
                                star_values)


if __name__ == '__main__':
    with SQLiteDatabaseInitializer(DB_FILENAME) as db_initializer:
        db_initializer.create_all_tables()

    parser = MovieCSVParser(MOVIES_FILENAME)
    movies = parser.read_csv_and_map_to_dto()

    db_seeder = DatabaseSeeder(DB_FILENAME)
    db_seeder.populate_from_dto(movies)

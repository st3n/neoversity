import sqlite3
from typing import Optional, List, Set

from db.finish.dto import MovieDTO
from db.finish.definitions import DB_FILENAME
from db.finish.exceptions import (
    MovieDBBaseError,
    MovieAlreadyExistError,
    CertificationDoesNotExistError,
    GenreDoesNotExistError,
    DirectorDoesNotExistError,
    MovieGenreAlreadyExistError,
    MovieDoesNotExistError,
)


class MovieSQLiteRepository:
    def __init__(self, db_name: str):
        self.db_name = db_name

    def _get_connection(self):
        return sqlite3.connect(self.db_name)

    def _get_certification_id(self, certification_name: str) -> int:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id FROM Certification WHERE name = ?", (certification_name,)
            )
            certification_id = cursor.fetchone()
            if not certification_id:
                raise CertificationDoesNotExistError(
                    f"Certification {certification_name} does not exist!"
                )
            return certification_id[0]

    def _get_genre_ids(self, genres: set[str]) -> List[int]:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            genre_ids = []
            for genre in genres:
                cursor.execute("SELECT id FROM Genre WHERE name = ?", (genre,))
                genre_id = cursor.fetchone()
                if not genre_id:
                    raise GenreDoesNotExistError(f"Genre {genre} does not exist!")
                genre_ids.append(genre_id[0])
        return genre_ids

    def _get_director_ids(self, directors: set[str]) -> List[int]:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            directors_ids = []
            for director in directors:
                cursor.execute("SELECT id FROM Director WHERE name = ?", (director,))
                director_id = cursor.fetchone()
                if not director_id:
                    raise DirectorDoesNotExistError(
                        f"Director {director} does not exist!"
                    )
                directors_ids.append(director_id[0])
        return directors_ids

    def _link_movie_to_genres(self, movie_id: int, genre_ids: List[int]):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            data = [(movie_id, genre_id) for genre_id in genre_ids]
            try:
                cursor.executemany(
                    "INSERT INTO MovieGenre (movie_id, genre_id) VALUES (?, ?)", data
                )
            except sqlite3.IntegrityError as e:
                if (
                    "UNIQUE constraint failed: MovieGenre.movie_id, MovieGenre.genre_id"
                    in str(e)
                ):
                    raise MovieGenreAlreadyExistError(
                        "This movie-genre link already exists in the database!"
                    ) from e
                raise

    def _link_movie_to_directors(self, movie_id: int, directors_ids: List[int]):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            data = [(movie_id, director_id) for director_id in directors_ids]
            try:
                cursor.executemany(
                    "INSERT INTO MovieDirector (movie_id, director_id) VALUES (?, ?)",
                    data,
                )
            except sqlite3.IntegrityError as e:
                if (
                    "UNIQUE constraint failed: MovieDirector.movie_id, MovieDirector.director_id"
                    in str(e)
                ):
                    raise MovieAlreadyExistError(
                        "This movie-director link already exists in the database!"
                    ) from e
                raise

    def add_movie(self, movie: MovieDTO) -> int:
        certification_id = self._get_certification_id(movie.certification)
        genre_ids = self._get_genre_ids(movie.genres)
        directors_ids = self._get_director_ids(movie.directors)

        with self._get_connection() as conn:
            cursor = conn.cursor()
            try:
                cursor.execute(
                    """
                        INSERT INTO Movie (name, year, time, imdb, votes, meta_score, gross, certification_id, description)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                        """,
                    (
                        movie.name,
                        movie.year,
                        movie.time,
                        movie.imdb,
                        movie.votes,
                        movie.meta_score,
                        movie.gross,
                        certification_id,
                        movie.description,
                    ),
                )
            except sqlite3.IntegrityError as e:
                if (
                    "UNIQUE constraint failed: Movie.name, Movie.year, Movie.time"
                    in str(e)
                ):
                    raise MovieAlreadyExistError(
                        "This movie already exists in the database!"
                    ) from e
                raise

        movie_id = cursor.lastrowid
        self._link_movie_to_genres(movie_id, genre_ids)
        self._link_movie_to_directors(movie_id, directors_ids)
        return movie_id

    def _get_certification_name_by_id(self, certification_id: int) -> str:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT name FROM Certification WHERE id = ?", (certification_id,)
            )
            return cursor.fetchone()[0]

    def _get_directors_by_movie_id(self, movie_id: int) -> Set[str]:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
            SELECT Director.name
            FROM MovieDirector
            JOIN Director
                ON MovieDirector.director_id = Director.id
            WHERE movie_id = ?
            """,
                (movie_id,),
            )
            return {name[0] for name in cursor.fetchall()}

    def _get_stars_by_movie_id(self, movie_id: int) -> Set[str]:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
            SELECT Star.name
            FROM MovieStar
            JOIN Star
                ON MovieStar.star_id = Star.id
            WHERE movie_id = ?
            """,
                (movie_id,),
            )
            return {name[0] for name in cursor.fetchall()}

    def _get_genres_by_movie_id(self, movie_id: int) -> Set[str]:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
            SELECT Genre.name
            FROM MovieGenre
            JOIN Genre
                ON MovieGenre.genre_id = Genre.id
            WHERE MovieGenre.movie_id = ?
            """,
                (movie_id,),
            )
            return {genre[0] for genre in cursor.fetchall()}

    def get_movie_by_id(self, movie_id: int) -> MovieDTO:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
            SELECT name, year, time, imdb, votes, meta_score, gross, certification_id, description
            FROM Movie
            WHERE id = ?
            """,
                (movie_id,),
            )
            row = cursor.fetchone()
            if not row:
                raise MovieDoesNotExistError(
                    f"Movie with id {movie_id} does not exist!"
                )

        certification = self._get_certification_name_by_id(row[7])
        directors = self._get_directors_by_movie_id(movie_id)
        stars = self._get_stars_by_movie_id(movie_id)
        genres = self._get_genres_by_movie_id(movie_id)
        return MovieDTO(
            name=row[0],
            year=row[1],
            time=row[2],
            imdb=row[3],
            votes=row[4],
            meta_score=row[5],
            gross=row[6],
            genres=genres,
            certification=certification,
            directors=directors,
            stars=stars,
            description=row[8],
        )

    def get_all_movies(self) -> List[MovieDTO]:
        movies = []

        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id, name, year, time, imdb, votes, meta_score, gross, certification_id, description"
                " FROM Movie"
            )
            rows = cursor.fetchall()

        for row in rows:
            certification = self._get_certification_name_by_id(row[0])
            directors = self._get_directors_by_movie_id(row[0])
            stars = self._get_stars_by_movie_id(row[0])
            genres = self._get_genres_by_movie_id(row[0])
            movies.append(
                MovieDTO(
                    name=row[1],
                    year=row[2],
                    time=row[3],
                    imdb=row[4],
                    votes=row[5],
                    meta_score=row[6],
                    gross=row[7],
                    genres=genres,
                    certification=certification,
                    directors=directors,
                    stars=stars,
                    description=row[9],
                )
            )
        return movies

    def update_movie(self, movie_id: int, movie: MovieDTO) -> None:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
            UPDATE Movie
            SET name=?, year=?, time=?, imdb=?, votes=?, meta_score=?, gross=?, certification_id=?, description=?
            WHERE id=?
            """,
                (
                    movie.name,
                    movie.year,
                    movie.time,
                    movie.imdb,
                    movie.votes,
                    movie.meta_score,
                    movie.gross,
                    None,
                    movie.description,
                    movie_id,
                ),
            )

    def delete_movie(self, movie_id: int) -> None:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Movie WHERE id=?", (movie_id,))


if __name__ == "__main__":
    movie_data = MovieDTO(
        name="The Shawshank Redemption director edition",
        year=1994,
        time=142,
        imdb=9.3,
        votes=2804443,
        meta_score=82.0,
        gross=28340000.0,
        genres={"Drama"},
        certification="R",
        directors={"Frank Darabont"},
        stars={"Tim Robbins", "Morgan Freeman", "Bob Gunton", "William Sadler"},
        description="Over the course of several years, two convicts form a friendship, "
        "seeking consolation and, eventually, redemption through basic compassion.",
    )

    movie_repository = MovieSQLiteRepository(DB_FILENAME)
    try:
        # last_id = movie_repository.add_movie(movie_data)
        # movie = movie_repository.get_movie_by_id(1)
        # print(movie)
        movies = movie_repository.get_all_movies()
        for movie in movies:
            print(movie)
    except MovieDBBaseError as e:
        print(str(e))

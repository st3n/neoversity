from pymongo import MongoClient, ASCENDING, DESCENDING
from tqdm import tqdm

from app.dto import MoviesDTO
from app.mapper import MovieCSVParser
from app.definitions import MOVIES_FILENAME_CSV, DB_NAME, DB_CONNECT_URI


class MongoDatabaseSeeder:
    def __init__(self, db_name: str, uri: str):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]

    def populate_from_dto(self, movies_dto: MoviesDTO):
        self._populate_genres(movies_dto.genres)
        self._populate_certifications(movies_dto.certifications)
        self._populate_directors(movies_dto.directors)
        self._populate_stars(movies_dto.stars)
        self._populate_movies(movies_dto.movies)

    def _populate_genres(self, genres):
        genres_collection = self.db["Genre"]
        genres_docs = [{"name": genre} for genre in genres]
        genres_collection.insert_many(genres_docs, ordered=False)

    def _populate_certifications(self, certifications):
        certifications_collection = self.db["Certification"]
        certifications_docs = [{"name": cert} for cert in certifications]
        certifications_collection.insert_many(certifications_docs, ordered=False)

    def _populate_directors(self, directors):
        directors_collection = self.db["Director"]
        directors_docs = [{"name": director} for director in directors]
        directors_collection.insert_many(directors_docs, ordered=False)

    def _populate_stars(self, stars):
        stars_collection = self.db["Star"]
        stars_docs = [{"name": star} for star in stars]
        stars_collection.insert_many(stars_docs, ordered=False)

    def _populate_movies(self, movies):
        for movie in tqdm(movies, desc="Populating Movies"):
            certification_id = self.db.Certification.find_one({"name": movie.certification})["_id"]
            genre_ids = [self.db.Genre.find_one({"name": genre})["_id"] for genre in movie.genres]
            director_ids = [self.db.Director.find_one({"name": director})["_id"] for director in movie.directors]
            star_ids = [self.db.Star.find_one({"name": star})["_id"] for star in movie.stars]

            movie_doc = {
                "name": movie.name,
                "year": movie.year,
                "time": movie.time,
                "imdb": movie.imdb,
                "votes": movie.votes,
                "meta_score": movie.meta_score,
                "gross": movie.gross,
                "certification": certification_id,
                "description": movie.description,
                "genres": genre_ids,
                "directors": director_ids,
                "stars": star_ids
            }
            self.db.Movie.insert_one(movie_doc)


if __name__ == '__main__':
    parser = MovieCSVParser(MOVIES_FILENAME_CSV)
    movies = parser.read_csv_and_map_to_dto()

    db_seeder = MongoDatabaseSeeder(DB_NAME, DB_CONNECT_URI)
    db_seeder.populate_from_dto(movies)

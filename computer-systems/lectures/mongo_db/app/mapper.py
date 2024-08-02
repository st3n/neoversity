import pandas as pd
from abc import ABC, abstractmethod
from typing import Tuple, Set
import ast

from tqdm import tqdm

from app.definitions import MOVIES_FILENAME_CSV
from app.dto import MoviesDTO, MovieDTO


class MovieParserInterface(ABC):
    @abstractmethod
    def read_csv_and_map_to_dto(self) -> MoviesDTO:
        pass


class MovieCSVParser(MovieParserInterface):
    def __init__(self, filename: str):
        self.filename = filename

    def _read_csv_file(self) -> pd.DataFrame:
        df = pd.read_csv(self.filename)
        return df

    def _map_rows_to_dto(self, df: pd.DataFrame) -> MoviesDTO:
        genres, directors, stars, certifications = self._extract_unique_values(df)
        movies = [self._create_movie_dto(row) for _, row in df.iterrows()]
        return MoviesDTO(genres, certifications, directors, stars, movies)

    def _extract_unique_values(self, df: pd.DataFrame) -> Tuple[Set, Set, Set, Set]:
        genres = set()
        directors = set()
        stars = set()
        certifications = set()

        for _, row in tqdm(df.iterrows(), desc="Mapping Movies"):
            movie_genres = {row_genre.strip() for row_genre in ast.literal_eval(row['Genre'])}
            genres.update(movie_genres)

            movie_directors = {row_director.strip() for row_director in ast.literal_eval(row['Director'])}
            directors.update(movie_directors)

            movie_stars = {row_star.strip() for row_star in ast.literal_eval(row['Stars'])}
            stars.update(movie_stars)

            certification = row['Certification']
            if isinstance(certification, str) and certification.strip():
                movie_certification = certification.strip()
            else:
                movie_certification = 'Not Rated'
            certifications.add(movie_certification)

        return genres, directors, stars, certifications

    def _create_movie_dto(self, row: pd.Series) -> MovieDTO:
        name = row['Movie Name'].strip()
        year = int(row['Year of Release'])
        time = int(row['Run Time in minutes'])
        imdb = float(row['Movie Rating'])
        votes = int(row['Votes'])
        meta_score = float(row['MetaScore']) if pd.notnull(row['MetaScore']) else None
        gross = float(row['Gross']) if pd.notnull(row['Gross']) else None

        movie_genres = {row_genre.strip() for row_genre in ast.literal_eval(row['Genre'])}
        certification = row['Certification']
        if isinstance(certification, str) and certification.strip():
            movie_certification = certification.strip()
        else:
            movie_certification = 'Not Rated'
        movie_directors = {row_director.strip() for row_director in ast.literal_eval(row['Director'])}
        movie_stars = {row_star.strip() for row_star in ast.literal_eval(row['Stars'])}
        description = ' '.join([desc.strip() for desc in ast.literal_eval(row['Description'])])

        return MovieDTO(
            name=name,
            year=year,
            time=time,
            imdb=imdb,
            votes=votes,
            meta_score=meta_score,
            gross=gross,
            genres=movie_genres,
            certification=movie_certification,
            directors=movie_directors,
            stars=movie_stars,
            description=description
        )

    def read_csv_and_map_to_dto(self) -> MoviesDTO:
        df = self._read_csv_file()
        movies_dto = self._map_rows_to_dto(df)
        return movies_dto


def check_duplicates():
    df = pd.read_csv('movies.csv')
    duplicates = df[df.duplicated(subset=['Movie Name', 'Year of Release'], keep=False)]
    unique_duplicates = duplicates.drop_duplicates().values.tolist()

    for dup in unique_duplicates:
        print(dup)


if __name__ == '__main__':
    parser = MovieCSVParser(MOVIES_FILENAME_CSV)
    movies = parser.read_csv_and_map_to_dto()
    print(movies)
    # check_duplicates()


class MovieDBBaseError(Exception):
    pass


class MovieAlreadyExistError(MovieDBBaseError):
    pass


class MovieDoesNotExistError(MovieDBBaseError):
    pass


class CertificationDoesNotExistError(MovieDBBaseError):
    pass


class GenreDoesNotExistError(MovieDBBaseError):
    pass


class MovieGenreAlreadyExistError(MovieDBBaseError):
    pass


class MovieDirectorAlreadyExistError(MovieDBBaseError):
    pass


class DirectorDoesNotExistError(MovieDBBaseError):
    pass


class PyMovieDBError(Exception):
    """
    Base class for all PyMovieDB errors
    """


class TmdbApiError(PyMovieDBError):
    """
    raised when API response is not `OK 200`
    """


class ZeroResultsFound(PyMovieDBError):
    """
    raised when zero results are found
    against search query.
    """

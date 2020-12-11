class PyMovieDBError(Exception):
    """
    Base class for all PyMovieDB errors
    """

class TmdbApiError(PyMovieDBError):
    """
    raised when API response is not `OK 200`
    """

    def __init__(self, message):

        if message.get("status_message"):
            excp_msg = message["status_message"]
        else:
            excp_msg = str(message)

        super().__init__(excp_msg)

class ZeroResultsFound(PyMovieDBError):
    """
    raised when zero results are found
    against search query.
    """

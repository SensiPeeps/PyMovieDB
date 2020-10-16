class TmdbApiError(Exception):
    """
    raised when API response is not `OK 200`
    """

    def __init__(self, message):
        super().__init__(message["status_message"])


class ZeroResultsFound(Exception):
    """
    raise when zero results are found
    against search query.
    """

    def __init__(self, message):
        super().__init__(message)

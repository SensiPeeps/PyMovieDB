class TmdbApiError(Exception):
    """
    raised when API response is not `OK 200`
    """

    def __init__(self, message):

        if message.get("status_message"):
            super().__init__(message["status_message"])
        else:
            super().__init__(str(message))


class ZeroResultsFound(Exception):
    """
    raised when zero results are found
    against search query.
    """

    pass

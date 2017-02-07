class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class NixError(Error):
    def __init__(self, message: str, exception: Exception=None):
        self._message = message
        self._exception = exception

    def get_message(self) -> str:
        return self._message

    def get_exception(self) -> Exception:
        return self._exception

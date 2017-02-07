from abc import ABC, abstractmethod
import typing

from libnix.exception.nix_error import NixError


class AbstractRead(ABC):
    _PROC_PATH = "/proc"

    def __init__(self):
        self._data = None

    @abstractmethod
    def load(self):
        pass

    @staticmethod
    def _read(filename: str) -> typing.Optional[str]:
        try:
            with open(filename, 'r') as f:
                _data = f.read().strip()
        except OSError as _error:
            if _error.errno is 13:
                return None
            else:
                raise NixError("Unable to read file: {}".format(filename), _error)

        return _data

    def _get_value(self, key: str) -> typing.Optional[str]:
        if self._data is None:
            self.load()

        try:
            return self._data[key]
        except KeyError:
            return None

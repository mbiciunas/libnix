# Nix
# Copyright (c) 2017  Mark Biciunas.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from abc import ABC, abstractmethod
import typing

from libnix.exception.nix_error import NixError


class AbstractRead(ABC):
    _PROC_PATH = "/proc"
    _ETC_PATH = "/etc"

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

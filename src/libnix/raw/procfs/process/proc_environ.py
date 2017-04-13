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

import os

from libnix.raw.abstract_read import AbstractRead


class ProcEnviron(AbstractRead):
    _ARGS = "args"

    def __init__(self, pid: int) -> None:
        super().__init__()
        self._pid = pid

    def load(self) -> None:
        self._data = dict()

        _path = os.path.join(self._PROC_PATH, str(self._pid), "environ")
        _file_read = self._read(_path)

        if _file_read is not None:
            _file_data = _file_read.split('\x00')

            self._data[self._ARGS] = list(filter(None, _file_data[1:]))
        else:
            self._data[self._ARGS] = []

    @property
    def get_environment_count(self) -> int:
        return len(self._get_value(self._ARGS))

    @property
    def get_environments(self) -> str:
        return self._get_value(self._ARGS)

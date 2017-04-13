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
import typing

from libnix.raw.abstract_read import AbstractRead


class ReadGroup(AbstractRead):
    def __init__(self) -> None:
        super().__init__()

    def load(self) -> typing.List(str):
        _data = None

        _path = os.path.join(self._ETC_PATH, "group")
        _file_read = self._read(_path)

        if _file_read is not None:
            _data = _file_read.splitlines()

        return _data

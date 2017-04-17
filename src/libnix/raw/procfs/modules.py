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


class Module:
    _NAME = "name"
    _SIZE = "size"
    _INSTANCES = "instances"
    _DEPENDENCIES = "depends"
    _STATE = "state"
    _MEMORY_OFFSET = "memory_offset"

    def __init__(self, line: str) -> None:
        self._module = dict()

        _data = line.split()

        if len(_data) is 6:
            self._module[self._NAME] = _data[0]
            self._module[self._SIZE] = _data[1]
            self._module[self._INSTANCES] = _data[2]
            self._module[self._DEPENDENCIES] = _data[3]
            self._module[self._STATE] = _data[4]
            self._module[self._MEMORY_OFFSET] = _data[5]

    # @property
    def get_name(self) -> str:
        return self._get_value(self._NAME)

    # @property
    def get_size(self) -> str:
        return self._get_value(self._SIZE)

    # @property
    def get_instances(self) -> str:
        return self._get_value(self._INSTANCES)

    # @property
    def get_dependencies(self) -> str:
        return self._get_value(self._DEPENDENCIES)

    # @property
    def get_state(self) -> str:
        return self._get_value(self._STATE)

    # @property
    def get_memory_offset(self) -> str:
        return self._get_value(self._MEMORY_OFFSET)

    def _get_value(self, item: str) -> typing.Optional[str]:
        try:
            return self._module[item]
        except KeyError:
            return None


class Modules(AbstractRead):
    def __init__(self) -> None:
        super().__init__()

    def load(self) -> None:
        self._data = dict()

        _path = os.path.join(self._PROC_PATH, "modules")
        _file_read = self._read(_path)

        if _file_read is not None:
            for _line in _file_read.splitlines():
                _module = Module(_line)

                self._data[_module.get_name()] = _module

    def get_modules(self) -> typing.List[str]:
        if self._data is None:
            self.load()

        return list(self._data.keys())

    def get_module(self, name: str) -> Module:
        if self._data is None:
            self.load()

        return self._data[name]

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

from libnix.config.config import Config
from libnix.exception.nix_error import NixError


class ImportScript:
    def __init__(self, path):
        self._config = Config()
        self._path = path
        self._name = None
        self._desc = None
        self._tags = None
        self._code = None

    def create(self):
        self._import()

        _invalid_tags = self._config.get_tags().get_invalid_tags(self._tags)

        if len(_invalid_tags) is not 0:
            raise NixError("Unknown tags: {}".format(' '.join(_invalid_tags)))

        if self._config.get_scripts().exist(self._name):
            raise NixError("Script already exists: {}".format(self._name))

        _script = self._config.get_scripts().insert()
        _script.set_code(self._code)
        _script.set_name(self._name)
        _script.set_desc(self._desc)
        _script.add_tags(self._tags)

        if _script.is_compile():
            _script.set_status(_script.STATUS_NORMAL)
        else:
            _script.set_status(_script.STATUS_COMPILE_ERROR)

        self._config.write()

    def _import(self):
        _content = self._read()

        _lines = _content.splitlines()

        _code = ""

        for _line in _lines:
            if _line.startswith("#nix_name="):
                self._name = _line.split("=", 1)[1]
            elif _line.startswith("#nix_desc="):
                self._desc = _line.split("=", 1)[1]
            elif _line.startswith("#nix_tags="):
                self._tags = _line.split("=", 1)[1].split()
            else:
                _code += _line + "\n"

        self._code = _code

    def _read(self) -> str:
        with open(self._path, 'r') as _file:
            _contents = _file.read()

        return _contents

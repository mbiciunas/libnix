"""
LibNix
Copyright (C) 2017  Mark Biciunas

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from libnix.config.config import Config
from libnix.exception.nix_error import NixError


class DeleteScript:
    def __init__(self):
        self._config = Config()

    def delete(self, name: str):
        _script = self._config.get_scripts().find_by_name(name)

        if _script is None:
            raise NixError("Script not found: {}".format(name))

        self._config.get_scripts().delete(name)

        self._config.write()

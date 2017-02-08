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


class RenameScript:
    def __init__(self):
        self._config = Config()

    def rename(self, name_old: str, name_new: str):
        if name_old == name_new:
            raise NixError("Old and new script names are the same: {}".format(name_old))

        if self._config.get_scripts().exist(name_new):
            raise NixError("New script name is already used: {}".format(name_new))

        _script = self._config.get_scripts().find_by_name(name_old)

        if _script is None:
            raise NixError("Script not found: {}".format(name_old))

        _script.set_name(name_new)

        self._config.write()

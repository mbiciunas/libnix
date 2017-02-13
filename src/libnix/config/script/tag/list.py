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
from libnix.utility.print_table import PrintTable
from libnix.exception.nix_error import NixError


class List:
    def __init__(self):
        self._config = Config()
        self._tags = self._config.get_tags()

    def list(self, script: str):
        _script = self._config.get_scripts().find_by_name(script)

        if _script is None:
            raise NixError("Script not found: {}".format(script))

        _rows = []

        for _tag_name in _script.get_tags():
            _tag = self._tags.find(_tag_name)

            _rows.append([_tag.get_name(),
                          _tag.get_desc()])

        _print_table = PrintTable("Tag", "Description")
        _print_table.add_data(_rows)
        _print_table.print()

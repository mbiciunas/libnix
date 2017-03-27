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


class ExportScript:
    def __init__(self, name, path):
        self._config = Config()
        self._name = name
        self._path = path

    def export(self):
        _script = self._config.get_scripts().find_by_name(self._name)

        if _script is None:
            raise NixError("Script not found: {}".format(self._name))

        _content = self._make_content(_script)

        self._write(_content)

        # self._config.write()

    @staticmethod
    def _make_content(script):
        _content = ""
        _content += "#nix_name={}\n".format(script.get_name())
        _content += "#nix_desc={}\n".format(script.get_desc())
        _content += "#nix_tags={}\n".format(script.get_tags())
        # _content += "\n"
        _content += script.get_code()

        return _content

    def _write(self, contents: str):
        with open(self._path, 'w') as _file:
            _file.write(contents)

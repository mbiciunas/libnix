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

from shutil import copyfile

from libnix.config.config import Config


class SetupConfig:
    _PATH_DST = "/home/mbiciunas/.nix/script/tag.json"

    _config = None
    _count_tags = None
    _count_scripts = None

    def __init__(self, source_file):
        copyfile(source_file, self._PATH_DST)
        self._config = Config()

    def config(self):
        return self._config

    def set_count_tags(self, count):
        self._count_tags = count

    def get_count_tags(self):
        return self._count_tags

    def set_count_scripts(self, count):
        self._count_scripts = count

    def get_count_scripts(self):
        return self._count_scripts

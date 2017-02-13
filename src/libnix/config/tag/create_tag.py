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


class CreateTag:
    def __init__(self):
        self._config = Config()
        self._tags = self._config.get_tags()

    def create(self, tag: str, description: str):
        if self._tags.exist(tag):
            raise NixError("Tag already exists: {}".format(tag))

        _tag = self._tags.insert()
        _tag.set_name(tag)
        _tag.set_desc(description)

        self._config.write()

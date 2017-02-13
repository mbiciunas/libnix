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


class RenameTag:
    def __init__(self):
        self._config = Config()
        self._tags = self._config.get_tags()
        self._scripts = self._config.get_scripts()

    def rename(self, tag: str, tag_new: str):
        if tag == tag_new:
            raise NixError("Original and new tag names are the same: {}".format(tag_new))

        if not self._tags.exist(tag):
            raise NixError("Unknown tag: {}".format(tag))

        if self._tags.exist(tag_new):
            raise NixError("New tag already exists: {}".format(tag_new))

        self._tags.find(tag).set_name(tag_new)

        _scripts = self._config.get_scripts().find_by_tag(tag)

        for _script in _scripts:
            _script_tags = _script.get_tags()

            if tag in _script_tags:
                _script_tags[_script_tags.index(tag)] = tag_new

        self._config.write()

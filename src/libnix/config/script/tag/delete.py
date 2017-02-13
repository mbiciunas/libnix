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

import typing
from libnix.config.config import Config
from libnix.exception.nix_error import NixError


class Delete:
    def __init__(self):
        self._config = Config()
        self._tags = self._config.get_tags()

    def delete(self, script: str, tags: typing.List[str]):
        _script = self._config.get_scripts().find_by_name(script)

        if _script is None:
            raise NixError("Script not found: {}".format(script))

        _invalid_tags = self._config.get_tags().get_invalid_tags(tags)

        if len(_invalid_tags) is not 0:
            raise NixError("Unknown tags: {}".format(' '.join(_invalid_tags)))

        _invalid_tags = [_tag for _tag in set(tags) if _tag not in _script.get_tags()]

        if len(_invalid_tags) is not 0:
            raise NixError("Tags not attached to script: {}".format(' '.join(_invalid_tags)))

        _script.delete_tags(tags)

        self._config.write()

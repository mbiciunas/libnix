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

import typing

from libnix.config.config_tag import ConfigTag
from libnix.exception.nix_error import NixError


class ConfigTags:
    def __init__(self):
        self._tags = []

    def exist(self, name: str) -> bool:
        try:
            return True if self.find(name) else False
        except NixError:
            return False
        # return True if self.find(name) is not None else False

    def get_invalid_tags(self, tags: list) -> typing.List[str]:
        # Use set to remove any duplicate tags
        _new_tags = list(set(tags))
        _existing_tags = [_tag.get_name() for _tag in self.list()]
        _invalid_tags = []

        for _tag in _new_tags:
            if _tag not in _existing_tags:
                _invalid_tags.append(_tag)

        return _invalid_tags

    def insert(self) -> ConfigTag:
        _tag = ConfigTag()

        self._tags.append(_tag)

        return _tag

    def delete(self, name: str):
        _delete = False

        for _tag in self._tags:
            if _tag.get_name() == name:
                self._tags.remove(_tag)
                _delete = True
                break

        if not _delete:
            raise NixError("Unable to delete, tag not found: {}".format(name))

    def list(self) -> typing.List[ConfigTag]:
        return [_tag for _tag in self._tags]

    def find(self, name: str) -> ConfigTag:
        for _tag in self._tags:
            if _tag.get_name() == name:
                return _tag

        raise NixError("Unable to find tag: {}".format(name))

    def export_data(self) -> typing.List[str]:
        _export = []

        for _tag in self._tags:
            _export.append(_tag.export_data())

        return _export

    def import_data(self, _data: typing.List[dict]):
        for _tag_data in _data:
            _tag = ConfigTag()

            _tag.import_data(_tag_data)

            self._tags.append(_tag)

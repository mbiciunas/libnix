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


class ConfigTag:
    TAG_NAME = "name"
    TAG_DESCRIPTION = "description"

    def __init__(self):
        self._tag = {self.TAG_NAME: "", self.TAG_DESCRIPTION: ""}

    def set_name(self, name: str):
        self._tag[self.TAG_NAME] = name

    def get_name(self) -> str:
        return self._tag[self.TAG_NAME]

    def set_desc(self, description: str):
        self._tag[self.TAG_DESCRIPTION] = description

    def get_desc(self) -> str:
        return self._tag[self.TAG_DESCRIPTION]

    def export_data(self) -> typing.Dict[str, str]:
        return self._tag

    def import_data(self, _data: dict):
        self._tag[self.TAG_NAME] = _data[self.TAG_NAME]
        self._tag[self.TAG_DESCRIPTION] = _data[self.TAG_DESCRIPTION]

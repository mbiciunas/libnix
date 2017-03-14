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

from libnix.raw.etc.read_group import ReadGroup


class Groups:
    def __init__(self):
        self._data = dict()

    def load(self):
        _read_group = ReadGroup()

        for _line in _read_group.load():
            _group = Group(_line)

            self._data[_group.get_group()] = _group

    def get_groups(self) -> iter:
        if self._data is None:
            self.load()

        return self._data.keys()

    def get_group(self, name: str) -> iter:
        if self._data is None:
            self.load()

        return self._data[name]


class Group:
    _GROUP_NAME = "group"
    _PASSWORD = "password"
    _GROUP_ID = "group_id"
    _USERS = "users"

    def __init__(self, line):
        self._group = dict()

        _data = line.split(":")

        if len(_data) is 4:
            self._group[self._GROUP_NAME] = _data[0]
            self._group[self._PASSWORD] = _data[1]
            self._group[self._GROUP_ID] = _data[2]
            self._group[self._USERS] = _data[3]

    # @property
    def get_group(self) -> str:
        return self._get_value(self._GROUP_NAME)

    # @property
    def get_password(self) -> str:
        return self._get_value(self._PASSWORD)

    # @property
    def get_group_id(self) -> str:
        return self._get_value(self._GROUP_ID)

    # @property
    def get_users(self) -> str:
        return self._get_value(self._USERS)

    def _get_value(self, item: str) -> typing.Optional[str]:
        try:
            return self._group[item]
        except KeyError:
            return None


def main():
    _groups = Groups()

    _groups.load()

    for _group_name in _groups.get_groups():
        _group = _groups.get_group(_group_name)

        print("Group: {}".format(_group.get_group()))
        print("   Password:     {}".format(_group.get_password()))
        print("   Group Id:     {}".format(_group.get_group_id()))
        print("   Users:      {}".format(_group.get_users()))

        print("")


if __name__ == "__main__":
    main()

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

from libnix.raw.etc.passwd import Passwd


class Users:
    def __init__(self):
        self._data = dict()

    def load(self):
        _passwd = Passwd()

        for _line in _passwd.load():
            _user = User(_line)

            self._data[_user.get_user()] = _user

    def get_users(self) -> iter:
        if self._data is None:
            self.load()

        return self._data.keys()

    def get_user(self, name: str) -> iter:
        if self._data is None:
            self.load()

        return self._data[name]


class User:
    _USER_NAME = "user"
    _PASSWORD = "password"
    _USER_ID = "user_id"
    _GROUP_ID = "group_id"
    _COMMENT = "comment"

    _DIRECTORY = "dir"
    _SHELL = "shell"

    def __init__(self, line):
        self._user = dict()

        _data = line.split(":")

        if len(_data) is 7:
            self._user[self._USER_NAME] = _data[0]
            self._user[self._PASSWORD] = _data[1]
            self._user[self._USER_ID] = _data[2]
            self._user[self._GROUP_ID] = _data[3]
            self._user[self._COMMENT] = _data[4]
            self._user[self._DIRECTORY] = _data[5]
            self._user[self._SHELL] = _data[6]

    # @property
    def get_user(self) -> str:
        return self._get_value(self._USER_NAME)

    # @property
    def get_password(self) -> str:
        return self._get_value(self._PASSWORD)

    # @property
    def get_user_id(self) -> str:
        return self._get_value(self._USER_ID)

    # @property
    def get_group_id(self) -> str:
        return self._get_value(self._GROUP_ID)

    # @property
    def get_comment(self) -> str:
        return self._get_value(self._COMMENT)

    # @property
    def get_directory(self) -> str:
        return self._get_value(self._DIRECTORY)

    # @property
    def get_shell(self) -> str:
        return self._get_value(self._SHELL)

    def _get_value(self, item: str) -> typing.Optional[str]:
        try:
            return self._user[item]
        except KeyError:
            return None


def main():
    _users = Users()

    _users.load()

    for _user_name in _users.get_users():
        _user = _users.get_user(_user_name)

        print("Name: {}".format(_user.get_user()))
        print("   Password:     {}".format(_user.get_password()))
        print("   User Id:      {}".format(_user.get_user_id()))
        print("   Group Id:     {}".format(_user.get_group_id()))
        print("   Comment:      {}".format(_user.get_comment()))
        print("   Directory:    {}".format(_user.get_directory()))
        print("   Shell:        {}".format(_user.get_shell()))

        print("")


if __name__ == "__main__":
    main()

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

import os

from libnix.raw.abstract_read import AbstractRead


class Passwd(AbstractRead):
    def __init__(self):
        super().__init__()

    def load(self):
        _data = None

        _path = os.path.join(self._ETC_PATH, "passwd")
        _file_read = self._read(_path)

        if _file_read is not None:
            _data = _file_read.splitlines()

        return _data

    # def get_users(self) -> iter:
    #     if self._data is None:
    #         self.load()
    #
    #     return self._data.keys()

    # def get_user(self, name: str) -> iter:
    #     if self._data is None:
    #         self.load()
    #
    #     return self._data[name]


# def main():
#     _passwd = Passwd()
#
#     _passwd.load()
#
#     for _user_name in _passwd.get_users():
#         _user = _passwd.get_user(_user_name)
#
#         print("Name: {}".format(_user.get_user()))
#         print("   Password:     {}".format(_user.get_password()))
#         print("   User Id:      {}".format(_user.get_user_id()))
#         print("   Group Id:     {}".format(_user.get_group_id()))
#         print("   Comment:      {}".format(_user.get_comment()))
#         print("   Directory:    {}".format(_user.get_directory()))
#         print("   Shell:        {}".format(_user.get_shell()))
#
#         print("")
#
#
# if __name__ == "__main__":
#     main()

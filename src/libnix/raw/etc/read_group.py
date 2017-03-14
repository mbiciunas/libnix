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


class ReadGroup(AbstractRead):
    def __init__(self):
        super().__init__()

    def load(self):
        _data = None

        _path = os.path.join(self._ETC_PATH, "group")
        _file_read = self._read(_path)

        if _file_read is not None:
            _data = _file_read.splitlines()

        return _data

    # def get_groups(self) -> iter:
    #     if self._data is None:
    #         self.load()
    #
    #     return self._data.keys()

    # def get_group(self, name: str) -> iter:
    #     if self._data is None:
    #         self.load()
    #
    #     return self._data[name]


# def main():
#     _groups = Groups()
#
#     _groups.load()
#
#     for _group_name in _groups.get_groups():
#         _group = _groups.get_group(_group_name)
#
#         print("Group: {}".format(_group.get_group()))
#         print("   Password:     {}".format(_group.get_password()))
#         print("   Group Id:     {}".format(_group.get_group_id()))
#         print("   Users:      {}".format(_group.get_users()))
#
#         print("")
#
#
# if __name__ == "__main__":
#     main()

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

from libnix.sys.user.user import Users
from libnix.sys.user.group import Groups
from libnix.sys.fs.filesystem import Filesystem


class Sys:
    def __init__(self) -> None:
        pass

    @staticmethod
    def get_users(load: bool=False) -> Users:
        _users = Users()

        if load:
            _users.load()

        return _users

    @staticmethod
    def get_groups(load: bool=False) -> Groups:
        _groups = Groups()

        if load:
            _groups.load()

        return _groups

    @staticmethod
    def get_filesystem() -> Filesystem:
        return Filesystem()


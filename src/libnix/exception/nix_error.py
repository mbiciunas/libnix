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


class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class NixError(Error):
    def __init__(self, message: str, exception: Exception=None) -> None:
        self._message = message
        self._exception = exception

    def get_message(self) -> str:
        return self._message

    def get_exception(self) -> Exception:
        return self._exception

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


class UpdateScript:
    def __init__(self, name):
        self._config = Config()
        self._name = name

    def update(self):
        _script = self._config.get_scripts().find_by_name(self._name)

        if _script is None:
            raise NixError("Script not found: {}".format(self._name))

        _script.make_temp(_script.get_code())

        _script.call_editor()

        _script.set_code(_script.read_temp_file())

        if _script.is_compile():
            _script.set_status(_script.STATUS_NORMAL)
        else:
            _script.set_status(_script.STATUS_COMPILE_ERROR)

        self._config.write()


def main():
    update_script = UpdateScript("my_processes")

    update_script.update()


if __name__ == "__main__":
    main()

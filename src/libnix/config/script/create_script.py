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

from libnix.config.config import Config
from libnix.exception.nix_error import NixError


class CreateScript:
    TEMPLATE = "from libnix1.process.processes import Processes\n"
    TEMPLATE += "from libnix1.utility.print_table import PrintTable\n"
    TEMPLATE += "\n"
    TEMPLATE += "_processes = Processes()\n"
    TEMPLATE += "\n"

    def __init__(self, name, desc, tags):
        self._config = Config()
        self._name = name
        self._desc = desc
        self._tags = tags

    def create(self):
        _invalid_tags = self._config.get_tags().get_invalid_tags(self._tags)

        if len(_invalid_tags) is not 0:
            raise NixError("Unknown tags: {}".format(' '.join(_invalid_tags)))

        if self._config.get_scripts().exist(self._name):
            raise NixError("Script already exists: {}".format(self._name))

        _script = self._config.get_scripts().insert()

        _script.make_temp(self.TEMPLATE)

        _script.call_editor()

        _script.set_code(_script.read_temp_file())
        _script.set_name(self._name)
        _script.set_desc(self._desc)
        _script.add_tags(self._tags)

        if _script.is_compile():
            _script.set_status(_script.STATUS_NORMAL)
        else:
            _script.set_status(_script.STATUS_COMPILE_ERROR)

        self._config.write()


def main():
    create_script = CreateScript("my_processes", "new test process", ["test", "test1"])

    create_script.create()


if __name__ == "__main__":
    main()

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


class ProcCmdline(AbstractRead):
    _COMMAND = "size"
    _ARGS = "args"

    def __init__(self, pid: int):
        super().__init__()
        self._pid = pid

    def load(self):
        self._data = dict()

        _path = os.path.join(self._PROC_PATH, str(self._pid), "cmdline")
        _file_read = self._read(_path)

        if _file_read is not None:
            _file_data = _file_read.split('\x00')

            if len(_file_data) > 0:
                self._data[self._COMMAND] = _file_data[0]

            if len(_file_data) > 1:
                self._data[self._ARGS] = list(filter(None, _file_data[1:]))

    @property
    def get_command(self) -> str:
        return self._get_value(self._COMMAND)

    @property
    def get_argument_count(self) -> int:
        return len(self._get_value(self._ARGS))

    @property
    def get_arguments(self) -> str:
        return self._get_value(self._ARGS)


def main():
    run_cmdline(1637)


def run_cmdline(pid: int):
    proc_cmdline = ProcCmdline(pid)

    print("COMMAND:   {}".format(proc_cmdline.get_command))
    if proc_cmdline.get_argument_count > 0:
        print("ARGUMENTS: {}".format(proc_cmdline.get_arguments[0]))
    if proc_cmdline.get_argument_count > 1:
        for index in range(1, proc_cmdline.get_argument_count):
            print("           {}".format(proc_cmdline.get_arguments[index]))

    print("")

if __name__ == "__main__":
    main()

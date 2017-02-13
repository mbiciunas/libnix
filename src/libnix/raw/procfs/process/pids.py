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
import typing

from libnix.raw.procfs.process.process import Process


class Pids:
    def __init__(self):
        self._PATH = "/proc"

        self._pids = {}

        self.load()

    def load(self):
        self._pids = dict()

        for _name in self._get_immediate_subdirectories():
            if _name.isdigit():
                self._pids[_name] = Process(int(_name))

    def _get_immediate_subdirectories(self) -> list:
        return [name for name in os.listdir(self._PATH) if os.path.isdir(os.path.join(self._PATH, name))]

    @property
    def get_pids(self) -> iter:
        return self._pids.keys()

    def get_process(self, pid: str) -> typing.Any:
        return self._pids[pid]

    def find_process(self, name) -> typing.Optional[str]:
        for pid, process in self._pids.items():
            if process.get_comm.get_command == name:
                return self._pids[pid]

        return None


def main():
    _processes = Pids()

    for pid in _processes.get_pids:
        _process = _processes.get_process(pid)
        print("{} {} - {} - {} - {} - {} - {}".format(pid,
                                                      _process.get_comm.get_command,
                                                      _process.get_stat.get_nice,
                                                      _process.get_statm.get_size,
                                                      _process.get_environ.get_environment_count,
                                                      _process.get_io.get_char_read,
                                                      _process.get_status.get_uid_real))

if __name__ == "__main__":
    main()

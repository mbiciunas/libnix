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

from libnix.raw.procfs.process.proc_cmdline import ProcCmdline
from libnix.raw.procfs.process.proc_comm import ProcComm
from libnix.raw.procfs.process.proc_environ import ProcEnviron
from libnix.raw.procfs.process.proc_io import ProcIO
from libnix.raw.procfs.process.proc_stat import ProcStat
from libnix.raw.procfs.process.proc_statm import ProcStatM
from libnix.raw.procfs.process.proc_status import ProcStatus


class Process:

    def __init__(self, pid: int) -> None:
        self._pid = pid
        self._cmdline = ProcCmdline(pid)
        self._comm = ProcComm(pid)
        self._environ = ProcEnviron(pid)
        self._io = ProcIO(pid)
        self._stat = ProcStat(pid)
        self._statm = ProcStatM(pid)
        self._status = ProcStatus(pid)

    @property
    def get_pid(self) -> int:
        return self._pid

    @property
    def get_comm(self) -> ProcComm:
        return self._comm

    @property
    def get_cmdline(self) -> ProcCmdline:
        return self._cmdline

    @property
    def get_environ(self) -> ProcEnviron:
        return self._environ

    @property
    def get_io(self) -> ProcIO:
        return self._io

    @property
    def get_stat(self) -> ProcStat:
        return self._stat

    @property
    def get_statm(self) -> ProcStatM:
        return self._statm

    @property
    def get_status(self) -> ProcStatus:
        return self._status

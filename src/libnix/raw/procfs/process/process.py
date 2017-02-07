from libnix.raw.procfs.process.proc_cmdline import ProcCmdline
from libnix.raw.procfs.process.proc_comm import ProcComm
from libnix.raw.procfs.process.proc_environ import ProcEnviron
from libnix.raw.procfs.process.proc_io import ProcIO
from libnix.raw.procfs.process.proc_stat import ProcStat
from libnix.raw.procfs.process.proc_statm import ProcStatM
from libnix.raw.procfs.process.proc_status import ProcStatus


class Process:

    def __init__(self, pid: int):
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

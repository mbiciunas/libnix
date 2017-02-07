from libnix.raw.procfs.diskstats import DiskStats
from libnix.raw.procfs.modules import Modules
from libnix.raw.procfs.mounts import Mounts
from libnix.raw.procfs.process.pids import Pids
from libnix.raw.sysfs.clazz.net.sys_class_net import SysClassNet
from libnix.raw.sysfs.clazz.net.stat.sys_class_net_stat import SysClassNetStat


class Raw:
    def __init__(self):
        self._diskstats = DiskStats()
        self._modules = Modules()
        self._mounts = Mounts()
        self._pids = Pids()
        self._sys_class_net = SysClassNet()
        self._sys_class_net_stat = SysClassNetStat()

    def get_proc_diskstats(self) -> DiskStats:
        return self._diskstats

    def get_proc_modules(self) -> Modules:
        return self._modules

    def get_proc_mounts(self) -> Mounts:
        return self._mounts

    def get_proc_pids(self) -> Pids:
        return self._pids

    def get_sys_class_net(self) -> SysClassNet:
        return self._sys_class_net

    def get_sys_class_net_stat(self) -> SysClassNetStat:
        return self._sys_class_net_stat

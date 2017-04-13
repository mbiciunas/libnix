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

from libnix.raw.procfs.diskstats import DiskStats
from libnix.raw.procfs.modules import Modules
from libnix.raw.procfs.mounts import Mounts
from libnix.raw.procfs.process.pids import Pids
from libnix.raw.sysfs.clazz.net.sys_class_net import SysClassNet
from libnix.raw.sysfs.clazz.net.stat.sys_class_net_stat import SysClassNetStat


class Raw:
    def __init__(self) -> None:
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

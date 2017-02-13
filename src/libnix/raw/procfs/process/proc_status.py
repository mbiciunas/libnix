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


class ProcStatus(AbstractRead):
    _NAME = "Name:"
    _UMASK = "Umask:"
    _STATE = "State:"
    _THREAD_GID = "Tgid:"
    _NUMA_GID = "Ngid:"
    _PID = "Pid:"
    _PARENT_PID = "PPid:"
    _TRACER_PID = "TracerPid:"
    _UID = "Uid:"
    _GID = "Gid:"

    _FD_SIZE = "FDSize:"
    _GROUPS = "Groups:"
    _NAMESPACE_THREAD_GID = "NStgid:"
    _NAMESPACE_PID = "NSpid:"
    _NAMESPACE_PGID = "NSpgid:"
    _NAMESPACE_SID = "NSsid:"
    _VIRTUAL_MEMORY_PEAK = "VmPeak:"
    _VIRTUAL_MEMORY_SIZE = "VmSize:"
    _VIRTUAL_MEMORY_LOCK = "VmLck:"
    _VIRTUAL_MEMORY_PIN = "VmPin:"

    _VIRTUAL_MEMORY_HWM = "VmHWM:"
    _VIRTUAL_MEMORY_RSS = "VmRSS:"
    _RSS_ANON = "RssAnon:"
    _RSS_FILE = "RssFile:"
    _RSS_SHARED_MEM = "RssShmem:"
    _VM_DATA = "VmData:"
    _VIRTUAL_MEMORY_STACK = "VmStk:"
    _VIRTUAL_MEMORY_EXE = "VmExe:"
    _VIRTUAL_MEMORY_LIB = "VmLib:"
    _VIRTUAL_MEMORY_PTE = "VmPTE:"

    _VIRTUAL_MEMORY_PMD = "VmPMD:"
    _VIRTUAL_MEMORY_SWAP = "VmSwap:"
    _HUGE_TLB_PAGES = "HugetlbPages:"
    _THREADS = "Threads:"
    _SIGNAL_QUEUE = "SigQ:"
    _SIGNAL_PENDING = "SigPnd:"
    _SHD_PND = "ShdPnd:"
    _SIGNAL_BLOCK = "SigBlk:"
    _SIGNAL_IGNORE = "SigIgn:"
    _SIGNAL_CAUGHT = "SigCgt:"

    _CAPABILITY_INHERIT = "CapInh:"
    _CAPABILITY_PERMITTED = "CapPrm:"
    _CAPABILITY_EFFECTIVE = "CapEff:"
    _CAPABILITY_BOUND = "CapBnd:"
    _CAPABILITY_AMBIENT = "CapAmb:"
    _SECURE_COMPUTE = "Seccomp:"
    _CPU_ALLOWED = "Cpus_allowed:"
    _CPU_ALLOWED_LIST = "Cpus_allowed_list:"
    _MEMORY_NODES_ALLOWED = "Mems_allowed:"
    _MEMORY_NODES_ALLOWED_LIST = "Mems_allowed_list:"

    _VOLUNTARY_CONTEXT_SWITCH = "voluntary_ctxt_switches:"
    _NON_VOLUNTARY_CONTEXT_SWITCH = "nonvoluntary_ctxt_switches:"

    def __init__(self, pid: int):
        super().__init__()
        self._pid = pid

    def load(self):
        self._data = dict()

        _path = os.path.join(self._PROC_PATH, str(self._pid), "status")
        _file_read = self._read(_path)

        if _file_read is not None:
            _file_data = _file_read.splitlines()

            if len(_file_data) > 30:
                for _line in _file_data:
                    if _line.startswith(self._NAME):
                        self._data[self._NAME] = _line.split(":")[1]
                    elif _line.startswith(self._UMASK):
                        self._data[self._UMASK] = _line.split(":")[1]
                    elif _line.startswith(self._STATE):
                        self._data[self._STATE] = _line.split(":")[1]
                    elif _line.startswith(self._THREAD_GID):
                        self._data[self._THREAD_GID] = _line.split(":")[1]
                    elif _line.startswith(self._NUMA_GID):
                        self._data[self._NUMA_GID] = _line.split(":")[1]
                    elif _line.startswith(self._PID):
                        self._data[self._PID] = _line.split(":")[1]
                    elif _line.startswith(self._PARENT_PID):
                        self._data[self._PARENT_PID] = _line.split(":")[1]
                    elif _line.startswith(self._TRACER_PID):
                        self._data[self._TRACER_PID] = _line.split(":")[1]
                    elif _line.startswith(self._UID):
                        self._data[self._UID] = _line.split(":")[1]
                    elif _line.startswith(self._GID):
                        self._data[self._GID] = _line.split(":")[1]
                    elif _line.startswith(self._FD_SIZE):
                        self._data[self._FD_SIZE] = _line.split(":")[1]
                    elif _line.startswith(self._GROUPS):
                        self._data[self._GROUPS] = _line.split(":")[1]
                    elif _line.startswith(self._NAMESPACE_THREAD_GID):
                        self._data[self._NAMESPACE_THREAD_GID] = _line.split(":")[1]
                    elif _line.startswith(self._NAMESPACE_PID):
                        self._data[self._NAMESPACE_PID] = _line.split(":")[1]
                    elif _line.startswith(self._NAMESPACE_PGID):
                        self._data[self._NAMESPACE_PGID] = _line.split(":")[1]
                    elif _line.startswith(self._NAMESPACE_SID):
                        self._data[self._NAMESPACE_SID] = _line.split(":")[1]
                    elif _line.startswith(self._VIRTUAL_MEMORY_PEAK):
                        self._data[self._VIRTUAL_MEMORY_PEAK] = _line.split(":")[1]
                    elif _line.startswith(self._VIRTUAL_MEMORY_SIZE):
                        self._data[self._VIRTUAL_MEMORY_SIZE] = _line.split(":")[1]
                    elif _line.startswith(self._VIRTUAL_MEMORY_LOCK):
                        self._data[self._VIRTUAL_MEMORY_LOCK] = _line.split(":")[1]
                    elif _line.startswith(self._VIRTUAL_MEMORY_PIN):
                        self._data[self._VIRTUAL_MEMORY_PIN] = _line.split(":")[1]
                    elif _line.startswith(self._VIRTUAL_MEMORY_HWM):
                        self._data[self._VIRTUAL_MEMORY_HWM] = _line.split(":")[1]
                    elif _line.startswith(self._VIRTUAL_MEMORY_RSS):
                        self._data[self._VIRTUAL_MEMORY_RSS] = _line.split(":")[1]
                    elif _line.startswith(self._RSS_ANON):
                        self._data[self._RSS_ANON] = _line.split(":")[1]
                    elif _line.startswith(self._RSS_FILE):
                        self._data[self._RSS_FILE] = _line.split(":")[1]
                    elif _line.startswith(self._RSS_SHARED_MEM):
                        self._data[self._RSS_SHARED_MEM] = _line.split(":")[1]
                    elif _line.startswith(self._VM_DATA):
                        self._data[self._VM_DATA] = _line.split(":")[1]
                    elif _line.startswith(self._VIRTUAL_MEMORY_STACK):
                        self._data[self._VIRTUAL_MEMORY_STACK] = _line.split(":")[1]
                    elif _line.startswith(self._VIRTUAL_MEMORY_EXE):
                        self._data[self._VIRTUAL_MEMORY_EXE] = _line.split(":")[1]
                    elif _line.startswith(self._VIRTUAL_MEMORY_LIB):
                        self._data[self._VIRTUAL_MEMORY_LIB] = _line.split(":")[1]
                    elif _line.startswith(self._VIRTUAL_MEMORY_PTE):
                        self._data[self._VIRTUAL_MEMORY_PTE] = _line.split(":")[1]
                    elif _line.startswith(self._VIRTUAL_MEMORY_PMD):
                        self._data[self._VIRTUAL_MEMORY_PMD] = _line.split(":")[1]
                    elif _line.startswith(self._VIRTUAL_MEMORY_SWAP):
                        self._data[self._VIRTUAL_MEMORY_SWAP] = _line.split(":")[1]
                    elif _line.startswith(self._HUGE_TLB_PAGES):
                        self._data[self._HUGE_TLB_PAGES] = _line.split(":")[1]
                    elif _line.startswith(self._THREADS):
                        self._data[self._THREADS] = _line.split(":")[1]
                    elif _line.startswith(self._SIGNAL_QUEUE):
                        self._data[self._SIGNAL_QUEUE] = _line.split(":")[1]
                    elif _line.startswith(self._SIGNAL_PENDING):
                        self._data[self._SIGNAL_PENDING] = _line.split(":")[1]
                    elif _line.startswith(self._SHD_PND):
                        self._data[self._SHD_PND] = _line.split(":")[1]
                    elif _line.startswith(self._SIGNAL_BLOCK):
                        self._data[self._SIGNAL_BLOCK] = _line.split(":")[1]
                    elif _line.startswith(self._SIGNAL_IGNORE):
                        self._data[self._SIGNAL_IGNORE] = _line.split(":")[1]
                    elif _line.startswith(self._SIGNAL_CAUGHT):
                        self._data[self._SIGNAL_CAUGHT] = _line.split(":")[1]
                    elif _line.startswith(self._CAPABILITY_INHERIT):
                        self._data[self._CAPABILITY_INHERIT] = _line.split(":")[1]
                    elif _line.startswith(self._CAPABILITY_PERMITTED):
                        self._data[self._CAPABILITY_PERMITTED] = _line.split(":")[1]
                    elif _line.startswith(self._CAPABILITY_EFFECTIVE):
                        self._data[self._CAPABILITY_EFFECTIVE] = _line.split(":")[1]
                    elif _line.startswith(self._CAPABILITY_BOUND):
                        self._data[self._CAPABILITY_BOUND] = _line.split(":")[1]
                    elif _line.startswith(self._CAPABILITY_AMBIENT):
                        self._data[self._CAPABILITY_AMBIENT] = _line.split(":")[1]
                    elif _line.startswith(self._SECURE_COMPUTE):
                        self._data[self._SECURE_COMPUTE] = _line.split(":")[1]
                    elif _line.startswith(self._CPU_ALLOWED):
                        self._data[self._CPU_ALLOWED] = _line.split(":")[1]
                    elif _line.startswith(self._CPU_ALLOWED_LIST):
                        self._data[self._CPU_ALLOWED_LIST] = _line.split(":")[1]
                    elif _line.startswith(self._MEMORY_NODES_ALLOWED):
                        self._data[self._MEMORY_NODES_ALLOWED] = _line.split(":")[1]
                    elif _line.startswith(self._MEMORY_NODES_ALLOWED_LIST):
                        self._data[self._MEMORY_NODES_ALLOWED_LIST] = _line.split(":")[1]
                    elif _line.startswith(self._VOLUNTARY_CONTEXT_SWITCH):
                        self._data[self._VOLUNTARY_CONTEXT_SWITCH] = _line.split(":")[1]
                    elif _line.startswith(self._NON_VOLUNTARY_CONTEXT_SWITCH):
                        self._data[self._NON_VOLUNTARY_CONTEXT_SWITCH] = _line.split(":")[1]

    @property
    def get_name(self) -> str:
        return self._get_value(self._NAME)

    @property
    def get_umask(self) -> str:
        return self._get_value(self._UMASK)

    @property
    def get_state(self) -> str:
        return self._get_value(self._STATE)

    @property
    def get_thread_gid(self) -> str:
        return self._get_value(self._THREAD_GID)

    @property
    def get_numa_gid(self) -> str:
        return self._get_value(self._NUMA_GID)

    @property
    def get_pid(self) -> str:
        return self._get_value(self._PID)

    @property
    def get_parent_pid(self) -> str:
        return self._get_value(self._PARENT_PID)

    @property
    def get_tracer_pid(self) -> str:
        return self._get_value(self._TRACER_PID)

    @property
    def get_uid_real(self) -> str:
        return self._get_value(self._UID).split()[0]

    @property
    def get_uid_effective(self) -> str:
        return self._get_value(self._UID).split()[1]

    @property
    def get_uid_saved_set(self) -> str:
        return self._get_value(self._UID).split()[2]

    @property
    def get_uid_filesystem(self) -> str:
        return self._get_value(self._UID).split()[3]

    @property
    def get_gid_real(self) -> str:
        return self._get_value(self._GID).split()[0]

    @property
    def get_gid_effective(self) -> str:
        return self._get_value(self._GID).split()[1]

    @property
    def get_gid_saved_set(self) -> str:
        return self._get_value(self._GID).split()[2]

    @property
    def get_gid_filesystem(self) -> str:
        return self._get_value(self._GID).split()[3]

    @property
    def get_fd_size(self) -> str:
        return self._get_value(self._FD_SIZE)

    @property
    def get_groups(self) -> str:
        return self._get_value(self._GROUPS)

    @property
    def get_namespace_thread_gid(self) -> str:
        return self._get_value(self._NAMESPACE_THREAD_GID)

    @property
    def get_namespace_pid(self) -> str:
        return self._get_value(self._NAMESPACE_PID)

    @property
    def get_namespace_pgid(self) -> str:
        return self._get_value(self._NAMESPACE_PGID)

    @property
    def get_namespace_sid(self) -> str:
        return self._get_value(self._NAMESPACE_SID)

    @property
    def get_virtual_memory_peak(self) -> str:
        return self._get_value(self._VIRTUAL_MEMORY_PEAK)

    @property
    def get_virtual_memory_size(self) -> str:
        return self._get_value(self._VIRTUAL_MEMORY_SIZE)

    @property
    def get_virtual_memory_lock(self) -> str:
        return self._get_value(self._VIRTUAL_MEMORY_LOCK)

    @property
    def get_virtual_memory_pin(self) -> str:
        return self._get_value(self._VIRTUAL_MEMORY_PIN)

    @property
    def get_virtual_memory_hwm(self) -> str:
        return self._get_value(self._VIRTUAL_MEMORY_HWM)

    @property
    def get_virtual_memory_rss(self) -> str:
        return self._get_value(self._VIRTUAL_MEMORY_RSS)

    @property
    def get_rss_anon(self) -> str:
        return self._get_value(self._RSS_ANON)

    @property
    def get_rss_file(self) -> str:
        return self._get_value(self._RSS_FILE)

    @property
    def get_rss_shared(self) -> str:
        return self._get_value(self._RSS_SHARED_MEM)

    @property
    def get_virtual_memory_data(self) -> str:
        return self._get_value(self._VM_DATA)

    @property
    def get_virtual_memory_stack(self) -> str:
        return self._get_value(self._VIRTUAL_MEMORY_STACK)

    @property
    def get_virtual_memory_exe(self) -> str:
        return self._get_value(self._VIRTUAL_MEMORY_EXE)

    @property
    def get_virtual_memory_lib(self) -> str:
        return self._get_value(self._VIRTUAL_MEMORY_LIB)

    @property
    def get_virtual_memory_pte(self) -> str:
        return self._get_value(self._VIRTUAL_MEMORY_PTE)

    @property
    def get_virtual_memory_pmd(self) -> str:
        return self._get_value(self._VIRTUAL_MEMORY_PMD)

    @property
    def get_virtual_memory_swap(self) -> str:
        return self._get_value(self._VIRTUAL_MEMORY_SWAP)

    @property
    def get_huge_tlb_pages(self) -> str:
        return self._get_value(self._HUGE_TLB_PAGES)

    @property
    def get_threads(self) -> str:
        return self._get_value(self._THREADS)

    @property
    def get_signal_queue(self) -> str:
        return self._get_value(self._SIGNAL_QUEUE)

    @property
    def get_signal_pending(self) -> str:
        return self._get_value(self._SIGNAL_PENDING)

    @property
    def get_shd_pnd(self) -> str:
        return self._get_value(self._SHD_PND)

    @property
    def get_signal_block(self) -> str:
        return self._get_value(self._SIGNAL_BLOCK)

    @property
    def get_signal_ignore(self) -> str:
        return self._get_value(self._SIGNAL_IGNORE)

    @property
    def get_signal_caught(self) -> str:
        return self._get_value(self._SIGNAL_CAUGHT)

    @property
    def get_capability_inherit(self) -> str:
        return self._get_value(self._CAPABILITY_INHERIT)

    @property
    def get_capability_permitted(self) -> str:
        return self._get_value(self._CAPABILITY_PERMITTED)

    @property
    def get_capability_effective(self) -> str:
        return self._get_value(self._CAPABILITY_EFFECTIVE)

    @property
    def get_capability_bound(self) -> str:
        return self._get_value(self._CAPABILITY_BOUND)

    @property
    def get_capability_ambient(self) -> str:
        return self._get_value(self._CAPABILITY_AMBIENT)

    @property
    def get_secure_compute(self) -> str:
        return self._get_value(self._SECURE_COMPUTE)

    @property
    def get_cpu_allowed(self) -> str:
        return self._get_value(self._CPU_ALLOWED)

    @property
    def get_cpu_allowed_list(self) -> str:
        return self._get_value(self._CPU_ALLOWED_LIST)

    @property
    def get_memory_nodes_allowed(self) -> str:
        return self._get_value(self._MEMORY_NODES_ALLOWED)

    @property
    def get_memory_nodes_allowed_list(self) -> str:
        return self._get_value(self._MEMORY_NODES_ALLOWED_LIST)

    @property
    def get_voluntary_context_switch(self) -> str:
        return self._get_value(self._VOLUNTARY_CONTEXT_SWITCH)

    @property
    def get_non_voluntary_context_switch(self) -> str:
        return self._get_value(self._NON_VOLUNTARY_CONTEXT_SWITCH)


def main():
    proc_status = ProcStatus(1637)

    print("name:                         {}".format(proc_status.get_name))
    print("umask:                        {}".format(proc_status.get_umask))
    print("state:                        {}".format(proc_status.get_state))
    print("thread_gid:                   {}".format(proc_status.get_thread_gid))
    print("numa_gid:                     {}".format(proc_status.get_numa_gid))
    print("pid:                          {}".format(proc_status.get_pid))
    print("parent_pid:                   {}".format(proc_status.get_parent_pid))
    print("tracer_pid:                   {}".format(proc_status.get_tracer_pid))
    print("uid_real:                     {}".format(proc_status.get_uid_real))
    print("uid_effective:                {}".format(proc_status.get_uid_effective))
    print("uid saved set:                {}".format(proc_status.get_uid_saved_set))
    print("uid filesystem:               {}".format(proc_status.get_uid_filesystem))
    print("gid real:                     {}".format(proc_status.get_gid_real))
    print("gid effective:                {}".format(proc_status.get_gid_effective))
    print("gid saved set:                {}".format(proc_status.get_gid_saved_set))
    print("gid filesystem:               {}".format(proc_status.get_gid_filesystem))

    print("fd_size:                      {}".format(proc_status.get_fd_size))
    print("groups:                       {}".format(proc_status.get_groups))
    print("namespace_thread_gid:         {}".format(proc_status.get_namespace_thread_gid))
    print("namespace_pid:                {}".format(proc_status.get_namespace_pid))
    print("namespace_pgid:               {}".format(proc_status.get_namespace_pgid))
    print("namespace_sid:                {}".format(proc_status.get_namespace_sid))
    print("virtual_memory_peak:          {}".format(proc_status.get_virtual_memory_peak))
    print("virtual_memory_size:          {}".format(proc_status.get_virtual_memory_size))
    print("virtual_memory_lock:          {}".format(proc_status.get_virtual_memory_lock))
    print("virtual_memory_pin:           {}".format(proc_status.get_virtual_memory_pin))

    print("virtual_memory_hwm:           {}".format(proc_status.get_virtual_memory_hwm))
    print("virtual_memory_rss:           {}".format(proc_status.get_virtual_memory_rss))
    print("rss_anon:                     {}".format(proc_status.get_rss_anon))
    print("rss_file:                     {}".format(proc_status.get_rss_file))
    print("rss_shared:                   {}".format(proc_status.get_rss_shared))
    print("virtual_memory_data:          {}".format(proc_status.get_virtual_memory_data))
    print("virtual_memory_stack:         {}".format(proc_status.get_virtual_memory_stack))
    print("virtual_memory_exe:           {}".format(proc_status.get_virtual_memory_exe))
    print("virtual_memory_lib:           {}".format(proc_status.get_virtual_memory_lib))
    print("virtual_memory_pte:           {}".format(proc_status.get_virtual_memory_pte))

    print("virtual_memory_pmd:           {}".format(proc_status.get_virtual_memory_pmd))
    print("virtual_memory_swap:          {}".format(proc_status.get_virtual_memory_swap))
    print("huge_tlb_pages:               {}".format(proc_status.get_huge_tlb_pages))
    print("threads:                      {}".format(proc_status.get_threads))
    print("signal_queue:                 {}".format(proc_status.get_signal_queue))
    print("signal_pending:               {}".format(proc_status.get_signal_pending))
    print("shd_pnd:                      {}".format(proc_status.get_shd_pnd))
    print("signal_block:                 {}".format(proc_status.get_signal_block))
    print("signal_ignore:                {}".format(proc_status.get_signal_ignore))
    print("signal_caught:                {}".format(proc_status.get_signal_caught))

    print("capability_inherit:           {}".format(proc_status.get_capability_inherit))
    print("capability_permitted:         {}".format(proc_status.get_capability_permitted))
    print("capability_effective:         {}".format(proc_status.get_capability_effective))
    print("capability_bound:             {}".format(proc_status.get_capability_bound))
    print("capability_ambient:           {}".format(proc_status.get_capability_ambient))
    print("secure_compute:               {}".format(proc_status.get_secure_compute))
    print("cpu_allowed:                  {}".format(proc_status.get_cpu_allowed))
    print("cpu_allowed_list:             {}".format(proc_status.get_cpu_allowed_list))
    print("memory_nodes_allowed:         {}".format(proc_status.get_memory_nodes_allowed))
    print("memory_nodes_allowed_list:    {}".format(proc_status.get_memory_nodes_allowed_list))

    print("voluntary_context_switch:     {}".format(proc_status.get_voluntary_context_switch))
    print("non_voluntary_context_switch: {}".format(proc_status.get_non_voluntary_context_switch))

    print("")


if __name__ == "__main__":
    main()

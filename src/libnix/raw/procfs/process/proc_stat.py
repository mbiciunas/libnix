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
from libnix.exception.nix_error import NixError


class ProcStat(AbstractRead):
    _PID = "pid"
    _COMMAND = "comm"
    _STATE = "state"
    _PARENT_PID = "ppid"
    _PROCESS_GROUP = "pgrp"
    _SESSION = "session"
    _TTY_NR = "tty_nr"
    _TPGID = "tpgid"
    _FLAGS = "flags"
    _MINOR_FAULT = "minflt"
    _CHILD_MINOR_FAULT = "cminflt"
    _MAJOR_FAULT = "majflt"
    _CHILD_MAJOR_FAULT = "cmajflt"
    _USER_TIME = "utime"
    _SYSTEM_TIME = "stime"
    _CHILD_USER_TIME = "cutime"
    _CHILD_SYSTEM_TIME = "cstime"
    _PRIORITY = "priority"
    _NICE = "nice"
    _THREADS = "num_threads"
    _I_T_REAL_VALUE = "itrealvalue"
    _START_TIME = "starttime"
    _VIRTUAL_SIZE = "vsize"
    _RESIDENT_SET_SIZE = "rss"
    _RSS_LIMIT = "rsslim"
    _START_CODE = "startcode"
    _END_CODE = "endcode"
    _START_STACK = "startstack"
    _KERNEL_STACK_ESP = "kstkesp"
    _CURRENT_EIP = "kstkeip"
    _PENDING_SIGNAL = "signal"
    _BLOCKED_SIGNAL = "blocked"
    _IGNORED_SIGNAL = "sigignore"
    _CAUGHT_SIGNAL = "sigcatch"
    _WAIT_CHANNEL = "wchan"
    _PAGE_SWAP = "nswap"
    _CUMULATIVE_PAGE_SWAP = "cnswap"
    _EXIT_SIGNAL = "exit_signal"
    _PROCESSOR = "processor"
    _REAL_TIME_PRIORITY = "rt_priority"
    _POLICY = "policy"
    _AGGREGATE_BLOCK_IO = "delayacct_blkio_ticks"
    _GUEST_TIME = "guest_time"
    _CHILD_GUEST_TIME = "cguest_time"

    def __init__(self, pid: int):
        super().__init__()
        self._pid = pid

    def load(self):
        self._data = dict()

        _path = os.path.join(self._PROC_PATH, str(self._pid), "stat")
        _file_read = self._read(_path)

        _file_data = _file_read.split()

        if len(_file_data) is not 52:
            raise NixError("Incorrect number of data poinsts.  Found: {}, expected: {}".format(52, len(_file_data)))

        self._data[self._PID] = _file_data[0]
        self._data[self._COMMAND] = _file_data[1].strip("()")
        self._data[self._STATE] = _file_data[2]
        self._data[self._PARENT_PID] = _file_data[3]
        self._data[self._PROCESS_GROUP] = _file_data[4]
        self._data[self._SESSION] = _file_data[5]
        self._data[self._TTY_NR] = _file_data[6]
        self._data[self._TPGID] = _file_data[7]
        self._data[self._FLAGS] = _file_data[8]
        self._data[self._MINOR_FAULT] = _file_data[9]
        self._data[self._CHILD_MINOR_FAULT] = _file_data[10]
        self._data[self._MAJOR_FAULT] = _file_data[11]
        self._data[self._CHILD_MAJOR_FAULT] = _file_data[12]
        self._data[self._USER_TIME] = _file_data[13]
        self._data[self._SYSTEM_TIME] = _file_data[14]
        self._data[self._CHILD_USER_TIME] = _file_data[15]
        self._data[self._CHILD_SYSTEM_TIME] = _file_data[16]
        self._data[self._PRIORITY] = _file_data[17]
        self._data[self._NICE] = _file_data[18]
        self._data[self._THREADS] = _file_data[19]
        self._data[self._I_T_REAL_VALUE] = _file_data[20]
        self._data[self._START_TIME] = _file_data[21]
        self._data[self._VIRTUAL_SIZE] = _file_data[22]
        self._data[self._RESIDENT_SET_SIZE] = _file_data[23]
        self._data[self._RSS_LIMIT] = _file_data[24]
        self._data[self._START_CODE] = _file_data[25]
        self._data[self._END_CODE] = _file_data[26]
        self._data[self._START_STACK] = _file_data[27]
        self._data[self._KERNEL_STACK_ESP] = _file_data[28]
        self._data[self._CURRENT_EIP] = _file_data[29]
        self._data[self._PENDING_SIGNAL] = _file_data[30]
        self._data[self._BLOCKED_SIGNAL] = _file_data[31]
        self._data[self._IGNORED_SIGNAL] = _file_data[32]
        self._data[self._CAUGHT_SIGNAL] = _file_data[33]
        self._data[self._WAIT_CHANNEL] = _file_data[34]
        self._data[self._PAGE_SWAP] = _file_data[35]
        self._data[self._CUMULATIVE_PAGE_SWAP] = _file_data[36]
        self._data[self._EXIT_SIGNAL] = _file_data[37]
        self._data[self._PROCESSOR] = _file_data[38]
        self._data[self._REAL_TIME_PRIORITY] = _file_data[39]
        self._data[self._POLICY] = _file_data[40]
        self._data[self._AGGREGATE_BLOCK_IO] = _file_data[41]
        self._data[self._GUEST_TIME] = _file_data[42]
        self._data[self._CHILD_GUEST_TIME] = _file_data[43]

    @property
    def get_pid(self) -> str:
        return self._get_value(self._PID)

    @property
    def get_command(self) -> str:
        return self._get_value(self._COMMAND)

    @property
    def get_state(self) -> str:
        return self._get_value(self._STATE)

    @property
    def get_parent_pid(self) -> str:
        return self._get_value(self._PARENT_PID)

    @property
    def get_process_group(self) -> str:
        return self._get_value(self._PROCESS_GROUP)

    @property
    def get_session(self) -> str:
        return self._get_value(self._SESSION)

    @property
    def get_tty_nr(self) -> str:
        return self._get_value(self._TTY_NR)

    @property
    def get_tpgid(self) -> str:
        return self._get_value(self._TPGID)

    @property
    def get_flags(self) -> str:
        return self._get_value(self._FLAGS)

    @property
    def get_minor_fault(self) -> str:
        return self._get_value(self._MINOR_FAULT)

    @property
    def get_child_minor_fault(self) -> str:
        return self._get_value(self._CHILD_MINOR_FAULT)

    @property
    def get_major_fault(self) -> str:
        return self._get_value(self._MAJOR_FAULT)

    @property
    def get_child_major_fault(self) -> str:
        return self._get_value(self._CHILD_MAJOR_FAULT)

    @property
    def get_user_time(self) -> str:
        return self._get_value(self._USER_TIME)

    @property
    def get_system_time(self) -> str:
        return self._get_value(self._SYSTEM_TIME)

    @property
    def get_child_user_time(self) -> str:
        return self._get_value(self._CHILD_USER_TIME)

    @property
    def get_child_system_time(self) -> str:
        return self._get_value(self._CHILD_SYSTEM_TIME)

    @property
    def get_priority(self) -> str:
        return self._get_value(self._PRIORITY)

    @property
    def get_nice(self) -> str:
        return self._get_value(self._NICE)

    @property
    def get_threads(self) -> str:
        return self._get_value(self._THREADS)

    @property
    def get_i_t_real_value(self) -> str:
        return self._get_value(self._I_T_REAL_VALUE)

    @property
    def get_start_time(self) -> str:
        return self._get_value(self._START_TIME)

    @property
    def get_virtual_size(self) -> str:
        return self._get_value(self._VIRTUAL_SIZE)

    @property
    def get_resident_set_size(self) -> str:
        return self._get_value(self._RESIDENT_SET_SIZE)

    @property
    def get_rss_limit(self) -> str:
        return self._get_value(self._RSS_LIMIT)

    @property
    def get_start_code(self) -> str:
        return self._get_value(self._START_CODE)

    @property
    def get_end_code(self) -> str:
        return self._get_value(self._END_CODE)

    @property
    def get_start_stack(self) -> str:
        return self._get_value(self._START_STACK)

    @property
    def get_kernel_stack_esp(self) -> str:
        return self._get_value(self._KERNEL_STACK_ESP)

    @property
    def get_current_eip(self) -> str:
        return self._get_value(self._CURRENT_EIP)

    @property
    def get_pending_signal(self) -> str:
        return self._get_value(self._PENDING_SIGNAL)

    @property
    def get_blocked_signal(self) -> str:
        return self._get_value(self._BLOCKED_SIGNAL)

    @property
    def get_ignored_signal(self) -> str:
        return self._get_value(self._IGNORED_SIGNAL)

    @property
    def get_caught_signal(self) -> str:
        return self._get_value(self._CAUGHT_SIGNAL)

    @property
    def get_wait_channel(self) -> str:
        return self._get_value(self._WAIT_CHANNEL)

    @property
    def get_page_swap(self) -> str:
        return self._get_value(self._PAGE_SWAP)

    @property
    def get_cumulative_page_swap(self) -> str:
        return self._get_value(self._CUMULATIVE_PAGE_SWAP)

    @property
    def get_exit_signal(self) -> str:
        return self._get_value(self._EXIT_SIGNAL)

    @property
    def get_processor(self) -> str:
        return self._get_value(self._PROCESSOR)

    @property
    def get_real_time_priority(self) -> str:
        return self._get_value(self._REAL_TIME_PRIORITY)

    @property
    def get_policy(self) -> str:
        return self._get_value(self._POLICY)

    @property
    def get_aggregate_block_io(self) -> str:
        return self._get_value(self._AGGREGATE_BLOCK_IO)

    @property
    def get_guest_time(self) -> str:
        return self._get_value(self._GUEST_TIME)

    @property
    def get_child_guest_time(self) -> str:
        return self._get_value(self._CHILD_GUEST_TIME)


def main():
    proc_stat = ProcStat(1637)

    print("PID:                  {}".format(proc_stat.get_pid))
    print("COMMAND:              {}".format(proc_stat.get_command))
    print("STATE:                {}".format(proc_stat.get_state))
    print("PARENT_PID:           {}".format(proc_stat.get_parent_pid))
    print("PROCESS_GROUP:        {}".format(proc_stat.get_process_group))
    print("SESSION:              {}".format(proc_stat.get_session))
    print("TTY_NR:               {}".format(proc_stat.get_tty_nr))
    print("TPGID:                {}".format(proc_stat.get_tpgid))
    print("FLAGS:                {}".format(proc_stat.get_flags))
    print("MIN_FAULT:            {}".format(proc_stat.get_minor_fault))
    print("CHILD_MIN_FAULT:      {}".format(proc_stat.get_child_minor_fault))
    print("MAJOR_FAULT:          {}".format(proc_stat.get_major_fault))
    print("CHILD_MAJOR_FAULT:    {}".format(proc_stat.get_child_major_fault))
    print("UTIME:                {}".format(proc_stat.get_user_time))
    print("STIME:                {}".format(proc_stat.get_system_time))
    print("CHILD_UTIME:          {}".format(proc_stat.get_child_user_time))
    print("CHILD_STIME:          {}".format(proc_stat.get_child_system_time))
    print("PRIORITY:             {}".format(proc_stat.get_priority))
    print("NICE:                 {}".format(proc_stat.get_nice))
    print("THREADS:              {}".format(proc_stat.get_threads))
    print("I_T_REAL_VALUE:       {}".format(proc_stat.get_i_t_real_value))
    print("START_TIME:           {}".format(proc_stat.get_start_time))
    print("VIRTUAL_SIZE:         {}".format(proc_stat.get_virtual_size))
    print("RESIDENT_SET_SIZE:    {}".format(proc_stat.get_resident_set_size))
    print("RSS_LIMIT:            {}".format(proc_stat.get_rss_limit))
    print("START_CODE:           {}".format(proc_stat.get_start_code))
    print("END_CODE:             {}".format(proc_stat.get_end_code))
    print("START_STACK:          {}".format(proc_stat.get_start_stack))
    print("KERNEL_STACK_ESP:     {}".format(proc_stat.get_kernel_stack_esp))
    print("CURRENT_EIP:          {}".format(proc_stat.get_current_eip))
    print("PENDING_SIGNAL:       {}".format(proc_stat.get_pending_signal))
    print("BLOCKED_SIGNAL:       {}".format(proc_stat.get_blocked_signal))
    print("IGNORED_SIGNAL:       {}".format(proc_stat.get_ignored_signal))
    print("CAUGHT_SIGNAL:        {}".format(proc_stat.get_caught_signal))
    print("WAIT_CHANNEL:         {}".format(proc_stat.get_wait_channel))
    print("PAGE_SWAP:            {}".format(proc_stat.get_page_swap))
    print("CUMULATIVE_PAGE_SWAP: {}".format(proc_stat.get_cumulative_page_swap))
    print("EXIT_SIGNAL:          {}".format(proc_stat.get_exit_signal))
    print("PROCESSOR:            {}".format(proc_stat.get_processor))
    print("REAL_TIME_PRIORITY:   {}".format(proc_stat.get_real_time_priority))
    print("POLICY:               {}".format(proc_stat.get_policy))
    print("AGGREGATE_BLOCK_IO:   {}".format(proc_stat.get_aggregate_block_io))
    print("GUEST_TIME:           {}".format(proc_stat.get_guest_time))
    print("CHILD_GUEST_TIME:     {}".format(proc_stat.get_child_guest_time))

    print("")


if __name__ == "__main__":
    main()

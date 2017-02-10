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

import pytest
from libnix.raw.procfs.process.proc_stat import ProcStat


class TestProcStat:
    @pytest.fixture(scope="class")
    def proc_stat_valid(self, pid):
        _proc_stat = ProcStat(pid)

        _proc_stat.load()

        return _proc_stat

    def test_load_process(self, pid):
        proc_stat = ProcStat(pid)

        proc_stat.load()

    def test_get_pid(self, proc_stat_valid, pid):
        assert proc_stat_valid.get_pid == str(pid)

    def test_get_command(self, proc_stat_valid):
        assert len(proc_stat_valid.get_command) > 0

    def test_get_state(self, proc_stat_valid):
        assert len(proc_stat_valid.get_state) > 0

    def test_get_parent_pid(self, proc_stat_valid):
        assert len(proc_stat_valid.get_parent_pid) > 0

    def test_get_process_group(self, proc_stat_valid):
        assert len(proc_stat_valid.get_process_group) > 0

    def test_get_session(self, proc_stat_valid):
        assert len(proc_stat_valid.get_session) > 0

    def test_get_tty_nr(self, proc_stat_valid):
        assert len(proc_stat_valid.get_tty_nr) > 0

    def test_get_tpgid(self, proc_stat_valid):
        assert len(proc_stat_valid.get_tpgid) > 0

    def test_get_flags(self, proc_stat_valid):
        assert len(proc_stat_valid.get_flags) > 0

    def test_get_minor_fault(self, proc_stat_valid):
        assert len(proc_stat_valid.get_minor_fault) > 0

    def test_get_child_minor_fault(self, proc_stat_valid):
        assert len(proc_stat_valid.get_child_minor_fault) > 0

    def test_get_major_fault(self, proc_stat_valid):
        assert len(proc_stat_valid.get_major_fault) > 0

    def test_get_child_major_fault(self, proc_stat_valid):
        assert len(proc_stat_valid.get_child_major_fault) > 0

    def test_get_user_time(self, proc_stat_valid):
        assert len(proc_stat_valid.get_user_time) > 0

    def test_get_system_time(self, proc_stat_valid):
        assert len(proc_stat_valid.get_system_time) > 0

    def test_get_child_user_time(self, proc_stat_valid):
        assert len(proc_stat_valid.get_child_user_time) > 0

    def test_get_child_system_time(self, proc_stat_valid):
        assert len(proc_stat_valid.get_child_system_time) > 0

    def test_get_priority(self, proc_stat_valid):
        assert len(proc_stat_valid.get_priority) > 0

    def test_get_nice(self, proc_stat_valid):
        assert len(proc_stat_valid.get_nice) > 0

    def test_get_threads(self, proc_stat_valid):
        assert len(proc_stat_valid.get_threads) > 0

    def test_get_i_t_real_value(self, proc_stat_valid):
        assert len(proc_stat_valid.get_i_t_real_value) > 0

    def test_get_start_time(self, proc_stat_valid):
        assert len(proc_stat_valid.get_start_time) > 0

    def test_get_virtual_size(self, proc_stat_valid):
        assert len(proc_stat_valid.get_virtual_size) > 0

    def test_get_resident_set_size(self, proc_stat_valid):
        assert len(proc_stat_valid.get_resident_set_size) > 0

    def test_get_rss_limit(self, proc_stat_valid):
        assert len(proc_stat_valid.get_rss_limit) > 0

    def test_get_start_code(self, proc_stat_valid):
        assert len(proc_stat_valid.get_start_code) > 0

    def test_get_end_code(self, proc_stat_valid):
        assert len(proc_stat_valid.get_end_code) > 0

    def test_get_start_stack(self, proc_stat_valid):
        assert len(proc_stat_valid.get_start_stack) > 0

    def test_get_kernel_stack_esp(self, proc_stat_valid):
        assert len(proc_stat_valid.get_kernel_stack_esp) > 0

    def test_get_current_eip(self, proc_stat_valid):
        assert len(proc_stat_valid.get_current_eip) > 0

    def test_get_pending_signal(self, proc_stat_valid):
        assert len(proc_stat_valid.get_pending_signal) > 0

    def test_get_blocked_signal(self, proc_stat_valid):
        assert len(proc_stat_valid.get_blocked_signal) > 0

    def test_get_ignored_signal(self, proc_stat_valid):
        assert len(proc_stat_valid.get_ignored_signal) > 0

    def test_get_caught_signal(self, proc_stat_valid):
        assert len(proc_stat_valid.get_caught_signal) > 0

    def test_get_wait_channel(self, proc_stat_valid):
        assert len(proc_stat_valid.get_wait_channel) > 0

    def test_get_page_swap(self, proc_stat_valid):
        assert len(proc_stat_valid.get_page_swap) > 0

    def test_get_cumulative_page_swap(self, proc_stat_valid):
        assert len(proc_stat_valid.get_cumulative_page_swap) > 0

    def test_get_exit_signal(self, proc_stat_valid):
        assert len(proc_stat_valid.get_exit_signal) > 0

    def test_get_processor(self, proc_stat_valid):
        assert len(proc_stat_valid.get_processor) > 0

    def test_get_real_time_priority(self, proc_stat_valid):
        assert len(proc_stat_valid.get_real_time_priority) > 0

    def test_get_policy(self, proc_stat_valid):
        assert len(proc_stat_valid.get_policy) > 0

    def test_get_aggregate_block_io(self, proc_stat_valid):
        assert len(proc_stat_valid.get_aggregate_block_io) > 0

    def test_get_guest_time(self, proc_stat_valid):
        assert len(proc_stat_valid.get_guest_time) > 0

    def test_get_child_guest_time(self, proc_stat_valid):
        assert len(proc_stat_valid.get_child_guest_time) > 0

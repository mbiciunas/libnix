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
from libnix.raw.procfs.process.proc_status import ProcStatus


class TestProcStatus:
    _PID = 1617

    @pytest.fixture(scope="class")
    def proc_status_valid(self):
        _proc_status = ProcStatus(self._PID)

        _proc_status.load()

        return _proc_status

    def test_load_process(self):
        _proc_status = ProcStatus(self._PID)

        _proc_status.load()

    def test_get_name(self, proc_status_valid):
        assert len(proc_status_valid.get_name) > 0

    def test_get_umask(self, proc_status_valid):
        assert len(proc_status_valid.get_umask) > 0

    def test_get_state(self, proc_status_valid):
        assert len(proc_status_valid.get_state) > 0

    def test_get_thread_gid(self, proc_status_valid):
        assert len(proc_status_valid.get_thread_gid) > 0

    def test_get_numa_gid(self, proc_status_valid):
        assert len(proc_status_valid.get_numa_gid) > 0

    def test_get_pid(self, proc_status_valid):
        assert len(proc_status_valid.get_pid) > 0

    def test_get_parent_pid(self, proc_status_valid):
        assert len(proc_status_valid.get_parent_pid) > 0

    def test_get_tracer_pid(self, proc_status_valid):
        assert len(proc_status_valid.get_tracer_pid) > 0

    def test_get_uid_real(self, proc_status_valid):
        assert len(proc_status_valid.get_uid_real) > 0

    def test_get_uid_effective(self, proc_status_valid):
        assert len(proc_status_valid.get_uid_effective) > 0

    def test_get_uid_saved_set(self, proc_status_valid):
        assert len(proc_status_valid.get_uid_saved_set) > 0

    def test_get_uid_filesystem(self, proc_status_valid):
        assert len(proc_status_valid.get_uid_filesystem) > 0

    def test_get_gid_real(self, proc_status_valid):
        assert len(proc_status_valid.get_gid_real) > 0

    def test_get_gid_effective(self, proc_status_valid):
        assert len(proc_status_valid.get_gid_effective) > 0

    def test_get_gid_saved_set(self, proc_status_valid):
        assert len(proc_status_valid.get_gid_saved_set) > 0

    def test_get_gid_filesystem(self, proc_status_valid):
        assert len(proc_status_valid.get_gid_filesystem) > 0

    def test_get_fd_size(self, proc_status_valid):
        assert len(proc_status_valid.get_fd_size) > 0

    def test_get_groups(self, proc_status_valid):
        assert len(proc_status_valid.get_groups) > 0

    def test_get_namespace_thread_gid(self, proc_status_valid):
        assert len(proc_status_valid.get_namespace_thread_gid) > 0

    def test_get_namespace_pid(self, proc_status_valid):
        assert len(proc_status_valid.get_namespace_pid) > 0

    def test_get_namespace_pgid(self, proc_status_valid):
        assert len(proc_status_valid.get_namespace_pgid) > 0

    def test_get_namespace_sid(self, proc_status_valid):
        assert len(proc_status_valid.get_namespace_sid) > 0

    def test_get_virtual_memory_peak(self, proc_status_valid):
        assert len(proc_status_valid.get_virtual_memory_peak) > 0

    def test_get_virtual_memory_size(self, proc_status_valid):
        assert len(proc_status_valid.get_virtual_memory_size) > 0

    def test_get_virtual_memory_lock(self, proc_status_valid):
        assert len(proc_status_valid.get_virtual_memory_lock) > 0

    def test_get_virtual_memory_pin(self, proc_status_valid):
        assert len(proc_status_valid.get_virtual_memory_pin) > 0

    def test_get_virtual_memory_hwm(self, proc_status_valid):
        assert len(proc_status_valid.get_virtual_memory_hwm) > 0

    def test_get_virtual_memory_rss(self, proc_status_valid):
        assert len(proc_status_valid.get_virtual_memory_rss) > 0

    def test_get_rss_anon(self, proc_status_valid):
        assert len(proc_status_valid.get_rss_anon) > 0

    def test_get_rss_file(self, proc_status_valid):
        assert len(proc_status_valid.get_rss_file) > 0

    def test_get_rss_shared(self, proc_status_valid):
        assert len(proc_status_valid.get_rss_shared) > 0

    def test_get_virtual_memory_data(self, proc_status_valid):
        assert len(proc_status_valid.get_virtual_memory_data) > 0

    def test_get_virtual_memory_stack(self, proc_status_valid):
        assert len(proc_status_valid.get_virtual_memory_stack) > 0

    def test_get_virtual_memory_exe(self, proc_status_valid):
        assert len(proc_status_valid.get_virtual_memory_exe) > 0

    def test_get_virtual_memory_lib(self, proc_status_valid):
        assert len(proc_status_valid.get_virtual_memory_lib) > 0

    def test_get_virtual_memory_pte(self, proc_status_valid):
        assert len(proc_status_valid.get_virtual_memory_pte) > 0

    def test_get_virtual_memory_pmd(self, proc_status_valid):
        assert len(proc_status_valid.get_virtual_memory_pmd) > 0

    def test_get_virtual_memory_swap(self, proc_status_valid):
        assert len(proc_status_valid.get_virtual_memory_swap) > 0

    def test_get_huge_tlb_pages(self, proc_status_valid):
        assert len(proc_status_valid.get_huge_tlb_pages) > 0

    def test_get_threads(self, proc_status_valid):
        assert len(proc_status_valid.get_threads) > 0

    def test_get_signal_queue(self, proc_status_valid):
        assert len(proc_status_valid.get_signal_queue) > 0

    def test_get_signal_pending(self, proc_status_valid):
        assert len(proc_status_valid.get_signal_pending) > 0

    def test_get_shd_pnd(self, proc_status_valid):
        assert len(proc_status_valid.get_shd_pnd) > 0

    def test_get_signal_block(self, proc_status_valid):
        assert len(proc_status_valid.get_signal_block) > 0

    def test_get_signal_ignore(self, proc_status_valid):
        assert len(proc_status_valid.get_signal_ignore) > 0

    def test_get_signal_caught(self, proc_status_valid):
        assert len(proc_status_valid.get_signal_caught) > 0

    def test_get_capability_inherit(self, proc_status_valid):
        assert len(proc_status_valid.get_capability_inherit) > 0

    def test_get_capability_permitted(self, proc_status_valid):
        assert len(proc_status_valid.get_capability_permitted) > 0

    def test_get_capability_effective(self, proc_status_valid):
        assert len(proc_status_valid.get_capability_effective) > 0

    def test_get_capability_bound(self, proc_status_valid):
        assert len(proc_status_valid.get_capability_bound) > 0

    def test_get_capability_ambient(self, proc_status_valid):
        assert len(proc_status_valid.get_capability_ambient) > 0

    def test_get_secure_compute(self, proc_status_valid):
        assert len(proc_status_valid.get_secure_compute) > 0

    def test_get_cpu_allowed(self, proc_status_valid):
        assert len(proc_status_valid.get_cpu_allowed) > 0

    def test_get_cpu_allowed_list(self, proc_status_valid):
        assert len(proc_status_valid.get_cpu_allowed_list) > 0

    def test_get_memory_nodes_allowed(self, proc_status_valid):
        assert len(proc_status_valid.get_memory_nodes_allowed) > 0

    def test_get_memory_nodes_allowed_list(self, proc_status_valid):
        assert len(proc_status_valid.get_memory_nodes_allowed_list) > 0

    def test_get_voluntary_context_switch(self, proc_status_valid):
        assert len(proc_status_valid.get_voluntary_context_switch) > 0

    def test_get_non_voluntary_context_switch(self, proc_status_valid):
        assert len(proc_status_valid.get_non_voluntary_context_switch) > 0

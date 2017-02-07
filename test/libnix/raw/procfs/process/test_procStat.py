import pytest
from libnix.raw.procfs.process.proc_stat import ProcStat


class TestProcStat:
    _PID = 1617

    @pytest.fixture(scope="class")
    def proc_stat_valid(self):
        _proc_stat = ProcStat(self._PID)

        _proc_stat.load()

        return _proc_stat

    def test_load_process(self):
        proc_stat = ProcStat(self._PID)

        proc_stat.load()

    def test_get_pid(self, proc_stat_valid):
        assert proc_stat_valid.get_pid == str(self._PID)

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

import pytest
from libnix.src.libnix.raw.procfs.process.proc_cmdline import ProcCmdline


class TestProcCmdline:
    _PID = 1727

    @pytest.fixture(scope="class")
    def proc_cmdline_valid(self):
        _proc_cmdline = ProcCmdline(self._PID)

        _proc_cmdline.load()

        return _proc_cmdline

    def test_load_process(self):
        _proc_cmdline = ProcCmdline(self._PID)

        _proc_cmdline.load()

    def test_get_command(self, proc_cmdline_valid):
        assert len(proc_cmdline_valid.get_command) > 0

    def test_get_argument_count(self, proc_cmdline_valid):
        assert proc_cmdline_valid.get_argument_count >= 0

    def test_get_arguments(self, proc_cmdline_valid):
        assert len(proc_cmdline_valid.get_arguments) > 0

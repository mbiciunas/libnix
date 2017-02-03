import pytest
from libnix.raw.procfs.process.proc_io import ProcIO


class TestProcIO:
    _PID = 1930

    @pytest.fixture(scope="class")
    def proc_io_valid(self):
        _proc_io = ProcIO(self._PID)

        _proc_io.load()

        return _proc_io

    def test_load_process(self):
        _proc_io = ProcIO(self._PID)

        _proc_io.load()

    def test_get_char_read(self, proc_io_valid):
        assert len(proc_io_valid.get_char_read) > 0

    def test_get_char_write(self, proc_io_valid):
        assert len(proc_io_valid.get_char_write) > 0

    def test_get_call_read(self, proc_io_valid):
        assert len(proc_io_valid.get_call_read) > 0

    def test_get_call_write(self, proc_io_valid):
        assert len(proc_io_valid.get_call_write) > 0

    def test_get_bytes_read(self, proc_io_valid):
        assert len(proc_io_valid.get_bytes_read) > 0

    def test_get_bytes_write(self, proc_io_valid):
        assert len(proc_io_valid.get_bytes_write) > 0

    def test_get_cancel_bytes_write(self, proc_io_valid):
        assert len(proc_io_valid.get_cancel_bytes_write) > 0

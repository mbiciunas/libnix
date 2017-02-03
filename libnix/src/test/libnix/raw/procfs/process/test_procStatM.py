import pytest
from libnix.raw.procfs.process.proc_statm import ProcStatM


class TestProcStatM:
    _PID = 1930

    @pytest.fixture(scope="class")
    def proc_statm_valid(self):
        _proc_statm = ProcStatM(self._PID)

        _proc_statm.load()

        return _proc_statm

    def test_load_process(self):
        _proc_statm = ProcStatM(self._PID)

        _proc_statm.load()

    def test_get_size(self, proc_statm_valid):
        assert len(proc_statm_valid.get_size) > 0

    def test_get_resident(self, proc_statm_valid):
        assert len(proc_statm_valid.get_resident) > 0

    def test_get_shared(self, proc_statm_valid):
        assert len(proc_statm_valid.get_shared) > 0

    def test_get_text(self, proc_statm_valid):
        assert len(proc_statm_valid.get_text) > 0

    def test_get_library(self, proc_statm_valid):
        assert len(proc_statm_valid.get_library) > 0

    def test_get_data(self, proc_statm_valid):
        assert len(proc_statm_valid.get_data) > 0

    def test_get_dirty(self, proc_statm_valid):
        assert len(proc_statm_valid.get_dirty) > 0

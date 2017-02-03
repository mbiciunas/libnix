import pytest
from libnix.raw.procfs.process.proc_comm import ProcComm


class TestProcComm:
    _PID = 1930

    @pytest.fixture(scope="class")
    def proc_comm_valid(self):
        _proc_comm = ProcComm(self._PID)

        _proc_comm.load()

        return _proc_comm

    def test_load_process(self):
        _proc_comm = ProcComm(self._PID)

        _proc_comm.load()

    def test_get_command(self, proc_comm_valid):
        assert len(proc_comm_valid.get_command) > 0

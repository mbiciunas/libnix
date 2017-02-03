import pytest
from libnix.raw.procfs.process.proc_environ import ProcEnviron


class TestProcEnviron:
    _PID = 1930

    @pytest.fixture(scope="class")
    def proc_environ_valid(self):
        _proc_environ = ProcEnviron(self._PID)

        _proc_environ.load()

        return _proc_environ

    def test_load_process(self):
        _proc_environ = ProcEnviron(self._PID)

        _proc_environ.load()

    def test_get_environment_count(self, proc_environ_valid):
        assert proc_environ_valid.get_environment_count > 0

    def test_get_environments(self, proc_environ_valid):
        assert len(proc_environ_valid.get_environments) > 0

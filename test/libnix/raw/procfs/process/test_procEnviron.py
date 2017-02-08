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
from libnix.raw.procfs.process.proc_environ import ProcEnviron


class TestProcEnviron:
    _PID = 1617

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

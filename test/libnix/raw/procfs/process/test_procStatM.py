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
from libnix.raw.procfs.process.proc_statm import ProcStatM


class TestProcStatM:
    _PID = 1617

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

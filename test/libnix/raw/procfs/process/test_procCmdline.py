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
from libnix.raw.procfs.process.proc_cmdline import ProcCmdline


class TestProcCmdline:
    _PID = 10326

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

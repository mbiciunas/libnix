# Nix
# Copyright (c) 2017  Mark Biciunas.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import pytest
from libnix.raw.procfs.process.proc_io import ProcIO


class TestProcIO:
    @pytest.fixture(scope="class")
    def proc_io_valid(self, pid):
        _proc_io = ProcIO(pid)

        _proc_io.load()

        return _proc_io

    def test_load_process(self, pid):
        _proc_io = ProcIO(pid)

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

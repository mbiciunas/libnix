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
from libnix.raw.procfs.process.proc_comm import ProcComm


class TestProcComm:
    @pytest.fixture(scope="class")
    def proc_comm_valid(self, pid):
        _proc_comm = ProcComm(pid)

        _proc_comm.load()

        return _proc_comm

    def test_load_process(self, pid):
        _proc_comm = ProcComm(pid)

        _proc_comm.load()

    def test_get_command(self, proc_comm_valid):
        assert len(proc_comm_valid.get_command) > 0

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

from libnix.config.script.run_script import RunScript
from libnix.exception.nix_error import NixError


class TestRunScript:
    def test_run(self, config_valid, capsys):
        _run_script = RunScript()

        _run_script.run(config_valid.SCRIPT_VALID_1)

        out, err = capsys.readouterr()

        print(len(out))
        assert len(out) > 10
        assert len(err) == 0

    def test_run_invalid_name(self, config_valid):
        _run_script = RunScript()

        with pytest.raises(NixError):
            _run_script.run(config_valid.SCRIPT_INVALID_1)

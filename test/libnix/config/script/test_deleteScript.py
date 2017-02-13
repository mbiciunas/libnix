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

from libnix.config.script.delete_script import DeleteScript
from libnix.config.config import Config
from libnix.exception.nix_error import NixError


class TestDeleteScript:
    def test_delete(self, config_valid):
        _delete_script = DeleteScript()
        _delete_script.delete(config_valid.SCRIPT_VALID_1)

        _scripts = Config().get_scripts()

        assert not _scripts.exist(config_valid.SCRIPT_VALID_1), \
            "Script exists but should not exist: {}".format(config_valid.SCRIPT_VALID_1)

    def test_delete_invalid_name(self, config_valid):
        _delete_script = DeleteScript()

        with pytest.raises(NixError):
            _delete_script.delete(config_valid.SCRIPT_INVALID_1)

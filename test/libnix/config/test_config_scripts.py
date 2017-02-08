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
from libnix.config.config_script import ConfigScript

from libnix.config.config_scripts import ConfigScripts
from libnix.exception.nix_error import NixError


class TestConfigScripts:
    _TAG_VALID_1 = "tag1"
    _TAG_VALID_2 = "tag2"
    _TAG_INVALID_1 = "bad_tag_1"
    _TAG_INVALID_2 = "bad_tag_2"

    _SCRIPT_VALID_1 = "script1"
    _SCRIPT_VALID_2 = "script2"
    _SCRIPT_INVALID_1 = "bad_script_1"
    _SCRIPT_INVALID_2 = "bad_script_2"

    _SCRIPT_VALID_LIST = [_SCRIPT_VALID_1, _SCRIPT_VALID_2]
    _SCRIPT_INVALID_LIST = [_SCRIPT_INVALID_1, _SCRIPT_INVALID_2]
    _SCRIPT_MIX_LIST = [_SCRIPT_INVALID_1, _SCRIPT_VALID_1, _SCRIPT_INVALID_2, _SCRIPT_VALID_2]

    def test_exist(self, config_valid):
        _scripts = config_valid.config().get_scripts()

        assert _scripts.exist(config_valid.SCRIPT_VALID_1), \
            "Script not found: {}".format(config_valid.SCRIPT_VALID_1)
        assert not _scripts.exist(config_valid.SCRIPT_INVALID_1), \
            "Non existing script found: {}".format(config_valid.SCRIPT_INVALID_1)

    def test_insert(self, config_valid):
        _scripts = config_valid.config().get_scripts()

        _script = _scripts.insert()

        assert type(_script) is ConfigScript
        assert _script.get_name() is "", "Script name should be none, contains: {}".format(_script.get_name())
        assert _script.get_desc() is "", "Script description should be none, contains: {}".format(_script.get_desc())

    def test_delete(self, config_valid):
        _scripts = config_valid.config().get_scripts()

        _scripts.delete(self._SCRIPT_VALID_1)

        with pytest.raises(NixError):
            _scripts.delete(self._SCRIPT_INVALID_1)

    def test_list(self, config_valid):
        _scripts = config_valid.config().get_scripts()

        _script_list = _scripts.list()

        assert len(_script_list) == config_valid.get_count_scripts()

    def test_find_by_name(self, config_valid):
        _scripts = config_valid.config().get_scripts()

        _script = _scripts.find_by_name(self._SCRIPT_VALID_1)

        assert _script.get_name() == self._SCRIPT_VALID_1

        with pytest.raises(NixError):
            _scripts.find_by_name(self._SCRIPT_INVALID_1)

    def test_find_by_tag(self, config_valid):
        _scripts = config_valid.config().get_scripts()

        _script_list = _scripts.find_by_tag(self._TAG_VALID_1)

        assert _script_list[0].get_name() == self._SCRIPT_VALID_1

        with pytest.raises(NixError):
            _scripts.find_by_tag(self._TAG_INVALID_1)

    def test_export_data(self, config_valid):
        _scripts = config_valid.config().get_scripts()

        _export = _scripts.export_data()

        assert type(_export) == list
        assert len(_export) == config_valid.get_count_scripts()

    def test_import_data(self, config_valid):
        _scripts = config_valid.config().get_scripts()

        _export = _scripts.export_data()

        _scripts_new = ConfigScripts()

        _scripts_new.import_data(_export)

        assert len(_scripts_new.list()) == config_valid.get_count_scripts()

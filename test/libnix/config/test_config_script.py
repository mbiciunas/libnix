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

from libnix.config.config_script import ConfigScript


class TestConfigScript:
    def test_set_name(self, config_valid):
        _script = config_valid.config().get_scripts().find_by_name(config_valid.SCRIPT_VALID_1)

        _script.set_name(config_valid.SCRIPT_INVALID_1)

        assert _script.get_name() == config_valid.SCRIPT_INVALID_1, \
            "Changed script name incorrect - " \
            "Found: '{}', expected '{}'".format(_script.get_name(), config_valid.SCRIPT_INVALID_1)

    def test_get_name(self, config_valid):
        _script = config_valid.config().get_scripts().find_by_name(config_valid.SCRIPT_VALID_1)

        assert _script.get_name() == config_valid.SCRIPT_VALID_1, \
            "Script name incorrect - " \
            "Found: '{}', expected '{}'".format(_script.get_name(), config_valid.SCRIPT_VALID_1)

    def test_set_desc(self, config_valid):
        _script = config_valid.config().get_scripts().find_by_name(config_valid.SCRIPT_VALID_1)

        _script.set_desc(config_valid.SCRIPT_INVALID_DESC)

        assert _script.get_desc() == config_valid.SCRIPT_INVALID_DESC, \
            "Changed script description incorrect - " \
            "Found: '{}', expected '{}'".format(_script.get_desc(), config_valid.SCRIPT_INVALID_DESC)

    def test_get_desc(self, config_valid):
        _script = config_valid.config().get_scripts().find_by_name(config_valid.SCRIPT_VALID_1)

        assert _script.get_desc() == config_valid.SCRIPT_VALID_DESC_1, \
            "Script description incorrect - " \
            "Found: '{}', expected '{}'".format(_script.get_desc(), config_valid.SCRIPT_VALID_DESC_1)

    def test_set_status(self, config_valid):
        _script = config_valid.config().get_scripts().find_by_name(config_valid.SCRIPT_VALID_1)

        _script.set_status(config_valid.SCRIPT_INVALID_STATUS)

        assert _script.get_status() == config_valid.SCRIPT_INVALID_STATUS, \
            "Changed script status - " \
            "Found: '{}', expected '{}'".format(_script.get_status(), config_valid.SCRIPT_INVALID_STATUS)

    def test_get_status(self, config_valid):
        _script = config_valid.config().get_scripts().find_by_name(config_valid.SCRIPT_VALID_1)

        assert _script.get_status() == config_valid.SCRIPT_VALID_STATUS_1, \
            "Script status incorrect - " \
            "Found: '{}', expected '{}'".format(_script.get_status(), config_valid.SCRIPT_VALID_STATUS_1)

    def test_set_code(self, config_valid):
        _script = config_valid.config().get_scripts().find_by_name(config_valid.SCRIPT_VALID_1)

        _script.set_code(config_valid.SCRIPT_INVALID_CODE)

        assert _script.get_code() == config_valid.SCRIPT_INVALID_CODE, \
            "Changed script code - " \
            "Found: '{}', expected '{}'".format(_script.get_code(), config_valid.SCRIPT_INVALID_CODE)

    def test_get_code(self, config_valid):
        _script = config_valid.config().get_scripts().find_by_name(config_valid.SCRIPT_VALID_1)

        assert _script.get_code() == config_valid.SCRIPT_VALID_CODE_1, \
            "Script code incorrect - " \
            "Found: '{}', expected '{}'".format(_script.get_code(), config_valid.SCRIPT_VALID_CODE_1)

    def test_get_tags(self, config_valid):
        _script = config_valid.config().get_scripts().find_by_name(config_valid.SCRIPT_VALID_1)

        assert type(_script.get_tags()) == list, \
            "get_tags did not return a list - " \
            "Found: '{}'".format(type(_script.get_tags()))

        assert len(_script.get_tags()) == len(config_valid.SCRIPT_VALID_TAGS_1), \
            "get_tags did not return right number of tags - " \
            "Found: '{}', expected '{}'".format(len(_script.get_tags()), len(config_valid.SCRIPT_VALID_TAGS_1))

    def test_add_tags(self, config_valid):
        _script = config_valid.config().get_scripts().find_by_name(config_valid.SCRIPT_VALID_1)
        _valid_tags = config_valid.SCRIPT_VALID_TAGS_1
        _invalid_tags = config_valid.SCRIPT_INVALID_TAGS
        _script.add_tags(_invalid_tags)

        assert len(_script.get_tags()) == len(_valid_tags) + len(_invalid_tags), \
            "get_tags did not return right number of tags - " \
            "Found: '{}', expected '{}'".format(len(_script.get_tags()), len(_valid_tags) + len(_invalid_tags))

    def test_add_tag(self, config_valid):
        _script = config_valid.config().get_scripts().find_by_name(config_valid.SCRIPT_VALID_1)

        _script.add_tag(config_valid.SCRIPT_INVALID_TAG)

        assert len(_script.get_tags()) == len(config_valid.SCRIPT_VALID_TAGS_1) + 1, \
            "get_tags did not return right number of tags - " \
            "Found: '{}', expected '{}'".format(len(_script.get_tags()), len(config_valid.SCRIPT_VALID_TAGS_1) + 1)

    def test_delete_tag(self, config_valid):
        _script = config_valid.config().get_scripts().find_by_name(config_valid.SCRIPT_VALID_1)
        _valid_tags = config_valid.SCRIPT_VALID_TAGS_1

        _script.delete_tag(_valid_tags[0])

        assert len(_script.get_tags()) == len(config_valid.SCRIPT_VALID_TAGS_1) - 1, \
            "Get_tags did not return right number of tags - " \
            "Found: '{}', expected '{}'".format(len(_script.get_tags()), len(config_valid.SCRIPT_VALID_TAGS_1) - 1)

    def test_make_temp(self, config_valid):
        _script = config_valid.config().get_scripts().find_by_name(config_valid.SCRIPT_VALID_1)
        _contents_in = "Contents of temp file"
        _script.make_temp(_contents_in)

        _contents_out = _script.read_temp_file()

        assert _contents_in == _contents_out, \
            "Make_temp did not return right contents - " \
            "Found: '{}'. Expected: '{}'.".format(_contents_in, _contents_out)

    # def test_call_editor(self, config_valid):

    def test_read_temp_file(self, config_valid):
        _script = config_valid.config().get_scripts().find_by_name(config_valid.SCRIPT_VALID_1)
        _contents_in = "Contents of temp file"
        _script.make_temp(_contents_in)

        _contents_out = _script.read_temp_file()

        assert _contents_in == _contents_out, \
            "Read_temp_file did not return right contents - " \
            "Found: '{}'. Expected: '{}'.".format(_contents_in, _contents_out)

    def test_is_compile(self, config_valid):
        _script = config_valid.config().get_scripts().find_by_name(config_valid.SCRIPT_VALID_1)

        assert _script.is_compile(), "Script did not compile.  Contents: '{}'.".format(_script.get_code())

    def test_export_data(self, config_valid):
        _script = config_valid.config().get_scripts().find_by_name(config_valid.SCRIPT_VALID_1)

        _export = _script.export_data()

        assert type(_export) == dict
        assert len(_export) == 5

    def test_import_data(self, config_valid):
        _script = config_valid.config().get_scripts().find_by_name(config_valid.SCRIPT_VALID_1)

        _export = _script.export_data()
        _script_new = ConfigScript()
        _script_new.import_data(_export)

        assert type(_script_new._script) == dict
        assert len(_script_new._script) == 5

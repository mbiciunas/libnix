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

from libnix.config.tag.list_tag import ListTag


class TestListTag:
    def test_list(self, config_valid, capsys):
        _list_tag = ListTag()

        _list_tag.list()

        out, err = capsys.readouterr()

        assert config_valid.TAG_VALID_1 in out
        assert config_valid.TAG_VALID_2 in out
        assert len(err) == 0

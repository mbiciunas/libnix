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

from libnix.config.config import Config
from libnix.config.tag.delete_tag import DeleteTag
from libnix.exception.nix_error import NixError


class TestDeleteTag:
    def test_delete(self, config_valid):
        _delete_tag = DeleteTag()
        _delete_tag.delete(config_valid.TAG_VALID_3)

        _tags = Config().get_tags()

        assert not _tags.exist(config_valid.TAG_VALID_3), \
            "Tag exists but should not exist: {}".format(config_valid.TAG_VALID_3)

    def test_delete_in_use(self, config_valid):
        _delete_tag = DeleteTag()

        with pytest.raises(NixError):
            _delete_tag.delete(config_valid.TAG_VALID_1)

    def test_delete_invalid_name(self, config_valid):
        _delete_tag = DeleteTag()

        with pytest.raises(NixError):
            _delete_tag.delete(config_valid.TAG_INVALID_1)

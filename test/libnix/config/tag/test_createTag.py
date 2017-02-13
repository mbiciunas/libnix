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

from libnix.config.config import Config
from libnix.config.tag.create_tag import CreateTag
from libnix.exception.nix_error import NixError


class TestCreateTag:
    def test_create(self, config_valid):
        _create_tag = CreateTag()

        _create_tag.create(config_valid.TAG_INVALID_1, "invalid tag")

        _tags = Config().get_tags()

        assert _tags.exist(config_valid.TAG_INVALID_1), \
            "Tag was not created: {}".format(config_valid.TAG_INVALID_1)

    def test_create_exists(self, config_valid):
        _create_tag = CreateTag()

        with pytest.raises(NixError):
            _create_tag.create(config_valid.TAG_VALID_1, "valid tag")


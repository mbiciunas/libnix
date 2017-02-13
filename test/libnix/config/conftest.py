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

from ..setup.setup_config_empty import SetupConfigEmpty
from ..setup.setup_config_valid import SetupConfigValid


@pytest.fixture()
def config_empty():
    _setup_config = SetupConfigEmpty()
    _setup_config.set_count_tags(0)
    _setup_config.set_count_scripts(0)

    return _setup_config


@pytest.fixture()
def config_valid():
    _setup_config = SetupConfigValid()
    _setup_config.set_count_tags(3)
    _setup_config.set_count_scripts(3)

    return _setup_config

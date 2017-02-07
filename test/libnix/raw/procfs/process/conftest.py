import pytest

from ....setup.setup_config_valid import SetupConfigValid
# from libnix1.test.libnix1.setup.setup_config import SetupConfig

# _FILE_EMPTY = "../../data/config_empty.json"
# _FILE_VALID = "../../data/config_valid.json"
# _FILE_INVALID = "../../data/config_invalid.json"


# @pytest.fixture()
# def config_empty():
#     _setup_config = SetupConfigEmpty()
#     _setup_config.set_count_tags(0)
#     _setup_config.set_count_scripts(0)
#
#     return _setup_config


@pytest.fixture()
def config_valid():
    _setup_config = SetupConfigValid()
    _setup_config.set_count_tags(3)
    _setup_config.set_count_scripts(3)

    return _setup_config


# @pytest.fixture()
# def config_invalid():
#     _setup_config = SetupConfig(_FILE_INVALID)
#     _setup_config.set_count_tags(3)
#     _setup_config.set_count_scripts(4)
#
#     return _setup_config

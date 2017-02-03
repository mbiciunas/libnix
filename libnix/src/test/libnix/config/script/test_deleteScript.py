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

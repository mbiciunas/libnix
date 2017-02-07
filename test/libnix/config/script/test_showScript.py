import pytest

from libnix.config.script.show_script import ShowScript
from libnix.exception.nix_error import NixError


class TestShowScript:
    def test_show(self, config_valid, capsys):
        _show_script = ShowScript()

        _show_script.show(config_valid.SCRIPT_VALID_1)

        out, err = capsys.readouterr()

        assert config_valid.SCRIPT_VALID_CODE_1 in out

    def test_show_invalid_name(self, config_valid):
        _show_script = ShowScript()

        with pytest.raises(NixError):
            _show_script.show(config_valid.SCRIPT_INVALID_1)

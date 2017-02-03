import pytest

from libnix.config.tag.show_tag import ShowTag
from libnix.exception.nix_error import NixError


class TestShowTag:
    def test_show(self, config_valid, capsys):
        _show_tag = ShowTag()

        _show_tag.show(config_valid.TAG_VALID_1)

        out, err = capsys.readouterr()

        assert config_valid.SCRIPT_VALID_1 in out

    def test_show_invalid_name(self, config_valid):
        _show_tag = ShowTag()

        with pytest.raises(NixError):
            _show_tag.show(config_valid.TAG_INVALID_1)

import pytest

from libnix.config.tag.rename_tag import RenameTag
from libnix.exception.nix_error import NixError


class TestRenameTag:
    def test_rename(self, config_valid):
        _rename_tag = RenameTag()

        _rename_tag.rename(config_valid.TAG_VALID_1, config_valid.TAG_INVALID_1)

    def test_rename_same_name(self, config_valid):
        _rename_tag = RenameTag()

        with pytest.raises(NixError):
            _rename_tag.rename(config_valid.TAG_VALID_1, config_valid.TAG_VALID_1)

    def test_rename_invalid_name(self, config_valid):
        _rename_tag = RenameTag()

        with pytest.raises(NixError):
            _rename_tag.rename(config_valid.TAG_INVALID_1, config_valid.TAG_INVALID_2)

    def test_rename_existing_name(self, config_valid):
        _rename_tag = RenameTag()

        with pytest.raises(NixError):
            _rename_tag.rename(config_valid.SCRIPT_VALID_1, config_valid.SCRIPT_VALID_2)

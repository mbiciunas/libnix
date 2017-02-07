import pytest

from libnix.config.script.rename_script import RenameScript
from libnix.exception.nix_error import NixError


class TestRenameScript:
    def test_rename(self, config_valid):
        _rename_script = RenameScript()

        _rename_script.rename(config_valid.SCRIPT_VALID_1, config_valid.SCRIPT_INVALID_1)

    def test_rename_same_name(self, config_valid):
        _rename_script = RenameScript()

        with pytest.raises(NixError):
            _rename_script.rename(config_valid.SCRIPT_VALID_1, config_valid.SCRIPT_VALID_1)

    def test_rename_invalid_name(self, config_valid):
        _rename_script = RenameScript()

        with pytest.raises(NixError):
            _rename_script.rename(config_valid.SCRIPT_INVALID_1, config_valid.SCRIPT_INVALID_2)

    def test_rename_existing_name(self, config_valid):
        _rename_script = RenameScript()

        with pytest.raises(NixError):
            _rename_script.rename(config_valid.SCRIPT_VALID_1, config_valid.SCRIPT_VALID_2)

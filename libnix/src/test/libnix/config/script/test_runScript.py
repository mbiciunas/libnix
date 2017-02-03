import pytest

from libnix.config.script.run_script import RunScript
from libnix.exception.nix_error import NixError


class TestRunScript:
    def test_run(self, config_valid, capsys):
        _run_script = RunScript()

        _run_script.run(config_valid.SCRIPT_VALID_1)

        out, err = capsys.readouterr()

        print(len(out))
        assert len(out) > 10
        assert len(err) == 0

    def test_run_invalid_name(self, config_valid):
        _run_script = RunScript()

        with pytest.raises(NixError):
            _run_script.run(config_valid.SCRIPT_INVALID_1)

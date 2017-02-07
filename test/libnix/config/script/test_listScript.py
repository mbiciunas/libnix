from libnix.config.script.list_script import ListScript


class TestListScript:
    def test_list(self, config_valid, capsys):
        _list_script = ListScript()

        _list_script.list()

        out, err = capsys.readouterr()

        assert config_valid.SCRIPT_VALID_1 in out
        assert config_valid.SCRIPT_VALID_2 in out
        assert len(err) == 0

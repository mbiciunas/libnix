from libnix.config.tag.list_tag import ListTag


class TestListTag:
    def test_list(self, config_valid, capsys):
        _list_tag = ListTag()

        _list_tag.list()

        out, err = capsys.readouterr()

        assert config_valid.TAG_VALID_1 in out
        assert config_valid.TAG_VALID_2 in out
        assert len(err) == 0

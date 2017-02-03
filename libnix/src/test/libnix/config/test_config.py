from libnix.config.config import Config
from libnix.config.config_scripts import ConfigScripts
from libnix.config.config_tags import ConfigTags


class TestConfig:
    def test_get_tags(self, config_valid):
        _config = config_valid.config()

        _tags = _config.get_tags()
        assert type(_tags) is ConfigTags

        _len_tags = len(_config.get_tags().list())
        _count_tags = config_valid.get_count_tags()
        assert _len_tags is _count_tags, "Found {} tags, should be {}".format(_len_tags, _count_tags)

    def test_get_scripts(self, config_valid):
        _config = config_valid.config()
        _scripts = _config.get_scripts()
        assert type(_scripts) is ConfigScripts

        _len_scripts = len(_config.get_scripts().list())
        _count_scripts = config_valid.get_count_scripts()
        assert _len_scripts is _count_scripts, "Found {} scripts, should be {}".format(_len_scripts, _count_scripts)

    def test_write(self, config_empty, config_valid):
        _empty_count_tags = config_empty.get_count_tags()
        _valid_count_tags = config_valid.get_count_tags()

        config_empty.config().write()

        _config = Config()
        _count_tags = len(_config.get_tags().list())
        assert _count_tags is _empty_count_tags, "Found {} tags, should be {}".format(_count_tags, _empty_count_tags)

        config_valid.config().write()

        _config = Config()
        _count_tags = len(_config.get_tags().list())
        assert _count_tags is _valid_count_tags, "Found {} tags, should be {}".format(_count_tags, _valid_count_tags)

from libnix.config.config_tag import ConfigTag


class TestConfigTag:
    _TAG_VALID_1 = "tag1"
    _TAG_VALID_2 = "tag2"
    _TAG_INVALID_1 = "bad_tag_1"
    _TAG_INVALID_2 = "bad_tag_2"

    _TAG_VALID_DESC_1 = "This is tag 1"
    _TAG_VALID_DESC_2 = "This is tag 2"
    _TAG_VALID_DESC_3 = "This is tag 3"

    _TAG_VALID_LIST = [_TAG_VALID_1, _TAG_VALID_2]
    _TAG_INVALID_LIST = [_TAG_INVALID_1, _TAG_INVALID_2]
    _TAG_MIX_LIST = [_TAG_INVALID_1, _TAG_VALID_1, _TAG_INVALID_2, _TAG_VALID_2]

    _TAG_INVALID_DESC_1 = "Bad description for tag 1"
    _TAG_INVALID_DESC_2 = "Bad description for tag 2"
    _TAG_INVALID_DESC_3 = "Bad description for tag 3"

    def test_set_name(self, config_valid):
        _tag = config_valid.config().get_tags().find(self._TAG_VALID_1)

        assert _tag.get_name() == self._TAG_VALID_1, "Initial tag name incorrect: {}".format(_tag.get_name())
        _tag.set_name(self._TAG_INVALID_1)
        assert _tag.get_name() == self._TAG_INVALID_1, "Changed tag name incorrect: {}".format(_tag.get_name())

    def test_get_name(self, config_valid):
        _tag = config_valid.config().get_tags().find(self._TAG_VALID_1)

        assert _tag.get_name() == self._TAG_VALID_1, \
            "Tag name incorrect - Found: {}, should be: {}".format(_tag.get_name(), self._TAG_VALID_1)

    def test_set_desc(self, config_valid):
        _tag = config_valid.config().get_tags().find(self._TAG_VALID_1)

        assert _tag.get_desc() == self._TAG_VALID_DESC_1, \
            "Initial tag description incorrect - Found: {}, should be: {}".format(_tag.get_desc(),
                                                                                  self._TAG_VALID_DESC_1)

        _tag.set_desc(self._TAG_INVALID_DESC_1)
        assert _tag.get_desc() == self._TAG_INVALID_DESC_1, \
            "Changed description incorrect - Found: '{}', should be '{}'".format(_tag.get_desc(),
                                                                                 self._TAG_INVALID_DESC_1)

    def test_get_desc(self, config_valid):
        _tag = config_valid.config().get_tags().find(self._TAG_VALID_1)

        assert _tag.get_desc() == self._TAG_VALID_DESC_1, \
            "Initial tag description incorrect - Found: {}, should be: {}".format(_tag.get_desc(),
                                                                                  self._TAG_VALID_DESC_1)

    def test_export_data(self, config_valid):
        _tag = config_valid.config().get_tags().find(self._TAG_VALID_1)

        _export = _tag.export_data()

        assert type(_export) == dict
        assert len(_export) == 2

    def test_import_data(self, config_valid):
        _tag = config_valid.config().get_tags().find(self._TAG_VALID_1)

        _export = _tag.export_data()
        _tag_new = ConfigTag()
        _tag_new.import_data(_export)

        assert type(_tag_new._tag) == dict
        assert len(_tag_new._tag) == 2

import pytest
from libnix.config.config_tag import ConfigTag
from libnix.config.config_tags import ConfigTags
from libnix.exception.nix_error import NixError


class TestConfigTags:
    _TAG_VALID_1 = "tag1"
    _TAG_VALID_2 = "tag2"
    _TAG_INVALID_1 = "bad_tag_1"
    _TAG_INVALID_2 = "bad_tag_2"

    _TAG_VALID_LIST = [_TAG_VALID_1, _TAG_VALID_2]
    _TAG_INVALID_LIST = [_TAG_INVALID_1, _TAG_INVALID_2]
    _TAG_MIX_LIST = [_TAG_INVALID_1, _TAG_VALID_1, _TAG_INVALID_2, _TAG_VALID_2]

    def test_exist(self, config_valid):
        _tags = config_valid.config().get_tags()

        assert _tags.exist(self._TAG_VALID_1), "Tag not found: {}".format(self._TAG_VALID_1)
        assert not _tags.exist(self._TAG_INVALID_1), "Non existing tag found: {}".format(self._TAG_INVALID_1)

    def test_get_invalid_tags(self, config_valid):
        _tags = config_valid.config().get_tags()

        _result = _tags.get_invalid_tags(self._TAG_VALID_LIST)
        assert len(_result) == 0, "Valid Tags found as invalid: {}".format(_result)

        _result = _tags.get_invalid_tags(self._TAG_INVALID_LIST)
        assert len(_result) == len(self._TAG_INVALID_LIST), "Invalid Tags found as valid: {}".format(_result)

        _result = _tags.get_invalid_tags(self._TAG_MIX_LIST)
        _correct = [x for x in self._TAG_MIX_LIST if x not in self._TAG_VALID_LIST]
        assert len(_result) == len(_correct), "Mix of valid and invalid Tags wrong: {}".format(_result)

    def test_insert(self, config_valid):
        _tags = config_valid.config().get_tags()

        _tag = _tags.insert()

        assert type(_tag) is ConfigTag
        assert _tag.get_name() is "", "Tag name should be none, contains: {}".format(_tag.get_name())
        assert _tag.get_desc() is "", "Tag description should be none, contains: {}".format(_tag.get_desc())

    def test_delete(self, config_valid):
        _tags = config_valid.config().get_tags()

        _tags.delete(self._TAG_VALID_1)

        with pytest.raises(NixError):
            _tags.delete(self._TAG_INVALID_1)

    def test_list(self, config_valid):
        _tags = config_valid.config().get_tags()

        _tag_list = _tags.list()

        assert len(_tag_list) == config_valid.get_count_tags()

    def test_find(self, config_valid):
        _tags = config_valid.config().get_tags()

        _tag = _tags.find(self._TAG_VALID_1)

        assert _tag.get_name() == self._TAG_VALID_1

        with pytest.raises(NixError):
            _tags.find(self._TAG_INVALID_1)

    def test_export_data(self, config_valid):
        _tags = config_valid.config().get_tags()

        _export = _tags.export_data()

        assert type(_export) == list
        assert len(_export) == config_valid.get_count_tags()

    def test_import_data(self, config_valid):
        _tags = config_valid.config().get_tags()

        _export = _tags.export_data()

        _tags_new = ConfigTags()

        _tags_new.import_data(_export)

        assert len(_tags_new.list()) == config_valid.get_count_tags()

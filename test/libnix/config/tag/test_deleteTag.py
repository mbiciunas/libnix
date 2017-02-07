import pytest

from libnix.config.config import Config
from libnix.config.tag.delete_tag import DeleteTag
from libnix.exception.nix_error import NixError


class TestDeleteTag:
    def test_delete(self, config_valid):
        _delete_tag = DeleteTag()
        _delete_tag.delete(config_valid.TAG_VALID_3)

        _tags = Config().get_tags()

        assert not _tags.exist(config_valid.TAG_VALID_3), \
            "Tag exists but should not exist: {}".format(config_valid.TAG_VALID_3)

    def test_delete_in_use(self, config_valid):
        _delete_tag = DeleteTag()

        with pytest.raises(NixError):
            _delete_tag.delete(config_valid.TAG_VALID_1)

    def test_delete_invalid_name(self, config_valid):
        _delete_tag = DeleteTag()

        with pytest.raises(NixError):
            _delete_tag.delete(config_valid.TAG_INVALID_1)

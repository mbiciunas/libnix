from libnix.config.config import Config
from libnix.exception.nix_error import NixError


class CreateTag:
    def __init__(self):
        self._config = Config()
        self._tags = self._config.get_tags()

    def create(self, tag: str, description: str):
        if self._tags.exist(tag):
            raise NixError("Tag already exists: {}".format(tag))

        _tag = self._tags.insert()
        _tag.set_name(tag)
        _tag.set_desc(description)

        self._config.write()

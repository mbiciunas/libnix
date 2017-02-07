from libnix.config.config import Config
from libnix.exception.nix_error import NixError


class RenameTag:
    def __init__(self):
        self._config = Config()
        self._tags = self._config.get_tags()
        self._scripts = self._config.get_scripts()

    def rename(self, tag: str, tag_new: str):
        if tag == tag_new:
            raise NixError("Original and new tag names are the same: {}".format(tag_new))

        if not self._tags.exist(tag):
            raise NixError("Unknown tag: {}".format(tag))

        if self._tags.exist(tag_new):
            raise NixError("New tag already exists: {}".format(tag_new))

        self._tags.find(tag).set_name(tag_new)

        _scripts = self._config.get_scripts().find_by_tag(tag)

        for _script in _scripts:
            _script_tags = _script.get_tags()

            if tag in _script_tags:
                _script_tags[_script_tags.index(tag)] = tag_new

        self._config.write()

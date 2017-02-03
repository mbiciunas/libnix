from libnix.config.config import Config
from libnix.exception.nix_error import NixError


class DeleteTag:
    def __init__(self):
        self._config = Config()
        self._tags = self._config.get_tags()

    def delete(self, tag: str):
        if not self._tags.exist(tag):
            raise NixError("Unknown tag: {}".format(tag))

        try:
            _scripts = self._config.get_scripts().find_by_tag(tag)
        except NixError:
            _scripts = None

        if _scripts is not None:
            _names = [_script.get_name() for _script in _scripts]
            raise NixError("Unable to delete tag: {} while attached to scripts: {}".format(tag, ' '.join(_names)))

        self._tags.delete(tag)

        self._config.write()

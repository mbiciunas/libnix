from libnix.config.config import Config
from libnix.exception.nix_error import NixError


class DeleteScript:
    def __init__(self):
        self._config = Config()

    def delete(self, name: str):
        _script = self._config.get_scripts().find_by_name(name)

        if _script is None:
            raise NixError("Script not found: {}".format(name))

        self._config.get_scripts().delete(name)

        self._config.write()

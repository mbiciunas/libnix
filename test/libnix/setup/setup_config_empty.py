from libnix.config.config import Config
from .make_json import MakeJson


class SetupConfigEmpty:
    _PATH_DST = "/home/mbiciunas/.nix/script/tag.json"

    _config = None
    _count_tags = None
    _count_scripts = None

    def __init__(self):
        with open(self._PATH_DST, "w") as text_file:
            text_file.write(self._make_json())

        self._config = Config()

    def config(self):
        return self._config

    def set_count_tags(self, count: int):
        self._count_tags = count

    def get_count_tags(self) -> int:
        return self._count_tags

    def set_count_scripts(self, count: int):
        self._count_scripts = count

    def get_count_scripts(self) -> int:
        return self._count_scripts

    @staticmethod
    def _make_json() -> str:
        _make_json = MakeJson()

        _json = _make_json.make()

        return _json

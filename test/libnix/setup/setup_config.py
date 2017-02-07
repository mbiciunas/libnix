from shutil import copyfile

from libnix.config.config import Config


class SetupConfig:
    _PATH_DST = "/home/mbiciunas/.nix/script/tag.json"

    _config = None
    _count_tags = None
    _count_scripts = None

    def __init__(self, source_file):
        copyfile(source_file, self._PATH_DST)
        self._config = Config()

    def config(self):
        return self._config

    def set_count_tags(self, count):
        self._count_tags = count

    def get_count_tags(self):
        return self._count_tags

    def set_count_scripts(self, count):
        self._count_scripts = count

    def get_count_scripts(self):
        return self._count_scripts

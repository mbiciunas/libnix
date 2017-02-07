import typing

from libnix.config.config_script import ConfigScript
from libnix.exception.nix_error import NixError


class ConfigScripts:
    def __init__(self):
        self._scripts = []

    def exist(self, name: str) -> bool:
        try:
            return True if self.find_by_name(name) else False
        except NixError:
            return False

    def insert(self) -> ConfigScript:
        _script = ConfigScript()

        self._scripts.append(_script)

        return _script

    def delete(self, name: str):
        _delete = False

        for _script in self._scripts:
            if _script.get_name() == name:
                self._scripts.remove(_script)
                _delete = True
                break

        if not _delete:
            raise NixError("Unable to delete, script not found: {}".format(name))

    def list(self, tags: typing.List[str] = list()) -> typing.List[str]:
        if tags is None:
            tags = []

        _result = []

        for _script in self._scripts:
            if all(tag in _script.get_tags() for tag in tags):
                _result.append(_script.get_name())

        return _result

    def find_by_name(self, name: str) -> ConfigScript:
        for _script in self._scripts:
            if _script.get_name() == name:
                return _script

        raise NixError("Unable to find script: {}".format(name))

    def find_by_tag(self, tag: str) -> typing.List[ConfigScript]:
        _scripts = []

        for _script in self._scripts:
            if tag in _script.get_tags():
                _scripts.append(_script)

        if len(_scripts) > 0:
            return _scripts

        raise NixError("Unable to find script by tag: {}".format(tag))

    def find_by_tags(self, tags: typing.List[str]) -> typing.List[ConfigScript]:
        _scripts = []

        for _script in self._scripts:
            if all(tag in _script.get_tags() for tag in tags):
                _scripts.append(_script)

        return _scripts

    def export_data(self) -> typing.List[str]:
        _export = []

        for _script in self._scripts:
            _export.append(_script.export_data())

        return _export

    def import_data(self, _data: list):
        for _script_data in _data:
            _script = ConfigScript()

            _script.import_data(_script_data)

            self._scripts.append(_script)

from libnix.config.config import Config
from libnix.exception.nix_error import NixError


class UpdateScript:
    def __init__(self, name):
        self._config = Config()
        self._name = name

    def update(self):
        _script = self._config.get_scripts().find_by_name(self._name)

        if _script is None:
            raise NixError("Script not found: {}".format(self._name))

        _script.make_temp(_script.get_code())

        _script.call_editor()

        _script.set_code(_script.read_temp_file())

        if _script.is_compile():
            _script.set_status(_script.STATUS_NORMAL)
        else:
            _script.set_status(_script.STATUS_COMPILE_ERROR)

        self._config.write()


def main():
    update_script = UpdateScript("my_processes")

    update_script.update()


if __name__ == "__main__":
    main()

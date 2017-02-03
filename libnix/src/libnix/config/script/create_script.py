from libnix.config.config import Config
from libnix.exception.nix_error import NixError


class CreateScript:
    TEMPLATE = "from libnix.process.processes import Processes\n"
    TEMPLATE += "from libnix.utility.print_table import PrintTable\n"
    TEMPLATE += "\n"
    TEMPLATE += "_processes = Processes()\n"
    TEMPLATE += "\n"

    def __init__(self, name, desc, tags):
        self._config = Config()
        self._name = name
        self._desc = desc
        self._tags = tags

    def create(self):
        _invalid_tags = self._config.get_tags().get_invalid_tags(self._tags)

        if len(_invalid_tags) is not 0:
            raise NixError("Unknown tags: {}".format(' '.join(_invalid_tags)))

        if self._config.get_scripts().exist(self._name):
            raise NixError("Script already exists: {}".format(self._name))

        _script = self._config.get_scripts().insert()

        _script.make_temp(self.TEMPLATE)

        _script.call_editor()

        _script.set_code(_script.read_temp_file())
        _script.set_name(self._name)
        _script.set_desc(self._desc)
        _script.add_tags(self._tags)

        if _script.is_compile():
            _script.set_status(_script.STATUS_NORMAL)
        else:
            _script.set_status(_script.STATUS_COMPILE_ERROR)

        self._config.write()


def main():
    create_script = CreateScript("my_processes", "new test process", ["test", "test1"])

    create_script.create()


if __name__ == "__main__":
    main()

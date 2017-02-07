from libnix.config.config import Config
from libnix.exception.nix_error import NixError
from libnix.utility.print_table import PrintTable


class ShowTag:
    def __init__(self):
        self._config = Config()
        self._tags = self._config.get_tags()

    def show(self, tag: str):
        if not self._tags.exist(tag):
            raise NixError("Unknown tag: {}".format(tag))

        _rows = []

        for _script in self._config.get_scripts().find_by_tag(tag):
            _rows.append([_script.get_name(),
                          _script.get_desc(),
                          ' '.join(_script.get_tags()),
                          _script.get_status()])
            # print("{}".format(_script.get_name()))

        _print_table = PrintTable("Script", "desc", "tags", "status")
        _print_table.add_data(_rows)
        _print_table.print()

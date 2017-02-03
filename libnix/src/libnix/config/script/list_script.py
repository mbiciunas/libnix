import typing

from libnix.config.config import Config
from libnix.utility.print_table import PrintTable


class ListScript:
    def __init__(self):
        self._config = Config()

    def list(self, tags: typing.List[str] = list()):
        _rows = []

        for _script in self._config.get_scripts().find_by_tags(tags):
            _rows.append([_script.get_name(),
                          _script.get_desc(),
                          ' '.join(_script.get_tags()),
                          _script.get_status()])

        _print_table = PrintTable("Script", "desc", "tags", "status")
        _print_table.add_data(_rows)
        _print_table.print()

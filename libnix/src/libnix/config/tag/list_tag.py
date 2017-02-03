from libnix.config.config import Config
from libnix.utility.print_table import PrintTable


class ListTag:
    def __init__(self):
        self._config = Config()
        self._tags = self._config.get_tags()

    def list(self):
        _rows = []

        for _tag in self._tags.list():
            _rows.append([_tag.get_name(),
                          _tag.get_desc()]),
            # print("{}".format(_tag))

        _print_table = PrintTable("Tag", "Description")
        _print_table.add_data(_rows)
        _print_table.print()

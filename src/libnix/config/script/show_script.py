from libnix.config.config import Config
from libnix.exception.nix_error import NixError
from libnix.utility.print_table import PrintTable


class ShowScript:
    def __init__(self):
        self._config = Config()

    def show(self, name: str):
        _script = self._config.get_scripts().find_by_name(name)

        if _script is None:
            raise NixError("Script not found: {}".format(name))

        _rows = []

        _column = ['\n'.join(_script.get_tags()),
                   _script.get_status(),
                   _script.get_code()]

        _rows.append(_column)
        _print_table = PrintTable("Tags", "Status", "Script")
        _print_table.add_data(_rows)
        _print_table.print()

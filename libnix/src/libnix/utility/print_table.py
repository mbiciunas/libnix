class PrintTable(object):
    def __init__(self, *args):
        self._data = [list(args)]
        self._max_column = len(args)
        self._titles = args
        self.width_column = [0] * self._max_column

    def add_data(self, data: list):
        # convert all the data points to string before saving data
        self._data.extend([[column if isinstance(column, str) else str(column) for column in row] for row in data])

        self._calc_width()

    def print(self):
        for _index in range(0, len(self.width_column)):
            print("+-{0:{1}}-".format("-" * self.width_column[_index], self.width_column[_index]), end="")

        print("+")

        for _index in range(0, len(self._titles)):
            print("| {0:{1}} ".format(self._titles[_index], self.width_column[_index]), end="")

        print("|")

        for _index in range(0, len(self.width_column)):
            print("+-{0:{1}}-".format("-" * self.width_column[_index], self.width_column[_index]), end="")

        print("+")

        for _row in self._data[1:]:
            _max_sub_row = 0

            for _item in _row:
                _lines = _item.splitlines()

                if len(_lines) > _max_sub_row:
                    _max_sub_row = len(_lines)

            _split_row = []

            for _item in _row:
                _lines = _item.splitlines()
                _max_lines = len(_lines)
                _split_column = []
                for _index in range(0, _max_sub_row):
                    if _index < _max_lines:
                        _split_column.append(_lines[_index])
                    else:
                        _split_column.append("")

                _split_row.append(_split_column)

            for _index_line in range(0, _max_sub_row):
                for _index_row in range(0, len(_split_row)):
                    print("| {0:{1}} ".format(_split_row[_index_row][_index_line],
                                              self.width_column[_index_row]), end="")

                print("|")

        for _index in range(0, len(self.width_column)):
            print("+-{0:{1}}-".format("-" * self.width_column[_index], self.width_column[_index]), end="")

        print("+")

    def _calc_width(self):
        for _row in self._data:
            for _index in range(0, self._max_column):
                _width = self._calc_width_item(_row[_index])

                if _width > self.width_column[_index]:
                    self.width_column[_index] = _width

    @staticmethod
    def _calc_width_item(item) -> int:
        _width = 0

        for _line in item.splitlines():
            if len(_line) > _width:
                _width = len(_line)

        return _width

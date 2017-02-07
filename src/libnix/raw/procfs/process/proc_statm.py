import os

from libnix.raw.abstract_read import AbstractRead


class ProcStatM(AbstractRead):
    _SIZE = "size"
    _RESIDENT = "resident"
    _SHARED = "shared"
    _TEXT = "text"
    _LIBRARY = "lib"
    _DATA = "data"
    _DIRTY = "dt"

    def __init__(self, pid: int):
        super().__init__()
        self._pid = pid

    def load(self):
        self._data = dict()

        _path = os.path.join(self._PROC_PATH, str(self._pid), "statm")
        _file_read = self._read(_path)

        if _file_read is not None:
            _file_data = _file_read.split()

            if len(_file_data) is 7:
                self._data[self._SIZE] = _file_data[0]
                self._data[self._RESIDENT] = _file_data[1]
                self._data[self._SHARED] = _file_data[2]
                self._data[self._TEXT] = _file_data[3]
                self._data[self._LIBRARY] = _file_data[4]
                self._data[self._DATA] = _file_data[5]
                self._data[self._DIRTY] = _file_data[6]

    @property
    def get_size(self) -> str:
        return self._get_value(self._SIZE)

    @property
    def get_resident(self) -> str:
        return self._get_value(self._RESIDENT)

    @property
    def get_shared(self) -> str:
        return self._get_value(self._SHARED)

    @property
    def get_text(self) -> str:
        return self._get_value(self._TEXT)

    @property
    def get_library(self) -> str:
        return self._get_value(self._LIBRARY)

    @property
    def get_data(self) -> str:
        return self._get_value(self._DATA)

    @property
    def get_dirty(self) -> str:
        return self._get_value(self._DIRTY)


def main():
    proc_statm = ProcStatM(1637)

    print("SIZE:     {}".format(proc_statm.get_size))
    print("RESIDENT: {}".format(proc_statm.get_resident))
    print("SHARED:   {}".format(proc_statm.get_shared))
    print("TEXT:     {}".format(proc_statm.get_text))
    print("LIBRARY:  {}".format(proc_statm.get_library))
    print("DATA:     {}".format(proc_statm.get_data))
    print("DIRTY:    {}".format(proc_statm.get_dirty))

    print("")


if __name__ == "__main__":
    main()

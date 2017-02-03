import os

from libnix.raw.abstract_read import AbstractRead


class ProcIO(AbstractRead):
    _CHAR_READ = "rchar"
    _CHAR_WRITE = "wchar"
    _SYSTEM_CALL_READ = "syscr"
    _SYSTEM_CALL_WRITE = "syscw"
    _BYTES_READ = "read_bytes"
    _BYTES_WRITE = "write_bytes"
    _CANCEL_BYTES_WRITE = "cancelled_write_bytes"

    def __init__(self, pid: int):
        super().__init__()
        self._pid = pid

    def load(self):
        self._data = dict()

        _path = os.path.join(self._PROC_PATH, str(self._pid), "io")
        _file_read = self._read(_path)

        if _file_read is not None:
            _file_data = _file_read.splitlines()

            if len(_file_data) is 7:
                for _line in _file_data:
                    if _line.startswith(self._CHAR_READ):
                        self._data[self._CHAR_READ] = _line.split(":")[1]
                    elif _line.startswith(self._CHAR_WRITE):
                        self._data[self._CHAR_WRITE] = _line.split(":")[1]
                    elif _line.startswith(self._SYSTEM_CALL_READ):
                        self._data[self._SYSTEM_CALL_READ] = _line.split(":")[1]
                    elif _line.startswith(self._SYSTEM_CALL_WRITE):
                        self._data[self._SYSTEM_CALL_WRITE] = _line.split(":")[1]
                    elif _line.startswith(self._BYTES_READ):
                        self._data[self._BYTES_READ] = _line.split(":")[1]
                    elif _line.startswith(self._BYTES_WRITE):
                        self._data[self._BYTES_WRITE] = _line.split(":")[1]
                    elif _line.startswith(self._CANCEL_BYTES_WRITE):
                        self._data[self._CANCEL_BYTES_WRITE] = _line.split(":")[1]

    @property
    def get_char_read(self) -> str:
        return self._get_value(self._CHAR_READ)

    @property
    def get_char_write(self) -> str:
        return self._get_value(self._CHAR_WRITE)

    @property
    def get_call_read(self) -> str:
        return self._get_value(self._SYSTEM_CALL_READ)

    @property
    def get_call_write(self) -> str:
        return self._get_value(self._SYSTEM_CALL_WRITE)

    @property
    def get_bytes_read(self) -> str:
        return self._get_value(self._BYTES_READ)

    @property
    def get_bytes_write(self) -> str:
        return self._get_value(self._BYTES_WRITE)

    @property
    def get_cancel_bytes_write(self) -> str:
        return self._get_value(self._CANCEL_BYTES_WRITE)


def main():
    proc_io = ProcIO(1637)

    print("CHAR READ:          {}".format(proc_io.get_char_read))
    print("CHAR WRITE:         {}".format(proc_io.get_char_write))
    print("SYSTEM CALL READ:   {}".format(proc_io.get_call_read))
    print("SYSTEM CALL WRITE:  {}".format(proc_io.get_call_write))
    print("BYTES READ:         {}".format(proc_io.get_bytes_read))
    print("BYTES WRITE:        {}".format(proc_io.get_bytes_write))
    print("CANCEL BYTES WRITE: {}".format(proc_io.get_cancel_bytes_write))

    print("")


if __name__ == "__main__":
    main()

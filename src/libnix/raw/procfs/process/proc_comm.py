import os

from libnix.raw.abstract_read import AbstractRead


class ProcComm(AbstractRead):
    _COMMAND = "size"

    def __init__(self, pid: int):
        super().__init__()
        self._pid = pid

    def load(self):
        self._data = dict()

        _path = os.path.join(self._PROC_PATH, str(self._pid), "comm")
        _file_read = self._read(_path)

        if _file_read is not None:
            _file_data = _file_read.split()

            if len(_file_data) is 1:
                self._data[self._COMMAND] = _file_data[0]

    @property
    def get_command(self) -> str:
        return self._get_value(self._COMMAND)


def main():
    proc_comm = ProcComm(1637)

    print("COMMAND:    {}".format(proc_comm.get_command))

    print("")


if __name__ == "__main__":
    main()

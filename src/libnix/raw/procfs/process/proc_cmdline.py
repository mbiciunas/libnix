import os

from libnix.raw.abstract_read import AbstractRead


class ProcCmdline(AbstractRead):
    _COMMAND = "size"
    _ARGS = "args"

    def __init__(self, pid: int):
        super().__init__()
        self._pid = pid

    def load(self):
        self._data = dict()

        _path = os.path.join(self._PROC_PATH, str(self._pid), "cmdline")
        _file_read = self._read(_path)

        if _file_read is not None:
            _file_data = _file_read.split('\x00')

            if len(_file_data) > 0:
                self._data[self._COMMAND] = _file_data[0]

            if len(_file_data) > 1:
                self._data[self._ARGS] = list(filter(None, _file_data[1:]))

    @property
    def get_command(self) -> str:
        return self._get_value(self._COMMAND)

    @property
    def get_argument_count(self) -> int:
        return len(self._get_value(self._ARGS))

    @property
    def get_arguments(self) -> str:
        return self._get_value(self._ARGS)


def main():
    run_cmdline(1637)


def run_cmdline(pid: int):
    proc_cmdline = ProcCmdline(pid)

    print("COMMAND:   {}".format(proc_cmdline.get_command))
    if proc_cmdline.get_argument_count > 0:
        print("ARGUMENTS: {}".format(proc_cmdline.get_arguments[0]))
    if proc_cmdline.get_argument_count > 1:
        for index in range(1, proc_cmdline.get_argument_count):
            print("           {}".format(proc_cmdline.get_arguments[index]))

    print("")

if __name__ == "__main__":
    main()

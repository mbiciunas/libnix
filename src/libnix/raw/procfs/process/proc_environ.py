import os

from libnix.raw.abstract_read import AbstractRead


class ProcEnviron(AbstractRead):
    _ARGS = "args"

    def __init__(self, pid: int):
        super().__init__()
        self._pid = pid

    def load(self):
        self._data = dict()

        _path = os.path.join(self._PROC_PATH, str(self._pid), "environ")
        _file_read = self._read(_path)

        if _file_read is not None:
            _file_data = _file_read.split('\x00')

            self._data[self._ARGS] = list(filter(None, _file_data[1:]))
        else:
            self._data[self._ARGS] = []

    @property
    def get_environment_count(self) -> int:
        return len(self._get_value(self._ARGS))

    @property
    def get_environments(self) -> str:
        return self._get_value(self._ARGS)


def main():

    run_environ(1637)

    # run_environ("1620")

    # run_environ("1383")


def run_environ(pid: int):
    proc_environ = ProcEnviron(pid)

    print("PID:       {}".format(pid))
    print("ARG COUNT: {}".format(proc_environ.get_environment_count))

    if proc_environ.get_environment_count > 0:
        print("ARGUMENTS: {}".format(proc_environ.get_environments[0]))

    if proc_environ.get_environment_count > 1:
        for index in range(1, proc_environ.get_environment_count):
            print("           {}".format(proc_environ.get_environments[index]))

    print("")

if __name__ == "__main__":
    main()

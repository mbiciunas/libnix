import os
import typing

from libnix.raw.abstract_read import AbstractRead


class Mounts(AbstractRead):
    def __init__(self):
        super().__init__()

    def load(self):
        self._data = dict()

        _path = os.path.join(self._PROC_PATH, "mounts")
        _file_read = self._read(_path)

        if _file_read is not None:
            for _line in _file_read.splitlines():
                _mount = Mount(_line)

                self._data[_mount.get_mount_point()] = _mount

    def get_mounts(self) -> iter:
        if self._data is None:
            self.load()

        return self._data.keys()

    def get_mount(self, mount_point: str) -> iter:
        if self._data is None:
            self.load()

        return self._data[mount_point]


class Mount:
    _DEVICE = "device"
    _MOUNT_POINT = "mount_point"
    _TYPE = "type"
    _OPTIONS = "options"

    def __init__(self, line):
        self._module = dict()

        _data = line.split()

        if len(_data) is 6:
            self._module[self._DEVICE] = _data[0]
            self._module[self._MOUNT_POINT] = _data[1]
            self._module[self._TYPE] = _data[2]
            self._module[self._OPTIONS] = _data[3]

    # @property
    def get_device(self) -> str:
        return self._get_value(self._DEVICE)

    # @property
    def get_mount_point(self) -> str:
        return self._get_value(self._MOUNT_POINT)

    # @property
    def get_filesystem_type(self) -> str:
        return self._get_value(self._TYPE)

    # @property
    def get_options(self) -> str:
        return self._get_value(self._OPTIONS)

    def _get_value(self, item: str) -> typing.Optional[str]:
        try:
            return self._module[item]
        except KeyError:
            return None


def main():
    _mounts = Mounts()

    # _mounts.load()

    for _mount_point in _mounts.get_mounts():
        _mount = _mounts.get_mount(_mount_point)

        print("{:<35} {:<25} {:<10} {:<80}".format(_mount.get_mount_point(),
                                                   _mount.get_device(),
                                                   _mount.get_filesystem_type(),
                                                   _mount.get_options()))

        # print("")


if __name__ == "__main__":
    main()

import os
import typing

from libnix.raw.abstract_read import AbstractRead


class Modules(AbstractRead):
    def __init__(self):
        super().__init__()

    def load(self):
        self._data = dict()

        _path = os.path.join(self._PROC_PATH, "modules")
        _file_read = self._read(_path)

        if _file_read is not None:
            for _line in _file_read.splitlines():
                _module = Module(_line)

                self._data[_module.get_name()] = _module

    def get_modules(self) -> iter:
        if self._data is None:
            self.load()

        return self._data.keys()

    def get_module(self, name: str) -> iter:
        if self._data is None:
            self.load()

        return self._data[name]


class Module:
    _NAME = "name"
    _SIZE = "size"
    _INSTANCES = "instances"
    _DEPENDENCIES = "depends"
    _STATE = "state"
    _MEMORY_OFFSET = "memory_offset"

    def __init__(self, line):
        self._module = dict()

        _data = line.split()

        if len(_data) is 6:
            self._module[self._NAME] = _data[0]
            self._module[self._SIZE] = _data[1]
            self._module[self._INSTANCES] = _data[2]
            self._module[self._DEPENDENCIES] = _data[3]
            self._module[self._STATE] = _data[4]
            self._module[self._MEMORY_OFFSET] = _data[5]

    # @property
    def get_name(self) -> str:
        return self._get_value(self._NAME)

    # @property
    def get_size(self) -> str:
        return self._get_value(self._SIZE)

    # @property
    def get_instances(self) -> str:
        return self._get_value(self._INSTANCES)

    # @property
    def get_dependencies(self) -> str:
        return self._get_value(self._DEPENDENCIES)

    # @property
    def get_state(self) -> str:
        return self._get_value(self._STATE)

    # @property
    def get_memory_offset(self) -> str:
        return self._get_value(self._MEMORY_OFFSET)

    def _get_value(self, item: str) -> typing.Optional[str]:
        try:
            return self._module[item]
        except KeyError:
            return None


def main():
    _modules = Modules()

    _modules.load()

    for _name in _modules.get_modules():
        _module = _modules.get_module(_name)

        if _module.get_instances is not "0":
            print("{:<20} {:<10} {:<2} {:<80} {:<10} {:<10}".format(_module.get_name(),
                                                                    _module.get_size(),
                                                                    _module.get_instances(),
                                                                    _module.get_dependencies(),
                                                                    _module.get_state(),
                                                                    _module.get_memory_offset()))
            # print("   Size:          {}".format(_module.get_size()))
            # print("   Instances:     {}".format(_module.get_instances()))
            #
            # print("   Dependencies:  {}".format(_module.get_dependencies()))
            # print("   State:         {}".format(_module.get_state()))
            # print("   Memory Offset: {}".format(_module.get_memory_offset()))

            print("")


if __name__ == "__main__":
    main()

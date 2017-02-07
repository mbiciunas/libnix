import os
import typing

from libnix.utility.dir import Dir


class DirList:

    def __init__(self):
        pass

    @staticmethod
    def get_services() -> typing.List[str]:
        _top_dir = Dir.get_nix()

        return os.listdir(_top_dir)

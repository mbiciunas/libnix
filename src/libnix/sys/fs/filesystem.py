import os

from libnix.sys.fs.filesystem_filter import FilesystemFilter
from libnix.sys.fs.resultset import Resultset
from libnix.sys.fs.resultset import FileInfo


class Filesystem:
    def __init__(self) -> None:
        self._resultset = Resultset()
        # self._files = OrderedDict()
        # self._filter = list()
        self._path_include = list()
        self._path_exclude = list()

        self._filter = FilesystemFilter()

    # def filter(self, filesystem_filter) -> None:
    #     self._filter.append(filesystem_filter)

    def filter_file_type(self, *args) -> None:
        self._filter.filter_type(*args)

    def filter_user(self, *args) -> None:
        self._filter.filter_user(*args)

    def filter_group(self, *args) -> None:
        self._filter.filter_group(*args)

    def filter_size(self, size_min: int=None, size_max: int=None) -> None:
        self._filter.filter_size(size_min, size_max)

    def filter_permission_user(self, read: bool=None, write: bool=None, execute: bool=None) -> None:
        self._filter.filter_permission_user(read, write, execute)

    def filter_permission_group(self, read: bool=None, write: bool=None, execute: bool=None) -> None:
        self._filter.filter_permission_group(read, write, execute)

    def filter_permission_other(self, read: bool=None, write: bool=None, execute: bool=None) -> None:
        self._filter.filter_permission_other(read, write, execute)

    def filter_setid(self, uid: int=None, gid: int=None) -> None:
        self._filter.filter_setid(uid, gid)

    def path_include(self, path: str) -> None:
        self._path_include.append(path)

    def path_exclude(self, path: str) -> None:
        self._path_exclude.append(path)

    def load(self) -> Resultset:
        if len(self._path_include) == 0:
            self._path_include.append("/")

        for _path in self._path_include:
            self._load(_path)

        return self._resultset

    def _load(self, path: str) -> None:
        try:
            for _filename in os.listdir(path):
                _pathname = os.path.join(path, _filename)

                try:
                    _file_info = FileInfo(_pathname)
                    # statinfo = os.lstat(_pathname)
                    # mode = statinfo.st_mode
                except FileNotFoundError:
                    continue

                if self._test_filter(_file_info):
                    if not self._test_path_exclude(_pathname):
                        # self._files[_pathname] = statinfo
                        self._resultset.add(_file_info)
                if _file_info.get_type() is FileInfo.TYPE_DIR:
                    if not self._test_path_exclude(_pathname):
                        self._load(_pathname)
        except PermissionError:
            pass

    def _test_path_exclude(self, pathname: str) -> bool:
        for _path in self._path_exclude:
            if _path in pathname:
                return True

        return False

    def _test_filter(self, file_info: FileInfo) -> bool:
        if self._filter.test(file_info):
            return True
        else:
            return False

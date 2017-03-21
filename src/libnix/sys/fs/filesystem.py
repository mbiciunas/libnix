from collections import OrderedDict
import os
from stat import *

from libnix.sys.fs.filesystem_filter import FilesystemFilter


class Filesystem:
    def __init__(self):
        self._files = OrderedDict()
        # self._filter = list()
        self._path_include = list()
        self._path_exclude = list()

        self._filter = FilesystemFilter()

    # def filter(self, filesystem_filter):
    #     self._filter.append(filesystem_filter)

    def filter_file_type(self, *args):
        self._filter.filter_type(*args)

    def filter_user(self, *args):
        self._filter.filter_user(*args)

    def filter_group(self, *args):
        self._filter.filter_group(*args)

    def filter_size(self, size_min=None, size_max=None):
        self._filter.filter_size(size_min, size_max)

    def filter_permission_user(self, read=None, write=None, execute=None):
        self._filter.filter_permission_user(read, write, execute)

    def filter_permission_group(self, read=None, write=None, execute=None):
        self._filter.filter_permission_group(read, write, execute)

    def filter_permission_other(self, read=None, write=None, execute=None):
        self._filter.filter_permission_other(read, write, execute)

    def path_include(self, path):
        self._path_include.append(path)

    def path_exclude(self, path):
        self._path_exclude.append(path)

    def load(self):
        if len(self._path_include) == 0:
            self._path_include.append("/")

        for _path in self._path_include:
            self._load(_path)

    def _load(self, path):
        try:
            for _filename in os.listdir(path):
                _pathname = os.path.join(path, _filename)

                try:
                    statinfo = os.lstat(_pathname)
                    mode = statinfo.st_mode
                except FileNotFoundError:
                    continue

                if self._test_filter(_pathname, statinfo):
                    if not self._test_path_exclude(_pathname):
                        self._files[_pathname] = statinfo

                if S_ISDIR(mode):
                    if not self._test_path_exclude(_pathname):
                        self._load(_pathname)
        except PermissionError:
            pass

    def _test_path_exclude(self, pathname):
        for _path in self._path_exclude:
            if _path in pathname:
                return True

        return False

    def _test_filter(self, pathname, statinfo):
        if self._filter.test(pathname, statinfo):
            return True
        else:
            return False

    def get_files(self):
        return self._files


if __name__ == '__main__':
    _filesystem = Filesystem()
    _filesystem.path_include("/home")
    _filesystem.path_exclude("lost+found")
    _filesystem.path_exclude(".cache")
    _filesystem.filter_file_type(FilesystemFilter.FILE_TYPE_DIR,
                                 FilesystemFilter.FILE_TYPE_REG,
                                 FilesystemFilter.FILE_TYPE_LINK)
    _filesystem.filter_user(1000)
    _filesystem.filter_group(1000)
    _filesystem.filter_size(size_min=10, size_max=1000)
    _filesystem.filter_permission_user(read=True, write=True, execute=True)
    _filesystem.filter_permission_group(read=True, write=True, execute=True)
    _filesystem.filter_permission_other(read=None, write=None, execute=True)

    _filesystem.load()

    print("len: {}".format(len(_filesystem.get_files())))

    for _file, _stat in _filesystem.get_files().items():
        print("{}: {}-{}-{} - {}-{}-{} - {}-{}-{} {} {} {} {}".format(_file,
                                                          bool(_stat.st_mode & S_IRUSR),
                                                          bool(_stat.st_mode & S_IWUSR),
                                                          bool(_stat.st_mode & S_IXUSR),
                                                          bool(_stat.st_mode & S_IRGRP),
                                                          bool(_stat.st_mode & S_IWGRP),
                                                          bool(_stat.st_mode & S_IXGRP),
                                                          bool(_stat.st_mode & S_IROTH),
                                                          bool(_stat.st_mode & S_IWOTH),
                                                          bool(_stat.st_mode & S_IXOTH),
                                                          bool(_stat.st_mode & S_ISUID),
                                                          bool(_stat.st_mode & S_ISGID),
                                                          bool(_stat.st_mode & S_ISVTX),
                                                          oct(_stat.st_mode & 0o0777)))

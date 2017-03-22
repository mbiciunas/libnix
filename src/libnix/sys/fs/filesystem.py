import os

from libnix.sys.fs.filesystem_filter import FilesystemFilter
from libnix.sys.fs.resultset import Resultset
from libnix.sys.fs.resultset import File


class Filesystem:
    def __init__(self):
        self._resultset = Resultset()
        # self._files = OrderedDict()
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

    def filter_setid(self, uid=None, gid=None):
        self._filter.filter_setid(uid, gid)

    def path_include(self, path):
        self._path_include.append(path)

    def path_exclude(self, path):
        self._path_exclude.append(path)

    def load(self):
        if len(self._path_include) == 0:
            self._path_include.append("/")

        for _path in self._path_include:
            self._load(_path)

        return self._resultset

    def _load(self, path):
        try:
            for _filename in os.listdir(path):
                _pathname = os.path.join(path, _filename)

                try:
                    _file_info = File(_pathname)
                    # statinfo = os.lstat(_pathname)
                    # mode = statinfo.st_mode
                except FileNotFoundError:
                    continue

                if self._test_filter(_file_info):
                    if not self._test_path_exclude(_pathname):
                        # self._files[_pathname] = statinfo
                        self._resultset.add(_file_info)
                if _file_info.get_type() is File.TYPE_DIR:
                    if not self._test_path_exclude(_pathname):
                        self._load(_pathname)
        except PermissionError:
            pass

    def _test_path_exclude(self, pathname):
        for _path in self._path_exclude:
            if _path in pathname:
                return True

        return False

    def _test_filter(self, file_info):
        if self._filter.test(file_info):
            return True
        else:
            return False


if __name__ == '__main__':
    _filesystem = Filesystem()
    _filesystem.path_include("/usr")
    # _filesystem.path_include("/home")
    # _filesystem.path_exclude("lost+found")
    # _filesystem.path_exclude(".cache")
    # _filesystem.filter_file_type(File.TYPE_DIR, File.TYPE_REG, File.TYPE_LINK)
    # _filesystem.filter_user(1000)
    # _filesystem.filter_group(1000)
    _filesystem.filter_setid(uid=True)
    # _filesystem.filter_size(size_min=10, size_max=1000)
    # _filesystem.filter_permission_user(read=True, write=True, execute=True)
    # _filesystem.filter_permission_group(read=True, write=True, execute=True)
    # _filesystem.filter_permission_other(read=None, write=None, execute=True)

    _resultset = _filesystem.load()

    print("len: {}".format(_resultset.get_file_count()))

    for _file in _resultset.get_files():
        _permission = ""
        _permission += 'd' if _file.get_type() is File.TYPE_DIR else '-'
        _permission += 'r' if _file.get_user_read() else '-'
        _permission += 'w' if _file.get_user_write() else '-'
        _permission += 'x' if _file.get_user_execute() else '-'
        _permission += 'r' if _file.get_group_read() else '-'
        _permission += 'w' if _file.get_group_write() else '-'
        _permission += 'x' if _file.get_group_execute() else '-'
        _permission += 'r' if _file.get_other_read() else '-'
        _permission += 'w' if _file.get_other_write() else '-'
        _permission += 'x' if _file.get_other_execute() else '-'

        print("{} - {}".format(_permission, _file.get_path()))
        # print("{}: {}-{}-{} - {}-{}-{} - {}-{}-{} {} {} {}".format(_file.get_path(),
        #                                                            _file.get_user_read(),
        #                                                            _file.get_user_write(),
        #                                                            _file.get_user_execute(),
        #
        #                                                            _file.get_group_read(),
        #                                                            _file.get_group_write(),
        #                                                            _file.get_group_execute(),
        #
        #                                                            _file.get_other_read(),
        #                                                            _file.get_other_write(),
        #                                                            _file.get_other_execute(),
        #
        #                                                            _file.get_set_uid(),
        #                                                            _file.get_set_gid(),
        #                                                            _file.get_sticky_bit()))

from collections import OrderedDict
import os
from stat import *


class Resultset:
    def __init__(self):
        self._files = OrderedDict()

    def add(self, file):
        self._files[file.get_path()] = file

    def get_files(self):
        return self._files.values()

    def get_file_count(self):
        return len(self._files)


class File:
    TYPE_DIR = "dir"
    TYPE_REG = "regular"
    TYPE_CHAR = "char"
    TYPE_BLOCK = "block"
    TYPE_FIFO = "fifo"
    TYPE_LINK = "link"
    TYPE_SOCK = "sock"

    def __init__(self, path):
        self._path = path
        self._statinfo = os.lstat(path)

    def get_path(self):
        return self._path

    def get_user_read(self):
        return bool(self._statinfo.st_mode & S_IRUSR)

    def get_user_write(self):
        return bool(self._statinfo.st_mode & S_IWUSR)

    def get_user_execute(self):
        return bool(self._statinfo.st_mode & S_IXUSR)

    def get_group_read(self):
        return bool(self._statinfo.st_mode & S_IRGRP)

    def get_group_write(self):
        return bool(self._statinfo.st_mode & S_IWGRP)

    def get_group_execute(self):
        return bool(self._statinfo.st_mode & S_IXGRP)

    def get_other_read(self):
        return bool(self._statinfo.st_mode & S_IROTH)

    def get_other_write(self):
        return bool(self._statinfo.st_mode & S_IWOTH)

    def get_other_execute(self):
        return bool(self._statinfo.st_mode & S_IXOTH)

    def get_set_uid(self):
        return bool(self._statinfo.st_mode & S_ISUID)

    def get_set_gid(self):
        return bool(self._statinfo.st_mode & S_ISGID)

    def get_sticky_bit(self):
        return bool(self._statinfo.st_mode & S_ISVTX)

    def get_user_id(self):
        return self._statinfo.st_uid

    def get_group_id(self):
        return self._statinfo.st_gid

    def get_size(self):
        return self._statinfo.st_size

    def get_type(self):
        _mode = self._statinfo.st_mode

        if S_ISDIR(_mode):
            return self.TYPE_DIR
        elif S_ISREG(_mode):
            return self.TYPE_REG
        elif S_ISCHR(_mode):
            return self.TYPE_CHAR
        elif S_ISBLK(_mode):
            return self.TYPE_BLOCK
        elif S_ISFIFO(_mode):
            return self.TYPE_FIFO
        elif S_ISLNK(_mode):
            return self.TYPE_LINK
        elif S_ISSOCK(_mode):
            return self.TYPE_SOCK

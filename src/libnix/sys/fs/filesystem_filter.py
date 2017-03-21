from stat import *


class FilesystemFilter:
    FILE_TYPE_DIR = "dir"
    FILE_TYPE_REG = "regular"
    FILE_TYPE_CHAR = "char"
    FILE_TYPE_BLOCK = "block"
    FILE_TYPE_FIFO = "fifo"
    FILE_TYPE_LINK = "link"
    FILE_TYPE_SOCK = "sock"

    def __init__(self):
        self._file_type = None
        self._user = None
        self._group = None
        self._size_min = None
        self._size_max = None
        self._user_read = None
        self._user_write = None
        self._user_exec = None
        self._group_read = None
        self._group_write = None
        self._group_exec = None
        self._other_read = None
        self._other_write = None
        self._other_exec = None

    def filter_type(self, *args):
        self._file_type = list(args)

    def filter_user(self, *args):
        self._user = list(args)

    def filter_group(self, *args):
        self._group = list(args)

    def filter_size(self, size_min=None, size_max=None):
        self._size_min = size_min
        self._size_max = size_max

    def filter_permission_user(self, user_read=None, user_write=None, user_exec=None):
        self._user_read = user_read
        self._user_write = user_write
        self._user_exec = user_exec

    def filter_permission_group(self, group_read=None, group_write=None, group_exec=None):
        self._group_read = group_read
        self._group_write = group_write
        self._group_exec = group_exec

    def filter_permission_other(self, other_read=None, other_write=None, other_exec=None):
        self._other_read = other_read
        self._other_write = other_write
        self._other_exec = other_exec

    def test(self, pathname, statinfo):
        if not self._test_file_type(statinfo.st_mode):
            return False
        elif not self._test_user(statinfo.st_uid):
            return False
        elif not self._test_group(statinfo.st_gid):
            return False
        elif not self._test_size(statinfo.st_size):
            return False
        elif not self._test_permission(statinfo.st_mode):
            return False

        return True

    def _test_file_type(self, mode):
        if self._file_type is None:
            return True
        elif S_ISDIR(mode) and self.FILE_TYPE_DIR in self._file_type:
            return True
        elif S_ISREG(mode) and self.FILE_TYPE_REG in self._file_type:
            return True
        elif S_ISCHR(mode) and self.FILE_TYPE_CHAR in self._file_type:
            return True
        elif S_ISBLK(mode) and self.FILE_TYPE_BLOCK in self._file_type:
            return True
        elif S_ISFIFO(mode) and self.FILE_TYPE_FIFO in self._file_type:
            return True
        elif S_ISLNK(mode) and self.FILE_TYPE_LINK in self._file_type:
            return True
        elif S_ISSOCK(mode) and self.FILE_TYPE_SOCK in self._file_type:
            return True

        return False

    def _test_user(self, user):
        if self._user is None:
            return True
        elif user in self._user:
            return True

        return False

    def _test_group(self, group):
        if self._group is None:
            return True
        elif group in self._group:
            return True

        return False

    def _test_size(self, size):
        if self._size_min is not None and self._size_min > size:
            return False
        elif self._size_max is not None and self._size_max < size:
            return False
        else:
            return True

    def _test_permission(self, mode):
        if self._user_read is not None and self._user_read is not bool(mode & S_IRUSR):
            return False
        elif self._user_write is not None and self._user_write is not bool(mode & S_IWUSR):
            return False
        elif self._user_exec is not None and self._user_exec is not bool(mode & S_IXUSR):
            return False
        elif self._group_read is not None and self._group_read is not bool(mode & S_IRGRP):
            return False
        elif self._group_write is not None and self._group_write is not bool(mode & S_IWGRP):
            return False
        elif self._group_exec is not None and self._group_exec is not bool(mode & S_IXGRP):
            return False
        elif self._other_read is not None and self._other_read is not bool(mode & S_IROTH):
            return False
        elif self._other_write is not None and self._other_write is not bool(mode & S_IWOTH):
            return False
        elif self._other_exec is not None and self._other_exec is not bool(mode & S_IXOTH):
            return False
        else:
            return True

from libnix.sys.fs.resultset import File


class FilesystemFilter:
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
        self._set_uid = None
        self._set_gid = None

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

    def filter_setid(self, uid=None, gid=None):
        self._set_uid = uid
        self._set_gid = gid

    def test(self, file_info):
        if not self._test_file_type(file_info.get_type()):
            return False
        elif not self._test_user(file_info.get_user_id()):
            return False
        elif not self._test_group(file_info.get_group_id()):
            return False
        elif not self._test_size(file_info.get_size()):
            return False
        elif not self._test_permission(file_info):
            return False
        elif not self._test_setid(file_info):
            return False

        return True

    def _test_file_type(self, file_type):
        if self._file_type is None:
            return True
        elif file_type is File.TYPE_DIR and File.TYPE_DIR in self._file_type:
            return True
        elif file_type is File.TYPE_REG and File.TYPE_REG in self._file_type:
            return True
        elif file_type is File.TYPE_CHAR and File.TYPE_CHAR in self._file_type:
            return True
        elif file_type is File.TYPE_BLOCK and File.TYPE_BLOCK in self._file_type:
            return True
        elif file_type is File.TYPE_FIFO and File.TYPE_FIFO in self._file_type:
            return True
        elif file_type is File.TYPE_LINK and File.TYPE_LINK in self._file_type:
            return True
        elif file_type is File.TYPE_SOCK and File.TYPE_SOCK in self._file_type:
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

    def _test_permission(self, file_info):
        if self._user_read is not None and self._user_read is not file_info.get_user_read():
            return False
        elif self._user_write is not None and self._user_write is not file_info.get_user_write():
            return False
        elif self._user_exec is not None and self._user_exec is not file_info.get_user_execute():
            return False
        elif self._group_read is not None and self._group_read is not file_info.get_group_read():
            return False
        elif self._group_write is not None and self._group_write is not file_info.get_group_write():
            return False
        elif self._group_exec is not None and self._group_exec is not file_info.get_group_execute():
            return False
        elif self._other_read is not None and self._other_read is not file_info.get_other_read():
            return False
        elif self._other_write is not None and self._other_write is not file_info.get_other_write():
            return False
        elif self._other_exec is not None and self._other_exec is not file_info.get_other_execute():
            return False
        else:
            return True

    def _test_setid(self, file_info):
        if self._set_uid is not None and self._set_uid is not file_info.get_set_uid():
            return False
        elif self._set_gid is not None and self._set_gid is not file_info.get_set_gid():
            return False
        else:
            return True

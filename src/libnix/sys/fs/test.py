import os
import sys
from stat import *

files = list()
files_tuple = list()
files_dict = dict()
count_dir = 0
count_reg = 0
count_char = 0
count_block = 0
count_fifo = 0
count_link = 0
count_sock = 0
count_unknown = 0


def walktree(top, callback):
    try:
        for f in os.listdir(top):
            pathname = os.path.join(top, f)

            try:
                statinfo = os.lstat(pathname)
                mode = statinfo.st_mode
                uid = statinfo.st_uid
                gid = statinfo.st_gid
                # if uid == 0:
                #     print("Uid: {}, gid: {}".format(uid, gid))
                #     continue
            except FileNotFoundError:
                continue

            global files, files_tuple, files_dict
            files.append(pathname)
            files_tuple.append((pathname, statinfo))
            files_dict[pathname] = statinfo

            if S_ISDIR(mode):
                global count_dir
                count_dir += 1

                walktree(pathname, callback)
            elif S_ISREG(mode):
                global count_reg
                count_reg += 1
                # It's a file, call the callback function
                # callback(pathname)
            elif S_ISCHR(mode):
                global count_char
                count_char += 1
                # It's a file, call the callback function
                # print('Character special device file - {}'.format(pathname))
            elif S_ISBLK(mode):
                global count_block
                count_block += 1
                # It's a file, call the callback function
                # print('Block special device file - {}'.format(pathname))
            elif S_ISFIFO(mode):
                global count_fifo
                count_fifo += 1
                # It's a file, call the callback function
                # print('FIFO (named pipe) file - {}'.format(pathname))
            elif S_ISLNK(mode):
                global count_link
                count_link += 1
                # print('Symbolic link file - {}'.format(pathname))
            elif S_ISSOCK(mode):
                global count_sock
                count_sock += 1
                # It's a file, call the callback function
                # print('Socket file - {}'.format(pathname))
            else:
                # Unknown file type, print a message
                print('Skipping mode: {} - {}'.format(mode, pathname))
    except PermissionError:
        pass
        # print("permission error on {}".format(top))


def visitfile(file):
    # print('visiting', file)
    pass


def get_size(obj, seen=None):
    """Recursively finds size of objects"""
    size = sys.getsizeof(obj)
    if seen is None:
        seen = set()
    obj_id = id(obj)
    if obj_id in seen:
        return 0
    # Important mark as seen *before* entering recursion to gracefully handle
    # self-referential objects
    seen.add(obj_id)
    if isinstance(obj, dict):
        size += sum([get_size(v, seen) for v in obj.values()])
        size += sum([get_size(k, seen) for k in obj.keys()])
    elif hasattr(obj, '__dict__'):
        size += get_size(obj.__dict__, seen)
    elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
        size += sum([get_size(i, seen) for i in obj])
    return size


if __name__ == '__main__':
    # walktree(sys.argv[1], visitfile)
    walktree("/home", visitfile)
    print("Results")
    print("   List Entries:{}, bytes: {}".format(len(files), get_size(files)))
    print("   Tuple Entries:{}, bytes: {}".format(len(files_tuple), get_size(files_tuple)))
    print("   Dict Entries:{}, bytes: {}".format(len(files_dict), get_size(files_dict)))
    print("   Directories: {}".format(count_dir))
    print("   Regular file: {}".format(count_reg))
    print("   Character device: {}".format(count_char))
    print("   Block device: {}".format(count_block))
    print("   Named pipes: {}".format(count_fifo))
    print("   Symbolic Links: {}".format(count_link))
    print("   Sockets: {}".format(count_sock))
    print("   Unknown: {}".format(count_unknown))

    # for _path, _statinfo in files_tuple:
    #     print("path: {},  statinfo: {}".format(_path, _statinfo))
# Nix
# Copyright (c) 2017  Mark Biciunas.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import typing

from libnix.raw.abstract_read import AbstractRead


class DiskStat:
    _DEVICE_MAJOR = "major_number"
    _DEVICE_MINOR = "minor_number"
    _DEVICE_NAME = "device_name"
    _READ_COMPLETED = "reads_completed_successfully"
    _READ_MERGED = "reads_merged"

    _READ_SECTORS = "sectors_read"
    _READ_TIME = "time_spent_reading"
    _WRITE_COMPLETED = "writes_completed"
    _WRITE_MERGED = "writes_merged"
    _WRITE_SECTORS = "sectors_written"

    _WRITE_TIME = "time_spent_writing"
    _IO_IN_PROGRESS = "IO_currently_in_progress"
    _IO_TIME = "time_spent_doing_IO"
    _IO_TIME_WEIGHTED = "weighted_time_spent_doing_IO"

    def __init__(self, line) -> None:
        self._disk = dict()

        _data = line.split()

        if len(_data) is 14:
            self._disk[self._DEVICE_MAJOR] = _data[0]
            self._disk[self._DEVICE_MINOR] = _data[1]
            self._disk[self._DEVICE_NAME] = _data[2]
            self._disk[self._READ_COMPLETED] = _data[3]
            self._disk[self._READ_MERGED] = _data[4]
            self._disk[self._READ_SECTORS] = _data[5]
            self._disk[self._READ_TIME] = _data[6]
            self._disk[self._WRITE_COMPLETED] = _data[7]
            self._disk[self._WRITE_MERGED] = _data[8]
            self._disk[self._WRITE_SECTORS] = _data[9]
            self._disk[self._WRITE_TIME] = _data[10]
            self._disk[self._IO_IN_PROGRESS] = _data[11]
            self._disk[self._IO_TIME] = _data[12]
            self._disk[self._IO_TIME_WEIGHTED] = _data[13]

    # @property
    def get_device_major(self) -> str:
        return self._get_value(self._DEVICE_MAJOR)

    # @property
    def get_device_minor(self) -> str:
        return self._get_value(self._DEVICE_MINOR)

    # @property
    def get_device_name(self) -> str:
        return self._get_value(self._DEVICE_NAME)

    # @property
    def get_read_completed(self) -> str:
        return self._get_value(self._READ_COMPLETED)

    # @property
    def get_read_merged(self) -> str:
        return self._get_value(self._READ_MERGED)

    # @property
    def get_read_sectors(self) -> str:
        return self._get_value(self._READ_SECTORS)

    # @property
    def get_read_time(self) -> str:
        return self._get_value(self._READ_TIME)

    # @property
    def get_write_completed(self) -> str:
        return self._get_value(self._WRITE_COMPLETED)

    # @property
    def get_write_merged(self) -> str:
        return self._get_value(self._WRITE_MERGED)

    # @property
    def get_write_sectors(self) -> str:
        return self._get_value(self._WRITE_SECTORS)

    # @property
    def get_write_time(self) -> str:
        return self._get_value(self._WRITE_TIME)

    # @property
    def get_io_in_progress(self) -> str:
        return self._get_value(self._IO_IN_PROGRESS)

    # @property
    def get_io_time(self) -> str:
        return self._get_value(self._IO_TIME)

    # @property
    def get_io_time_weighted(self) -> str:
        return self._get_value(self._IO_TIME_WEIGHTED)

    def _get_value(self, item: str) -> typing.Optional[str]:
        try:
            return self._disk[item]
        except KeyError:
            return None


class DiskStats(AbstractRead):
    def __init__(self) -> None:
        super().__init__()

    def load(self):
        self._data = dict()

        _path = os.path.join(self._PROC_PATH, "diskstats")
        _file_read = self._read(_path)

        if _file_read is not None:
            for _line in _file_read.splitlines():
                _disk_stat = DiskStat(_line)

                self._data[_disk_stat.get_device_name()] = _disk_stat

    def get_disks(self) -> typing.List[str]:
        if self._data is None:
            self.load()

        return self._data.keys()

    def get_disk(self, name: str) -> DiskStat:
        if self._data is None:
            self.load()

        return self._data[name]

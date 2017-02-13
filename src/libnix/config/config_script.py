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
import subprocess
import tempfile
import typing


class ConfigScript:
    SCRIPT_NAME = "name"
    SCRIPT_DESCRIPTION = "description"
    SCRIPT_STATUS = "status"
    SCRIPT_CODE = "code"
    SCRIPT_TAG = "tag"

    STATUS_NORMAL = 0
    STATUS_COMPILE_ERROR = 1
    STATUS_RUNTIME_ERROR = 2

    def __init__(self):
        self._script = {self.SCRIPT_NAME: "",
                        self.SCRIPT_DESCRIPTION: "",
                        self.SCRIPT_STATUS: 0,
                        self.SCRIPT_CODE: "",
                        self.SCRIPT_TAG: []}

        self._path_temp = None

    def set_name(self, name: str):
        self._script[self.SCRIPT_NAME] = name

    def get_name(self) -> str:
        return self._script[self.SCRIPT_NAME]

    def set_desc(self, description: str):
        self._script[self.SCRIPT_DESCRIPTION] = description

    def get_desc(self) -> str:
        return self._script[self.SCRIPT_DESCRIPTION]

    def set_status(self, status: int):
        self._script[self.SCRIPT_STATUS] = status

    def get_status(self) -> int:
        return self._script[self.SCRIPT_STATUS]

    def set_code(self, code: str):
        self._script[self.SCRIPT_CODE] = code

    def get_code(self) -> str:
        return self._script[self.SCRIPT_CODE]

    def get_tags(self) -> typing.List[str]:
        return self._script[self.SCRIPT_TAG]

    def add_tags(self, tags: typing.List[str]):
        for _tag in tags:
            self.add_tag(_tag)

    def add_tag(self, tag: str):
        self._script[self.SCRIPT_TAG].append(tag)

    def delete_tags(self, tags: typing.List[str]):
        for _tag in tags:
            self._script[self.SCRIPT_TAG].remove(_tag)

    def delete_tag(self, tag: str):
        self._script[self.SCRIPT_TAG].remove(tag)

    def make_temp(self, contents: str):
        (_fd, _path) = tempfile.mkstemp()
        _fp = os.fdopen(_fd, 'w')
        _fp.write(contents)
        _fp.close()

        self._path_temp = _path

    def call_editor(self):
        editor = os.getenv('EDITOR', 'vi')

        subprocess.call('%s %s' % (editor, self._path_temp), shell=True)

    def read_temp_file(self) -> str:
        with open(self._path_temp, 'r') as f:
            _contents = f.read()

        os.unlink(self._path_temp)

        self._path_temp = None

        return _contents

    def is_compile(self) -> bool:
        try:
            _success = True
            compile(self.get_code(), self.get_name(), 'exec')
        except SyntaxError as e:
            _success = False
            # print("Syntax Error: {}".format(e))
            print("Syntax Error - filename: {}".format(e.filename))
            print("Syntax Error - line: {}".format(e.lineno))
            print("Syntax Error - msg: {}".format(e.msg))
            print("Syntax Error - offset: {}".format(e.offset))
            print("Syntax Error - text: {}".format(e.text))

        return _success

    def export_data(self) -> typing.Dict[str, typing.Union[str, int, typing.List[str]]]:
        return self._script

    def import_data(self, _data: dict):
        self._script[self.SCRIPT_NAME] = _data[self.SCRIPT_NAME]
        self._script[self.SCRIPT_DESCRIPTION] = _data[self.SCRIPT_DESCRIPTION]
        self._script[self.SCRIPT_STATUS] = _data[self.SCRIPT_STATUS]
        self._script[self.SCRIPT_CODE] = _data[self.SCRIPT_CODE]
        self._script[self.SCRIPT_TAG] = _data[self.SCRIPT_TAG]

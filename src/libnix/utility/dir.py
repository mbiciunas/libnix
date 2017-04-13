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


class Dir:
    _FOLDER_NIX = ".nix"
    _FOLDER_META = "meta"
    _FOLDER_SCRIPT = "script"

    _FILE_MANIFEST = "manifest.json"
    _FILE_META = "meta.json"

    _FILE_TAG = "tag.json"

    def __init__(self) -> None:
        pass

    @staticmethod
    def get_home() -> str:
        return os.path.expanduser('~')

    @staticmethod
    def get_nix() -> str:
        return os.path.join(Dir.get_home(), Dir._FOLDER_NIX)

    @staticmethod
    def get_dir_service(service: str) -> str:
        return os.path.join(Dir.get_nix(), service)

    @staticmethod
    def get_service(service: str) -> str:
        _path = Dir.get_dir_service(service)

        if not os.path.exists(_path):
            os.makedirs(_path, exist_ok=True)

        return os.path.join(_path, Dir._FILE_MANIFEST)

    @staticmethod
    def get_dir_script() -> str:
        return os.path.join(Dir.get_nix(), Dir._FOLDER_SCRIPT)

    @staticmethod
    def get_script(script: str) -> str:
        _path = Dir.get_dir_script()

        if not os.path.exists(_path):
            os.makedirs(_path, exist_ok=True)

        return os.path.join(_path, script)

    @staticmethod
    def get_script_tag() -> str:
        _path = Dir.get_dir_script()

        if not os.path.exists(_path):
            os.makedirs(_path, exist_ok=True)

        return os.path.join(_path, Dir._FILE_TAG)

    @staticmethod
    def get_meta(service: str) -> str:
        _path = os.path.join(Dir.get_dir_service(service), Dir._FOLDER_META)

        if not os.path.exists(_path):
            os.makedirs(_path, exist_ok=True)

        return os.path.join(_path, Dir._FILE_META)

    @staticmethod
    def isfile(path) -> bool:
        return os.path.isfile(path)

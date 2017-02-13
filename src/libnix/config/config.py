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

import json

from libnix.config.config_scripts import ConfigScripts
from libnix.config.config_tags import ConfigTags
from libnix.utility.dir import Dir


class Config:
    CONFIG_TAG = "tag"
    CONFIG_SCRIPT = "script"

    def __init__(self):
        self._data = {self.CONFIG_TAG: ConfigTags(),
                      self.CONFIG_SCRIPT: ConfigScripts()}

        with open(Dir.get_script_tag(), 'r') as infile:
            _import = json.load(infile)

        self._data[self.CONFIG_TAG].import_data(_import[self.CONFIG_TAG])
        self._data[self.CONFIG_SCRIPT].import_data(_import[self.CONFIG_SCRIPT])

    def get_tags(self) -> ConfigTags:
        return self._data[self.CONFIG_TAG]

    def get_scripts(self) -> ConfigScripts:
        return self._data[self.CONFIG_SCRIPT]

    def write(self):
        _export = {self.CONFIG_TAG: self.get_tags().export_data(),
                   self.CONFIG_SCRIPT: self.get_scripts().export_data()}

        with open(Dir.get_script_tag(), 'w') as outfile:
            json.dump(_export, outfile, sort_keys=False, indent=2)

    # def _read(self):
    #     with open(Dir.get_script_tag(), 'r') as infile:
    #         _import = json.load(infile)
    #
    #     self._data[self.CONFIG_TAG].import_data(_import[self.CONFIG_TAG])
    #     self._data[self.CONFIG_SCRIPT].import_data(_import[self.CONFIG_SCRIPT])


def main():
    _code = "from libnix1.process.processes import Processes\n"
    _code += "from libnix1.utility.print_table import PrintTable\n"
    _code += "\n"
    _code += "_processes = Processes()\n"

    _config = Config()
    _tags = _config.get_tags()
    _scripts = _config.get_scripts()

    new_tag(_tags, "tag1", "This is tag 1")
    new_tag(_tags, "tag2", "This is tag 2")
    # new_tag(_tags, "tag3", "This is tag 3")

    print_tags(_tags)

    new_script(_scripts, "script1", "This is script 1", 0, _code, ["tag1", "tag2"])
    new_script(_scripts, "script2", "This is script 2", 2, _code, ["tag1", "tag2"])

    print_scripts(_scripts)

    _config.write()

    # Build config from read data
    _config_read = Config()
    _tags_read = _config_read.get_tags()
    _scripts_read = _config_read.get_scripts()

    print_tags(_tags_read)

    print_scripts(_scripts_read)


def new_tag(tags, name, desc):
    _tag = tags.insert()
    _tag.set_name(name)
    _tag.set_desc(desc)


def new_script(scripts, name, desc, status, code, tags):
    _script = scripts.insert()
    _script.set_name(name)
    _script.set_desc(desc)
    _script.set_status(status)
    _script.set_code(code)

    for _tag in tags:
        _script.add_tag(_tag)


def print_tags(tags):
    print("Print_tags:")

    for _name in tags.list():
        _tag = tags.find(_name)
        print("tag: {} - {}".format(_tag.get_name(), _tag.get_desc()))

    print()


def print_scripts(scripts: ConfigScripts):
    print("Print_scripts:")

    for _name in scripts.list():
        _script = scripts.find_by_name(_name)
        print("script: {} - {} - {}".format(_script.get_name(), _script.get_desc(), _script.get_status()))
        print("{}".format(_script.get_code()))
        print("=====================")
    print()

if __name__ == "__main__":
    main()

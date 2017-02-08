"""
LibNix
Copyright (C) 2017  Mark Biciunas

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from libnix.config.config import Config


class RunScript:
    def __init__(self):
        self._config = Config()

    def run(self, name: str):
        _script = self._config.get_scripts().find_by_name(name)

        try:
            code = compile(_script.get_code(), name, 'exec')
            exec(code)
        except SyntaxError as e:
            # print("Syntax Error: {}".format(e))
            print("Syntax Error - filename: {}".format(e.filename))
            print("Syntax Error - line: {}".format(e.lineno))
            print("Syntax Error - msg: {}".format(e.msg))
            print("Syntax Error - offset: {}".format(e.offset))
            print("Syntax Error - text: {}".format(e.text))
        except NameError as e:
            for _arg in e.args:
                print("Syntax Error - args: {}".format(_arg))

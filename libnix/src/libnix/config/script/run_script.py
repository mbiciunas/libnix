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

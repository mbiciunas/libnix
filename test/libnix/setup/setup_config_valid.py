from libnix.config.config import Config
from .make_json import MakeJson


class SetupConfigValid:
    TAG_VALID_1 = "tag1"
    TAG_VALID_2 = "tag2"
    TAG_VALID_3 = "tag3"
    TAG_INVALID_1 = "bad_tag_1"
    TAG_INVALID_2 = "bad_tag_2"

    TAG_VALID_DESC_1 = "This is tag 1"
    TAG_VALID_DESC_2 = "This is tag 2"
    TAG_VALID_DESC_3 = "This is tag 3"

    TAG_VALID_LIST = [TAG_VALID_1, TAG_VALID_2]
    TAG_INVALID_LIST = [TAG_INVALID_1, TAG_INVALID_2]
    TAG_MIX_LIST = [TAG_INVALID_1, TAG_VALID_1, TAG_INVALID_2, TAG_VALID_2]

    TAG_INVALID_DESC_1 = "Bad description for tag 1"
    TAG_INVALID_DESC_2 = "Bad description for tag 2"
    TAG_INVALID_DESC_3 = "Bad description for tag 3"

    SCRIPT_VALID_1 = "script1"
    SCRIPT_VALID_2 = "script2"
    SCRIPT_VALID_3 = "script3"

    SCRIPT_VALID_DESC_1 = "This is script 1"
    SCRIPT_VALID_DESC_2 = "This is script 2"
    SCRIPT_VALID_DESC_3 = "This is script 3"

    SCRIPT_VALID_STATUS_1 = 0
    SCRIPT_VALID_STATUS_2 = 1
    SCRIPT_VALID_STATUS_3 = 2

    SCRIPT_VALID_CODE_1 = "print('This is code 1')"
    SCRIPT_VALID_CODE_2 = "print('This is code 2')"
    SCRIPT_VALID_CODE_3 = "print('This is code 3')"

    SCRIPT_VALID_TAGS_1 = ["tag1", "tag2"]
    SCRIPT_VALID_TAGS_2 = ["tag1"]
    SCRIPT_VALID_TAGS_3 = ["tag2"]

    SCRIPT_INVALID_1 = "bad_script_1"
    SCRIPT_INVALID_2 = "bad_script_2"

    SCRIPT_INVALID_STATUS = 4

    SCRIPT_INVALID_DESC = "Bad description for script 1"

    SCRIPT_INVALID_CODE = "Bad print('This is code 1')"

    SCRIPT_INVALID_TAGS = ["bad_tag1", "bad_tag2"]

    SCRIPT_INVALID_TAG = "bad_tag1"

    SCRIPT_VALID_LIST = [SCRIPT_VALID_1, SCRIPT_VALID_2]
    SCRIPT_INVALID_LIST = [SCRIPT_INVALID_1, SCRIPT_INVALID_2]
    SCRIPT_MIX_LIST = [SCRIPT_INVALID_1, SCRIPT_VALID_1, SCRIPT_INVALID_2, SCRIPT_VALID_2]

    _PATH_DST = "/home/mbiciunas/.nix/script/tag.json"

    _config = None
    _count_tags = None
    _count_scripts = None

    def __init__(self):
        with open(self._PATH_DST, "w") as text_file:
            text_file.write(self._make_json())

        self._config = Config()

    def config(self):
        return self._config

    def set_count_tags(self, count: int):
        self._count_tags = count

    def get_count_tags(self) -> int:
        return self._count_tags

    def set_count_scripts(self, count: int):
        self._count_scripts = count

    def get_count_scripts(self) -> int:
        return self._count_scripts

    def _make_json(self) -> str:
        _make_json = MakeJson()
        _make_json.add_script(self.SCRIPT_VALID_1, self.SCRIPT_VALID_DESC_1, self.SCRIPT_VALID_CODE_1,
                              self.SCRIPT_VALID_STATUS_1, self.SCRIPT_VALID_TAGS_1)
        _make_json.add_script(self.SCRIPT_VALID_2, self.SCRIPT_VALID_DESC_2, self.SCRIPT_VALID_CODE_2,
                              self.SCRIPT_VALID_STATUS_2, self.SCRIPT_VALID_TAGS_2)
        _make_json.add_script(self.SCRIPT_VALID_3, self.SCRIPT_VALID_DESC_3, self.SCRIPT_VALID_CODE_3,
                              self.SCRIPT_VALID_STATUS_3, self.SCRIPT_VALID_TAGS_3)
        _make_json.add_tag(self.TAG_VALID_1, self.TAG_VALID_DESC_1)
        _make_json.add_tag(self.TAG_VALID_2, self.TAG_VALID_DESC_2)
        _make_json.add_tag(self.TAG_VALID_3, self.TAG_VALID_DESC_3)

        _json = _make_json.make()

        return _json

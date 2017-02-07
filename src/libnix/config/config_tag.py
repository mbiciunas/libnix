import typing


class ConfigTag:
    TAG_NAME = "name"
    TAG_DESCRIPTION = "description"

    def __init__(self):
        self._tag = {self.TAG_NAME: "", self.TAG_DESCRIPTION: ""}

    def set_name(self, name: str):
        self._tag[self.TAG_NAME] = name

    def get_name(self) -> str:
        return self._tag[self.TAG_NAME]

    def set_desc(self, description: str):
        self._tag[self.TAG_DESCRIPTION] = description

    def get_desc(self) -> str:
        return self._tag[self.TAG_DESCRIPTION]

    def export_data(self) -> typing.Dict[str, str]:
        return self._tag

    def import_data(self, _data: dict):
        self._tag[self.TAG_NAME] = _data[self.TAG_NAME]
        self._tag[self.TAG_DESCRIPTION] = _data[self.TAG_DESCRIPTION]

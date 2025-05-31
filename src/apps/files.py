from apps.base import BaseApp

from bookmarks.types import FILE, FOLDER


class FilesApp(BaseApp):
    def __init__(self):
        super().__init__("files")

    def add(self, type: str, name: str, arg: str):
        if type == FILE:
            return self.add_file(name, arg)

        if type == FOLDER:
            return self.add_folder(name, arg)

        raise ValueError(f"{type} is not supported for {self.name}")

    def add_file(self, name: str, arg: str):
        if not arg.startswith("file://"):
            arg = f"file://{arg}"

        print(f"Adding {name}:{arg} to {self.name}")

    def add_folder(self, name: str, arg: str):
        if not arg.startswith("file://"):
            arg = f"file://{arg}"

        print(f"Adding {name}:{arg} to {self.name}")

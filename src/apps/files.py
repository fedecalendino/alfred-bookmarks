from apps.base import BaseApp
from bookmarks.base import Bookmark

from bookmarks.types import FILE, FOLDER


class FilesApp(BaseApp):
    def __init__(self):
        super().__init__("files")

    def add(self, type: str, name: str, arg: str) -> Bookmark:
        if type == FILE:
            return self.add_file(name, arg)

        if type == FOLDER:
            return self.add_folder(name, arg)

        raise ValueError(f"{type} is not supported for {self.name}")

    def add_file(self, name: str, arg: str) -> Bookmark:
        if not arg.startswith("file://"):
            arg = f"file://{arg}"

        return Bookmark(
            app=self.name,
            type=FILE,
            emoji="📄",
            name=name,
            location=arg,
        )

    def add_folder(self, name: str, arg: str) -> Bookmark:
        if not arg.startswith("file://"):
            arg = f"file://{arg}"

        return Bookmark(
            app=self.name,
            type=FOLDER,
            emoji="📁",
            name=name,
            location=arg,
        )

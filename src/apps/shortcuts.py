from apps.base import BaseApp
from bookmarks.base import Bookmark
from bookmarks.types import SHORTCUT


class ShortcutsApp(BaseApp):
    def __init__(self):
        super().__init__("shortcuts")

    def add(self, type: str, name: str, arg: str) -> Bookmark:
        if type == SHORTCUT:
            return self.add_shortcut(name, arg)

        raise ValueError(f"{type} is not supported for {self.name}")

    def add_shortcut(self, name: str, arg: str) -> Bookmark:
        arg = f"shortcuts://run-shortcut?name={arg}".replace(" ", "%20")

        return Bookmark(
            app=self.name,
            type=SHORTCUT,
            emoji="🌀",
            name=name,
            location=arg,
        )

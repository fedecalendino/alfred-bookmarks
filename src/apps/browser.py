from apps.base import BaseApp
from bookmarks.base import Bookmark

from bookmarks.types import WEBSITE


class BrowserApp(BaseApp):
    def __init__(self):
        super().__init__("browser")

    def add(self, type: str, name: str, arg: str) -> Bookmark:
        if type == WEBSITE:
            return self.add_website(name, arg)

        raise ValueError(f"{type} is not supported for {self.name}")

    def add_website(self, name: str, arg: str) -> Bookmark:
        if not arg.startswith("http"):
            arg = f"https://{arg}"

        return Bookmark(
            app=self.name,
            type=WEBSITE,
            emoji="🌐",
            name=name,
            location=arg,
        )

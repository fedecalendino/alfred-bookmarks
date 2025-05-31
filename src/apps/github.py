from apps.base import BaseApp
from bookmarks.base import Bookmark

from bookmarks.types import REPOSITORY


class GithubApp(BaseApp):
    def __init__(self):
        super().__init__("github")

    def add(self, type: str, name: str, arg: str) -> Bookmark:
        if type == REPOSITORY:
            return self.add_repository(name, arg)

        raise ValueError(f"{type} is not supported for {self.name}")

    def add_repository(self, name: str, arg: str) -> Bookmark:
        arg = f"https://github.com/{arg}"

        return Bookmark(
            app=self.name,
            type=REPOSITORY,
            emoji="🐙",
            name=name,
            location=arg,
        )

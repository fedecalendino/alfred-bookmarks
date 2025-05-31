from apps.base import BaseApp
from bookmarks.base import Bookmark
from bookmarks.types import CHANNEL


class YoutubeApp(BaseApp):
    def __init__(self):
        super().__init__("youtube")

    def add(self, type: str, name: str, arg: str) -> Bookmark:
        if type == CHANNEL:
            return self.add_channel(name, arg)

        raise ValueError(f"{type} is not supported for {self.name}")

    def add_channel(self, name: str, arg: str) -> Bookmark:
        arg = f"https://youtube.com/@{arg}/streams"

        return Bookmark(
            app=self.name,
            type=CHANNEL,
            emoji="📺",
            name=name,
            location=arg,
        )

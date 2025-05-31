from apps.base import BaseApp
from bookmarks.types import CHANNEL


class YoutubeApp(BaseApp):
    def __init__(self):
        super().__init__("youtube")

    def add(self, type: str, name: str, arg: str):
        if type == CHANNEL:
            return self.add_channel(name, arg)

        raise ValueError(f"{type} is not supported for {self.name}")

    def add_channel(self, name: str, arg: str):
        arg = f"https://youtube.com/@{arg}/streams"

        print(f"Adding {name}:{arg} to {self.name}")

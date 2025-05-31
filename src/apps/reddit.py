from apps.base import BaseApp
from bookmarks.types import SUBREDDIT


class RedditApp(BaseApp):
    def __init__(self):
        super().__init__("reddit")

    def add(self, type: str, name: str, arg: str):
        if type == SUBREDDIT:
            return self.add_subreddit(name, arg)

        raise ValueError(f"{type} is not supported for {self.name}")

    def add_subreddit(self, name: str, arg: str):
        arg = f"https://reddit.com/r/{arg}"

        print(f"Adding {name}:{arg} to {self.name}")

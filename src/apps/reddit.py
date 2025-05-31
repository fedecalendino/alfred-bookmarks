from apps.base import BaseApp
from bookmarks.base import Bookmark
from bookmarks.types import SUBREDDIT


class RedditApp(BaseApp):
    def __init__(self):
        super().__init__("reddit")

    def add(self, type: str, name: str, arg: str) -> Bookmark:
        if type == SUBREDDIT:
            return self.add_subreddit(name, arg)

        raise ValueError(f"{type} is not supported for {self.name}")

    def add_subreddit(self, name: str, arg: str) -> Bookmark:
        arg = f"https://reddit.com/r/{arg}"

        return Bookmark(
            app=self.name,
            type=SUBREDDIT,
            emoji="👽",
            name=name,
            location=arg,
        )

from uuid import uuid4


class Bookmark:
    def __init__(
        self,
        app: str,
        name: str,
        type: str,
        emoji: str,
        location: str,
        id: str = None,
        enabled: bool = False,
    ):
        self.id: str = id or str(uuid4())

        self.app: str = app
        self.type: str = type
        self.name: str = name
        self.emoji: str = emoji
        self.location: str = location
        self.enabled: bool = enabled

    @property
    def icon(self) -> str:
        return f"./img/{self.app}.png"

    def __repr__(self) -> str:
        return f"{self.emoji} {self.name} ({self.location})"

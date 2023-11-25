class Bookmark:
    def __init__(self, id: str, name: str, location: str, type_: str):
        self.id: str = id
        self.name: str = name
        self.location: str = location
        self.type: str = type_

    def __repr__(self):
        return f"{self.name} ({self.location}) [{self.type}]"

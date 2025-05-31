class BaseApp:
    def __init__(self, name: str):
        self.name: str = name

    def add(self, type: str, name: str, arg: str):
        raise NotImplementedError()

    def __repr__(self) -> str:
        return self.name

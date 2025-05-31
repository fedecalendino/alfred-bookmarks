class BaseApp:
    def __init__(self, name: str):
        self.name: str = name

    @property
    def image(self) -> str:
        return f"./img/{self.name}.png"

    def add(self, type: str, name: str, arg: str):
        raise NotImplementedError()

    def __repr__(self) -> str:
        return self.name

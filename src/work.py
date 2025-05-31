from apps import APPS


SEPARATOR = " || "


def parse(args: list[str]) -> tuple[str, str, str, str]:
    if len(args) != 3:
        raise ValueError(f"Missing parameters: [name]{SEPARATOR}[location]")

    app = args[0]
    type = args[1]

    split = args[2].split(SEPARATOR)

    if len(split) == 1:
        name, arg = split[0], split[0]
    elif len(split) == 2:
        name, arg = split[0], split[1]
    else:
        raise ValueError(f"Invalid format: {args[2]}")

    return app.strip(), type.strip(), name.strip(), arg.strip()


def process(args: list[str]):
    app, type, name, arg = parse(args)
    app = APPS.get(app)

    if app is None:
        raise ValueError(f"Unknown app name '{app}'")

    return app.add(type, name, arg)

from typing import Tuple

from pyflow import Workflow

SEPARATOR = " || "


def bookmark_args(workflow: Workflow) -> Tuple[str, str, str]:
    try:
        split = " ".join(workflow.args).split(SEPARATOR)

        if len(split) == 2:
            name, location, type_ = split[0], split[0], split[1]
        elif len(split) == 3:
            name, location, type_ = split[0], split[1], split[2]
        else:
            raise ValueError(f"Missing parameters: [name]{SEPARATOR}[location]")

        return name, location, type_
    except:
        raise ValueError(f"Missing parameters: [name]{SEPARATOR}[location]")

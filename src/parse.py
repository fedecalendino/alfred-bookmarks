from typing import Tuple

from pyflow import Workflow


def bookmark_args(workflow: Workflow) -> Tuple[str, str, str]:
    try:
        name, location, type_ = " ".join(workflow.args).split(" / ")

        return name, location, type_
    except:
        raise ValueError(f"Missing parameters: [name] / [location]")

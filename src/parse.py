from typing import Tuple

from pyflow import Workflow


def bookmark_args(workflow: Workflow) -> Tuple[str, str, str]:
    try:
        return " ".join(workflow.args).split(" / ")
    except:
        raise ValueError(f"Missing parameters: [name] / [location] / [type]")

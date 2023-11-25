import sys

from pyflow import Workflow

from db import DB


def main(workflow: Workflow):
    if len(workflow.args) != 1:
        raise ValueError("Missing parameters: [id]")

    db = DB(workflow)

    id = workflow.args[0]
    db.remove_bookmark(id)


if __name__ == "__main__":
    wf = Workflow()
    wf.run(main)
    wf.send_feedback()
    sys.exit()

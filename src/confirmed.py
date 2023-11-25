import sys

from pyflow import Workflow

import parse
from db import DB


def main(workflow: Workflow):
    name, location, type_ = parse.bookmark_args(workflow)

    db = DB(workflow)
    db.add_bookmark(name, location, type_)


if __name__ == "__main__":
    wf = Workflow()
    wf.run(main)
    wf.send_feedback()
    sys.exit()

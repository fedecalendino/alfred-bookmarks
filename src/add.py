import sys

from pyflow import Workflow

import work
from database import DB


def main(workflow: Workflow):
    db = DB(workflow)

    bookmark = work.process(workflow.args)

    db.save_bookmark(bookmark)

    workflow.new_item(
        title='Do you want to bookmark "{name}"?'.format(
            name=bookmark.name,
        ),
        subtitle=bookmark.location,
        arg=bookmark.id,
        uid=bookmark.id,
        valid=True,
    ).set_icon_file(
        path=bookmark.icon,
    )


if __name__ == "__main__":
    wf = Workflow()
    wf.run(main)
    wf.send_feedback()
    sys.exit()

import sys

from pyflow import Workflow

import work


def main(workflow: Workflow):
    bookmark = work.process(workflow.args)

    workflow.new_item(
        title='Do you want to bookmark "{name}"?'.format(
            name=bookmark.name,
        ),
        subtitle=bookmark.location,
        arg="{app} {type} '{arg}'".format(
            app=bookmark.app.name,
            type=bookmark.type,
            arg=bookmark.arg,
        ),
        valid=True,
    ).set_icon_file(
        path=bookmark.app.image,
    )


if __name__ == "__main__":
    wf = Workflow()
    wf.run(main)
    wf.send_feedback()
    sys.exit()

import sys

from pyflow import Workflow

from database import DB


def main(workflow: Workflow):
    db = DB(workflow)
    db.clean()

    bookmarks = list(db.list_bookmarks())

    if not bookmarks:
        return workflow.new_item(
            title="No bookmarks found...",
            valid=False,
        )

    for bookmark in bookmarks:
        workflow.new_item(
            title=f"{bookmark.emoji} {bookmark.name}",
            subtitle=bookmark.location,
            arg=f"open {bookmark.location}",
            copytext=bookmark.location,
            uid=bookmark.id,
            valid=True,
        ).set_alt_mod(
            arg=f"remove {bookmark.id}",
            subtitle=f"remove {bookmark.name}?",
        ).set_cmd_mod(
            arg=f"remove {bookmark.id}",
            subtitle=f"remove {bookmark.name}?",
        ).set_icon_file(
            path=bookmark.icon,
        )


if __name__ == "__main__":
    wf = Workflow()
    wf.run(main)
    wf.send_feedback()
    sys.exit()

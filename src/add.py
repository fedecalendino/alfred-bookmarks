import sys

from pyflow import Workflow

import parse
from constants import (
    WEBSITE,
    FILE,
    FOLDER,
    YOUTUBE_CHANNEL,
    YOUTUBE_STREAM,
    REDDIT_SUBREDDIT,
    GITHUB_REPOSITORY,
)


def format_bookmark(name: str, location: str, type_: str) -> str:
    name = name.strip()
    location = location.strip()
    type_ = type_.strip()

    if type_ == WEBSITE:
        if not location.startswith("http"):
            location = f"https://{location}"
    elif type_ in (FILE, FOLDER):
        if not location.startswith("file://"):
            location = f"file://{location}"
    elif type_ == YOUTUBE_CHANNEL:
        location = f"https://youtube.com/@{location}/streams"
    elif type_ == YOUTUBE_STREAM:
        location = f"https://youtube.com/watch?v={location}"
    elif type_ == REDDIT_SUBREDDIT:
        name = f"/r/{name}"
        location = f"https://reddit.com/r/{location}"
    elif type_ == GITHUB_REPOSITORY:
        name = f"{name}"
        location = f"https://github.com/{location}"

    return name, location, type_


def main(workflow: Workflow):
    name, location, type_ = parse.bookmark_args(workflow)
    name, location, type_ = format_bookmark(name, location, type_)

    workflow.new_item(
        title="Do you want to bookmark `{name}`?".format(
            name=name,
        ),
        subtitle=location,
        arg=f"{name} / {location} / {type_}",
        valid=True,
    ).set_icon_file(
        path=f"./img/types/{type_}.png",
    )


if __name__ == "__main__":
    wf = Workflow()
    wf.run(main)
    wf.send_feedback()
    sys.exit()

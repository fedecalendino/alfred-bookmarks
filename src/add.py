import sys

from pyflow import Workflow

import parse
import constants


def format_name(name: str) -> str:
    return name.strip()


def format_type(type_: str) -> str:
    return type_.strip()


def format_location(location: str, type_: str) -> str:
    location = location.strip()

    if type_ == constants.WEBSITE:
        if not location.startswith("http"):
            location = f"https://{location}"
    elif type_ in (constants.FILE, constants.FOLDER):
        if not location.startswith("file://"):
            location = f"file://{location}"
    elif type_ == constants.YOUTUBE_CHANNEL:
        location = f"https://www.youtube.com/@{location}/streams"
    elif type_ == constants.YOUTUBE_STREAM:
        location = f"https://www.youtube.com/watch?v={location}"
    elif type_ == constants.SUBREDDIT:
        location = f"https://www.reddit.com/r/{location}"

    return location


def main(workflow: Workflow):
    name, location, type_ = parse.bookmark_args(workflow)

    name = format_name(name)
    type_ = format_type(type_)
    location = format_location(location, type_)

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

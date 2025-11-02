from apps.base import BaseApp
from .browser import BrowserApp
from .files import FilesApp
from .github import GithubApp
from .reddit import RedditApp
from .shortcuts import ShortcutsApp
from .youtube import YoutubeApp

APPS = {}

for App in BaseApp.__subclasses__():
    app = App()
    APPS[app.name] = app

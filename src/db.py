import sqlite3
from typing import Iterable
from uuid import uuid4

from pyflow import Workflow

from classes import Bookmark
from migrations import migrations


class DB:
    def __init__(self, workflow: Workflow):
        self.workflow: Workflow = workflow
        self.path: str = f"{self.workflow.cache.cachedir}/bookmarks.db"

        self.init()
        self.migrate()

    @property
    def conn(self):
        return sqlite3.connect(self.path)

    def init(self):
        with self.conn as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS migrations (
                    name VARCHAR(255) NOT NULL,
                    version INTEGER NOT NULL,
                    
                    PRIMARY KEY (name)
                )
                """
            )

    def migrate(self):
        with self.conn as conn:
            for version, (name, sql) in enumerate(migrations):
                res = conn.execute(
                    f"SELECT * FROM migrations WHERE version = ?",
                    (version,),
                )

                if res.fetchone():
                    continue

                conn.execute(sql)
                conn.execute(
                    f"INSERT INTO migrations VALUES(?, ?)",
                    (name, version),
                )

    def list_bookmarks(self) -> Iterable[Bookmark]:
        with self.conn as conn:
            res = conn.execute(f"SELECT * FROM bookmarks ORDER BY name")

            for item in res:
                yield Bookmark(*item)

    def add_bookmark(self, name: str, location: str, type_: str) -> Bookmark:
        with self.conn as conn:
            id = str(uuid4())
            conn.execute(
                "INSERT INTO bookmarks VALUES (?, ?, ?, ?)",
                (id, name, location, type_),
            )

        return Bookmark(id, name, location, type_)

    def remove_bookmark(self, id: str):
        with self.conn as conn:
            conn.execute(
                "DELETE FROM bookmarks WHERE id = ?",
                (id,),
            )

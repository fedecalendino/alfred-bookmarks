import sqlite3
from typing import Iterable

from pyflow import Workflow

from bookmarks.base import Bookmark
from database.migrations import migrations


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

    def clean(self):
        query = "DELETE FROM bookmarks WHERE enabled = 0"

        with self.conn as conn:
            conn.execute(query)

    def list_bookmarks(self) -> Iterable[Bookmark]:
        query = f"SELECT * FROM bookmarks WHERE enabled = 1 ORDER BY name"

        with self.conn as conn:
            res = conn.execute(query)

            for item in res:
                yield Bookmark(
                    id=item[0],
                    app=item[1],
                    type=item[2],
                    emoji=item[3],
                    name=item[4],
                    location=item[5],
                    enabled=item[6],
                )

    def save_bookmark(self, bookmark: Bookmark):
        query = "INSERT INTO bookmarks VALUES (?, ?, ?, ?, ?, ?, ?)"
        params = (
            bookmark.id,
            bookmark.app,
            bookmark.type,
            bookmark.emoji,
            bookmark.name,
            bookmark.location,
            bookmark.enabled,
        )

        with self.conn as conn:
            conn.execute(query, params)

    def enable_bookmark(self, id: str):
        query = "UPDATE bookmarks SET enabled = 1 WHERE id = ?"
        params = (id,)

        with self.conn as conn:
            conn.execute(query, params)

    def remove_bookmark(self, id: str):
        query = "DELETE FROM bookmarks WHERE id = ?"
        params = (id,)

        with self.conn as conn:
            conn.execute(query, params)

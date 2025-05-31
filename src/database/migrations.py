v0 = """
CREATE TABLE bookmarks (
    id VARCHAR(36) NOT NULL UNIQUE,
    app VARCHAR(255) NOT NULL,
    type VARCHAR(50) NOT NULL,
    emoji VARCHAR(50) NOT NULL,
    name VARCHAR(255) NOT NULL,
    location VARCHAR(255) NOT NULL,
    enabled BOOLEAN NOT NULL DEFAULT FALSE,
    
    PRIMARY KEY (id)
);
"""


migrations = [
    ("create_bookmarks_table", v0),
]

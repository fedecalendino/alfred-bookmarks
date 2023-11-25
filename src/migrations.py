v0 = """
CREATE TABLE bookmarks (
    id VARCHAR(36) NOT NULL UNIQUE,
    name VARCHAR(255) NOT NULL,
    location VARCHAR(255) NOT NULL,
    
    PRIMARY KEY (id)
);
"""

v1 = """
    ALTER TABLE bookmarks 
    ADD COLUMN type VARCHAR(10) DEFAULT 'website';
"""


migrations = [
    ("create_bookmarks_table", v0),
    ("add_type_column", v1),
]

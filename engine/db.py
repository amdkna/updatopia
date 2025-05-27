# engine/db.py
import sqlite3

def init_db():
    conn = sqlite3.connect("updatopia.sqlite3")
    cursor = conn.cursor()
    # e.g. create a dummy table for testing
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

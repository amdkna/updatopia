# engine/db.py

import sqlite3
from engine.models import Player

DB_FILE = "updatopia.sqlite3"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS players (
            id          INTEGER PRIMARY KEY,
            name        TEXT    NOT NULL,
            dept_coins  INTEGER NOT NULL DEFAULT 0,
            dept_xp     INTEGER NOT NULL DEFAULT 0,
            n_coins     INTEGER NOT NULL DEFAULT 0,
            n_xp        INTEGER NOT NULL DEFAULT 0
        )
    """)
    # ensure a default player exists
    c.execute("INSERT OR IGNORE INTO players (id, name) VALUES (1, 'Player1')")
    conn.commit()
    conn.close()

def get_player() -> Player:
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    row = c.execute("SELECT id,name,dept_coins,dept_xp,n_coins,n_xp FROM players WHERE id = 1").fetchone()
    conn.close()
    return Player(*row)

def update_player(player: Player):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("""
        UPDATE players
           SET dept_coins = ?, dept_xp = ?, n_coins = ?, n_xp = ?
         WHERE id = ?
    """, (player.dept_coins, player.dept_xp, player.n_coins, player.n_xp, player.id))
    conn.commit()
    conn.close()

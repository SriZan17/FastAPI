# might have to make environment variable(remove quotes)
# CRYPTID_SQLITE_DB = "cryptid.db"

import os
from pathlib import Path
from sqlite3 import connect, Connection, Cursor, IntegrityError

conn: Connection | None = None
curs: Cursor | None = None


def get_db(name: str | None = None, reset: bool = False):
    global conn, curs
    if conn:
        if not reset:
            return
        conn.close()
        conn, curs = None, None
    if not name:
        name = os.getenv("CRYPTID_SQLITE_DB")
        top_dir = Path(__file__).resolve().parents[1]  # repo top
        db_dir = top_dir / "db"
        db_name = "cryptid.db"
        db_path = str(db_dir / db_name)
        name = os.getenv("CRYPTID_SQLITE_DB", db_path)

        # name = CRYPTID_SQLITE_DB
        # top_dir = Path(__file__).resolve().parents[1]
        # db_dir = top_dir / "db"
        # db_dir.mkdir(parents=True, exist_ok=True)
        # db_name = "cryptid.db"
        # db_path = str(db_dir / db_name)
        # name = db_path
    conn = connect(name, check_same_thread=False)
    curs = conn.cursor()


get_db()

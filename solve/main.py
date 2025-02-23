import sqlite3
import argparse
from pathlib import Path


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--db_path', '-d', default='./test/simple_bd/tutorial.db', help='path to data base', type=Path)

    args = parser.parse_args()

    print(args.db_path)

    con = sqlite3.connect(args.db_path)
    cur = con.cursor()

    res = cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = res.fetchone()

    schema = {}
    for table in tables:
        res = cur.execute(f"PRAGMA table_info({table});")
        schema[table] = res.fetchall()

    print(schema)



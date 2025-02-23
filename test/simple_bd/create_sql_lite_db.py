import sqlite3


if __name__ == '__main__':
    
    con = sqlite3.connect("tutorial.db")
    cur = con.cursor()

    # create tables
    try:
        cur.execute("CREATE TABLE movie(title, year, score)")
    except sqlite3.OperationalError as e:
        print(e)

    res = cur.execute("SELECT name FROM sqlite_master")
    res.fetchone()
    
    cur.execute("""
    INSERT INTO movie VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
    """)
    con.commit()
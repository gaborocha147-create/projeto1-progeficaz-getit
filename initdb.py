import sqlite3

con = sqlite3.connect('banco.db')
cur = con.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS note (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        content TEXT NOT NULL
    )
''')

con.commit()
con.close()
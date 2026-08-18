import sqlite3

con = sqlite3.connect('banco.db')
cur = con.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        detalhes TEXT NOT NULL
    )
''')

con.commit()
con.close()
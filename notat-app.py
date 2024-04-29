import sqlite3

conn = sqlite3.connect('notater.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS notater
             (id INTEGER PRIMARY KEY,
              tittel TEXT,
              innhold TEXT,
              tags TEXT)''')

def opprett_notat(tittel, innhold, tags):
    c.execute('''INSERT INTO notater (tittel, innhold, tags)
                 VALUES (?, ?, ?)''', (tittel, innhold, tags))
    conn.commit()

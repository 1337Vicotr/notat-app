import sqlite3

conn = sqlite3.connect('notater.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS notater
             (id INTEGER PRIMARY KEY,
              tittel TEXT,
              tekst TEXT,
              tags TEXT)''')

def lag_notat(tittel, tekst, tags):
    c.execute('''INSERT INTO notater (tittel, tekst, tags)
                 VALUES (?, ?, ?)''', (tittel, tekst, tags))
    conn.commit()

def vis_alle_notater():
    c.execute('''SELECT * FROM notater''')
    notater = c.fetchall()
    for note in notater:
        print("ID:", note[0])
        print("Tittel:", note[1])
        print("Tekst:", note[2])
        print("Tags:", note[3])
        print("")

def sok_notater(tittel):
    c.execute('''SELECT * FROM notater WHERE tittel LIKE ?''', ('%' + tittel + '%',))
    notater = c.fetchall()
    for note in notater:
        print("ID:", note[0])
        print("Tittel:", note[1])
        print("Tekst:", note[2])
        print("Tags:", note[3])
        print("")

def oppdater_notat(notat_id, ny_tittel, ny_tekst, nye_tags):
    c.execute('''UPDATE notater SET tittel = ?, tekst = ?, tags = ? WHERE id = ?''', (ny_tittel, ny_tekst, nye_tags, notat_id))
    conn.commit()

# lag_notat("Tittel test", "Tekst test", "testtag, testtag2")
# sok_notater("Tittel test")
oppdater_notat(1, "Tittel oppdatering test", "Hei og hopp din fluesopp", "test, eksempel, ny_tag")
vis_alle_notater()
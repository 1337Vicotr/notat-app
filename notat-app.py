import sqlite3
import json

conn = sqlite3.connect('notater.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS notater
             (id INTEGER PRIMARY KEY,
              tittel TEXT,
              tekst TEXT,
              tags TEXT)''')

def lag_notat(tittel, tekst, tags):
    c.execute('''INSERT INTO notater (tittel, tekst, tags)
                 VALUES (?, ?, ?)''', (tittel, tekst, json.dumps(tags)))
    conn.commit()

def vis_alle_notater():
    c.execute('''SELECT * FROM notater''')
    notater = c.fetchall()
    for note in notater:
        print("ID:", note[0])
        print("Tittel:", note[1])
        print("Tekst:", note[2])
        print("Tags:", note[3].split(', '))
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

def slett_notat(notat_id):
    c.execute('''DELETE FROM notater WHERE id = ?''', (notat_id,))
    conn.commit()

def eksporter_notater(filnavn):
    c.execute('''SELECT * FROM notater''')
    notater = c.fetchall()
    notater_dict = [{"id": note[0], "tittel": note[1], "tekst": note[2], "tags": note[3]} for note in notater]
    with open(filnavn, 'w') as f:
        json.dump(notater_dict, f)

def slett_alle_notes():
    c.execute('''DELETE FROM notater''')
    conn.commit()   

print("___________________")
print("")
lag_notat("Tittel test", "Tekst test", "testtag, testtag2")
lag_notat("Tittel test2", "Tekst test2", "testtag, testtag2")
vis_alle_notater()
print("___________________")
print("")

# sok_notater("Tittel test")
# oppdater_notat(1, "Tittel oppdatering test", "Hei og hopp din fluesopp", "test, ny_tag")
vis_alle_notater()
print("___________________")
print("")

print("")
vis_alle_notater()
print("___________________")
print("")

eksporter_notater("notater.json")
slett_alle_notes()
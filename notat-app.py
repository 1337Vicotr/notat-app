import sqlite3
import json
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

conn = sqlite3.connect('notater.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS notater
             (id INTEGER PRIMARY KEY,
              tittel TEXT,
              tekst TEXT,
              tags TEXT,
              opprettelses_tid TEXT,
              sist_endret TEXT)''')

def lag_notat():
    tittel = tittel_entry.get()
    tekst = tekst_entry.get("1.0", tk.END)
    tags = tags_entry.get()
    opprettelses_tid = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    sist_endret = opprettelses_tid
    c.execute('''INSERT INTO notater (tittel, tekst, tags, opprettelses_tid, sist_endret)
                 VALUES (?, ?, ?, ?, ?)''', (tittel, tekst, tags, opprettelses_tid, sist_endret))
    conn.commit()
    messagebox.showinfo("Notat lagt til", "Notat lagt til")
    vis_alle_notater()

def vis_alle_notater():
    notat_liste.delete(0, tk.END)
    c.execute('''SELECT * FROM notater''')
    notater = c.fetchall()
    for note in notater:
        notat_liste.insert(tk.END, note[1])  

root = tk.Tk()
root.title("Notat app")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

tittel_label = tk.Label(frame, text="Tittel:")
tittel_label.grid(row=0, column=0, sticky="w")
tittel_entry = tk.Entry(frame)
tittel_entry.grid(row=0, column=1, padx=5, pady=5)

tekst_label = tk.Label(frame, text="Tekst:")
tekst_label.grid(row=1, column=0, sticky="w")
tekst_entry = tk.Text(frame, height=4, width=30)
tekst_entry.grid(row=1, column=1, padx=5, pady=5)

tags_label = tk.Label(frame, text="Tags:")
tags_label.grid(row=2, column=0, sticky="w")
tags_entry = tk.Entry(frame)
tags_entry.grid(row=2, column=1, padx=5, pady=5)

legg_til_button = tk.Button(frame, text="Legg til notat", command=lag_notat)
legg_til_button.grid(row=3, columnspan=2, pady=10)

notat_liste = tk.Listbox(frame)
notat_liste.grid(row=4, columnspan=2, padx=5, pady=5, sticky="nsew")

vis_alle_notater()

root.mainloop()

print("")
print("  _______________________________________________")
print(" │                                               │")
print("│  ██╗░░░██╗██╗░█████╗░████████╗░█████╗░██████╗░  │")
print("│  ██║░░░██║██║██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗  │")
print("│  ╚██╗░██╔╝██║██║░░╚═╝░░░██║░░░██║░░██║██████╔╝  │")
print("│  ░╚████╔╝░██║██║░░██╗░░░██║░░░██║░░██║██╔══██╗  │")
print("│  ░░╚██╔╝░░██║╚█████╔╝░░░██║░░░╚█████╔╝██║░░██║  │")
print("│  ░░░╚═╝░░░╚═╝░╚════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝  │")
print(" │_______________________________________________│")
print("")
print("")
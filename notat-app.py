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
    for widget in frame.winfo_children():
        widget.destroy()

    c.execute('''SELECT * FROM notater''')
    notater = c.fetchall()
    for i, note in enumerate(notater):
        note_frame = tk.Frame(frame, relief=tk.RAISED, borderwidth=1)
        note_frame.grid(row=i, column=0, padx=5, pady=5, sticky="ew")
        tk.Label(note_frame, text=f"Tittel: {note[1]}", font=("Helvetica", 14)).grid(row=0, column=0, sticky="w", padx=5, pady=5)
        tk.Label(note_frame, text=f"Notat: {note[2]}", wraplength=400, justify=tk.LEFT).grid(row=1, column=0, sticky="w", padx=5, pady=5)
        tk.Label(note_frame, text=f"Laget: {note[3]}", font=("Helvetica", 10)).grid(row=2, column=0, sticky="w", padx=5, pady=5)

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

slett_knapp = tk.Button

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
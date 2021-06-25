import sqlite3
try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

conn = sqlite3.connect("music.sqlite")

# for x in conn.execute("SELECT albums.name FROM albums WHERE albums.artist = ? ORDER BY albums.name",(196,)):
#     print(x)



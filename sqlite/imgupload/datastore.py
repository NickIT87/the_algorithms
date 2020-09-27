import sqlite3
import codecs
import os

print(os.getcwd())


conn = sqlite3.connect('image.db')
cursor = conn.cursor()

print(cursor)

name = "nick"

with open( "sqlite/imgupload/nature.jpg", "rb") as f:
    data = f.read()
    #print( data )

cursor.execute("""
CREATE TABLE IF NOT EXISTS my_table (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL)
""")

cursor.execute("INSERT INTO my_table (name, data) VALUES (?,?)", (name, data))

conn.commit()
cursor.close()
conn.close()
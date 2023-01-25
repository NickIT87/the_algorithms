import sqlite3
import time
import datetime
import random

connection = sqlite3.connect('less3.db')
c = connection.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)')

def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES(1234, '2016-01-01', 'Python', 5)")
    connection.commit()
    c.close()
    connection.close()

def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Python'
    value = random.randrange(0,100)
    c.execute("INSERT INTO stuffToPlot (unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)",
              (unix, date, keyword, value))
    connection.commit()

def read_from_db():
    #c.execute("SELECT * FROM stuffToPlot WHERE value=51 AND keyword='Python'")
    c.execute("SELECT * FROM stuffToPlot WHERE unix > 1582998880")
    #c.execute("SELECT * FROM stuffToPlot")
    #data = c.fetchall()
    #print(data)
    for row in c.fetchall():
        print(row[1])


def update_data():
    c.execute("UPDATE stuffToPlot SET value = 14.2 WHERE keyword = 'java'")
    connection.commit()


update_data()
c.close()
connection.close()
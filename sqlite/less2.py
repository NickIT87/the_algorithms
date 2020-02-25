import sqlite3
import time
import datetime
import random

connection = sqlite3.connect('less2.db')
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

create_table()
for i in range(10):
    dynamic_data_entry()
    time.sleep(1)
c.close()
connection.close()

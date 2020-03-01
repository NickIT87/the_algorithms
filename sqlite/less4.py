import sqlite3
import time
import datetime
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style
style.use('fivethirtyeight')


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
    #c.execute("SELECT * FROM stuffToPlot WHERE unix > 1452618731")
    #c.execute("SELECT * FROM stuffToPlot")
    c.execute("SELECT keyword, unix FROM stuffToPlot WHERE unix > 1452618731")
    #data = c.fetchall()
    #print(data)
    for row in c.fetchall():
        print(row)

def graph_data():
    c.execute('SELECT unix, value FROM stuffToPlot')
    dates = []
    values = []
    for row in c.fetchall():
        #print(row[0])
        #print(datetime.datetime.fromtimestamp(row[0]))

        dates.append(datetime.datetime.fromtimestamp(row[0]))
        values.append(row[1])

    plt.plot_date(dates, values, '-')
    plt.show()


##create_table()
##for i in range(10):
##    dynamic_data_entry()
##    time.sleep(1)
##read_from_db()
graph_data()
c.close()
connection.close()
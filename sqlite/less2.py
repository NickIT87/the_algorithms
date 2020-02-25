import sqlite3

connection = sqlite3.connect('less1.db')
c = connection.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)')

def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES(1234, '2016-01-01', 'Python', 5)")
    connection.commit()
    c.close()
    connection.close()


create_table()
data_entry()
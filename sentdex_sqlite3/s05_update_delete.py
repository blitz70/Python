#   05. update delete

import sqlite3 as s3
import time as t, datetime as dt, random as rd
import matplotlib.pyplot as mplt
from matplotlib import style

conn = s3.connect('tutorial.db')
c = conn.cursor()

def create_table():
    c.execute('''CREATE TABLE IF NOT EXISTS stuffTOPlot(
        unix REAL, datestamp TEXT, keyword TEXT, value REAL
        )''')

def data_entry():
    c.execute('''INSERT INTO stuffToPlot VALUES(
        2881030,'2016-01-01','Python',8
        )''')
    conn.commit()

def dynamic_data_entry():
    unix = int(t.time())
    date = str(dt.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Python'
    value = rd.randrange(0,10)
    c.execute('''INSERT INTO stuffToPlot
        (unix, datestamp, keyword, value) VALUES
        (?, ?, ?, ?)'''
        ,(unix, date, keyword, value))
    conn.commit()
    print('done')

def read_from_db():
    c.execute("SELECT keyword, datestamp FROM stuffToPlot WHERE value=3")
    rows = c.fetchall()
    for row in rows:
        print(row)

def plot_data():
    c.execute("SELECT unix, value FROM stuffToPlot")
    rows = c.fetchall()
    x = []
    y = []
    for row in rows:
        #print(row[0], dt.datetime.fromtimestamp(row[0]),row[1])
        x.append(dt.datetime.fromtimestamp(row[0]))
        y.append(row[1])
    style.use('fivethirtyeight')
    mplt.plot(x,y)
    mplt.show()

def check_db():
    print('checking...')
    c.execute("SELECT * FROM stuffToPlot")
    [print(row) for row in c.fetchall()]

def update_db():
    c.execute("UPDATE stuffToPlot SET value=99 WHERE value=8")
    conn.commit()

def delete_from_db():
    if True:
        c.execute("DELETE FROM stuffToPlot WHERE value=99")
        conn.commit()
    else:
        print('Delete aborted')

#create_table()

#data_entry()

'''for i in range(100):
    dynamic_data_entry()
    t.sleep(1)'''

#read_from_db()

#plot_data()

#check_db()
#update_db()
#check_db()

check_db()
delete_from_db()
check_db()

c.close()
conn.close()

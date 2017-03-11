#   01. intro - create insert
#   http://sqlitebrowser.org/

import sqlite3 as s3

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
    c.close()
    conn.close()

create_table()
data_entry()

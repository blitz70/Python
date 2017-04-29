import pymysql

def connect():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='mysql',
        db='pythonprogramming')
    c = conn.cursor()
    return c, conn

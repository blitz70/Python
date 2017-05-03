import pymysql


def connect():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        db='')
    c = conn.cursor()
    return c, conn

import pymysql


def connect():
    conn = pymysql.connect(
        host='localhost',
        user='',
        password='',
        db='')
    c = conn.cursor()
    return c, conn

import mysql_conn
import pymysql

q1='select * from test'

def select_table(CONN):
    curs=CONN.cursor(pymysql.cursors.DictCursor)
    curs.execute(q1)
    rows = curs.fetchall()
    for row in rows:
        print(row)
    CONN.close()

def conn():
    CONN=mysql_conn.connect_to_mysql()
    return CONN

def main():
    try:
        CONN=conn()
    except Exception as err:
        print(str(err))
    else:
        select_table(CONN)

if __name__ == '__main__':
    main()
import informix_conn

q1='select first 10 tabname from mondb:systables where tabid > 99;'

def select_table():
    """select table"""
    curs = _CONN.cursor()
    curs.execute(q1)
    for row in curs.fetchall():
        print(row)

def main():
    """main"""
    try:
        global _CONN
        _CONN=informix_conn.init_db_conn(informix_conn.connect_string)
    except Exception as err:
        print(str(err))
    else:
        select_table()
        _CONN.close()

if __name__ == '__main__':
        main()
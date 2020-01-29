import pymysql

HOST='192.168.0.47'
PORT=9001
USER='jilee'
PASSWORD='Mynamepass123!@#'
DBNAME='testdb'

def connect_to_mysql():
    CONN = pymysql.connect(host=HOST, port=PORT, user=USER,
                        password=PASSWORD,
                        db=DBNAME, charset='utf8')
    return CONN

def main():
    try:
        CONN=connect_to_mysql()
    except Exception as err:
        print(str(err))
    else:
        print('DB Connection Success')
        CONN.close()

if __name__ == '__main__':
    main()
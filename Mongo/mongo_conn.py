import pymongo
import urllib

HOST='192.168.0.47'
PORT=9002
USER='jilee'
PASSWORD=urllib.parse.quote_plus('Myname123!@#')

print('mongodb://'+USER+':'+PASSWORD+'@'+HOST+':'+str(PORT))

def conn(HOST,PORT,USER,PASSWORD):
    CONN=pymongo.MongoClient('mongodb://'+USER+':'+PASSWORD+'@'+HOST+':'+str(PORT))
    return CONN

def main():
    try:
        CONN=conn(HOST,PORT,USER,PASSWORD)
    except Exception as err:
        print(str(err))
    else:
        print('Connection Success')
        CONN.close()


if __name__ == '__main__':
    main()
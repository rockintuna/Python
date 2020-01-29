import pymongo
import urllib

HOST='192.168.0.47'
PORT=9002
USER='jilee'
PASSWORD=urllib.parse.quote_plus('Myname123!@#')
DATABASE='test'

print('mongodb://'+USER+':'+PASSWORD+'@'+HOST+':'+str(PORT))

def conn():
    CONN=pymongo.MongoClient('mongodb://'+USER+':'+PASSWORD+'@'+HOST+':'+str(PORT)+'/'+DATABASE)
    return CONN

def main():
    try:
        CONN=conn()
    except Exception as err:
        print(str(err))
    else:
        print('Connection Success')
        CONN.close()


if __name__ == '__main__':
    main()
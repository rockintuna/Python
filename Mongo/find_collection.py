import pymongo
import urllib
import mongo_conn
from Mongo.mongo_conn import HOST,PORT

USER='jilee'
PASSWORD=urllib.parse.quote_plus('Myname123!@#')


def find_collection(CONN):
    db = CONN.get_database('test')
    collection.insert
    #collection = db.get_collection('book')
    #results = collection.find()
    #for result in results:
    #    print(result)

def main():
    try:
        print(HOST,PORT)
        CONN=mongo_conn.conn(HOST,PORT,USER,PASSWORD)
        find_collection(CONN)
    except Exception as err:
        print(str(err))
    else:
        print('No Error')

if __name__ == '__main__':
    main()
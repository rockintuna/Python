import mongo_conn
import pymongo
import urllib

USER='jilee'
PASSWORD=urllib.parse.quote_plus('Myname123!@#')
print(pymongo.version)

def find_collection(CONN):
    db = CONN.get_database()
    collection_list = db.list_collection_names()
    print(collection_list)
    collection = db.get_collection('book')
    results = collection.find()
    for result1 in results:
        print(result1)
    print('''
    ''')
    collection.update_one({'name':'MongoDB Tutorial2'},{'$set':{'author':'velopert2'}})
    results = collection.find({'name':'MongoDB Tutorial2'})
    for result2 in results:
        print(result2)
    collection.delete_one({'name':'MongoDB Tutorial2'})
    results = collection.find({'name':'MongoDB Tutorial2'})
    for result2 in results:
        print(result2)
    collection.insert_one({'name':'MongoDB Tutorial2','author':'velopert'})
    results = collection.find({'name':'MongoDB Tutorial2'})
    for result2 in results:
        print(result2)

def main():
    try:
        CONN=mongo_conn.conn()
        find_collection(CONN)
    except Exception as err:
        print(str(err))
    else:
        print('\n\nNo Error')

if __name__ == '__main__':
    main()
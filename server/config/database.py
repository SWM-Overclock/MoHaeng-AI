import pymongo

HOST = 'localhost'
PORT = 27017

client = pymongo.MongoClient(HOST, PORT)
db = client['Mohaeng']
event_collection = db['event']
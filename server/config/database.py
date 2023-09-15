import pymongo
import os
from dotenv import load_dotenv

load_dotenv()
HOST = os.getenv("DB_HOST")
PORT = int(os.getenv("DB_PORT"))

client = pymongo.MongoClient(HOST, PORT)
db = client['Mohaeng']
event_collection = db['event']